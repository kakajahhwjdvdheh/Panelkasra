# outbound.py
# ══════════════════════════════════════════════════════════════════════════════
# Outbound Manager — مثل سنایی/3x-ui
# پشتیبانی از: direct (freedom) | block (blackhole) | socks5 | vless-chain
# ══════════════════════════════════════════════════════════════════════════════

import asyncio
import base64
import json
import secrets
from datetime import datetime
from urllib.parse import urlparse, parse_qs, unquote

# این‌ها از main.py میان (بعد از main لود می‌شن)
OUTBOUNDS: dict = {}          # outbound_id -> record
OUTBOUNDS_LOCK = asyncio.Lock()

# پیش‌فرض‌ها همیشه وجود دارن
BUILTIN_OUTBOUNDS = {
    "direct": {
        "id": "direct",
        "name": "مستقیم (Freedom)",
        "type": "freedom",
        "active": True,
        "builtin": True,
    },
    "block": {
        "id": "block",
        "name": "مسدود (Block)",
        "type": "blackhole",
        "active": True,
        "builtin": True,
    },
}


def list_all_outbounds() -> list:
    """لیست همه outbound‌ها (builtin + user)"""
    out = list(BUILTIN_OUTBOUNDS.values())
    out.extend(OUTBOUNDS.values())
    return out


def get_outbound(outbound_id: str | None) -> dict:
    """گرفتن یه outbound یا برگرداندن direct به عنوان fallback"""
    if not outbound_id:
        return BUILTIN_OUTBOUNDS["direct"]
    if outbound_id in BUILTIN_OUTBOUNDS:
        return BUILTIN_OUTBOUNDS[outbound_id]
    ob = OUTBOUNDS.get(outbound_id)
    if not ob or not ob.get("active", True):
        return BUILTIN_OUTBOUNDS["direct"]
    return ob


# ══════════════════════════════════════════════════════════════════════════════
# SOCKS5 Client (RFC 1928 + RFC 1929 برای auth)
# ══════════════════════════════════════════════════════════════════════════════

async def _socks5_connect(
    proxy_host: str,
    proxy_port: int,
    target_host: str,
    target_port: int,
    username: str = "",
    password: str = "",
    timeout: float = 10.0,
):
    """
    اتصال به مقصد از طریق یه پروکسی SOCKS5.
    خروجی: (reader, writer) مثل asyncio.open_connection
    """
    reader, writer = await asyncio.wait_for(
        asyncio.open_connection(proxy_host, proxy_port),
        timeout=timeout,
    )

    try:
        # ── مرحله ۱: greeting ──────────────────────────────
        if username:
            # پشتیبانی از user/pass auth
            writer.write(b"\x05\x02\x00\x02")
        else:
            writer.write(b"\x05\x01\x00")
        await writer.drain()

        resp = await asyncio.wait_for(reader.readexactly(2), timeout=timeout)
        if resp[0] != 0x05:
            raise ConnectionError("SOCKS5: bad version")
        method = resp[1]

        # ── مرحله ۲: auth (اگه لازم بود) ──────────────────
        if method == 0x02:
            if not username:
                raise ConnectionError("SOCKS5: server requires auth")
            u = username.encode()
            p = password.encode()
            writer.write(b"\x01" + bytes([len(u)]) + u + bytes([len(p)]) + p)
            await writer.drain()
            auth_resp = await asyncio.wait_for(reader.readexactly(2), timeout=timeout)
            if auth_resp[1] != 0x00:
                raise ConnectionError("SOCKS5: auth failed")
        elif method == 0x00:
            pass  # بدون auth
        elif method == 0xFF:
            raise ConnectionError("SOCKS5: no acceptable method")
        else:
            raise ConnectionError(f"SOCKS5: unknown method {method}")

        # ── مرحله ۳: CONNECT request ──────────────────────
        # address type: 0x03 = domain
        host_b = target_host.encode()
        if len(host_b) > 255:
            raise ConnectionError("SOCKS5: host too long")
        req = b"\x05\x01\x00\x03" + bytes([len(host_b)]) + host_b + target_port.to_bytes(2, "big")
        writer.write(req)
        await writer.drain()

        # پاسخ: VER REP RSV ATYP BND.ADDR BND.PORT
        head = await asyncio.wait_for(reader.readexactly(4), timeout=timeout)
        if head[1] != 0x00:
            raise ConnectionError(f"SOCKS5: connect failed (code {head[1]})")
        atyp = head[3]
        if atyp == 0x01:
            await reader.readexactly(4 + 2)
        elif atyp == 0x03:
            ln = (await reader.readexactly(1))[0]
            await reader.readexactly(ln + 2)
        elif atyp == 0x04:
            await reader.readexactly(16 + 2)
        else:
            raise ConnectionError("SOCKS5: bad atyp")

        return reader, writer

    except Exception:
        try:
            writer.close()
        except Exception:
            pass
        raise


# ══════════════════════════════════════════════════════════════════════════════
# VLESS Chain Client — تونل VLESS روی WebSocket
# ══════════════════════════════════════════════════════════════════════════════

def parse_vless_url(url: str) -> dict:
    """
    پارس کردن یه vless:// share-link به dict کانفیگ.
    فرمت: vless://uuid@host:port?type=ws&security=tls&path=/ws/xxx&host=...&sni=...&fp=chrome#label
    """
    if not url.startswith("vless://"):
        raise ValueError("only vless:// supported")
    u = urlparse(url)
    if not u.hostname or not u.username:
        raise ValueError("invalid vless url")
    q = parse_qs(u.query)
    return {
        "uuid": unquote(u.username),
        "host": u.hostname,
        "port": u.port or 443,
        "type": (q.get("type", ["ws"])[0]).lower(),
        "security": (q.get("security", ["tls"])[0]).lower(),
        "path": q.get("path", ["/ws/" + unquote(u.username)])[0],
        "sni": q.get("sni", [u.hostname])[0],
        "host_header": q.get("host", [u.hostname])[0],
        "fp": q.get("fp", ["chrome"])[0],
        "alpn": q.get("alpn", ["http/1.1"])[0],
        "remark": unquote(u.fragment) if u.fragment else "",
    }


def _build_vless_header(target_host: str, target_port: int) -> bytes:
    """ساخت هدر VLESS برای درخواست CONNECT به مقصد."""
    import os
    # نسخه‌ی VLESS: 0x00
    header = bytearray()
    header.append(0x00)                                  # version
    # UUID placeholder — اینجا خودمون UUID سرور مقصد رو می‌ذاریم
    return bytes(header)


async def _vless_chain_connect(
    outbound: dict,
    target_host: str,
    target_port: int,
    timeout: float = 10.0,
):
    """
    اتصال به مقصد از طریق یه سرور VLESS دیگه (زنجیره).
    به این صورت:
      1) به سرور VLESS (host:port) با WebSocket + TLS وصل می‌شیم
      2) هدر VLESS می‌سازیم برای CONNECT به target_host:target_port
      3) یه wrapper برمی‌گردونیم که مثل reader/writer asyncio کار کنه

    خروجی: (reader-like, writer-like)
    """
    import websockets  # اگه نصب نیست: pip install websockets

    url = outbound.get("url", "")
    cfg = parse_vless_url(url)

    # WebSocket URL بساز
    scheme = "wss" if cfg["security"] == "tls" else "ws"
    ws_url = f"{scheme}://{cfg['host']}:{cfg['port']}{cfg['path']}"

    headers = {
        "Host": cfg["host_header"],
        "User-Agent": "Mozilla/5.0",
    }

    try:
        ws = await asyncio.wait_for(
            websockets.connect(
                ws_url,
                extra_headers=headers,
                open_timeout=timeout,
                max_size=None,
                ping_interval=None,
            ),
            timeout=timeout,
        )
    except Exception as e:
        raise ConnectionError(f"VLESS chain: ws connect failed: {e}")

    # ── ساخت هدر VLESS ──────────────────────────────────
    import uuid as uuid_mod

    vless_uuid = uuid_mod.UUID(cfg["uuid"]).bytes
    header = bytearray()
    header.append(0x00)                    # version
    header.extend(vless_uuid)              # 16 bytes UUID
    header.append(0x00)                    # addon length = 0
    header.append(0x01)                    # command = TCP CONNECT
    header.extend(target_port.to_bytes(2, "big"))
    # address
    try:
        # IPv4?
        parts = target_host.split(".")
        if len(parts) == 4 and all(p.isdigit() for p in parts):
            header.append(0x01)
            header.extend(bytes(int(p) for p in parts))
        else:
            raise ValueError
    except Exception:
        # domain
        hb = target_host.encode()
        header.append(0x02)
        header.append(len(hb))
        header.extend(hb)
    # payload نداریم، اول کار

    try:
        await ws.send(bytes(header))
    except Exception as e:
        await ws.close()
        raise ConnectionError(f"VLESS chain: header send failed: {e}")

    # ── Wrapper که رفتار reader/writer asyncio رو تقلید کنه ──
    return _VlessChainStream(ws)


class _VlessChainStream:
    """
    Adapter که یه WebSocket رو به شکل (reader, writer) asyncio ارائه می‌ده.
    فقط متدهای مورد نیاز relay_vless.py و xhttp_siz10.py:
      reader.read(n), reader.readexactly(n)
      writer.write(data), writer.drain(), writer.close(), writer.wait_closed()
      writer.transport.get_write_buffer_size()
      writer.transport.get_extra_info('socket')
      writer.write_eof()
    """
    class _FakeTransport:
        def __init__(self):
            self._buf = 0
        def get_write_buffer_size(self):
            return self._buf
        def get_extra_info(self, name):
            return None

    def __init__(self, ws):
        self.ws = ws
        self._buf_queue: asyncio.Queue = asyncio.Queue()
        self._closed = False
        self._recv_task = asyncio.create_task(self._recv_loop())
        self.transport = self._FakeTransport()
        self._reader = self  # reader = self

    async def _recv_loop(self):
        try:
            async for msg in self.ws:
                if isinstance(msg, str):
                    msg = msg.encode()
                await self._buf_queue.put(msg)
        except Exception:
            pass
        finally:
            await self._buf_queue.put(None)  # EOF

    # ── reader API ─────────────────────────────────────
    async def read(self, n: int = -1) -> bytes:
        if self._closed:
            return b""
        chunk = await self._buf_queue.get()
        if chunk is None:
            self._closed = True
            return b""
        return chunk

    async def readexactly(self, n: int) -> bytes:
        out = bytearray()
        while len(out) < n:
            chunk = await self.read(n - len(out))
            if not chunk:
                raise asyncio.IncompleteReadError(bytes(out), n)
            out.extend(chunk)
        return bytes(out)

    # ── writer API ─────────────────────────────────────
    def write(self, data: bytes):
        if self._closed:
            return
        self.transport._buf += len(data)
        asyncio.create_task(self._send(data))

    async def _send(self, data: bytes):
        try:
            await self.ws.send(data)
        except Exception:
            pass
        finally:
            self.transport._buf = max(0, self.transport._buf - len(data))

    async def drain(self):
        # WebSocket backpressure رو خودش هندل می‌کنه
        await asyncio.sleep(0)

    def write_eof(self):
        pass

    def close(self):
        if not self._closed:
            self._closed = True
            asyncio.create_task(self.ws.close())

    async def wait_closed(self):
        try:
            await self.ws.wait_closed()
        except Exception:
            pass
        if self._recv_task:
            self._recv_task.cancel()
            try:
                await self._recv_task
            except (asyncio.CancelledError, Exception):
                pass


# ══════════════════════════════════════════════════════════════════════════════
# تابع اصلی: اتصال از روی Outbound
# ══════════════════════════════════════════════════════════════════════════════

async def open_via_outbound(
    outbound_id: str | None,
    target_host: str,
    target_port: int,
    timeout: float = 10.0,
):
    """
    جایگزین asyncio.open_connection:
      - direct  → asyncio.open_connection مستقیم
      - block   → خطا (اتصال رد)
      - socks5  → از طریق SOCKS5
      - vless   → از طریق VLESS chain
    خروجی: (reader, writer)
    """
    ob = get_outbound(outbound_id)
    ob_type = ob.get("type", "freedom")

    if ob_type == "blackhole":
        raise ConnectionError("outbound: blocked")

    if ob_type == "socks5":
        return await _socks5_connect(
            proxy_host=ob["address"],
            proxy_port=int(ob["port"]),
            target_host=target_host,
            target_port=target_port,
            username=ob.get("username", ""),
            password=ob.get("password", ""),
            timeout=timeout,
        )

    if ob_type == "vless":
        stream = await _vless_chain_connect(ob, target_host, target_port, timeout)
        return stream, stream  # reader = writer = stream

    # freedom (direct)
    return await asyncio.wait_for(
        asyncio.open_connection(target_host, target_port),
        timeout=timeout,
    )


# ══════════════════════════════════════════════════════════════════════════════
# CRUD helpers (اختیاری — اگه خواستی از API صدا بزنی)
# ══════════════════════════════════════════════════════════════════════════════

def make_outbound_record(
    name: str,
    ob_type: str,
    address: str = "",
    port: int = 0,
    username: str = "",
    password: str = "",
    url: str = "",
) -> tuple[str, dict]:
    """ساخت یه رکورد outbound جدید و برگرداندن (id, record)"""
    oid = secrets.token_hex(6)
    record = {
        "id": oid,
        "name": (name or f"Outbound {oid}").strip()[:60],
        "type": ob_type,           # "socks5" | "vless"
        "address": address.strip(),
        "port": int(port or 0),
        "username": username.strip(),
        "password": password,
        "url": url.strip(),        # برای vless
        "active": True,
        "created_at": datetime.now().isoformat(),
    }
    return oid, record
