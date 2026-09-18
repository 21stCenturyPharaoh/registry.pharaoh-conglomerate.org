from pathlib import Path
html=Path("index.html").read_text()

manifesto='''
<!-- MOVEMENT MANIFESTO — SOUL RESTORED -->
<div style="background:radial-gradient(ellipse at center,#1a1500,#000);border-top:4px solid gold;border-bottom:4px solid gold;padding:24px 16px;text-align:center">
<h2 style="font-family:'Cinzel',serif;color:#ffd700;margin:0;font-size:18px;letter-spacing:0.12em">WE DON'T SELL RECORDS<br><span style="color:#fff;font-size:20px">WE SELL THE MOVEMENT</span></h2>
<div style="max-width:600px;margin:16px auto;background:rgba(255,215,0,0.08);border-left:4px solid gold;border-radius:10px;padding:14px;text-align:left">
<p style="font-size:12px;color:#fff;margin:0 0 10px 0;line-height:1.6"><b style="color:#ffd700">Micdom AI Records is NOT a record label in the old sense.</b> We don't sell mp3s. We don't chase streams. We don't beg Spotify.</p>
<p style="font-size:11px;color:#ccc;margin:0 0 10px 0">Every AI music video, every Spoken Word Revelation, every Unsealing — is a <b style="color:#ffd700">visual testimony</b> that the Dream Stele 2026 is alive in Monrovia. The record is just the receipt. The Movement is the product.</p>
<p style="font-size:11px;color:#fff;margin:0;font-weight:700"><span style="color:#ffd700">Registry</span> = infrastructure that holds it<br><span style="color:#ffd700">Micdom AI Records</span> = cultural voice that speaks it<br><span style="color:#ffd700">9 Businesses</span> = living proof that it accelerates</p>
</div>
<p style="font-size:10px;color:#ffd700;font-family:'Cinzel';letter-spacing:0.15em;margin-top:14px">FROM GIZA TO MONROVIA • FROM REVELATION TO RECORD • FROM RECORD TO MOVEMENT</p>
<a href="https://registry.pharaoh-conglomerate.org/mama-hajah-seal" style="display:inline-block;background:linear-gradient(180deg,#ffd700,#b89600);color:#000;padding:10px 20px;border-radius:20px;font-family:'Cinzel';font-weight:900;text-decoration:none;font-size:11px;margin-top:10px">ENTER THE MOVEMENT → $0.00</a>
</div>
'''

# Insert after MICDOM AI RECORDS section, before QR
html=html.replace('<img src="assets/04-ebook-qr.webp"', manifesto + '\n<img src="assets/04-ebook-qr.webp"')

Path("index.html").write_text(html)
print(f"Added Movement manifesto — {len(html)} bytes")
