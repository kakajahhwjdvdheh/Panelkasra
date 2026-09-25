# external_configs.py
import secrets
from datetime import datetime

EXTERNAL_CONFIGS: dict = {}


def list_all() -> list:
    return list(EXTERNAL_CONFIGS.values())


def add_config(name: str, url: str) -> tuple[str, dict]:
    eid = secrets.token_hex(6)
    record = {
        "id": eid,
        "name": (name or "سرور خارجی").strip()[:60],
        "url": url.strip(),
        "active": True,
        "created_at": datetime.now().isoformat(),
    }
    EXTERNAL_CONFIGS[eid] = record
    return eid, record


def remove_config(eid: str) -> dict | None:
    return EXTERNAL_CONFIGS.pop(eid, None)


def update_config(eid: str, name: str | None = None, url: str | None = None, active: bool | None = None) -> dict | None:
    rec = EXTERNAL_CONFIGS.get(eid)
    if not rec:
        return None
    if name is not None:
        rec["name"] = name.strip()[:60]
    if url is not None:
        rec["url"] = url.strip()
    if active is not None:
        rec["active"] = bool(active)
    return rec


def get_active_urls() -> list[str]:
    return [c["url"] for c in EXTERNAL_CONFIGS.values() if c.get("active", True)]
