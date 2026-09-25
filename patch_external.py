# patch_external.py
import re
import sys
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════
# ۱. پچ main.py
# ═══════════════════════════════════════════════════════════════════
print("🔧 در حال پچ main.py ...")
MAIN = Path("main.py")
if not MAIN.exists():
    print("❌ main.py پیدا نشد!")
    sys.exit(1)

src = MAIN.read_text(encoding="utf-8")
original_len = len(src)

def replace_once(s, old, new, label):
    if old in s:
        s = s.replace(old, new, 1)
        print(f"  ✅ {label}")
    else:
        print(f"  ⚠️  {label} — الگو پیدا نشد")
    return s

# ۱.۱: بارگذاری external_configs توی load_state
src = replace_once(src,
    '''                logger.info(f"Outbounds loaded: {len(_OB)}")
            except Exception as e:
                logger.warning(f"Could not load outbounds: {e}")''',
    '''                logger.info(f"Outbounds loaded: {len(_OB)}")
            except Exception as e:
                logger.warning(f"Could not load outbounds: {e}")
            # Load external configs from state
            try:
                from external_configs import EXTERNAL_CONFIGS as _EC
                saved_ec = data.get("external_configs", {})
                if isinstance(saved_ec, dict):
                    _EC.update(saved_ec)
                    logger.info(f"External configs loaded: {len(_EC)}")
            except Exception as e:
                logger.warning(f"Could not load external configs: {e}")''',
    "load_state external_configs")

# ۱.۲: ذخیره‌ی external_configs توی save_state
src = replace_once(src,
    '''            try:
                from outbound import OUTBOUNDS as _OB
                outbounds_snapshot = dict(_OB)
            except Exception:
                outbounds_snapshot = {}
            data = {''',
    '''            try:
                from outbound import OUTBOUNDS as _OB
                outbounds_snapshot = dict(_OB)
            except Exception:
                outbounds_snapshot = {}
            try:
                from external_configs import EXTERNAL_CONFIGS as _EC
                external_configs_snapshot = dict(_EC)
            except Exception:
                external_configs_snapshot = {}
            data = {''',
    "save_state external_configs snapshot")

src = replace_once(src,
    '''                "outbounds": outbounds_snapshot,
                "saved_at": datetime.now().isoformat(),''',
    '''                "outbounds": outbounds_snapshot,
                "external_configs": external_configs_snapshot,
                "saved_at": datetime.now().isoformat(),''',
    "save_state external_configs in data")

# ۱.۳: append به /sub-all
src = replace_once(src,
    '''@app.get("/sub-all")
async def subscription_all(request: Request, _=Depends(require_auth)):
    import base64
    host = get_host(request)
    async with LINKS_LOCK:
        lines = [
            vless_link_for_link(d, uid, host)
            for uid, d in LINKS.items()
            if is_link_allowed(d)
        ]
    content = base64.b64encode("\\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain")''',
    '''@app.get("/sub-all")
async def subscription_all(request: Request, _=Depends(require_auth)):
    import base64
    host = get_host(request)
    async with LINKS_LOCK:
        lines = [
            vless_link_for_link(d, uid, host)
            for uid, d in LINKS.items()
            if is_link_allowed(d)
        ]
    # اضافه کردن کانفیگ‌های خارجی
    try:
        from external_configs import get_active_urls
        lines.extend(get_active_urls())
    except Exception:
        pass
    content = base64.b64encode("\\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain")''',
    "/sub-all external configs")

# ۱.۴: append به /sub-group/{key}
src = replace_once(src,
    '''    async with LINKS_LOCK:
        lines = []
        for lid in link_ids:
            link = LINKS.get(lid)
            if link and is_link_allowed(link):
                lines.append(vless_link_for_link(link, lid, host))

    content = base64.b64encode("\\n".join(lines).encode()).decode()
    return Response(
        content=content,
        media_type="text/plain",
        headers={
            "profile-title": quote(sub["name"]),
            "support-url": "https://t.me/technamooz",
            "profile-update-interval": "12",
        }
    )''',
    '''    async with LINKS_LOCK:
        lines = []
        for lid in link_ids:
            link = LINKS.get(lid)
            if link and is_link_allowed(link):
                lines.append(vless_link_for_link(link, lid, host))

    # اضافه کردن کانفیگ‌های خارجی
    try:
        from external_configs import get_active_urls
        lines.extend(get_active_urls())
    except Exception:
        pass

    content = base64.b64encode("\\n".join(lines).encode()).decode()
    return Response(
        content=content,
        media_type="text/plain",
        headers={
            "profile-title": quote(sub["name"]),
            "support-url": "https://t.me/technamooz",
            "profile-update-interval": "12",
        }
    )''',
    "/sub-group external configs")

# ۱.۵: ۴ تا API جدید
externals_api = '''

# ══════════════════════════════════════════════════════════════════════════════
# EXTERNAL CONFIGS API  (سرورهای خارجی — مثل سنایی)
# ══════════════════════════════════════════════════════════════════════════════

@app.get("/api/external-configs")
async def list_external_configs(_=Depends(require_auth)):
    """لیست کانفیگ‌های خارجی"""
    try:
        from external_configs import list_all
        return {"configs": list_all()}
    except Exception as e:
        logger.warning(f"external_configs module unavailable: {e}")
        return {"configs": []}

@app.post("/api/external-configs")
async def create_external_config(request: Request, _=Depends(require_auth)):
    """افزودن یک کانفیگ خارجی جدید"""
    body = await request.json()
    name = str(body.get("name") or "").strip()
    url = str(body.get("url") or "").strip()
    if not url:
        raise HTTPException(status_code=400, detail="لینک کانفیگ الزامی است")
    if not (url.startswith("vless://") or url.startswith("vmess://") or url.startswith("trojan://") or url.startswith("ss://")):
        raise HTTPException(status_code=400, detail="فقط لینک‌های vless/vmess/trojan/ss پشتیبانی می‌شوند")
    if not name:
        name = "سرور خارجی"
    try:
        from external_configs import add_config
        eid, record = add_config(name, url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"external_configs module unavailable: {e}")
    asyncio.create_task(save_state())
    log_activity("external", f"سرور خارجی «{name}» اضافه شد", "ok")
    return {"ok": True, "id": eid, "config": record}

@app.patch("/api/external-configs/{eid}")
async def update_external_config(eid: str, request: Request, _=Depends(require_auth)):
    """ویرایش یک کانفیگ خارجی"""
    body = await request.json()
    try:
        from external_configs import update_config
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"external_configs module unavailable: {e}")
    rec = update_config(eid, name=body.get("name"), url=body.get("url"), active=body.get("active"))
    if rec is None:
        raise HTTPException(status_code=404, detail="config not found")
    await save_state()
    log_activity("external", f"سرور خارجی «{rec.get('name', eid)}» ویرایش شد", "info")
    return {"ok": True, "config": rec}

@app.delete("/api/external-configs/{eid}")
async def delete_external_config(eid: str, _=Depends(require_auth)):
    """حذف یک کانفیگ خارجی"""
    try:
        from external_configs import remove_config
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"external_configs module unavailable: {e}")
    rec = remove_config(eid)
    if rec is None:
        raise HTTPException(status_code=404, detail="config not found")
    await save_state()
    log_activity("external", f"سرور خارجی «{rec.get('name', eid)}» حذف شد", "warn")
    return {"ok": True, "deleted": eid}
'''

marker = '''# ══════════════════════════════════════════════════════════════════════════════
# VLESS Relay — جدا شده به relay_vless.py (دست نخورده)
# ══════════════════════════════════════════════════════════════════════════════'''

if "/api/external-configs" not in src and marker in src:
    src = src.replace(marker, externals_api + "\n" + marker, 1)
    print("  ✅ API /api/external-configs اضافه شد")
else:
    if "/api/external-configs" in src:
        print("  ⚠️  API قبلاً اضافه شده")
    else:
        print("  ⚠️  marker پیدا نشد")

# ذخیره main.py
if len(src) != original_len:
    MAIN.write_text(src, encoding="utf-8")
    print(f"✅ main.py پچ شد (+{len(src)-original_len} کاراکتر)\n")
else:
    print("⚠️  main.py تغییر نکرد\n")


# ═══════════════════════════════════════════════════════════════════
# ۲. پچ pages.py
# ═══════════════════════════════════════════════════════════════════
print("🔧 در حال پچ pages.py ...")
PAGES = Path("pages.py")
if not PAGES.exists():
    print("❌ pages.py پیدا نشد!")
    sys.exit(1)

src = PAGES.read_text(encoding="utf-8")
original_len = len(src)

# ۲.۱: آیتم سایدبار
src = replace_once(src,
    '<div class="nav-it" data-pg="outbounds"><i class="ti ti-route"></i> خروجی‌ها <span class="nav-badge" id="outbounds-nb">0</span></div>',
    '<div class="nav-it" data-pg="outbounds"><i class="ti ti-route"></i> خروجی‌ها <span class="nav-badge" id="outbounds-nb">0</span></div>\n    <div class="nav-it" data-pg="externals"><i class="ti ti-world-upload"></i> سرورهای خارجی <span class="nav-badge" id="externals-nb">0</span></div>',
    "آیتم سایدبار سرورهای خارجی")

# ۲.۲: بخش pg-externals
externals_section = '''
<section class="pg" id="pg-externals">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-world-upload"></i> سرورهای خارجی</div><div class="tb-sub">کانفیگ‌های خارجی که توی ساب‌لینک کاربرا نمایش داده می‌شن</div></div>
    <div class="tb-right">
      <span class="badge bg-green" id="externals-pg-cnt">۰ سرور</span>
      <button class="btn btn-p" onclick="openModal('modal-create-external')" style="background:linear-gradient(135deg,#22c55e,#15803d)"><i class="ti ti-plus"></i> سرور جدید</button>
    </div>
  </div>
  <div class="cl" style="margin-bottom:16px;background:rgba(34,197,94,.08);border-color:rgba(34,197,94,.2);color:#86efac">
    <i class="ti ti-info-circle" style="color:#22c55e"></i>
    <span>
      این کانفیگ‌ها <b>مستقیم</b> در ساب‌لینک کاربرا قرار می‌گیرن (کنار کانفیگ‌های پنل). کاربر توی v2rayNG می‌بینه و می‌تونه مستقیم بهشون وصل شه. برخلاف Outbound، ترافیک از پنل رد نمی‌شه.
    </span>
  </div>
  <div class="cfg-grid" id="externals-grid"></div>
  <div class="empty" id="externals-empty" style="display:none">
    <i class="ti ti-world-off"></i>
    <p>هنوز سرور خارجی‌ای اضافه نشده</p>
  </div>
</section>
'''

if 'id="pg-externals"' not in src:
    pattern = r'(<section class="pg" id="pg-outbounds">.*?</section>)'
    match = re.search(pattern, src, re.DOTALL)
    if match:
        src = src.replace(match.group(1), match.group(1) + "\n" + externals_section, 1)
        print("  ✅ بخش pg-externals اضافه شد")
    else:
        print("  ⚠️  pg-outbounds پیدا نشد")
else:
    print("  ⚠️  pg-externals قبلاً اضافه شده")

# ۲.۳: مودال
externals_modal = '''
<div class="modal-bg" id="modal-create-external">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-external')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon" style="background:linear-gradient(135deg,#22c55e,#15803d)"><i class="ti ti-world-upload"></i></div>
      <div class="modal-v2-title">سرور خارجی جدید</div>
      <div class="modal-v2-sub">یه کانفیگ از پنل دیگه رو اضافه کن تا توی ساب‌لینک کاربرا بیاد</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> نام نمایشی</label>
        <input class="modal-v2-input" id="ne-name" placeholder="مثلاً: سرور آلمان">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-link"></i> لینک کانفیگ (vless / vmess / trojan / ss)</label>
        <input class="modal-v2-input" id="ne-url" placeholder="vless://uuid@server.com:443?..." style="padding-right:13px">
      </div>
      <div class="modal-v2-hint">
        <i class="ti ti-info-circle"></i>
        <span>این کانفیگ کنار کانفیگ‌های پنل توی ساب‌لینک کاربرا نمایش داده می‌شه. کاربر می‌تونه مستقیم بهش وصل شه.</span>
      </div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-external')" style="flex:.6">انصراف</button>
        <button class="btn btn-p" onclick="createExternalConfig()" style="background:linear-gradient(135deg,#22c55e,#15803d)"><i class="ti ti-check"></i> افزودن</button>
      </div>
    </div>
  </div>
</div>
'''

if 'id="modal-create-external"' not in src:
    pattern = r'(<div class="modal-bg" id="modal-create-outbound">.*?</div>\s*</div>\s*</div>)'
    match = re.search(pattern, src, re.DOTALL)
    if match:
        src = src.replace(match.group(1), match.group(1) + "\n" + externals_modal, 1)
        print("  ✅ مودال اضافه شد")
    else:
        print("  ⚠️  modal-create-outbound پیدا نشد")
else:
    print("  ⚠️  مودال قبلاً اضافه شده")

# ۲.۴: اضافه به loaders
src = replace_once(src,
    "const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity,outbounds:loadOutbounds};",
    "const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity,outbounds:loadOutbounds,externals:loadExternals};",
    "loader externals")

# ۲.۵: توابع JS
js_funcs = '''
// ══════ External Configs ══════
let allExternals=[];
async function loadExternals(){
  try{
    const r=await authF('/api/external-configs'),d=await r.json();
    allExternals=d.configs||[];
    document.getElementById('externals-nb').textContent=allExternals.length;
    document.getElementById('externals-pg-cnt').textContent=toFa(allExternals.length)+' سرور';
    const grid=document.getElementById('externals-grid'),empty=document.getElementById('externals-empty');
    if(!allExternals.length){grid.innerHTML='';empty.style.display='block';return}
    empty.style.display='none';
    grid.innerHTML=allExternals.map(c=>`
      <div class="cfg-card">
        <div class="cfg-row">
          <span class="cfg-status-dot" style="background:${c.active?'var(--green)':'var(--red)'}"></span>
          <div class="cfg-identity">
            <div class="cfg-label">${esc(c.name)}</div>
            <div class="cfg-sub-meta">
              <span class="cfg-uuid-mini">${esc(c.id)}</span>
            </div>
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-usage-col">
            <div style="font-size:10.5px;color:var(--t2);line-height:1.8;word-break:break-all">
              ${esc((c.url||'').slice(0,70))}${(c.url||'').length>70?'…':''}
            </div>
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-actions">
            <button class="tog${c.active?' on':''}" onclick="toggleExternal('${c.id}',${!c.active})" title="فعال/غیرفعال"></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(c.url)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی"><i class="ti ti-copy"></i></button>
            <button class="btn btn-sm btn-d btn-icon" onclick="deleteExternalConfig('${c.id}')" title="حذف"><i class="ti ti-trash"></i></button>
          </div>
        </div>
      </div>
    `).join('');
  }catch(e){console.error(e)}
}
async function createExternalConfig(){
  const name=document.getElementById('ne-name').value.trim()||'سرور خارجی';
  const url=document.getElementById('ne-url').value.trim();
  if(!url){toast('لینک کانفیگ الزامی است','err');return}
  try{
    const r=await authF('/api/external-configs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,url})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا')}
    ['ne-name','ne-url'].forEach(id=>document.getElementById(id).value='');
    closeModal('modal-create-external');
    toast('سرور خارجی اضافه شد ✓','ok');
    loadExternals();
  }catch(e){toast('✗ '+e.message,'err')}
}
async function toggleExternal(id,newState){
  try{
    const r=await authF('/api/external-configs/'+id,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});
    if(!r.ok)throw new Error();
    toast(newState?'فعال شد ✓':'غیرفعال شد','ok');
    loadExternals();
  }catch(e){toast('خطا','err')}
}
async function deleteExternalConfig(id){
  if(!confirm('این سرور خارجی حذف بشه؟'))return;
  try{
    const r=await authF('/api/external-configs/'+id,{method:'DELETE'});
    if(!r.ok)throw new Error();
    toast('حذف شد ✓','ok');
    loadExternals();
  }catch(e){toast('خطا','err')}
}
'''

if 'async function loadExternals()' not in src:
    marker2 = "document.addEventListener('DOMContentLoaded',async()=>{"
    if marker2 in src:
        src = src.replace(marker2, js_funcs + "\n" + marker2, 1)
        print("  ✅ توابع JS اضافه شدند")
    else:
        print("  ⚠️  DOMContentLoaded پیدا نشد")
else:
    print("  ⚠️  توابع JS قبلاً اضافه شده")

# ۲.۶: فراخوانی loadExternals
src = replace_once(src,
    "  fetchStats();fetchDefaultVless();loadLinks();loadSubs();loadOutbounds();",
    "  fetchStats();fetchDefaultVless();loadLinks();loadSubs();loadOutbounds();loadExternals();",
    "فراخوانی loadExternals")

# ۲.۷: setInterval
src = replace_once(src,
    "    if(document.getElementById('pg-outbounds').classList.contains('on'))loadOutbounds();",
    "    if(document.getElementById('pg-outbounds').classList.contains('on'))loadOutbounds();\n    if(document.getElementById('pg-externals').classList.contains('on'))loadExternals();",
    "setInterval externals")

# ذخیره pages.py
if len(src) != original_len:
    PAGES.write_text(src, encoding="utf-8")
    print(f"✅ pages.py پچ شد (+{len(src)-original_len} کاراکتر)\n")
else:
    print("⚠️  pages.py تغییر نکرد\n")

print("🎉 تموم شد! حالا سرور رو ری‌استارت کن.")
