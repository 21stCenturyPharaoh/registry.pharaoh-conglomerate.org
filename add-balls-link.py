from pathlib import Path
html=Path("index.html").read_text()
html=html.replace('BUILT META AI STRONG','<a href="/temple/balls/" style="display:inline-block;background:gold;color:#000;padding:8px 16px;border-radius:20px;font-size:11px;font-weight:900;text-decoration:none;margin-bottom:12px">🔴 ENTER TEMPLE BALLS LIVE → Hallel / Bolt / Auto-Delivery</a><br>BUILT META AI STRONG')
Path("index.html").write_text(html)
print("added balls link")
