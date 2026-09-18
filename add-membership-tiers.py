from pathlib import Path
html=Path("index.html").read_text()

tiers='''
<!-- MEMBERSHIP TIERS — CITIZENS FULFILL TASKS -->
<div style="background:#111;padding:20px 14px;border-top:4px solid gold;border-bottom:4px solid gold">
<h2 style="font-family:'Cinzel',serif;color:#ffd700;margin:0;text-align:center;font-size:15px;letter-spacing:0.1em">CITIZENSHIP TIERS • WE FULFILL TASKS</h2>
<p style="font-size:10px;color:#ccc;text-align:center;margin:8px 0">We don't sell memberships. We enlist citizens who fulfill. Each tier = tasks completed.</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px">

<div style="background:linear-gradient(180deg,#1a1500,#0a0a0a);border:1px solid gold;border-radius:12px;padding:12px;text-align:center">
<b style="color:#ffd700;font-family:'Cinzel';font-size:12px">CHERISHED • $0</b><br>
<span style="font-size:9px;color:#fff">ENTRY • WITNESS</span><br>
<span style="font-size:8px;color:#aaa">Tasks: Watch 2 explainers + 1 Silent Testimony • Share QR</span><br>
<span style="font-size:8px;color:#ffd700">→ Gets Ebook + Dream Stele access</span>
</div>

<div style="background:linear-gradient(180deg,#111,#000);border:1px solid #555;border-radius:12px;padding:12px;text-align:center">
<b style="color:#ffd700;font-family:'Cinzel';font-size:12px">SCRIBE • $7/mo</b><br>
<span style="font-size:9px;color:#fff">DOCUMENT</span><br>
<span style="font-size:8px;color:#aaa">Tasks: Transcribe 1 Temple Session • Post testimony • Route via Hermes-Toth</span><br>
<span style="font-size:8px;color:#ffd700">→ Micdom AI Records credit</span>
</div>

<div style="background:linear-gradient(180deg,#111,#000);border:1px solid #555;border-radius:12px;padding:12px;text-align:center">
<b style="color:#ffd700;font-family:'Cinzel';font-size:12px">BUILDER • $21/mo</b><br>
<span style="font-size:9px;color:#fff">BUILD</span><br>
<span style="font-size:8px;color:#aaa">Tasks: Build 1 business page • cwebp <70K • Git push via Micdom-iPhone</span><br>
<span style="font-size:8px;color:#ffd700">→ Registry listing + Bolt.new</span>
</div>

<div style="background:linear-gradient(180deg,#221a00,#000);border:2px solid gold;border-radius:12px;padding:12px;text-align:center;box-shadow:0 0 15px rgba(255,215,0,0.3)">
<b style="color:#ffd700;font-family:'Cinzel';font-size:12px">ACCELERATOR • $77/mo</b><br>
<span style="font-size:9px;color:#fff">ACCELERATE</span><br>
<span style="font-size:8px;color:#aaa">Tasks: Fulfill 9 business tasks • Auto-delivery via TOTH • WhatsApp Temple routing</span><br>
<span style="font-size:8px;color:#ffd700">→ Full Pharaoh Conglomerate • EIN 88-0836464</span>
</div>

</div>

<p style="font-size:9px;color:#666;text-align:center;margin:14px 0 0 0">All tiers fulfill tasks. No passive subscribers. Tasks = proof of citizenship. Registry tracks fulfillment via pharaoh-auto-delivery.sh in Termux.</p>
<a href="https://registry.pharaoh-conglomerate.org/mama-hajah-seal" style="display:block;background:linear-gradient(180deg,#ffd700,#b89600);color:#000;padding:12px;border-radius:10px;font-family:'Cinzel';font-weight:900;text-align:center;text-decoration:none;font-size:11px;margin-top:12px">FULFILL FIRST TASK → $0.00</a>
</div>
'''

html=html.replace('<!-- MEMBERSHIP TIERS', tiers) if '<!-- MEMBERSHIP TIERS' in html else html.replace('<div style="padding:18px;background:#111;border-bottom:3px solid gold">\n<h2 style="color:#ffd700', tiers + '\n<div style="padding:18px;background:#111;border-bottom:3px solid gold">\n<h2 style="color:#ffd700')

# Second attempt insert before WORKER INTERFACES if first failed
if tiers not in html:
    html=Path("index.html").read_text()
    html=html.replace('<div style="padding:18px;background:#111;border-bottom:3px solid gold">\n<h2 style="color:#ffd700;margin:0 0 12px 0;font-size:13px;text-align:center">⚙️ WORKER INTERFACES', tiers + '\n<div style="padding:18px;background:#111;border-bottom:3px solid gold">\n<h2 style="color:#ffd700;margin:0 0 12px 0;font-size:13px;text-align:center">⚙️ WORKER INTERFACES')

Path("index.html").write_text(html)
print("Added tiers")
