import os, sqlite3
from flask import Flask, render_template_string, jsonify, request
app = Flask(__name__)
DB="/tmp/alpha_maya_mod.db"
def init():
    con=sqlite3.connect(DB)
    con.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, agent TEXT, task TEXT, created TEXT)")
    con.commit(); con.close()
init()

@app.route('/')
def home():
    return render_template_string("""
<html><head><meta name=viewport content="width=device-width,initial-scale=1"><title>ALPHA MAYA MOD - 645</title>
<style>
*{box-sizing:border-box} body{margin:0;background:#050508;color:#fff;font-family:Inter;overflow:hidden}
.desktop{width:100vw;height:100vh;background:radial-gradient(ellipse at 30% 20%,#0a2a1a 0%,#050510 60%);position:relative}
.left-icons{position:absolute;left:12px;top:12px;display:flex;flex-direction:column;gap:14px}
.ico{width:52px;text-align:center;font-size:9px;color:#00ff88}
.ico div{width:42px;height:42px;background:linear-gradient(135deg,#00ff8815,#00ff8825);border:1px solid #00ff8844;border-radius:12px;display:flex;align-items:center;justify-content:center;margin:0 auto 4px;font-size:18px;box-shadow:0 0 15px #00ff8820}
.center{position:absolute;left:50%;top:48%;transform:translate(-50%,-50%);text-align:center}
.alpha-girl{width:300px;height:400px;background:linear-gradient(180deg,#0f2a1a 0%,#05100a 100%);border:1px solid #00ff8844;border-radius:32px;position:relative;box-shadow:0 0 80px #00ff8830, inset 0 0 30px #00ff8810;overflow:hidden}
.alpha-girl::before{content:'ALPHA ♡ 645';position:absolute;top:16px;left:16px;font-size:13px;font-weight:900;color:#00ff88;letter-spacing:2px;text-shadow:0 0 10px #00ff88}
.neon-line{position:absolute;top:0;left:0;width:100%;height:2px;background:linear-gradient(90deg,transparent,#00ff88,transparent);animation:slide 2s infinite}
@keyframes slide{0%{transform:translateX(-100%)}100%{transform:translateX(100%)}}
.face{position:absolute;top:42%;left:50%;transform:translate(-50%,-50%);font-size:88px;filter:drop-shadow(0 0 20px #00ff8860);animation:float 3s infinite}
@keyframes float{0%,100%{transform:translate(-50%,-50%)}50%{transform:translate(-50%,-58%)}}
.mug{position:absolute;bottom:50px;left:14px;background:#000c;border:1px solid #00ff8844;padding:7px 12px;border-radius:20px;font-size:10px;color:#00ff88}
.status{position:absolute;bottom:18px;left:14px;font-size:8px;color:#00ff88;letter-spacing:1px}
.status::before{content:'●';animation:blink 1s infinite} @keyframes blink{0%,100%{opacity:1}50%{opacity:0.2}}
.phone{position:absolute;right:18px;top:18px;width:158px;height:340px;background:#000;border:1.5px solid #1a1a1a;border-radius:28px;overflow:hidden;box-shadow:0 0 40px #000, 0 0 20px #00ff8820}
.p-screen{width:100%;height:100%;background:linear-gradient(180deg,#0a1a12 0%,#000 100%);padding:10px;position:relative}
.p-girl{width:100%;height:58%;background:linear-gradient(180deg,#0f2a1a,#05100a);border:1px solid #00ff8822;border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:38px;position:relative}
.p-girl::after{content:'ALPHA-001';position:absolute;bottom:6px;font-size:7px;color:#00ff88}
.p-info{font-size:7.5px;color:#00ff8888;margin-top:8px;line-height:1.4}
.p-info b{color:#00ff88}
.dock{position:absolute;bottom:10px;left:10px;right:10px;display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.d{height:26px;background:#00ff8810;border:1px solid #00ff8815;border-radius:8px}
.chat{position:absolute;bottom:14px;left:50%;transform:translateX(-50%);width:92%;max-width:440px;background:#000d;border:1px solid #00ff8844;border-radius:20px;padding:10px;backdrop-filter:blur(12px);box-shadow:0 0 30px #00ff8815}
.msg{font-size:11px;padding:8px 12px;border-radius:14px;margin:5px 0}
.a{background:#00ff8815;border:1px solid #00ff8825} .u{background:#00ff88;color:#000;margin-left:auto;text-align:right}
.ctrl{display:flex;gap:5px;margin-top:8px}
.ctrl input{flex:1;padding:10px;background:#0a0a0a;border:1px solid #222;border-radius:20px;color:#fff;font-size:11px}
.ctrl button{padding:10px 12px;border-radius:20px;border:none;font-weight:800;font-size:10px;cursor:pointer}
.badge{position:absolute;top:12px;left:50%;transform:translateX(-50%);background:#00ff88;color:#000;padding:5px 12px;border-radius:20px;font-size:9px;font-weight:900;letter-spacing:1px}
</style></head>
<body>
<div class=desktop>
<div class=left-icons>
<div class=ico><div>♡</div>ALPHA<br>CORE</div>
<div class=ico><div>📦</div>KDP<br>FACTORY</div>
<div class=ico><div>🎨</div>DESIGN<br>100</div>
<div class=ico><div>🛡️</div>SECURITY<br>QC</div>
</div>

<div class=badge>ALPHA MOD • 645 AGENTS • VOICE • CAMERA • MODIFIED FROM MAYA</div>

<div class=center>
<div class=alpha-girl>
<div class=neon-line></div>
<div class=face>😉</div>
<div class=mug>☕ ALPHA Coffee - 24/7 Active</div>
<div class=status> ALPHA LISTENING • 645 READY • MODIFIED</div>
</div>
</div>

<div class=phone>
<div class=p-screen>
<div class=p-girl>🤖</div>
<div class=p-info>
<b>ALPHA AI</b> ♡<br>
Your AI Assistant<br>
● 645 Agents<br>
● KDP Factory<br>
● Design Master<br>
● Always Listening<br>
● Camera Se Padhna
</div>
<div class=dock><div class=d></div><div class=d></div><div class=d></div><div class=d></div><div class=d></div><div class=d></div><div class=d></div><div class=d></div></div>
</div>
</div>

<div class=chat>
<div id=ch>
<div class=msg a>🤖 <b>ALPHA MOD:</b> Ho gaya scanner band - Main ALPHA modified version me aa gayi! Same placement - lekin ALPHA style me! ☕<br>Camera se padhna ready - bolo "54 se KDP banao" - main voice me bolungi!</div>
</div>
<div class=ctrl>
<input id=inp placeholder="Bolo... 54 se KDP / Camera se padhna...">
<button style="background:#00ff88;color:#000" onclick="send()">SEND</button>
<button style="background:#111;color:#00ff88;border:1px solid #00ff88" onclick="mic()">🎤</button>
<button style="background:#111;color:#00ff88;border:1px solid #00ff88" onclick="cam()">📷</button>
</div>
<video id=vid style="display:none;width:100%;height:100px;border-radius:12px;margin-top:6px" autoplay></video>
</div>

</div>

<script>
function speak(t){
 let c=t.replace(/<[^>]*>/g,''); let u=new SpeechSynthesisUtterance(c); u.lang='bn-BD'; u.rate=1;
 speechSynthesis.cancel(); speechSynthesis.speak(u);
 document.querySelector('.face').textContent='😊'; setTimeout(()=>document.querySelector('.face').textContent='😉',1200);
}
function add(h,cls){
 let ch=document.getElementById('ch'); let d=document.createElement('div'); d.className='msg '+cls; d.innerHTML=h; ch.appendChild(d); ch.scrollTop=9999;
 speak(h);
 fetch('/t',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({task:h})});
}
function send(){
 let i=document.getElementById('inp'); let t=i.value.trim(); if(!t) return;
 add(t,'u'); i.value='';
 let l=t.toLowerCase(); let r='';
 if(l.includes('54')||l.includes('kdp')) r='Agent 54 - KDP Expert ko de diya - 50 books bana raha hai - MODIFIED ALPHA style me - 100% check!';
 else if(l.includes('camera')||l.includes('padhna')) r='Camera on kar diya - dikhao kya padhna hai - main modified ALPHA hu - MAYA se better!';
 else if(l.includes('design')||l.includes('100')) r='Design Master 100 - Modified ALPHA design - 100 T-shirt ready ho rahe hai!';
 else r='Ho gaya bhai! '+t+' - ALPHA MOD - 645 agents - same placement lekin mera apna style!';
 setTimeout(()=>add('🤖 ALPHA MOD: '+r,'a'),500);
}
function mic(){
 let R=window.SpeechRecognition||window.webkitSpeechRecognition;
 if(!R){ alert('Chrome use karo'); return; }
 let r=new R(); r.lang='bn-BD'; r.start(); add('🎤 Sun rahi hu... bolo!','u');
 r.onresult=e=>{ document.getElementById('inp').value=e.results[0][0].transcript; send(); };
}
function cam(){
 let v=document.getElementById('vid'); v.style.display='block';
 navigator.mediaDevices.getUserMedia({video:true}).then(s=>{ v.srcObject=s; add('📷 Camera se padhna - MODIFIED ALPHA - dekh rahi hu - kya padhu?','a'); }).catch(()=>add('Camera permission do bhai!','a'));
}
document.getElementById('inp').addEventListener('keydown',e=>{ if(e.key==='Enter') send(); });
setTimeout(()=>{ speak('Ho gaya scanner band - main ALPHA modified version me aa gayi home screen par - same placement lekin ALPHA style'); },800);
</script>
</body></html>
    """)

@app.route('/t', methods=['POST'])
def t():
    try:
        d=request.json; con=sqlite3.connect(DB); con.execute("INSERT INTO tasks VALUES (NULL,?,?,?)",("ALPHA-MOD",d.get('task',''),str(__import__('datetime').datetime.now()))); con.commit(); con.close()
    except: pass
    return jsonify({"ok":True})

@app.route('/use', methods=['GET','POST'])
@app.route('/fix', methods=['GET','POST'])
def c(): return "<script>location.href='/'</script>"

if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))
