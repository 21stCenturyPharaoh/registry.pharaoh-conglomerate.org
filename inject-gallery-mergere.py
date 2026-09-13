from pathlib import Path
import re
html=Path("index.html").read_text()

# Remove any old broken gallery
html=re.sub(r'<section id="bells-gallery".*?</section>','',html,flags=re.DOTALL)

# Correct gallery - using your compressed webp that ARE in assets/
gallery="""
<section id="bells-gallery" style="background:#000;border-top:4px solid gold;border-bottom:4px solid gold">
<div style="background:#111;text-align:center;padding:12px;color:#ffd700;font-weight:900;letter-spacing:3px;font-size:11px">🔔 BELLS & WHISTLES • VISUAL TESTIMONY • DREAM STELE 2026</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;background:gold">
<div style="background:#000"><img src="assets/02-out-of-africa.webp" style="width:100%;display:block" alt="OUT OF AFRICA"><div style="padding:6px;background:#000;color:#ffd700;font-size:9px;text-align:center">OUT OF AFRICA I CALLED MY SON</div></div>
<div style="background:#000"><img src="assets/03-dream-stele.webp" style="width:100%;display:block" alt="DREAM STELE"><div style="padding:6px;background:#000;color:#ffd700;font-size:9px;text-align:center">DREAM STELE 2026 • TUTMOSE IV</div></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;background:gold;margin-top:2px">
<div style="background:#000"><img src="assets/01-micdom-regalia.webp" style="width:100%;display:block" alt="MICDOM REGALIA"><div style="padding:6px;background:#000;color:#ffd700;font-size:9px;text-align:center">MICDOM REGALIA • COLONEL LAW48</div></div>
<div style="background:#000"><img src="assets/04-ebook-qr.webp" style="width:100%;display:block" alt="QR"><div style="padding:8px;background:gold;color:#000;font-size:10px;text-align:center;font-weight:900">SCAN TO ENSHRINE →</div></div>
</div>
</section>
"""

# Inject BEFORE Commerce Theater (so after Sphinx/Unsealing, before registry)
if 'COMMERCE THEATER' in html:
    html=html.replace('COMMERCE THEATER', gallery+'\n<h2>COMMERCE THEATER',1)
else:
    # fallback before BUSINESS REGISTRY
    html=html.replace('BUSINESS REGISTRY', gallery+'\n<h3>BUSINESS REGISTRY',1)

# Force webp
html=html.replace('.jpg','.webp').replace('.webp.webp','.webp')

Path("index.html").write_text(html)
print("Injected Bells into MERGERE - commerce preserved!")
