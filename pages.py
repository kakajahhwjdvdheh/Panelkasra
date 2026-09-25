# pages.py — bogzarnet Panel v2.0.0 (بدون لوگوی base64)

# جایگزین لوگو با یک SVG ساده‌ی داخلی
# لوگوی bogzarnet (به‌صورت base64 داخلی، بدون نیاز به هاست خارجی)
LOGO_INLINE = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" '
    'width="100%" height="100%" style="display:block;border-radius:50%">'
    '<defs><linearGradient id="bg1" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#ef234f"/>'
    '<stop offset="1" stop-color="#9f1239"/>'
    '</linearGradient></defs>'
    '<circle cx="50" cy="50" r="48" fill="url(#bg1)"/>'
    '<path d="M30 38h9v34h-9zM45 30h10v42H45zM60 38h9v34h-9z" fill="#fff"/>'
    '</svg>'
)



LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>bogzarnet Panel · ورود</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#09090b;--accent:#ef234f;--accent-2:#fb3b62;--accent-dark:#9f1239;--text:#f7f7f8;--muted:#a1a1aa;--dim:#71717a;--border:rgba(255,255,255,.075);--border-red:rgba(225,29,72,.35);--shadow:0 24px 70px rgba(0,0,0,.45)}
html,body{height:100%;overflow:hidden}
body{font-family:'Vazirmatn',Tahoma,Arial,sans-serif;background:var(--bg);color:var(--text);display:flex;align-items:center;justify-content:center;padding:20px;background-image:radial-gradient(circle at 15% 0%,rgba(225,29,72,.12),transparent 34%),radial-gradient(circle at 95% 100%,rgba(159,18,57,.10),transparent 30%)}
.bg{position:fixed;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(239,35,79,.1),transparent 70%);z-index:0}
.grid{position:fixed;inset:0;background-image:linear-gradient(rgba(239,35,79,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(239,35,79,.04) 1px,transparent 1px);background-size:44px 44px;z-index:0;opacity:.5}
.orb{position:fixed;border-radius:50%;filter:blur(90px);z-index:0;animation:fl 9s ease-in-out infinite}
.o1{width:380px;height:380px;background:rgba(239,35,79,.1);top:-100px;right:-80px}
.o2{width:280px;height:280px;background:rgba(159,18,57,.08);bottom:-60px;left:-60px;animation-delay:4s}
@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-18px)}}
.wrap{position:relative;z-index:10;width:100%;max-width:400px}
.card{background:linear-gradient(145deg,rgba(24,24,30,.98),rgba(9,9,12,.98));border:1px solid rgba(225,29,72,.26);border-radius:20px;padding:38px 34px 34px;backdrop-filter:blur(24px);box-shadow:0 30px 90px rgba(0,0,0,.55),0 0 40px rgba(225,29,72,.09)}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:28px}
.brand-img{width:48px;height:48px;border-radius:50%;overflow:hidden;border:1px solid var(--border-red);box-shadow:0 0 20px rgba(239,35,79,.35);flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#0d0d11}
.brand-img svg{width:100%;height:100%;border-radius:50%}
.brand-name{font-size:16px;font-weight:700;color:var(--text)}
.brand-sub{font-size:11px;color:var(--accent-2);margin-top:2px;font-weight:700}
h1{font-size:21px;font-weight:700;color:var(--text);margin-bottom:5px;letter-spacing:-.02em}
.sub{font-size:12px;color:var(--muted);margin-bottom:24px;line-height:1.6}
.hint{display:flex;align-items:center;gap:10px;background:rgba(225,29,72,.08);border:1px solid rgba(225,29,72,.24);border-radius:10px;padding:10px 14px;margin-bottom:20px}
.hint-label{font-size:11px;color:var(--muted);flex:1}
.hint-val{font-family:ui-monospace,monospace;font-size:14px;font-weight:700;color:#fb7185;background:rgba(225,29,72,.1);border:1px solid rgba(225,29,72,.25);padding:3px 11px;border-radius:7px;cursor:pointer;transition:.15s;letter-spacing:.08em}
.hint-val:hover{background:rgba(225,29,72,.22)}
.field{margin-bottom:18px}
.field label{display:block;font-size:10.5px;font-weight:600;color:var(--muted);margin-bottom:7px;text-transform:uppercase;letter-spacing:.06em}
.inp-wrap{position:relative}
input[type=text],input[type=password]{width:100%;padding:13px 44px 13px 16px;border-radius:11px;border:1px solid #2b2b34;background:#0d0d11;color:var(--text);font-family:inherit;font-size:14px;outline:none;transition:.2s}
input[type=text]:focus,input[type=password]:focus{border-color:var(--accent);background:#0f0f14;box-shadow:0 0 0 3px rgba(225,29,72,.13)}
.ic{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--dim);font-size:18px;pointer-events:none;transition:.2s}
input:focus+.ic{color:var(--accent-2)}
.err{display:none;background:rgba(239,68,68,.08);border:1px solid rgba(239,68,68,.2);border-radius:10px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:#F87171;align-items:center;gap:8px}
.err.show{display:flex}
.btn{width:100%;padding:13px;border-radius:11px;border:none;cursor:pointer;background:linear-gradient(135deg,#f12b57,#a90f39);color:#fff;font-family:inherit;font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 4px 20px rgba(239,35,79,.35);transition:.2s}
.btn:hover{transform:translateY(-1px);box-shadow:0 6px 24px rgba(239,35,79,.45)}
.btn:disabled{opacity:.5;cursor:not-allowed}
.footer{margin-top:22px;padding-top:18px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:center;gap:8px;font-size:11px;color:var(--dim)}
.footer a{color:var(--accent-2);font-weight:600;text-decoration:none;display:flex;align-items:center;gap:4px}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<div class="bg"></div><div class="grid"></div>
<div class="orb o1"></div><div class="orb o2"></div>
<div class="wrap">
  <div class="card">
    <div class="brand">
      <div class="brand-img">__LOGO_INLINE__</div>
      <div><div class="brand-name">bogzarnet</div><div class="brand-sub">Panel v2.0.0</div></div>
    </div>
    <h1>ورود به پنل <span style="font-size:12px;color:var(--accent-2)">/ Admin Sign In</span></h1>
    <p class="sub">با نام کاربری، رمز عبور و کد امنیتی وارد شوید · Sign in securely</p>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
      <div class="hint">
      <span class="hint-label">پیش‌فرض اولیه · Initial defaults</span>
      <span class="hint-val">Amirparsa / bogzarnet</span>
    </div>
    <form id="form">
      <div class="field">
        <label>نام کاربری</label>
        <div class="inp-wrap"><input type="text" id="username" placeholder="نام کاربری مدیر" autocomplete="username" autofocus required><i class="ti ti-user ic"></i></div>
      </div>
      <div class="field">
        <label>رمز عبور · Password</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="رمز عبور را وارد کنید" required>
          <i class="ti ti-lock ic"></i>
        </div>
      </div>
      <div class="field">
        <label>کد امنیتی · Security code</label>
        <div style="display:flex;gap:8px;align-items:center">
          <div style="flex:1;display:flex;align-items:center;justify-content:center;letter-spacing:.28em;font:800 20px ui-monospace;color:#fff;background:linear-gradient(135deg,rgba(239,35,79,.28),rgba(35,35,48,.7));border:1px solid rgba(239,35,79,.35);border-radius:11px;padding:10px;user-select:none" id="captcha-display">__CAPTCHA_CODE__</div>
          <input type="text" id="captcha" maxlength="5" autocomplete="off" placeholder="کد / code" required style="width:42%;text-transform:uppercase">
        </div>
        <input type="hidden" id="captcha-id" value="__CAPTCHA_ID__">
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
    </form>
    <div class="footer">پشتیبانی <a href="https://t.me/bogzarnet" target="_blank"><i class="ti ti-brand-telegram"></i>@bogzarnet</a></div>
  </div>
</div>
<script>
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:document.getElementById('username').value,password:document.getElementById('pw').value,captcha_id:document.getElementById('captcha-id').value,captcha_code:document.getElementById('captcha').value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به داشبورد';
  }
});
</script>
</body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>bogzarnet Panel</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#09090b;--bg2:#0e0e12;--bg3:#131319;
  --card:#121217;--card-b:rgba(239,35,79,0.16);--card-bh:rgba(239,35,79,0.34);
  --accent:#ef234f;--accent2:#ff5578;--accent-d:rgba(239,35,79,0.1);
  --green:#22c55e;--green-bg:rgba(34,197,94,0.1);--green-t:#4ade80;
  --red:#ef4444;--red-bg:rgba(239,68,68,0.1);--red-t:#f87171;
  --amber:#f59e0b;--amber-bg:rgba(245,158,11,0.1);--amber-t:#fbbf24;
  --purple:#a855f7;--purple-bg:rgba(168,85,247,0.1);
  --t1:#f7f7f8;--t2:#a1a1aa;--t3:#71717a;
  --sidebar-w:248px;--radius:16px;
  --shadow:0 4px 24px rgba(0,0,0,0.45);
}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;background-image:radial-gradient(circle at 15% 0%,rgba(239,35,79,.12),transparent 34%),radial-gradient(circle at 95% 100%,rgba(159,18,57,.10),transparent 30%)}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:#2a2a33;border-radius:3px}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:rgba(10,10,13,.94);border-left:1px solid rgba(239,35,79,.18);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;backdrop-filter:blur(20px)}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b)}
.logo-img{width:38px;height:38px;border-radius:50%;overflow:hidden;border:1px solid rgba(239,35,79,.65);box-shadow:0 0 20px rgba(239,35,79,.28);flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#0d0d11}
.logo-img svg{width:100%;height:100%}
.logo-name{font-size:13.5px;font-weight:700;color:#fff}
.logo-sub{font-size:10px;color:var(--accent2);margin-top:1px;font-weight:700}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:#a1a1aa;font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .15s;margin:3px 10px;border-radius:12px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0;color:var(--accent2)}
.nav-it:hover{background:var(--accent-d);color:#fff}
.nav-it.on{background:linear-gradient(90deg,rgba(239,35,79,.22),rgba(239,35,79,.06));color:#fff;border-right:3px solid var(--accent);font-weight:600}
.nav-badge{margin-right:auto;background:rgba(239,35,79,0.15);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.15s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:#fff}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.2);cursor:pointer;width:100%;transition:.15s;margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.2)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:rgba(10,10,13,.94);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px;backdrop-filter:blur(20px)}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:28px;height:28px;border-radius:50%;overflow:hidden;box-shadow:0 0 8px rgba(239,35,79,.35);display:flex;align-items:center;justify-content:center;background:#0d0d11}
.mob-logo svg{width:100%;height:100%}
.mob-title{color:#fff;font-size:13px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0}
.pg{display:none}
.pg.on{display:block;animation:fi .2s ease}
@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px;padding-bottom:18px;border-bottom:1px solid var(--card-b)}
.tb-title{font-size:18px;font-weight:800;color:#fff;display:flex;align-items:center;gap:8px;letter-spacing:-.02em}
.tb-title i{color:var(--accent2);font-size:20px}
.tb-sub{font-size:11px;color:var(--t2);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:#c084fc}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.metric{background:linear-gradient(145deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:var(--radius);padding:17px;transition:all .2s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent2);font-size:17px;border:1px solid rgba(239,35,79,.2)}
.m-icon.suc{background:var(--green-bg);color:var(--green-t);border-color:rgba(34,197,94,.2)}
.m-icon.pur{background:var(--purple-bg);color:#c084fc;border-color:rgba(168,85,247,.2)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:#fff;line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}
.vless-box{background:linear-gradient(135deg,var(--bg3) 0%,var(--bg2) 100%);border:1px solid var(--card-b);border-radius:18px;padding:20px 22px;margin-bottom:18px;box-shadow:var(--shadow)}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent2);font-size:15px}
.vl-code{background:rgba(4,4,7,.55);border:1px solid var(--card-b);border-radius:9px;padding:13px 15px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.8}
.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:12px;font-weight:500;border-radius:9px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}
.btn i{font-size:13px}
.btn-p{background:linear-gradient(135deg,#f12b57,#a90f39);color:#fff;box-shadow:0 3px 14px rgba(239,35,79,.35)}
.btn-p:hover{background:linear-gradient(135deg,#ff5578,#f12b57);transform:translateY(-1px)}
.btn-o{background:transparent;border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:var(--accent-d);color:#fff}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(239,35,79,.2)}
.btn-g:hover{background:rgba(239,35,79,.2)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.2)}
.btn-d:hover{background:rgba(239,68,68,.2)}
.btn-pur{background:var(--purple-bg);color:#c084fc;border:1px solid rgba(168,85,247,.2)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,.2)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:5px}
.card{background:linear-gradient(145deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;backdrop-filter:blur(20px)}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:12.5px;font-weight:700;color:#fff;margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent2)}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(239,35,79,.06);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:#fff;font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px}
.ch-sm{position:relative;height:185px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:34px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;bottom:3px;transition:.2s}
.tog.on{background:var(--green)}
.tog.on::after{bottom:18px}
.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:9px 12px;border-radius:9px;border:1px solid #2b2b34;background:#0d0d11;color:#fff;font-family:inherit;font-size:12px;outline:none;transition:.15s;min-width:100px}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(239,35,79,.13)}
.fs option{background:#0d0d11}
.cl{background:var(--accent-d);border:1px solid rgba(239,35,79,.15);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent2);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(245,158,11,.2);color:var(--amber-t)}

/* Create panel */
.create-panel{background:linear-gradient(155deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px;backdrop-filter:blur(20px)}
.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px}
.cp-head-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 18px rgba(239,35,79,.35)}
.cp-head-title{font-size:15px;font-weight:800;color:#fff}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 24px 22px}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,.2);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:11px}
.cp-block-label i{color:var(--accent2);font-size:14px}
.cp-input-full{width:100%;padding:10px 13px;border-radius:10px;border:1px solid #2b2b34;background:#0d0d11;color:#fff;font-family:inherit;font-size:12.5px;outline:none}
.cp-input-full:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(239,35,79,.13)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:8px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;white-space:nowrap}
.chip:hover{background:rgba(239,35,79,.18);color:var(--accent2)}
.chip.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 10px rgba(239,35,79,.35)}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.proto-card{border:1.5px solid var(--card-b);border-radius:13px;padding:13px 12px;cursor:pointer;transition:.18s;text-align:center;position:relative;background:rgba(0,0,0,.15)}
.proto-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(239,35,79,.1)}
.proto-card-check{position:absolute;top:7px;left:7px;width:16px;height:16px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.18s}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent2);display:flex;align-items:center;justify-content:center;font-size:16px;margin:0 auto 8px}
.proto-card.active .proto-card-icon{background:var(--accent);color:#fff}
.proto-card-title{font-size:11px;font-weight:800;color:#fff}
.proto-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent2);font-size:15px;flex-shrink:0}
.cp-submit-btn{background:linear-gradient(135deg,#f12b57,#a90f39);color:#fff;border:none;border-radius:13px;padding:13px 26px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(239,35,79,.35);transition:.18s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(239,35,79,.45)}

/* Server panel */
.srv-panel{background:linear-gradient(155deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);backdrop-filter:blur(20px)}
.srv-hero{display:flex;align-items:center;gap:14px;padding:22px 24px;border-bottom:1px solid var(--card-b);background:linear-gradient(115deg,rgba(239,35,79,.15),rgba(23,23,30,.28))}
.srv-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(239,35,79,.35)}
.srv-hero-domain{font-size:15px;font-weight:800;color:#fff;word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px}
.srv-tile{display:flex;align-items:center;gap:11px;background:rgba(255,255,255,.03);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;transition:.18s}
.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.srv-tile-icon{width:34px;height:34px;border-radius:10px;background:rgba(239,35,79,.11);color:var(--accent2);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12px;font-weight:700;color:#fff;word-break:break-word}

/* Password panel */
.pw-panel{background:linear-gradient(155deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);backdrop-filter:blur(20px)}
.pw-hero{display:flex;align-items:center;gap:14px;padding:22px 24px 18px}
.pw-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(139,92,246,.35)}
.pw-hero-title{font-size:15px;font-weight:800;color:#fff}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:2px 24px 22px}
.pw-field{position:relative;margin-bottom:13px}
.pw-field label{display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}
.pw-input{width:100%;padding:11px 42px 11px 14px;border-radius:11px;border:1px solid #2b2b34;background:#0d0d11;color:#fff;font-family:inherit;font-size:12.5px;outline:none}
.pw-input:focus{border-color:var(--purple);box-shadow:0 0 0 3px rgba(168,85,247,.13)}
.pw-eye{position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.pw-eye:hover{color:#c084fc}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,var(--purple),#6D48D6);color:#fff;border:none;border-radius:12px;padding:12px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 18px rgba(139,92,246,.32);transition:.18s}
.pw-submit:hover{transform:translateY(-2px)}

/* Configs list */
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:linear-gradient(145deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:14px;transition:all .2s;backdrop-filter:blur(20px)}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:var(--shadow)}
.cfg-card.is-off{opacity:.6}
.cfg-card.is-exp{opacity:.78}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px;flex-wrap:wrap}
.cfg-status-dot{width:9px;height:9px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:#fff}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);background:var(--accent-d);padding:2px 7px;border-radius:5px;cursor:pointer}
.cfg-uuid-mini:hover{background:rgba(239,35,79,.2)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:5px;border-radius:4px;background:rgba(239,35,79,0.1);overflow:hidden}
.ubar-f{height:100%;border-radius:4px;transition:width .4s ease}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.proto-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;white-space:nowrap}
.pc-ws{background:var(--accent-d);color:var(--accent2)}
.pc-xhttp{background:var(--purple-bg);color:#c084fc}
.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:#c084fc;font-size:11px}

/* Sub groups */
.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px}
.sub-card{background:linear-gradient(145deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:20px;overflow:hidden;transition:all .25s;backdrop-filter:blur(20px)}
.sub-card:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:var(--shadow)}
.sub-card-top{background:linear-gradient(155deg,rgba(168,85,247,.1) 0%,transparent 65%);padding:20px 20px 16px}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:13px}
.sub-card-icon{width:46px;height:46px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 16px rgba(139,92,246,.35)}
.sub-card-name-v2{font-size:15.5px;font-weight:800;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6}
.sub-card-lock-badge{flex-shrink:0;width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}
.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:16px;background:rgba(0,0,0,.2);border:1px solid var(--card-b);border-radius:13px;overflow:hidden}
.sub-card-stat{padding:11px 8px;text-align:center;border-left:1px solid var(--card-b)}
.sub-card-stat:last-child{border-left:none}
.sub-card-stat-val{font-size:15px;font-weight:800;color:#fff;line-height:1.2}
.sub-card-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}
.sub-card-url-row{margin:14px 20px 0;background:rgba(168,85,247,.08);border:1px dashed rgba(168,85,247,.25);border-radius:11px;padding:9px 12px;display:flex;align-items:center;gap:8px}
.sub-card-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:#c084fc;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-url-copy{background:none;border:none;color:var(--purple);cursor:pointer;font-size:13px;padding:3px;display:flex;flex-shrink:0}
.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}
.subs-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:20px;grid-column:1/-1}
.subs-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--purple-bg);display:flex;align-items:center;justify-content:center;font-size:28px;color:#c084fc;margin:0 auto 16px}
.subs-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.subs-empty-v2-sub{font-size:11px;color:var(--t3)}
.subs-toolbar{display:flex;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:11px 40px 11px 15px;border-radius:12px;border:1px solid #2b2b34;background:#0d0d11;color:#fff;font-family:inherit;font-size:12.5px;outline:none}
.subs-search input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(239,35,79,.13)}
.subs-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}

/* Modals */
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.modal-bg.open{display:flex}
.modal,.modal-v2{background:linear-gradient(145deg,rgba(28,28,37,.96),rgba(12,12,17,.96));border:1px solid var(--card-b);border-radius:22px;padding:0;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;animation:fi .2s ease;box-shadow:0 24px 70px rgba(0,0,0,.6)}
.modal{padding:28px 26px}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer}
.modal-title{font-size:16px;font-weight:700;color:#fff;margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--accent2)}
.modal-v2-head{background:linear-gradient(155deg,rgba(239,35,79,.15) 0%,transparent 65%);padding:18px 22px 14px;position:relative}
.modal-v2-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:9px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t)}
.modal-v2-icon{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;margin-bottom:10px;box-shadow:0 8px 18px rgba(239,35,79,.4)}
.modal-v2-title{font-size:15.5px;font-weight:800;color:#fff}
.modal-v2-sub{font-size:10.5px;color:var(--t3);margin-top:3px;line-height:1.6}
.modal-v2-body{padding:16px 22px 20px;border-top:1px solid var(--card-b)}
.modal-v2-field{margin-bottom:11px}
.modal-v2-field label{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.modal-v2-field label i{color:var(--accent2);font-size:13px}
.modal-v2-input{width:100%;padding:9px 13px;border-radius:11px;border:1px solid #2b2b34;background:#0d0d11;color:#fff;font-family:inherit;font-size:12.5px;outline:none}
.modal-v2-input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(239,35,79,.13)}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-hint{background:var(--accent-d);border:1px solid rgba(239,35,79,.18);border-radius:11px;padding:9px 12px;font-size:10px;color:var(--t2);display:flex;gap:7px;line-height:1.6;margin-top:2px}
.modal-v2-hint i{font-size:14px;color:var(--accent2)}
.modal-v2-footer{display:flex;gap:8px;margin-top:15px}
.modal-v2-btn-cancel,.modal-v2-btn-submit{padding:10px;border-radius:11px;font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:6px}
.modal-v2-btn-cancel{flex:.6;background:transparent;border:1px solid var(--card-b);color:var(--t2)}
.modal-v2-btn-cancel:hover{background:var(--accent-d);color:#fff}
.modal-v2-btn-submit{flex:1;background:linear-gradient(135deg,#f12b57,#a90f39);color:#fff;border:none;box-shadow:0 6px 18px rgba(239,35,79,.4)}
.modal-v2-btn-submit:hover{transform:translateY(-2px)}

/* Toast */
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:linear-gradient(145deg,rgba(28,28,37,.96),rgba(12,12,17,.96));border:1px solid var(--card-b);color:#fff;border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap;backdrop-filter:blur(18px)}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(34,197,94,.35);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.35);background:var(--red-bg);color:var(--red-t)}

/* Footer */
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}

/* Connections */
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:18px}
.conn-hero-tile{background:linear-gradient(145deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:16px;padding:16px 18px}
.conn-hero-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;margin-bottom:10px}
.conn-hero-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.conn-hero-val{font-size:21px;font-weight:800;color:#fff;line-height:1}
.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.conn-card-v2{background:linear-gradient(145deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:18px;overflow:hidden;backdrop-filter:blur(20px)}
.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 17px 13px}
.conn-avatar{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--green),#0D9668);display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;box-shadow:0 4px 14px rgba(34,197,94,.3)}
.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:#fff;display:flex;align-items:center;gap:6px}
.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex}
.conn-ip-copy:hover{color:var(--accent2)}
.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px}
.conn-status-pill{font-size:9px;font-weight:800;padding:4px 9px;border-radius:20px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;gap:4px;white-space:nowrap}
.conn-card-v2-divider{height:1px;background:var(--card-b);margin:0 17px}
.conn-card-v2-body{padding:14px 17px 16px}
.conn-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:20px}
.conn-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--t3);margin:0 auto 16px}
.conn-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}

/* Logs */
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid rgba(239,35,79,.06)}
.log-item:last-child{border-bottom:none}
.log-ic{width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.log-ic.err{background:var(--red-bg);color:var(--red-t)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-ic.info{background:var(--accent-d);color:var(--accent2)}
.log-msg{font-size:12.5px;color:#fff;line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:8.5px;padding:1px 7px;border-radius:10px;background:var(--accent-d);color:var(--accent2);font-weight:700}
.erow{padding:9px 0;border-bottom:1px solid rgba(239,35,79,.06)}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px}
.emsg{color:var(--red-t);font-family:ui-monospace,monospace;background:var(--red-bg);padding:6px 9px;border-radius:6px;word-break:break-all;font-size:10.5px}

.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}

@media(max-width:1050px){
  .sidebar{transform:translateX(100%);transition:transform .25s}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 40px rgba(0,0,0,.5)}
  .sb-close{display:flex}
  .main{margin-right:0;padding-top:70px}
  .mob-top{display:flex}
  .metrics,.conn-hero{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
  .cp-row{grid-template-columns:1fr}
  .proto-cards{grid-template-columns:1fr}
  .conn-grid-v2,.sub-grid,.cfg-grid{grid-template-columns:1fr}
}
@media(max-width:500px){
  .metrics,.conn-hero{grid-template-columns:1fr}
  .main{padding:62px 12px 50px}
}
</style>
</head>
<body>
<div class="toast" id="toast"></div>

<!-- ============ MODAL: manage sub links ============ -->
<div class="modal-bg" id="modal-links">
  <div class="modal-v2" style="max-width:500px">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-links')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-link-plus"></i></div>
      <div class="modal-v2-title">مدیریت کانفیگ‌های <span id="modal-sub-name" style="color:var(--accent2)">—</span></div>
      <div class="modal-v2-sub">کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید</div>
    </div>
    <div class="modal-v2-body">
      <div style="display:flex;gap:8px;margin-bottom:11px">
        <button class="btn btn-sm btn-g" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> انتخاب همه</button>
        <button class="btn btn-sm btn-g" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> لغو همه</button>
        <span style="margin-right:auto;font-size:10.5px;color:var(--t3)" id="lmodal-count">۰ انتخاب شده</span>
      </div>
      <div class="modal-v2-field" style="margin-bottom:10px">
        <input class="modal-v2-input" type="text" id="lmodal-search-inp" placeholder="جستجو..." oninput="filterLmodal(this.value)">
      </div>
      <div id="modal-links-body" style="max-height:340px;overflow-y:auto">در حال بارگذاری...</div>
      <div class="modal-v2-footer">
        <button class="modal-v2-btn-cancel" onclick="closeModal('modal-links')">بستن</button>
        <button class="modal-v2-btn-submit" onclick="saveSubLinks()"><i class="ti ti-check"></i> ذخیره</button>
      </div>
    </div>
  </div>
</div>

<!-- ============ MODAL: create sub group ============ -->
<div class="modal-bg" id="modal-create-sub">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-folder-plus"></i></div>
      <div class="modal-v2-title">ساخت گروه جدید</div>
      <div class="modal-v2-sub">یک صفحه پابلیک مجزا برای مدیریت کانفیگ‌ها بسازید</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> نام گروه</label>
        <input class="modal-v2-input" id="ns-name" placeholder="مثلاً: کانال تلگرام">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> توضیحات (اختیاری)</label>
        <input class="modal-v2-input" id="ns-desc" placeholder="توضیح کوتاه">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-lock"></i> رمز صفحه پابلیک (اختیاری)</label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="خالی = بدون رمز">
      </div>
      <div class="modal-v2-footer">
        <button class="modal-v2-btn-cancel" onclick="closeModal('modal-create-sub')">انصراف</button>
        <button class="modal-v2-btn-submit" onclick="createSub()"><i class="ti ti-folder-plus"></i> ساخت گروه</button>
      </div>
    </div>
  </div>
</div>

<!-- ============ MODAL: edit link ============ -->
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> ویرایش کانفیگ</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label>عنوان</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>سهمیه (0 = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label>انقضا (روز، 0 = بدون تغییر)</label><input class="fi" id="el-exp" type="number" min="0" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label>یادداشت</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>Fingerprint</label>
        <select class="fs" id="el-fp" style="width:100%">
          <option value="chrome">chrome</option><option value="firefox">firefox</option>
          <option value="safari">safari</option><option value="ios">ios</option>
          <option value="android">android</option><option value="edge">edge</option>
          <option value="random">random</option><option value="randomized">randomized</option>
        </select>
      </div>
      <div class="fg" style="flex:1"><label>ALPN</label><input class="fi" id="el-alpn" placeholder="h2,http/1.1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>پورت</label><input class="fi" id="el-port" type="number" min="1" max="65535" style="width:100%"></div>
      <div class="fg" style="flex:1"><label>محدودیت IP</label><input class="fi" id="el-iplimit" type="number" min="0" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>محدودیت سرعت</label><input class="fi" id="el-speed" type="number" min="0" step="0.5" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:16px">
      <label>خروجی ترافیک</label>
      <select class="fs" id="el-outbound" style="width:100%"></select>
    </div>
    <div style="display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">انصراف</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> ذخیره</button>
    </div>
  </div>
</div>

<!-- ============ MODAL: create outbound ============ -->
<div class="modal-bg" id="modal-create-outbound">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-outbound')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-route"></i></div>
      <div class="modal-v2-title">خروجی جدید</div>
      <div class="modal-v2-sub">مسیر خروج ترافیک را تعریف کنید</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> نام</label>
        <input class="modal-v2-input" id="no-name" placeholder="مثلاً: WARP Germany">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-category"></i> نوع</label>
        <select class="modal-v2-input" id="no-type" onchange="onOutboundTypeChange()">
          <option value="socks5">SOCKS5</option>
          <option value="vless">VLESS</option>
        </select>
      </div>
      <div id="no-fields-socks5">
        <div class="modal-v2-field"><label><i class="ti ti-world"></i> آدرس</label><input class="modal-v2-input" id="no-address" placeholder="127.0.0.1"></div>
        <div class="modal-v2-field"><label><i class="ti ti-route"></i> پورت</label><input class="modal-v2-input" id="no-port" type="number" placeholder="1080"></div>
        <div class="modal-v2-field"><label><i class="ti ti-user"></i> یوزر</label><input class="modal-v2-input" id="no-username" placeholder="(اختیاری)"></div>
        <div class="modal-v2-field"><label><i class="ti ti-key"></i> پسورد</label><input class="modal-v2-input" id="no-password" type="password" placeholder="(اختیاری)"></div>
      </div>
      <div id="no-fields-vless" style="display:none">
        <div class="modal-v2-field"><label><i class="ti ti-link"></i> لینک VLESS</label><input class="modal-v2-input" id="no-url" placeholder="vless://..."></div>
      </div>
      <div class="modal-v2-footer">
        <button class="modal-v2-btn-cancel" onclick="closeModal('modal-create-outbound')">انصراف</button>
        <button class="modal-v2-btn-submit" onclick="createOutbound()"><i class="ti ti-check"></i> ساخت</button>
      </div>
    </div>
  </div>
</div>

<!-- ============ MODAL: create external ============ -->
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
      <div class="modal-v2-field"><label><i class="ti ti-link"></i> لینک کانفیگ</label><input class="modal-v2-input" id="ne-url" placeholder="vless://..."></div>
      <div class="modal-v2-footer">
        <button class="modal-v2-btn-cancel" onclick="closeModal('modal-create-external')">انصراف</button>
        <button class="modal-v2-btn-submit" onclick="createExternalConfig()" style="background:linear-gradient(135deg,#22c55e,#15803d)"><i class="ti ti-check"></i> افزودن</button>
      </div>
    </div>
  </div>
</div>

<!-- ============ MOBILE TOP ============ -->
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo">__LOGO_INLINE__</div>
    <span class="mob-title">bogzarnet</span>
  </div>
  <div class="mob-right">
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>

<!-- ============ SIDEBAR ============ -->
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-img">__LOGO_INLINE__</div>
    <div><div class="logo-name">bogzarnet</div><div class="logo-sub">Panel v2.0.0</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">پنل</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> گروه‌های ساب <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> سابسکریپشن</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-sec">سیستم</div>
    <div class="nav-it" data-pg="outbounds"><i class="ti ti-route"></i> خروجی‌ها <span class="nav-badge" id="outbounds-nb">0</span></div>
    <div class="nav-it" data-pg="externals"><i class="ti ti-world-upload"></i> سرورهای خارجی <span class="nav-badge" id="externals-nb">0</span></div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> خطاها</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> تست WebSocket</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
    <div class="nav-it" data-pg="telegram"><i class="ti ti-brand-telegram"></i> ربات تلگرام</div>
    <div class="nav-it" data-pg="support"><i class="ti ti-headset"></i> پشتیبانی</div>
  </div>
  <div class="sb-foot">
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>

<main class="main">

<!-- ============ PAGE: OVERVIEW ============ -->
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="tb-sub" id="last-upd">در حال بارگذاری...</div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot dg pulse"></span> فعال</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
    </div>
  </div>
  <div class="metrics">
    <div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">اتصالات فعال</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span class="dot dg pulse"></span> زنده</div></div>
    <div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label">کل ترافیک</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">از راه‌اندازی</div></div>
    <div class="metric"><div class="m-icon suc"><i class="ti ti-link"></i></div><div class="m-label">کانفیگ فعال</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">از کل</div></div>
    <div class="metric"><div class="m-icon pur"><i class="ti ti-folders"></i></div><div class="m-label">گروه‌های ساب</div><div class="m-val" id="m-subs">—</div><div class="m-sub">فعال</div></div>
  </div>
  <div class="vless-box">
    <div class="vl-header">
      <div class="vl-title"><i class="ti ti-link"></i> لینک پیش‌فرض (بدون محدودیت)</div>
      <span class="badge bg-blue"><span class="dot db"></span> TLS 443 · WS</span>
    </div>
    <div class="vl-code" id="vless-main">در حال دریافت...</div>
    <div class="vl-actions">
      <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> کپی</button>
      <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> کانفیگ محدود</button>
      <button class="btn btn-pur" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> گروه‌های ساب</button>
    </div>
  </div>
  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> ترافیک ساعتی (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-donut"></i> توزیع</div><div class="ch-sm"><canvas id="ch2"></canvas></div></div>
  </div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-activity"></i> وضعیت سرویس</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-folders"></i> Sub Groups</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> Subscription</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-route"></i> Outbound Engine</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptime-inline">—</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="ml-auto badge bg-blue" id="lsummary-badge">۰</span></div>
      <div id="lsummary">—</div>
    </div>
  </div>
  <div class="dash-footer">
    <span class="df-text">bogzarnet Panel v2.0.0 · Railway Ready</span>
    <span class="df-text">تیم bogzarnet · amirparsa</span>
    <a class="df-link" href="https://t.me/bogzarnet_support" target="_blank"><i class="ti ti-headset"></i> پشتیبانی</a>
  </div>
</section>

<!-- ============ PAGE: LINKS ============ -->
<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ساخت و مدیریت کانفیگ</div></div>
    <div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">۰ کانفیگ</span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">ساخت کانفیگ جدید</div>
        <div class="cp-head-sub">UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> شناسه کانفیگ</div>
          <input class="cp-input-full" id="nl-label" placeholder="مثلاً: کاربر علی">
          <div class="cp-mini-row"><input class="cp-input-full" id="nl-note" placeholder="یادداشت (اختیاری)"></div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> گروه ساب و انقضا</div>
          <select class="cp-input-full fs" id="nl-sub"><option value="">— بدون گروه —</option></select>
          <div class="cp-mini-row"><input class="cp-input-full" id="nl-exp" type="number" min="0" placeholder="انقضا (روز) · 0 = نامحدود"></div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">نامحدود</span>
            <span class="chip" onclick="setExpiry(7,this)">۷ روز</span>
            <span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span>
            <span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> سهمیه ترافیک</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">۱ GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">۵ GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">۱۰ GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">۵۰ GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> پروتکل انتقال</div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WebSocket</option>
          <option value="xhttp-packet-up">XHTTP packet-up</option>
          <option value="xhttp-stream-up">XHTTP stream-up</option>
        </select>
        <div class="proto-cards">
          <div class="proto-card active" data-val="vless-ws" onclick="selectProto('vless-ws',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-link"></i></div>
            <div class="proto-card-title">VLESS / WS</div>
            <div class="proto-card-desc">پایدار و همه‌منظوره</div>
          </div>
          <div class="proto-card" data-val="xhttp-packet-up" onclick="selectProto('xhttp-packet-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-bolt"></i></div>
            <div class="proto-card-title">XHTTP · packet</div>
            <div class="proto-card-desc">سازگار با CDN</div>
          </div>
          <div class="proto-card" data-val="xhttp-stream-up" onclick="selectProto('xhttp-stream-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-rocket"></i></div>
            <div class="proto-card-title">XHTTP · stream</div>
            <div class="proto-card-desc">تاخیر پایین‌تر</div>
          </div>
        </div>
      </div>
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-fingerprint"></i> Fingerprint</div>
          <select class="cp-input-full fs" id="nl-fp">
            <option value="chrome" selected>chrome</option>
            <option value="firefox">firefox</option>
            <option value="safari">safari</option>
            <option value="ios">ios</option>
            <option value="android">android</option>
            <option value="edge">edge</option>
            <option value="random">random</option>
            <option value="randomized">randomized</option>
          </select>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-antenna-bars-5"></i> ALPN</div>
          <select class="cp-input-full fs" id="nl-alpn-preset" onchange="onAlpnPresetChange()">
            <option value="">پیش‌فرض پروتکل</option>
            <option value="h2,http/1.1">h2,http/1.1</option>
            <option value="http/1.1">http/1.1</option>
            <option value="h2">h2</option>
            <option value="__custom__">دستی...</option>
          </select>
          <div class="cp-mini-row"><input class="cp-input-full" id="nl-alpn" placeholder="مقدار دستی" style="display:none"></div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-route"></i> پورت اتصال</div>
          <input class="cp-input-full" id="nl-port" type="number" min="1" max="65535" value="443">
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-users"></i> محدودیت IP</div>
          <input class="cp-input-full" id="nl-iplimit" type="number" min="0" value="0">
          <div class="chip-row" id="iplimit-chips">
            <span class="chip active" onclick="setIpLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setIpLimit(1,this)">۱</span>
            <span class="chip" onclick="setIpLimit(2,this)">۲</span>
            <span class="chip" onclick="setIpLimit(5,this)">۵</span>
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-gauge"></i> محدودیت سرعت</div>
          <div class="form-row">
            <input class="cp-input-full" id="nl-speed" type="number" min="0" step="0.5" value="0" style="flex:1">
            <select class="fs" id="nl-speed-unit" style="flex:0 0 100px">
              <option value="MBIT" selected>Mbps</option>
              <option value="KB">KB/s</option>
              <option value="MB">MB/s</option>
            </select>
          </div>
          <div class="chip-row" id="speed-chips">
            <span class="chip active" onclick="setSpeedLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setSpeedLimit(1,this)">۱</span>
            <span class="chip" onclick="setSpeedLimit(5,this)">۵</span>
            <span class="chip" onclick="setSpeedLimit(10,this)">۱۰</span>
            <span class="chip" onclick="setSpeedLimit(25,this)">۲۵</span>
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-route"></i> خروجی ترافیک</div>
          <select class="cp-input-full fs" id="nl-outbound"><option value="direct">مستقیم (Freedom)</option></select>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
      </div>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>

<!-- ============ PAGE: SUBGROUPS ============ -->
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-folders"></i> گروه‌های ساب</div><div class="tb-sub">هر گروه یک صفحه پابلیک مجزا دارد</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">۰ گروه</span>
      <button class="btn btn-p" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> گروه جدید</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search"><i class="ti ti-search"></i><input type="text" id="subs-search-inp" placeholder="جستجو..." oninput="filterSubs(this.value)"></div>
  </div>
  <div class="sub-grid" id="subs-grid"></div>
</section>

<!-- ============ PAGE: OUTBOUNDS ============ -->
<section class="pg" id="pg-outbounds">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-route"></i> خروجی‌ها</div><div class="tb-sub">مسیرهای خروج ترافیک (Freedom / Block / SOCKS5 / VLESS Chain)</div></div>
    <div class="tb-right">
      <span class="badge bg-blue" id="outbounds-pg-cnt">۰ خروجی</span>
      <button class="btn btn-p" onclick="openModal('modal-create-outbound')"><i class="ti ti-plus"></i> خروجی جدید</button>
    </div>
  </div>
  <div class="cl" style="margin-bottom:16px">
    <i class="ti ti-info-circle"></i>
    <span>خروجی‌ها مسیر عبور ترافیک کانفیگ‌ها رو مشخص می‌کنن. برای WARP از SOCKS5 لوکال استفاده کن.</span>
  </div>
  <div class="cfg-grid" id="outbounds-grid"></div>
  <div class="empty" id="outbounds-empty" style="display:none">
    <i class="ti ti-route-off"></i><p>هنوز خروجی سفارشی‌ای نساختی</p>
  </div>
</section>

<!-- ============ PAGE: EXTERNALS ============ -->
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
    <span>این کانفیگ‌ها <b>مستقیم</b> در ساب‌لینک کاربرا و صفحه پابلیک قرار می‌گیرن.</span>
  </div>
  <div class="cfg-grid" id="externals-grid"></div>
  <div class="empty" id="externals-empty" style="display:none">
    <i class="ti ti-world-off"></i><p>هنوز سرور خارجی‌ای اضافه نشده</p>
  </div>
</section>

<!-- ============ PAGE: LOGS ============ -->
<section class="pg" id="pg-logs">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div>
  </div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div></div>
</section>

<!-- ============ PAGE: ERRORS ============ -->
<section class="pg" id="pg-errors">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-alert-triangle"></i> خطاها</div></div>
    <div class="tb-right"><span class="badge bg-red" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div>
  </div>
  <div class="card"><div id="errs-full">—</div></div>
</section>

<!-- ============ PAGE: CONNECTIONS ============ -->
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div>
  </div>
  <div class="conn-hero">
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div><div class="conn-hero-label">اتصالات زنده</div><div class="conn-hero-val" id="ch-count">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-transfer"></i></div><div class="conn-hero-label">مجموع ترافیک</div><div class="conn-hero-val" id="ch-traffic">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-clock"></i></div><div class="conn-hero-label">میانگین مدت</div><div class="conn-hero-val" id="ch-avgdur">—</div></div>
    <div class="conn-hero-tile"><div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div><div class="conn-hero-label">IP یکتا</div><div class="conn-hero-val" id="ch-uniq">—</div></div>
  </div>
  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none"><div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div><div class="conn-empty-v2-title">هیچ اتصال فعالی نیست</div></div>
</section>

<!-- ============ PAGE: TRAFFIC ============ -->
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل مصرف</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>
  <div class="card"><div class="card-title"><i class="ti ti-activity"></i> روند مصرف</div><div class="ch"><canvas id="ch3"></canvas></div></div>
</section>

<!-- ============ PAGE: SUBSCRIPTIONS ============ -->
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> سابسکریپشن</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-rss"></i> سابسکریپشن تکی</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:12px">هر کانفیگ URL سابسکریپشن مخصوص دارد.</p>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-database"></i> سابسکریپشن کامل (ادمین)</div>
      <div class="sub-box" style="background:rgba(168,85,247,.07);border:1px solid rgba(168,85,247,.2);border-radius:10px;padding:14px;display:flex;gap:10px;align-items:center;flex-wrap:wrap">
        <span id="sub-all-url" style="font-family:ui-monospace,monospace;font-size:10.5px;color:#c084fc;flex:1;word-break:break-all">در حال دریافت...</span>
        <button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button>
      </div>
    </div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-folders"></i> لینک گروه‌ها</div>
    <div id="sub-groups-list">در حال بارگذاری...</div>
  </div>
</section>

<!-- ============ PAGE: SETTINGS ============ -->
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div></div></div>
  <div class="g2">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> آنلاین · Railway</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div><div class="srv-tile-label">پورت پیش‌فرض</div><div class="srv-tile-val">443 (TLS)</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div><div class="srv-tile-label">نسخه</div><div class="srv-tile-val">v2.0.0</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div><div class="srv-tile-label">ابزارها</div><div style="display:flex;gap:8px;margin-top:9px;flex-wrap:wrap"><button class="btn btn-o btn-sm" onclick="downloadBackup()"><i class="ti ti-download"></i> Backup</button><button class="btn btn-o btn-sm" onclick="exportActiveLinks()"><i class="ti ti-file-export"></i> Export</button></div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">تغییر رمز عبور</div>
          <div class="pw-hero-sub">رمز قوی انتخاب کنید</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field">
          <label>رمز فعلی</label>
          <input class="pw-input" type="password" id="cp-cur">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field">
          <label>رمز جدید</label>
          <input class="pw-input" type="password" id="cp-new">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field">
          <label>تکرار رمز جدید</label>
          <input class="pw-input" type="password" id="cp-cf">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
        </div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> ذخیره رمز جدید</button>
      </div>
    </div>
  </div>
</section>

<!-- ============ PAGE: SUPPORT ============ -->
<section class="pg" id="pg-support">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-headset"></i> پشتیبانی</div></div></div>
  <div class="srv-panel">
    <div class="srv-hero">
      <div class="srv-hero-icon"><i class="ti ti-headset"></i></div>
      <div class="srv-hero-text">
        <div class="srv-hero-domain">پشتیبانی bogzarnet</div>
        <div class="srv-hero-sub"><span class="dot dg pulse"></span> راه‌های ارتباطی</div>
      </div>
    </div>
    <div class="srv-tiles">
      <a class="srv-tile" href="https://t.me/bogzarnet" target="_blank"><div class="srv-tile-icon"><i class="ti ti-brand-telegram"></i></div><div><div class="srv-tile-label">تلگرام</div><div class="srv-tile-val">@bogzarnet</div></div></a>
      <a class="srv-tile" href="https://t.me/bogzarnet_support" target="_blank"><div class="srv-tile-icon"><i class="ti ti-message-circle"></i></div><div><div class="srv-tile-label">پشتیبانی</div><div class="srv-tile-val">@bogzarnet_support</div></div></a>
      <a class="srv-tile" href="https://bogzarnet.ir" target="_blank"><div class="srv-tile-icon"><i class="ti ti-world-www"></i></div><div><div class="srv-tile-label">وب‌سایت</div><div class="srv-tile-val">bogzarnet.ir</div></div></a>
      <a class="srv-tile" href="mailto:bogzarnet@gmail.com"><div class="srv-tile-icon"><i class="ti ti-mail"></i></div><div><div class="srv-tile-label">ایمیل</div><div class="srv-tile-val">bogzarnet@gmail.com</div></div></a>
    </div>
  </div>
</section>

<!-- ============ PAGE: TELEGRAM ============ -->
<section class="pg" id="pg-telegram">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-brand-telegram"></i> ربات تلگرام</div></div><div class="tb-right"><span class="badge bg-green" id="tg-status">در حال بررسی...</span></div></div>
  <div class="srv-panel">
    <div class="srv-hero"><div class="srv-hero-icon"><i class="ti ti-robot"></i></div><div class="srv-hero-text"><div class="srv-hero-domain">Telegram Operations</div><div class="srv-hero-sub">مدیریت ربات از داخل پنل</div></div></div>
    <div class="cp-body" style="padding:22px">
      <div class="cp-row">
        <div class="cp-block"><div class="cp-block-label"><i class="ti ti-key"></i> Bot Token</div><input class="cp-input-full" id="tg-token" type="password" placeholder="توکن"></div>
        <div class="cp-block"><div class="cp-block-label"><i class="ti ti-users"></i> Admin IDs</div><input class="cp-input-full" id="tg-admins" placeholder="123456789,987654321"></div>
      </div>
      <div style="display:flex;gap:12px;align-items:center;margin-top:18px;flex-wrap:wrap">
        <label><input id="tg-enabled" type="checkbox"> فعال‌سازی ربات</label>
        <button class="btn btn-p" onclick="saveTelegramSettings()"><i class="ti ti-device-floppy"></i> ذخیره</button>
      </div>
    </div>
  </div>
</section>

<!-- ============ PAGE: SECURITY ============ -->
<section class="pg" id="pg-security">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> امنیت</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-lock"></i> رمزنگاری</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> هش رمز</span><span class="sr-v">PBKDF2-SHA256</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> سشن</span><span class="sr-v">HttpOnly · 1Y</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-shield-check"></i> کنترل دسترسی</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> سهمیه</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> تاریخ انقضا</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> رمز صفحه پابلیک</span><span class="sr-v" style="color:var(--green-t)">● اختیاری</span></div>
    </div>
  </div>
</section>

<!-- ============ PAGE: TEST WS ============ -->
<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> تست WebSocket</div></div></div>
  <div class="card" style="max-width:660px">
    <div class="form-row" style="margin-bottom:12px">
      <div class="fg" style="flex:1"><label>UUID</label><input class="fi" id="ws-uuid" placeholder="UUID یک کانفیگ فعال" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> اتصال</button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> قطع</button>
    </div>
    <div class="form-row" style="margin-bottom:12px">
      <input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i></button>
    </div>
    <div style="background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:10px;padding:14px;height:250px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log">
      <p style="color:var(--t3)">منتظر اتصال...</p>
    </div>
  </div>
</section>

</main>

<script>
// ═══ Theme toggle disabled (dark only) ═══
document.getElementById('logout-btn').addEventListener('click',logout);

// ═══ Toast ═══
function toast(msg,type=''){
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
  const d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(d<=3)return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${toFa(d)} روز</span>`;
  return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${toFa(d)} روز</span>`;
}
function protoBadge(p){
  const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp-packet-up':['XHTTP · packet','pc-xhttp'],'xhttp-stream-up':['XHTTP · stream','pc-xhttp']};
  const v=m[p]||m['vless-ws'];
  return `<span class="proto-chip ${v[1]}">${v[0]}</span>`;
}

// ═══ Auth ═══
async function authF(url,opts={}){
  const r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}

// ═══ Modals ═══
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}

// ═══ Sidebar ═══
const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);

// ═══ Navigation ═══
function navTo(name){
  document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));
  document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));
  const loaders={
    links:loadLinks,
    connections:loadConns,
    errors:loadErrs,
    subscriptions:loadSubsPage,
    subgroups:loadSubs,
    logs:loadActivity,
    outbounds:loadOutbounds,
    externals:loadExternals
  };
  if(loaders[name])loaders[name]();
  closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));

// ═══ Form helpers ═══
function setQuota(val,unit,el){
  document.getElementById('nl-val').value = val===0?'':val;
  document.getElementById('nl-unit').value = unit;
  document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setExpiry(days,el){
  document.getElementById('nl-exp').value = days===0?'':days;
  document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function selectProto(val,el){
  document.getElementById('nl-proto').value = val;
  document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setIpLimit(n,el){
  document.getElementById('nl-iplimit').value = n;
  document.querySelectorAll('#iplimit-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setSpeedLimit(n,el){
  document.getElementById('nl-speed').value = n;
  document.getElementById('nl-speed-unit').value = 'MBIT';
  document.querySelectorAll('#speed-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function onAlpnPresetChange(){
  const p=document.getElementById('nl-alpn-preset').value;
  const inp=document.getElementById('nl-alpn');
  if(p==='__custom__'){inp.style.display='block';inp.value='';inp.focus();}
  else{inp.style.display='none';inp.value=p;}
}
function togglePwField(id,btn){
  const inp=document.getElementById(id);
  const icon=btn.querySelector('i');
  const toText=inp.type==='password';
  inp.type=toText?'text':'password';
  icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}

// ═══ Charts ═══
let ch1,ch2,ch3;
function initCharts(){
  const opts={
    responsive:true,maintainAspectRatio:false,
    interaction:{mode:'index',intersect:false},
    plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(13,13,17,.96)',borderColor:'rgba(239,35,79,.3)',borderWidth:1,titleColor:'#fff',bodyColor:'#a1a1aa',padding:11,cornerRadius:10,displayColors:false,callbacks:{label:v=>`${v.parsed.y.toFixed(2)} MB`}}},
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:'#71717a',font:{size:9,family:'Vazirmatn'}}},
      y:{grid:{color:'rgba(239,35,79,.06)'},border:{display:false},ticks:{color:'#71717a',font:{size:9,family:'Vazirmatn'},callback:v=>v+' MB'}}
    }
  };
  const c1=document.getElementById('ch1').getContext('2d');
  const g1=c1.createLinearGradient(0,0,0,260);
  g1.addColorStop(0,'rgba(239,35,79,.4)');g1.addColorStop(1,'rgba(239,35,79,0)');
  ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[{label:'MB',data:[],borderColor:'#ef234f',backgroundColor:g1,fill:true,tension:.4,pointRadius:0,borderWidth:2.5}]},options:opts});
  const c3ctx=document.getElementById('ch3').getContext('2d');
  const g3=c3ctx.createLinearGradient(0,0,0,320);
  g3.addColorStop(0,'rgba(239,35,79,.45)');g3.addColorStop(1,'rgba(239,35,79,0)');
  ch3=new Chart(document.getElementById('ch3'),{type:'line',data:{labels:[],datasets:[{label:'مصرف',data:[],borderColor:'#ef234f',backgroundColor:g3,fill:true,tension:.45,pointRadius:0,borderWidth:3}]},options:opts});
  ch2=new Chart(document.getElementById('ch2'),{type:'doughnut',data:{labels:['VLESS/WS','XHTTP','HTTP'],datasets:[{data:[55,35,10],backgroundColor:['#ef234f','#22c55e','#a855f7'],borderColor:'#0d0d11',borderWidth:4,hoverOffset:10,borderRadius:6,spacing:3}]},options:{responsive:true,maintainAspectRatio:false,cutout:'72%',plugins:{legend:{position:'bottom',labels:{color:'#a1a1aa',font:{size:10,family:'Vazirmatn'},padding:12,usePointStyle:true,pointStyle:'circle'}}}}});
}

// ═══ Stats ═══
let prevTraf=0;
async function fetchStats(){
  try{
    const r=await authF('/stats'),d=await r.json();
    document.getElementById('m-conns').textContent=d.active_connections;
    document.getElementById('conns-nb').textContent=d.active_connections;
    document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    document.getElementById('m-alinks').textContent=d.active_links??'—';
    document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';
    document.getElementById('m-subs').textContent=d.subs_count??'—';
    document.getElementById('errs-badge').textContent=d.total_errors+' خطا';
    document.getElementById('uptime-inline').textContent=d.uptime;
    document.getElementById('uptime-badge').textContent='Railway · '+d.uptime;
    document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' اتصال';
    prevTraf=d.total_traffic_mb;
    if(d.hourly){
      const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));
      [ch1,ch3].forEach(c=>{if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});
    }
    renderErrs(d.recent_errors||[]);
  }catch(e){console.error(e)}
}
function renderErrs(errs){
  const el=document.getElementById('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}
  el.innerHTML=errs.slice().reverse().map(e=>`<div class="erow"><div class="etime"><i class="ti ti-clock"></i>${new Date(e.time).toLocaleString('fa-IR')}</div><div class="emsg">${esc(e.error)}</div></div>`).join('');
}

// ═══ Activity ═══
async function loadActivity(){
  try{
    const r=await authF('/api/activity'),d=await r.json();
    const logs=(d.logs||[]).slice().reverse();
    const el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');
    if(!logs.length){el.innerHTML='';em.style.display='block';return}
    em.style.display='none';
    const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
    el.innerHTML=logs.map(l=>`
      <div class="log-item">
        <div class="log-ic ${l.level}"><i class="ti ${icMap[l.level]||'ti-info-circle'}"></i></div>
        <div>
          <div class="log-msg">${esc(l.message)}</div>
          <div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString('fa-IR')} <span class="log-kind">${l.kind}</span></div>
        </div>
      </div>
    `).join('');
  }catch(e){console.error(e)}
}

// ═══ Outbounds ═══
let allOutbounds=[];
async function loadOutbounds(){
  try{
    const r=await authF('/api/outbounds'),d=await r.json();
    allOutbounds=d.outbounds||[];
    const customs=allOutbounds.filter(o=>!o.builtin);
    document.getElementById('outbounds-nb').textContent=customs.length;
    document.getElementById('outbounds-pg-cnt').textContent=toFa(customs.length)+' خروجی';

    // پر کردن select ایجاد کانفیگ
    const sel=document.getElementById('nl-outbound');
    if(sel){
      sel.innerHTML=allOutbounds.map(o=>`<option value="${esc(o.id)}">${esc(o.name)} (${esc(o.type)})</option>`).join('');
    }
    // پر کردن select ویرایش کانفیگ
    const sel2=document.getElementById('el-outbound');
    if(sel2){
      sel2.innerHTML=allOutbounds.map(o=>`<option value="${esc(o.id)}">${esc(o.name)} (${esc(o.type)})</option>`).join('');
    }

    const grid=document.getElementById('outbounds-grid'),empty=document.getElementById('outbounds-empty');
    if(!customs.length){grid.innerHTML='';empty.style.display='block';return}
    empty.style.display='none';
    const typeColor={freedom:'var(--green)',blackhole:'var(--red)',socks5:'var(--accent)',vless:'var(--purple)'};
    grid.innerHTML=customs.map(o=>`
      <div class="cfg-card">
        <div class="cfg-row">
          <span class="cfg-status-dot" style="background:${typeColor[o.type]||'var(--accent)'}"></span>
          <div class="cfg-identity">
            <div class="cfg-label">${esc(o.name)}</div>
            <div class="cfg-sub-meta"><span class="cfg-uuid-mini">${esc(o.id).slice(0,10)}…</span></div>
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-usage-col">
            <div style="font-size:11px;color:var(--t2);line-height:1.8">
              <div><b>نوع:</b> ${esc(o.type)}</div>
              ${o.type==='socks5'?`<div><b>آدرس:</b> ${esc(o.address)}:${esc(o.port)}</div>`:''}
              ${o.type==='vless'?`<div><b>VLESS:</b> ${esc((o.url||'').slice(0,40))}…</div>`:''}
            </div>
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-actions">
            <button class="btn btn-sm btn-d btn-icon" onclick="deleteOutbound('${o.id}')"><i class="ti ti-trash"></i></button>
          </div>
        </div>
      </div>
    `).join('');
  }catch(e){console.error(e)}
}
function onOutboundTypeChange(){
  const t=document.getElementById('no-type').value;
  document.getElementById('no-fields-socks5').style.display=t==='socks5'?'':'none';
  document.getElementById('no-fields-vless').style.display=t==='vless'?'':'none';
}
async function createOutbound(){
  const name=document.getElementById('no-name').value.trim();
  const type=document.getElementById('no-type').value;
  const body={name,type};
  if(type==='socks5'){
    body.address=document.getElementById('no-address').value.trim();
    body.port=Number(document.getElementById('no-port').value)||0;
    body.username=document.getElementById('no-username').value.trim();
    body.password=document.getElementById('no-password').value;
    if(!body.address||!body.port){toast('آدرس و پورت را وارد کنید','err');return}
  }else if(type==='vless'){
    body.url=document.getElementById('no-url').value.trim();
    if(!body.url){toast('لینک VLESS را وارد کنید','err');return}
  }
  try{
    const r=await authF('/api/outbounds',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا')}
    ['no-name','no-address','no-port','no-username','no-password','no-url'].forEach(id=>document.getElementById(id).value='');
    closeModal('modal-create-outbound');
    toast('خروجی ساخته شد ✓','ok');
    loadOutbounds();
  }catch(e){toast('✗ '+e.message,'err')}
}
async function deleteOutbound(id){
  if(!confirm('حذف این خروجی؟'))return;
  try{const r=await authF('/api/outbounds/'+id,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadOutbounds();}catch(e){toast('خطا','err')}
}

// ═══ External Configs ═══
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
          <div class="cfg-identity"><div class="cfg-label">${esc(c.name)}</div></div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-usage-col"><div style="font-size:10.5px;color:var(--t2);word-break:break-all">${esc((c.url||'').slice(0,70))}</div></div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-actions">
            <button class="tog${c.active?' on':''}" onclick="toggleExternal('${c.id}',${!c.active})"></button>
            <button class="btn btn-sm btn-d btn-icon" onclick="deleteExternalConfig('${c.id}')"><i class="ti ti-trash"></i></button>
          </div>
        </div>
      </div>
    `).join('');
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

// ═══ Links ═══
let allSubsList=[],allLinksList=[];
async function loadLinks(){
  try{
    const [lr,sr,or_]=await Promise.all([authF('/api/links'),authF('/api/subs'),authF('/api/outbounds')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    const {outbounds=[]}=await or_.json();
    allSubsList=subs;allLinksList=links;allOutbounds=outbounds;

    const nlSub=document.getElementById('nl-sub');
    nlSub.innerHTML='<option value="">— بدون گروه —</option>'+subs.map(s=>`<option value="${esc(s.sub_id)}">${esc(s.name)}</option>`).join('');
    document.getElementById('links-nb').textContent=links.length;
    document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' کانفیگ';
    document.getElementById('lsummary-badge').textContent=toFa(links.length);

    const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!links.length){grid.innerHTML='';empty.style.display='block';document.getElementById('lsummary').innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی وجود ندارد</p></div>';return}
    empty.style.display='none';

    grid.innerHTML=links.map(l=>{
      const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
      const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
      const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
      const allowed=l.active&&!l.expired;
      const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
      return `<div class="cfg-card ${cardCls}">
        <div class="cfg-row">
          <span class="cfg-status-dot ${allowed?'pulse':''}"></span>
          <div class="cfg-identity">
            <div class="cfg-label">${esc(l.label)}</div>
            <div class="cfg-sub-meta">
              <span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID کپی شد','ok'))"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
              <span>${new Date(l.created_at).toLocaleDateString('fa-IR')}</span>
            </div>
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-usage-col">
            <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
            <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>از ${lim}</span></div>
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-exp-col">${expChip(l.expires_at,l.expired)}</div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-badges-col">
            ${protoBadge(l.protocol)}
            <span class="cfg-sub-tag"><i class="ti ti-route"></i> :${l.port||443}</span>
            <span class="cfg-sub-tag"><i class="ti ti-users"></i> ${l.connected_ips||0}${l.ip_limit?('/'+l.ip_limit):' (∞)'}</span>
          </div>
          <div class="cfg-divider-v"></div>
          <div class="cfg-actions">
            <button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})"></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))"><i class="ti ti-copy"></i></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('Sub کپی شد','ok'))"><i class="ti ti-rss"></i></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')"><i class="ti ti-qrcode"></i></button>
            <button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')"><i class="ti ti-edit"></i></button>
            <button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')"><i class="ti ti-rotate"></i></button>
            <button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')"><i class="ti ti-trash"></i></button>
          </div>
        </div>
      </div>`;
    }).join('');

    document.getElementById('lsummary').innerHTML=links.slice(0,6).map(l=>`<div class="sr"><span class="sr-k"><i class="ti ${l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x'}"></i>${esc(l.label)}</span><span class="sr-v" style="font-size:10px">${fmtB(l.used_bytes)}</span></div>`).join('');
  }catch(e){console.error(e)}
}
async function createLink(){
  const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';
  const val=document.getElementById('nl-val').value;
  const unit=document.getElementById('nl-unit').value;
  const exp=document.getElementById('nl-exp').value;
  const note=document.getElementById('nl-note').value.trim();
  const sub_id=document.getElementById('nl-sub').value||null;
  const protocol=document.getElementById('nl-proto').value||'vless-ws';
  const fingerprint=document.getElementById('nl-fp').value||'chrome';
  const alpn=document.getElementById('nl-alpn').value.trim();
  const port=Number(document.getElementById('nl-port').value)||443;
  const ip_limit=Number(document.getElementById('nl-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('nl-speed').value)||0;
  const speed_limit_unit=document.getElementById('nl-speed-unit').value;
  const outbound_id=document.getElementById('nl-outbound').value||'direct';
  try{
    const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,protocol,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit,outbound_id})});
    if(!r.ok)throw new Error('failed');
    ['nl-label','nl-val','nl-exp','nl-note','nl-alpn'].forEach(id=>document.getElementById(id).value='');
    document.getElementById('nl-port').value='443';
    document.getElementById('nl-iplimit').value='0';
    document.getElementById('nl-speed').value='0';
    document.getElementById('nl-alpn-preset').value='';
    document.getElementById('nl-alpn').style.display='none';
    toast('کانفیگ ساخته شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ساخت','err')}
}
function openEditLink(uuid){
  const l=allLinksList.find(x=>x.uuid===uuid);
  if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label;
  document.getElementById('el-note').value=l.note||'';
  if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
  else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}
  document.getElementById('el-exp').value='';
  document.getElementById('el-fp').value=l.fingerprint||'chrome';
  document.getElementById('el-alpn').value=l.alpn||'';
  document.getElementById('el-port').value=l.port||443;
  document.getElementById('el-iplimit').value=l.ip_limit||0;
  document.getElementById('el-outbound').value=l.outbound_id||'direct';
  if(!l.speed_limit_bytes){document.getElementById('el-speed').value='0';document.getElementById('el-speed-unit').value='MBIT';}
  else{document.getElementById('el-speed').value=(l.speed_limit_bytes*8/1024/1024).toFixed(2);document.getElementById('el-speed-unit').value='MBIT';}
  openModal('modal-edit-link');
}
async function saveEditLink(){
  const uuid=document.getElementById('el-uuid').value;
  const body={
    label:document.getElementById('el-label').value.trim(),
    note:document.getElementById('el-note').value.trim(),
    limit_value:document.getElementById('el-val').value||0,
    limit_unit:document.getElementById('el-unit').value,
    fingerprint:document.getElementById('el-fp').value||'chrome',
    alpn:document.getElementById('el-alpn').value.trim(),
    port:Number(document.getElementById('el-port').value)||443,
    ip_limit:Number(document.getElementById('el-iplimit').value)||0,
    speed_limit_value:Number(document.getElementById('el-speed').value)||0,
    speed_limit_unit:document.getElementById('el-speed-unit').value,
    outbound_id:document.getElementById('el-outbound').value||'direct'
  };
  const exp=document.getElementById('el-exp').value;
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('ویرایش شد ✓','ok');loadLinks();
  }catch(e){toast('خطا','err')}
}
async function toggleActive(uuid,newState){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function resetUsage(uuid){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('ریست شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function deleteLink(uuid){
  if(!confirm('حذف این کانفیگ؟'))return;
  try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}

// ═══ Sub Groups ═══
let allSubsRaw=[];
async function loadSubs(){
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-nb').textContent=subs.length;
    document.getElementById('subs-pg-cnt').textContent=toFa(subs.length)+' گروه';
    renderSubsGrid(subs);
  }catch(e){console.error(e)}
}
function renderSubsGrid(subs){
  const grid=document.getElementById('subs-grid');
  if(!subs.length){
    grid.innerHTML='<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید</div></div>';
    return;
  }
  grid.innerHTML=subs.map(s=>`
    <div class="sub-card">
      <div class="sub-card-top">
        <div class="sub-card-head-v2">
          <div class="sub-card-icon"><i class="ti ti-folder"></i></div>
          <div style="flex:1;min-width:0">
            <div class="sub-card-name-v2">${esc(s.name)}</div>
            ${s.desc?`<div class="sub-card-desc-v2">${esc(s.desc)}</div>`:'<div class="sub-card-desc-v2" style="opacity:.5">بدون توضیحات</div>'}
          </div>
          <div class="sub-card-lock-badge ${s.has_password?'locked':'open'}">
            <i class="ti ${s.has_password?'ti-lock':'ti-lock-open'}"></i>
          </div>
        </div>
        <div class="sub-card-stats">
          <div class="sub-card-stat"><div class="sub-card-stat-val">${toFa(s.links_count)}</div><div class="sub-card-stat-label">کانفیگ</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">${toFa(s.active_count)}</div><div class="sub-card-stat-label">فعال</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-card-stat-label">مصرف</div></div>
        </div>
      </div>
      <div class="sub-card-url-row">
        <span class="sub-card-url-text">${esc(s.public_url)}</span>
        <button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-copy"></i></button>
        <button class="sub-card-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')"><i class="ti ti-external-link"></i></button>
      </div>
      <div class="sub-card-bottom">
        <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> کانفیگ‌ها</button>
        <button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-rss"></i> ساب</button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteSub('${esc(s.sub_id)}')"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  `).join('');
}
function filterSubs(q){
  q=q.trim().toLowerCase();
  if(!q){renderSubsGrid(allSubsRaw);return}
  renderSubsGrid(allSubsRaw.filter(s=>s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q)));
}
async function createSub(){
  const name=document.getElementById('ns-name').value.trim()||'گروه جدید';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  try{
    const r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(id=>document.getElementById(id).value='');
    closeModal('modal-create-sub');
    toast('گروه ساخته شد ✓','ok');loadSubs();
  }catch(e){toast('خطا','err')}
}
async function deleteSub(sub_id){
  if(!confirm('حذف این گروه؟'))return;
  try{const r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadSubs();loadLinks();}catch(e){toast('خطا','err')}
}

// ═══ Sub-Links modal ═══
let lmodalLinks=[],lmodalInSub=new Set(),currentSubId=null;
async function openSubLinks(sub_id,name){
  currentSubId=sub_id;
  document.getElementById('modal-sub-name').textContent=name;
  document.getElementById('modal-links-body').innerHTML='<div style="color:var(--t3);font-size:12px;padding:20px;text-align:center">در حال بارگذاری...</div>';
  document.getElementById('lmodal-search-inp').value='';
  openModal('modal-links');
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    const thisSub=subs.find(s=>s.sub_id===sub_id);
    lmodalInSub=new Set(thisSub?.link_ids||[]);
    lmodalLinks=links;
    renderLmodalList(links);
  }catch(e){toast('خطا','err')}
}
function renderLmodalList(links){
  const body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div style="text-align:center;padding:30px;color:var(--t3)">کانفیگی نیست</div>';updateLmodalCount();return}
  body.innerHTML=links.map(l=>{
    const checked=lmodalInSub.has(l.uuid);
    const on=l.active&&!l.expired;
    return `<div class="cfg-card" data-uuid="${l.uuid}" data-name="${esc(l.label).toLowerCase()}" onclick="toggleLrow('${l.uuid}',this)" style="cursor:pointer;margin-bottom:6px;${checked?'border-color:var(--accent);background:var(--accent-d)':''}">
      <div style="padding:11px 13px;display:flex;align-items:center;gap:10px">
        <div style="width:20px;height:20px;border-radius:7px;border:2px solid ${checked?'var(--accent)':'var(--card-b)'};background:${checked?'var(--accent)':'rgba(0,0,0,.2)'};display:flex;align-items:center;justify-content:center;flex-shrink:0">
          <i class="ti ti-check" style="font-size:12px;color:#fff;opacity:${checked?1:0}"></i>
        </div>
        <div style="flex:1;min-width:0">
          <div style="font-size:12.5px;font-weight:700;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${esc(l.label)}</div>
          <div style="font-size:9.5px;color:var(--t3);margin-top:2px">${fmtB(l.used_bytes)}</div>
        </div>
        <span style="font-size:9px;font-weight:800;padding:3px 9px;border-radius:20px;${on?'background:var(--green-bg);color:var(--green-t)':'background:var(--red-bg);color:var(--red-t)'}">${on?'فعال':'غیرفعال'}</span>
      </div>
    </div>`;
  }).join('');
  updateLmodalCount();
}
function toggleLrow(uuid,el){
  if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid);el.style.borderColor='var(--card-b)';el.style.background='';el.querySelector('div>div').style.background='rgba(0,0,0,.2)';el.querySelector('div>div').style.borderColor='var(--card-b)';el.querySelector('i.ti-check').style.opacity='0';}
  else{lmodalInSub.add(uuid);el.style.borderColor='var(--accent)';el.style.background='var(--accent-d)';el.querySelector('div>div').style.background='var(--accent)';el.querySelector('div>div').style.borderColor='var(--accent)';el.querySelector('i.ti-check').style.opacity='1';}
  updateLmodalCount();
}
function lmodalSelectAll(state){
  lmodalLinks.forEach(l=>{if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid)});
  renderLmodalList(lmodalLinks);
}
function updateLmodalCount(){
  const el=document.getElementById('lmodal-count');
  if(el)el.textContent=toFa(lmodalInSub.size)+' انتخاب شده';
}
function filterLmodal(q){
  q=q.trim().toLowerCase();
  document.querySelectorAll('#modal-links-body .cfg-card').forEach(row=>{
    row.style.display = !q || row.dataset.name.includes(q) ? '' : 'none';
  });
}
async function saveSubLinks(){
  if(!currentSubId)return;
  const link_ids=[...lmodalInSub];
  try{
    const r=await authF('/api/subs/'+currentSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids})});
    if(!r.ok)throw new Error();
    closeModal('modal-links');
    toast('ذخیره شد ✓','ok');
    await Promise.all([loadSubs(),loadLinks()]);
  }catch(e){toast('خطا','err')}
}

// ═══ Subs Page ═══
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    const el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>هنوز گروهی ندارید</p></div>';return}
    el.innerHTML=subs.map(s=>`
      <div style="padding:13px 15px;background:rgba(168,85,247,.07);border:1px solid rgba(168,85,247,.2);border-radius:10px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">
        <div>
          <div style="font-weight:700;font-size:13px;margin-bottom:3px;color:#fff">${esc(s.name)}</div>
          <div style="font-family:ui-monospace,monospace;font-size:10px;color:#c084fc">${esc(s.sub_url)}</div>
        </div>
        <div style="display:flex;gap:5px;flex-wrap:wrap">
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-copy"></i> ساب</button>
          <button class="btn btn-sm btn-g" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
        </div>
      </div>
    `).join('');
  }catch(e){}
}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(()=>toast('کپی شد ✓','ok'))}

// ═══ Connections ═══
function parseBytesFmt(s){
  if(!s)return 0;
  const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);
  if(!m)return 0;
  const n=parseFloat(m[1]),u=m[2].toUpperCase();
  const mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};
  return n*(mult[u]||1);
}
async function loadConns(){
  try{
    const r=await authF('/api/connections'),d=await r.json();
    const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.count+' اتصال';
    document.getElementById('ch-count').textContent=toFa(d.count);
    const conns=d.connections||[];
    if(!d.count){
      grid.innerHTML='';ce.style.display='block';
      document.getElementById('ch-traffic').textContent='—';
      document.getElementById('ch-avgdur').textContent='—';
      document.getElementById('ch-uniq').textContent='—';
      return;
    }
    ce.style.display='none';
    const totalBytes=conns.reduce((s,c)=>s+parseBytesFmt(c.bytes_fmt),0);
    document.getElementById('ch-traffic').textContent=fmtB(totalBytes);
    document.getElementById('ch-uniq').textContent=toFa(new Set(conns.map(c=>c.ip)).size);
    const durs=conns.map(c=>c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0);
    const avgSec=durs.length?Math.floor(durs.reduce((a,b)=>a+b,0)/durs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';
    grid.innerHTML=conns.map(c=>{
      const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';
      return `<div class="conn-card-v2">
        <div class="conn-card-v2-top">
          <div class="conn-avatar"><i class="ti ti-device-desktop"></i></div>
          <div style="flex:1;min-width:0">
            <div class="conn-ip-v2">${esc(c.ip)}
              <button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-copy"></i></button>
            </div>
            <div class="conn-label-v2">${esc(c.label)}</div>
          </div>
          <span class="conn-status-pill"><span class="dot dg pulse"></span> زنده</span>
        </div>
        <div class="conn-card-v2-divider"></div>
        <div class="conn-card-v2-body">
          <div style="display:flex;gap:10px">
            <div style="flex:1;text-align:center;padding:8px;background:rgba(0,0,0,.2);border-radius:8px">
              <div style="font-size:8.5px;color:var(--t3);font-weight:700">ترافیک</div>
              <div style="font-size:11.5px;font-weight:700;color:#fff;margin-top:2px">${esc(c.bytes_fmt)}</div>
            </div>
            <div style="flex:1;text-align:center;padding:8px;background:rgba(0,0,0,.2);border-radius:8px">
              <div style="font-size:8.5px;color:var(--t3);font-weight:700">مدت</div>
              <div style="font-size:11.5px;font-weight:700;color:#fff;margin-top:2px">${dur}</div>
            </div>
          </div>
        </div>
      </div>`;
    }).join('');
  }catch(e){console.error(e)}
}
async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}

// ═══ Misc ═══
async function fetchDefaultVless(){
  try{
    const r=await authF('/api/links'),d=await r.json();
    const links=d.links||[];
    const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];
    document.getElementById('vless-main').textContent=def?def.vless_link:'هنوز کانفیگی وجود ندارد';
  }catch(e){}
}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ✓','ok'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();loadOutbounds();loadExternals();if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('رفرش شد','ok')}

async function changePw(){
  const cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;
  if(!cur||!nw||!cf){toast('همه فیلدها را پر کنید','err');return}
  if(nw.length<10){toast('حداقل ۱۰ کاراکتر','err');return}
  if(nw!==cf){toast('تکرار رمز اشتباه','err');return}
  try{
    const r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'خطا');
    toast('رمز تغییر کرد ✓','ok');
    ['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='');
  }catch(e){toast('✗ '+e.message,'err')}
}

async function downloadBackup(){
  try{
    const r=await authF('/api/backup');
    if(!r.ok)throw new Error();
    const blob=await r.blob(), a=document.createElement('a');
    a.href=URL.createObjectURL(blob);a.download='bogzarnet-backup.json';a.click();URL.revokeObjectURL(a.href);
    toast('دانلود شد','ok');
  }catch(e){toast('خطا','err')}
}
async function exportActiveLinks(){
  try{
    const r=await authF('/api/links/export'), d=await r.json();
    const blob=new Blob([(d.links||[]).join('\n')+'\n'],{type:'text/plain;charset=utf-8'}), a=document.createElement('a');
    a.href=URL.createObjectURL(blob);a.download='bogzarnet-active-links.txt';a.click();URL.revokeObjectURL(a.href);
    toast(`${d.count||0} لینک export شد`,'ok');
  }catch(e){toast('خطا','err')}
}
async function loadTelegramSettings(){try{const r=await authF('/api/telegram/status');const d=await r.json();document.getElementById('tg-enabled').checked=d.enabled;document.getElementById('tg-admins').value=d.admin_ids||'';document.getElementById('tg-status').textContent=d.running?'ONLINE':'OFFLINE';}catch(e){}}
async function saveTelegramSettings(){const token=document.getElementById('tg-token').value,admins=document.getElementById('tg-admins').value,enabled=document.getElementById('tg-enabled').checked;try{const r=await authF('/api/telegram/settings',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({token,admin_ids:admins,enabled})});if(!r.ok)throw Error();toast('ذخیره شد','ok');document.getElementById('tg-token').value='';loadTelegramSettings();}catch(e){toast('خطا','err')}}

// ═══ WebSocket test ═══
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log'),p=document.createElement('p');const colors={ok:'#4ade80',err:'#f87171',info:'#a1a1aa',sent:'#fbbf24'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('fa-IR')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','اتصال: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ متصل');ws.onerror=()=>wsLog('err','✗ خطا');ws.onmessage=m=>wsLog('info','دریافت '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','قطع ('+e.code+')')}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}

// ═══ Init ═══
document.addEventListener('DOMContentLoaded',async()=>{
  await checkAuth();
  loadTelegramSettings();
  initCharts();
  document.getElementById('set-host').textContent=location.host;
  fetchStats();fetchDefaultVless();loadLinks();loadSubs();loadOutbounds();loadExternals();
  setInterval(fetchStats,4000);
  setInterval(()=>{
    if(document.getElementById('pg-links').classList.contains('on'))loadLinks();
    if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();
    if(document.getElementById('pg-connections').classList.contains('on'))loadConns();
    if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();
    if(document.getElementById('pg-outbounds').classList.contains('on'))loadOutbounds();
    if(document.getElementById('pg-externals').classList.contains('on'))loadExternals();
  },5000);
});
</script>
</body></html>"""


# ═══════════════════════════════════════════════════════════════════════════════
# صفحه‌ی پابلیک گروه ساب — اینجاست که سرورهای خارجی نمایش داده میشن
# ═══════════════════════════════════════════════════════════════════════════════
PUBLIC_PAGE_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>bogzarnet Subscription</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --bg:#09090b;--bg2:#0e0e12;--card:#121217;
  --card-b:rgba(239,35,79,0.16);--card-bh:rgba(239,35,79,0.34);
  --accent:#ef234f;--accent2:#ff5578;--accent-d:rgba(239,35,79,0.1);
  --green:#22c55e;--green-bg:rgba(34,197,94,0.1);--green-t:#4ade80;
  --red:#ef4444;--red-bg:rgba(239,68,68,0.1);--red-t:#f87171;
  --amber:#f59e0b;--amber-bg:rgba(245,158,11,0.1);--amber-t:#fbbf24;
  --purple:#a855f7;--purple-bg:rgba(168,85,247,0.1);--purple-t:#c084fc;
  --t1:#f7f7f8;--t2:#a1a1aa;--t3:#71717a;
  --shadow:0 12px 40px rgba(0,0,0,0.45);
}
html,body{min-height:100%;background:var(--bg);font-family:'Vazirmatn',sans-serif;color:var(--t1);font-size:14px;background-image:radial-gradient(circle at 15% 0%,rgba(239,35,79,.14),transparent 34%),radial-gradient(circle at 95% 100%,rgba(159,18,57,.10),transparent 30%)}
.bg-fx{position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(239,35,79,0.13),transparent 62%);z-index:0;pointer-events:none}
.grid-fx{position:fixed;inset:0;background-image:linear-gradient(rgba(239,35,79,0.025) 1px,transparent 1px),linear-gradient(90deg,rgba(239,35,79,0.025) 1px,transparent 1px);background-size:46px 46px;z-index:0;pointer-events:none}
.wrap{position:relative;z-index:10;max-width:800px;margin:0 auto;padding:24px 16px 64px}
.top{display:flex;align-items:center;justify-content:space-between;margin-bottom:26px;gap:10px}
.brand{display:flex;align-items:center;gap:11px;min-width:0}
.brand-img{width:40px;height:40px;border-radius:50%;overflow:hidden;border:1px solid var(--card-b);box-shadow:0 0 14px rgba(239,35,79,.3);flex-shrink:0;display:flex;align-items:center;justify-content:center;background:#0d0d11}
.brand-img svg{width:100%;height:100%}
.brand-name{font-size:14.5px;font-weight:800;color:#fff}
.brand-sub{font-size:9.5px;color:var(--accent2);font-weight:700}

.sub-info{background:linear-gradient(145deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:22px;padding:24px;margin-bottom:16px;box-shadow:var(--shadow);backdrop-filter:blur(20px)}
.sub-eyebrow{font-size:10px;font-weight:700;color:var(--accent2);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:6px}
.sub-name{font-size:23px;font-weight:800;color:#fff;margin-bottom:6px}
.sub-desc{font-size:12.5px;color:var(--t2);line-height:1.8;margin-bottom:14px}
.sub-meta-row{font-size:10.5px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:6px}
.sub-sub-box{background:var(--accent-d);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;display:flex;align-items:center;gap:9px;flex-wrap:wrap}
.sub-sub-url{font-family:ui-monospace,monospace;font-size:10px;color:var(--accent2);word-break:break-all;flex:1;min-width:140px}

.stats-bar{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}
.stat-card{background:linear-gradient(145deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:16px;padding:16px 17px;backdrop-filter:blur(20px)}
.stat-label{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:7px}
.stat-val{font-size:22px;font-weight:800;color:#fff;line-height:1}
.stat-sub{font-size:9.5px;color:var(--t3);margin-top:6px}

.copy-all-bar{display:flex;align-items:center;gap:12px;background:linear-gradient(120deg,#ef234f 0%,#9f1239 100%);border-radius:18px;padding:16px 19px;margin-bottom:18px;box-shadow:0 10px 30px rgba(239,35,79,.28);flex-wrap:wrap}
.copy-all-title{font-size:13.5px;font-weight:800;color:#fff;display:flex;align-items:center;gap:6px}
.copy-all-sub{font-size:10px;color:rgba(255,255,255,.78);margin-top:3px}
.copy-all-btn{background:#fff;color:#9f1239;border:none;border-radius:12px;padding:10px 19px;font-family:inherit;font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.18s;white-space:nowrap}
.copy-all-btn:hover{transform:translateY(-1px)}

.cfg-title{font-size:12px;font-weight:800;color:var(--t2);margin-bottom:13px;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.07em;margin-top:22px}
.cfg-title:first-child{margin-top:0}
.cfg-title i{color:var(--accent2);font-size:15px}
.cfg-grid{display:grid;gap:13px}

.cfg-card{background:linear-gradient(145deg,rgba(28,28,37,.74),rgba(12,12,17,.78));border:1px solid var(--card-b);border-radius:18px;transition:all .2s;overflow:hidden;backdrop-filter:blur(20px)}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:var(--shadow)}
.cfg-card.inactive{opacity:.6}
.cfg-card.external{border-color:rgba(34,197,94,.3)}
.cfg-top{padding:17px 19px 15px;position:relative}
.cfg-top::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}
.cfg-card.inactive .cfg-top::after{background:var(--red)}
.cfg-card.external .cfg-top::after{background:#22c55e}
.cfg-head{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;flex-wrap:wrap}
.cfg-label{font-size:14.5px;font-weight:700;color:#fff}
.cfg-badges{display:flex;gap:5px;flex-wrap:wrap;margin-top:6px}
.proto-chip{font-size:9px;padding:3px 8px;border-radius:7px;font-weight:800}
.pc-ws{background:var(--accent-d);color:var(--accent2)}
.pc-xhttp{background:var(--purple-bg);color:var(--purple-t)}
.pc-external{background:var(--green-bg);color:var(--green-t)}
.cfg-status{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;padding:4px 10px;border-radius:20px;white-space:nowrap}
.cfg-status.ok{background:var(--green-bg);color:var(--green-t)}
.cfg-status.no{background:var(--red-bg);color:var(--red-t)}
.cfg-usage{margin-bottom:4px}
.ubar{height:6px;border-radius:4px;background:rgba(239,35,79,0.1);overflow:hidden;margin-bottom:5px}
.ubar-f{height:100%;border-radius:4px;transition:width .5s ease}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}

.cfg-tear{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 19px}
.cfg-tear::before,.cfg-tear::after{content:'';position:absolute;top:50%;width:18px;height:18px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-b)}
.cfg-tear::before{right:-28px}
.cfg-tear::after{left:-28px}

.cfg-bottom{padding:15px 19px 18px}
.cfg-link-toggle{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px dashed var(--card-b);border-radius:11px;padding:10px 13px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:11.5px;font-weight:600;transition:.15s}
.cfg-link-toggle:hover{background:var(--accent-d);border-color:var(--card-bh);color:var(--accent2)}
.cfg-link-toggle .ltl{display:flex;align-items:center;gap:7px}
.cfg-link-toggle i.ti-chevron-down{transition:transform .2s}
.cfg-link-toggle.open i.ti-chevron-down{transform:rotate(180deg)}
.cfg-vless-wrap{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}
.cfg-vless-wrap.open{grid-template-rows:1fr}
.cfg-vless-inner{overflow:hidden}
.cfg-vless{background:rgba(4,4,7,.55);border:1px solid var(--card-b);border-radius:10px;padding:11px 13px;font-size:9.8px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.7;margin-top:9px;max-height:90px;overflow-y:auto}
.cfg-actions{display:flex;gap:7px;flex-wrap:wrap;margin-top:11px}
.btn{font-family:inherit;font-size:11.5px;font-weight:700;border-radius:10px;padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}
.btn i{font-size:13px}
.btn-p{background:linear-gradient(135deg,#f12b57,#a90f39);color:#fff;box-shadow:0 3px 14px rgba(239,35,79,.35)}
.btn-p:hover{transform:translateY(-1px)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(239,35,79,.16)}
.btn-pur{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(168,85,247,.2)}
.conn-chip{display:inline-flex;align-items:center;gap:4px;font-size:9.5px;padding:3px 8px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-weight:700}
.dot{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}

.lock-stage{display:flex;align-items:center;justify-content:center;min-height:78vh;padding:20px 0}
.lock-card{background:linear-gradient(145deg,rgba(28,28,37,.94),rgba(12,12,17,.94));border:1px solid var(--card-b);border-radius:26px;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow);overflow:hidden;backdrop-filter:blur(20px)}
.lock-banner{background:linear-gradient(150deg,rgba(239,35,79,.16),rgba(239,35,79,.02) 70%);padding:38px 30px 26px}
.lock-shield{width:64px;height:64px;border-radius:18px;background:var(--accent-d);border:1px solid var(--card-bh);display:flex;align-items:center;justify-content:center;margin:0 auto 18px}
.lock-shield i{font-size:28px;color:var(--accent2)}
.lock-title{font-size:18px;font-weight:800;margin-bottom:6px;color:#fff}
.lock-sub{font-size:12px;color:var(--t3);line-height:1.7}
.lock-form{padding:24px 30px 30px}
.lock-field{position:relative;margin-bottom:13px}
.lock-inp{width:100%;padding:13px 44px;border-radius:13px;border:1px solid #2b2b34;background:#0d0d11;color:#fff;font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.14em}
.lock-inp:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}
.lock-eye{position:absolute;left:13px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.lock-lockicon{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none}
.lock-err{color:var(--red-t);font-size:11.5px;margin-bottom:10px;min-height:16px}
.lock-btn{width:100%;justify-content:center;padding:13px;font-size:13px;border-radius:13px}
.lock-footer{padding:14px 30px;border-top:1px solid var(--card-b);font-size:10px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}

.empty-state{text-align:center;padding:80px 20px;color:var(--t3)}
.empty-state i{font-size:38px;display:block;margin-bottom:14px}

.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:linear-gradient(145deg,rgba(28,28,37,.96),rgba(12,12,17,.96));border:1px solid var(--card-b);color:#fff;border-radius:12px;padding:10px 20px;font-size:12.5px;font-weight:600;opacity:0;transition:all .25s;z-index:999;pointer-events:none;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(34,197,94,.35);background:var(--green-bg);color:var(--green-t)}

.qr-modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.72);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}
.qr-modal.open{display:flex}
.qr-box{background:linear-gradient(145deg,rgba(28,28,37,.96),rgba(12,12,17,.96));border:1px solid var(--card-b);border-radius:22px;padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow)}
.qr-title{font-size:13.5px;font-weight:800;margin-bottom:16px;color:#fff}
.qr-img img{width:100%;display:block;background:#fff;padding:10px;border-radius:14px;margin-bottom:15px}

.footer{text-align:center;padding-top:28px;font-size:10.5px;color:var(--t3)}
.footer a{color:var(--accent2);font-weight:700}

@media(max-width:520px){
  .stats-bar{grid-template-columns:1fr 1fr}
  .stats-bar .stat-card:nth-child(3){grid-column:1/-1}
  .sub-name{font-size:19px}
  .copy-all-bar{flex-direction:column;align-items:stretch}
  .copy-all-btn{justify-content:center}
  .wrap{padding:16px 12px 50px}
}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<div class="bg-fx"></div><div class="grid-fx"></div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-img">__LOGO_INLINE__</div>
      <div><div class="brand-name">bogzarnet</div><div class="brand-sub">Panel v2.0.0</div></div>
    </div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
  </div>
  <div class="footer">پشتیبانی: <a href="https://t.me/bogzarnet" target="_blank">@bogzarnet</a></div>
</div>
<script>
const UUID_KEY='__UUID_KEY__';
let savedPw='';

function toast(msg,type=''){
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function protoChip(p,isExt){
  if(isExt)return '<span class="proto-chip pc-external"><i class="ti ti-world"></i> EXTERNAL</span>';
  if(p==='xhttp-stream-up')return '<span class="proto-chip pc-xhttp">XHTTP · stream</span>';
  if(p==='xhttp-packet-up')return '<span class="proto-chip pc-xhttp">XHTTP · packet</span>';
  return '<span class="proto-chip pc-ws">VLESS · WS</span>';
}
function showQR(label,link){
  document.getElementById('qr-label').textContent=label;
  document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);
  document.getElementById('qr-modal').classList.add('open');
}
function toggleLink(i){
  const wrap=document.getElementById('vw-'+i);
  const btn=document.getElementById('vt-'+i);
  const open=wrap.classList.toggle('open');
  btn.classList.toggle('open',open);
  btn.querySelector('.ltl span').textContent = open ? 'پنهان کردن لینک' : 'نمایش لینک کانفیگ';
}
async function loadData(pw=''){
  const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');
  const r=await fetch(url);
  return r.json();
}
function renderLock(name,errMsg=''){
  document.getElementById('root').innerHTML=`
    <div class="lock-stage">
      <div class="lock-card">
        <div class="lock-banner">
          <div class="lock-shield"><i class="ti ti-shield-lock"></i></div>
          <div class="lock-title">${esc(name)}</div>
          <div class="lock-sub">این گروه با رمز محافظت شده. رمز رو وارد کنید.</div>
        </div>
        <div class="lock-form">
          <div class="lock-err" id="lock-err">${errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : ''}</div>
          <div class="lock-field">
            <i class="ti ti-lock lock-lockicon"></i>
            <input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus>
            <button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button>
          </div>
          <button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود به گروه</button>
        </div>
        <div class="lock-footer"><i class="ti ti-shield-check"></i> اتصال رمزنگاری‌شده</div>
      </div>
    </div>
  `;
  const inp=document.getElementById('lock-pw');
  inp.addEventListener('keydown',e=>{if(e.key==='Enter')submitLock()});
}
function togglePwVis(){
  const inp=document.getElementById('lock-pw');
  const icon=document.getElementById('lock-eye-icon');
  const toText = inp.type==='password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti '+(toText ? 'ti-eye-off' : 'ti-eye');
}
async function submitLock(){
  const pw=document.getElementById('lock-pw').value;
  const data=await loadData(pw);
  if(data.locked){renderLock(data.name,'رمز اشتباه است');return}
  savedPw=pw;
  renderContent(data);
}
function renderContent(d){
  const internalLinks = d.links.filter(l => !l.is_external);
  const externalLinks = d.links.filter(l => l.is_external);
  const activeCount = internalLinks.filter(l=>l.active).length + externalLinks.length;
  const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/sub-group/' + UUID_KEY);
  const subUrl = baseSubUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');

  window._bogzarnetSubUrl  = subUrl;
  window._bogzarnetSubName = d.name;
  window._bogzarnetLinks   = d.links.map(l => ({
    vless : l.vless_link,
    sub   : (l.sub_url || '') + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : ''),
    label : l.label,
    is_external: !!l.is_external,
  }));

  const renderCard = (l, i) => {
    const pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
    const bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
    const lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
    return `
      <div class="cfg-card${l.active ? '' : ' inactive'}${l.is_external ? ' external' : ''}">
        <div class="cfg-top">
          <div class="cfg-head">
            <div>
              <div class="cfg-label">${esc(l.label)}</div>
              <div class="cfg-badges">
                ${protoChip(l.protocol, l.is_external)}
                ${l.connections > 0 ? `<span class="conn-chip"><span class="dot"></span> ${toFa(l.connections)} اتصال</span>` : ''}
              </div>
            </div>
            <span class="cfg-status ${l.active ? 'ok' : 'no'}">${l.active ? '<i class="ti ti-circle-check"></i> فعال' : '<i class="ti ti-circle-x"></i> غیرفعال'}</span>
          </div>
          ${!l.is_external ? `
          <div class="cfg-usage">
            <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
            <div class="utxt"><span>${esc(l.used_fmt)} مصرف شده</span><span>سهمیه: ${lim}</span></div>
          </div>` : ''}
        </div>
        <div class="cfg-tear"></div>
        <div class="cfg-bottom">
          <button class="cfg-link-toggle" id="vt-${i}" onclick="toggleLink(${i})">
            <span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک کانفیگ</span></span>
            <i class="ti ti-chevron-down"></i>
          </button>
          <div class="cfg-vless-wrap" id="vw-${i}">
            <div class="cfg-vless-inner">
              <div class="cfg-vless">${esc(l.vless_link)}</div>
            </div>
          </div>
          <div class="cfg-actions">
            <button class="btn btn-p" onclick="navigator.clipboard.writeText(window._bogzarnetLinks[${i}].vless).then(()=>toast('لینک کپی شد ✓','ok'))">
              <i class="ti ti-copy"></i> کپی لینک
            </button>
            <button class="btn btn-g" onclick="showQR(window._bogzarnetLinks[${i}].label, window._bogzarnetLinks[${i}].vless)">
              <i class="ti ti-qrcode"></i> QR
            </button>
          </div>
        </div>
      </div>
    `;
  };

  document.getElementById('root').innerHTML=`
    <div class="sub-info">
      <div class="sub-eyebrow"><i class="ti ti-folders"></i> گروه دسترسی</div>
      <div class="sub-name">${esc(d.name)}</div>
      ${d.desc ? `<div class="sub-desc">${esc(d.desc)}</div>` : ''}
      <div class="sub-meta-row"><i class="ti ti-clock"></i> آخرین بروزرسانی: ${new Date().toLocaleTimeString('fa-IR')}</div>
      <div class="sub-sub-box">
        <span class="sub-sub-url">${esc(subUrl)}</span>
        <button class="btn btn-pur" style="padding:7px 12px;font-size:10.5px" onclick="navigator.clipboard.writeText(window._bogzarnetSubUrl).then(()=>toast('لینک ساب کپی شد ✓','ok'))">
          <i class="ti ti-copy"></i> کپی لینک ساب
        </button>
        <button class="btn btn-g" style="padding:7px 12px;font-size:10.5px" onclick="showQR(window._bogzarnetSubName + ' — کل گروه', window._bogzarnetSubUrl)">
          <i class="ti ti-qrcode"></i> QR کل
        </button>
      </div>
    </div>

    <div class="copy-all-bar">
      <div style="flex:1;min-width:160px">
        <div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه‌ی کانفیگ‌ها</div>
        <div class="copy-all-sub">تمام لینک‌های فعال این گروه را یک‌جا کپی کن</div>
      </div>
      <button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> کپی همه (${toFa(activeCount)})</button>
    </div>

    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-label">کانفیگ‌های فعال</div>
        <div class="stat-val">${toFa(activeCount)}</div>
        <div class="stat-sub">از ${toFa(d.links.length)} کانفیگ</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">اتصالات زنده</div>
        <div class="stat-val">${toFa(d.active_connections)}</div>
        <div class="stat-sub" style="color:var(--green-t);display:flex;align-items:center;gap:4px"><span class="dot"></span> آنلاین</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">کل مصرف</div>
        <div class="stat-val" style="font-size:17px;margin-top:3px">${esc(d.total_used_fmt)}</div>
        <div class="stat-sub">همه کانفیگ‌ها</div>
      </div>
    </div>

    ${internalLinks.length ? `
      <div class="cfg-title"><i class="ti ti-link"></i> کانفیگ‌های پنل (${toFa(internalLinks.length)})</div>
      <div class="cfg-grid">
        ${internalLinks.map((l, i) => renderCard(l, i)).join('')}
      </div>
    ` : ''}

    ${externalLinks.length ? `
      <div class="cfg-title"><i class="ti ti-world-upload"></i> سرورهای خارجی (${toFa(externalLinks.length)})</div>
      <div class="cfg-grid">
        ${externalLinks.map((l, i) => renderCard(l, internalLinks.length + i)).join('')}
      </div>
    ` : ''}
  `;
  setTimeout(() => autoRefresh(), 30000);
}
function copyAllConfigs(){
  const links=window._bogzarnetLinks||[];
  if(!links.length){toast('کانفیگی برای کپی نیست','');return}
  const text=links.map(l=>l.vless).join('\n');
  navigator.clipboard.writeText(text).then(()=>toast('همه‌ی '+toFa(links.length)+' کانفیگ کپی شد ✓','ok'));
}
async function autoRefresh(){
  try{
    const data = await loadData(savedPw);
    if (!data.locked) renderContent(data);
  } catch(e) {}
}
async function init(){
  try{
    const data = await loadData();
    if (data.locked) { renderLock(data.name); return; }
    renderContent(data);
  } catch(e) {
    document.getElementById('root').innerHTML =
      '<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری</div>';
  }
}
init();
</script>
</body></html>"""


# ═══════════════════════════════════════════════════════════════════════════════
# جایگزینی placeholder ها در HTML
# ═══════════════════════════════════════════════════════════════════════════════
LOGIN_HTML     = LOGIN_HTML.replace("__LOGO_INLINE__", LOGO_INLINE)
DASHBOARD_HTML = DASHBOARD_HTML.replace("__LOGO_INLINE__", LOGO_INLINE)


def get_public_page_html(uuid_key: str) -> str:
    return (
        PUBLIC_PAGE_HTML
        .replace("__LOGO_INLINE__", LOGO_INLINE)
        .replace("__UUID_KEY__", str(uuid_key))
    )
