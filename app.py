from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ALPHA OS v3 FINAL - Desert King</title>
<style>
body{background:#000;color:#00ff88;font-family:monospace;margin:0;padding:15px}
.card{border:1px solid #00ff88;border-radius:15px;padding:15px;margin:10px 0;background:#0a1a0f;box-shadow:0 0 20px #00ff8844}
h1{color:#00ff88;text-align:center;text-shadow:0 0 10px #00ff88}
.glow{color:#fff;text-shadow:0 0 10px #00ff88}
.btn{background:#00ff88;color:#000;padding:12px 20px;border-radius:10px;text-decoration:none;display:inline-block;font-weight:bold;margin:5px}
.factory{background:linear-gradient(45deg,#0a1a0f,#1a3a2f);border-color:gold}
.gold{color:gold;border-color:gold}
</style>
</head>
<body>
<h1>🚀 ALPHA MONEY OS v3 FINAL</h1>
<div style="text-align:center" class="glow">Riyadh Desert King 👑 | CEO: Tanvir | ONLINE</div>
<div class="card">
<b>👑 MISSION: $140k/month</b><br>
Protect Tanvir & Make $140k/month via Coloring Books<br>
Safety: <span style="color:lime">Emergency Kill Active ✅</span><br>
Status: <span style="color:lime">ONLINE FINAL ✅</span>
</div>
<div class="card factory gold">
<b>🏭 COLORING BOOK FACTORY READY</b><br>
Cozy Friends KDP 50 Pages | $9.99<br>
Style: Coco Wyo Style<br>
Target: $9.99 x 100 = $999<br>
<button class="btn" onclick="alert('Factory Starting... 50 Pages Generating!')">🎨 GENERATE BOOK NOW</button>
</div>
<div class="card">
<b>💰 6 STREAMS EMPIRE</b><br>
✅ KDP Coloring Books<br>
✅ POD Desert King Designs<br>
✅ Digital Products<br>
✅ Pinterest Empire 10k Target<br>
✅ YouTube Automation<br>
✅ Trading DEMO - Halal Only
</div>
<div class="card">
<b>🧠 MEMORY TREE - ALPHA BRAIN</b><br>
Root: Alpha<br>
Synapses: 1482 Online<br>
- Hunter loves Blue Holographic UI 🔵<br>
- Works at night 2AM 🌙<br>
- Scent: ALFA AL OUD NOOR 540 👑<br>
- Location: Riyadh Desert King<br>
<div style="height:8px;background:#003311;margin-top:10px;border-radius:10px"><div style="width:88%;height:100%;background:#00ff88;box-shadow:0 0 10px #00ff88"></div></div>
88% Memory Loaded
</div>
<div class="card">
<b>📊 TODAY GOAL</b><br>
Upload Cozy Friends Book on Amazon KDP<br>
Log: First Sale Loading...<br>
Factory: 20mb RAM | 0% CPU | ONLINE 24/7<br>
No Stress - Auto Mode ✅
</div>
<div style="text-align:center;margin-top:20px">
<a class="btn" href="/">🔄 REFRESH OS</a>
<a class="btn" style="background:gold" href="#">👑 DESERT KING MODE</a>
</div>
<p style="text-align:center;color:#555;margin-top:30px">#ALFAEmpire | ALPHA-OS v3 FINAL | Tanvir ALFA - Riyadh CEO</p>
</body>
</html>
"""
@app.route('/')
def home():
    return HTML
if __name__ == '__main__':
    app.run()
