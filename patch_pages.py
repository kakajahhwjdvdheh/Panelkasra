# patch_pages.py
import re
from pathlib import Path

print("🔧 Patching pages.py...")

PAGES = Path("pages.py")
if not PAGES.exists():
    print("❌ pages.py not found!")
    exit(1)

src = PAGES.read_text(encoding="utf-8")
original_len = len(src)

# 1. Sidebar item
if 'data-pg="externals"' not in src:
    src = src.replace(
        '<div class="nav-it" data-pg="outbounds"><i class="ti ti-route"></i> خروجی‌ها <span class="nav-badge" id="outbounds-nb">0</span></div>',
        '<div class="nav-it" data-pg="outbounds"><i class="ti ti-route"></i> خروجی‌ها <span class="nav-badge" id="outbounds-nb">0</span></div>\n    <div class="nav-it" data-pg="externals"><i class="ti ti-world-upload"></i> سرورهای خارجی <span class="nav-badge" id="externals-nb">0</span></div>'
    )
    print("  ✅ Sidebar item added")

# 2. Section
if 'id="pg-externals"' not in src:
    section = '''
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
    <span>این کانفیگ‌ها <b>مستقیم</b> در ساب‌لینک کاربرا قرار می‌گیرن (کنار کانفیگ‌های پنل).</span>
  </div>
  <div class="cfg-grid" id="externals-grid"></div>
  <div class="empty" id="externals-empty" style="display:none"><i class="ti ti-world-off"></i><p>هنوز سرور خارجی‌ای اضافه نشده</p></div>
</section>
'''
    pattern = r'(<section class="pg" id="pg-outbounds">.*?</section>)'
    match = re.search(pattern, src, re.DOTALL)
    if match:
        src = src.replace(match.group(1), match.group(1) + "\n" + section, 1)
        print("  ✅ Section added")
    else:
        print("  ⚠️ pg-outbounds not found")

# 3. Modal
if 'id="modal-create-external"' not in src:
    modal = '''
<div class="modal-bg" id="modal-create-external">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-external')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon" style="background:linear-gradient(135deg,#22c55e,#15803d)"><i class="ti ti-world-upload"></i></div>
      <div class="modal-v2-title">سرور خارجی جدید</div>
      <div class="modal-v2-sub">یه کانفیگ از پنل دیگه رو اضافه کن</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field"><label><i class="ti ti-tag"></i> نام نمایشی</label><input class="modal-v2-input" id="ne-name" placeholder="مثلاً: سرور آلمان"></div>
      <div class="modal-v2-field" style="margin-bottom:0"><label><i class="ti ti-link"></i> لینک کانفیگ</label><input class="modal-v2-input" id="ne-url" placeholder="vless://..." style="padding-right:13px"></div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-external')" style="flex:.6">انصراف</button>
        <button class="btn btn-p" onclick="createExternalConfig()" style="background:linear-gradient(135deg,#22c55e,#15803d)"><i class="ti ti-check"></i> افزودن</button>
      </div>
    </div>
  </div>
</div>
'''
    pattern = r'(<div class="modal-bg" id="modal-create-outbound">.*?</div>\s*</div>\s*</div>)'
    match = re.search(pattern, src, re.DOTALL)
    if match:
        src = src.replace(match.group(1), match.group(1) + "\n" + modal, 1)
        print("  ✅ Modal added")
    else:
        print("  ⚠️ modal-create-outbound not found")

# 4. Loaders
src = src.replace(
    "const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity,outbounds:loadOutbounds};",
    "const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity,outbounds:loadOutbounds,externals:loadExternals};"
)

# 5. JS functions
if 'async function loadExternals()' not in src:
    js = '''
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
    grid.innerHTML=allExternals.map(c=>`<div class="cfg-card"><div class="cfg-row"><span class="cfg-status-dot" style="background:${c.active?'var(--green)':'var(--red)'}"></span><div class="cfg-identity"><div class="cfg-label">${esc(c.name)}</div></div><div class="cfg-divider-v"></div><div class="cfg-usage-col"><div style="font-size:10.5px;color:var(--t2);word-break:break-all">${esc((c.url||'').slice(0,70))}</div></div><div class="cfg-divider-v"></div><div class="cfg-actions"><button class="tog${c.active?' on':''}" onclick="toggleExternal('${c.id}',${!c.active})"></button><button class="btn btn-sm btn-d btn-icon" onclick="deleteExternalConfig('${c.id}')"><i class="ti ti-trash"></i></button></div></div></div>`).join('');
  }catch(e){console.error(e)}
}
async function createExternalConfig(){
  const name=document.getElementById('ne-name').value.trim()||'سرور خارجی';
  const url=document.getElementById('ne-url').value.trim();
  if(!url){toast('لینک الزامی است','err');return}
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
  try{const r=await authF('/api/external-configs/'+id,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد':'غیرفعال شد','ok');loadExternals();}catch(e){toast('خطا','err')}
}
async function deleteExternalConfig(id){
  if(!confirm('حذف بشه؟'))return;
  try{const r=await authF('/api/external-configs/'+id,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد','ok');loadExternals();}catch(e){toast('خطا','err')}
}
'''
    marker = "document.addEventListener('DOMContentLoaded',async()=>{"
    if marker in src:
        src = src.replace(marker, js + "\n" + marker, 1)
        print("  ✅ JS functions added")

# 6. Call loadExternals
src = src.replace(
    "  fetchStats();fetchDefaultVless();loadLinks();loadSubs();loadOutbounds();",
    "  fetchStats();fetchDefaultVless();loadLinks();loadSubs();loadOutbounds();loadExternals();"
)

# 7. setInterval
src = src.replace(
    "    if(document.getElementById('pg-outbounds').classList.contains('on'))loadOutbounds();",
    "    if(document.getElementById('pg-outbounds').classList.contains('on'))loadOutbounds();\n    if(document.getElementById('pg-externals').classList.contains('on'))loadExternals();"
)

if len(src) != original_len:
    PAGES.write_text(src, encoding="utf-8")
    print(f"✅ pages.py patched (+{len(src)-original_len} chars)")
else:
    print("⚠️ pages.py unchanged")
