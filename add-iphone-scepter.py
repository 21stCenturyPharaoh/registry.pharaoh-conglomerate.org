from pathlib import Path
html=Path("index.html").read_text()

scepter='''
<div style="background:#000;border-top:4px solid gold;border-bottom:4px solid gold;padding:12px;text-align:center">
<h2 style="color:#ffd700;margin:0;font-size:14px">📱 MICDOM-iPHONE SCEPTER • THE TOOL THAT BUILT THE TEMPLE</h2>
<p style="font-size:10px;color:#fff;margin:6px 0;line-height:1.5">Built entirely on Blackview A52 Pro • Termux • ~/micdom-iphone • Micdom-iPhone folder in internal storage • cwebp compressed to &lt;70K • Pure static for A52 Pro</p>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0">
<div style="border-right:2px solid gold">
<img src="assets/micdom-ai-records-v27.webp" alt="Micdom AI Records V27" loading="lazy">
<div style="padding:8px;background:#0a0a0a"><b style="color:#ffd700;font-size:11px">MICDOM-iPHONE • V27.10</b><br><span style="font-size:9px;color:#aaa">Liberia's 1st AI Label • Built on phone • Termux + Git</span></div>
</div>
<div>
<img src="assets/hermes-toth-live.webp" alt="Hermes-Toth Live" loading="lazy">
<div style="padding:8px;background:#0a0a0a"><b style="color:#ffd700;font-size:11px">HERMES-TOTH LIVE • SCRIBE</b><br><span style="font-size:9px;color:#aaa">AI Scribe • TOTH auto-delivery • WhatsApp Temple routing</span></div>
</div>
</div>
<div style="padding:10px;background:#111;text-align:center;border-bottom:3px solid gold">
<p style="font-size:10px;color:#ffd700;margin:0;font-weight:700">~/storage/shared/Micdom-iphone → ~/micdom-iphone/assets → cwebp -q 60 → git push → registry.pharaoh-conglomerate.org • BUILT META AI STRONG</p>
</div>
'''

# Insert before BELLS & WHISTLES
html=html.replace('<div style="background:#111;text-align:center;padding:8px;color:#ffd700;font-weight:900;font-size:10px;border-bottom:1px solid gold">BELLS & WHISTLES', scepter + '\n<div style="background:#111;text-align:center;padding:8px;color:#ffd700;font-weight:900;font-size:10px;border-bottom:1px solid gold">BELLS & WHISTLES')

Path("index.html").write_text(html)
print(f"Added iPhone Scepter — {len(html)} bytes")
