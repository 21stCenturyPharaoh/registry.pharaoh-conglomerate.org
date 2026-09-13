from pathlib import Path
import re
html=Path("index.html").read_text()

# Remove any old bells gallery
html=re.sub(r'<section id="bells-gallery".*?</section>', '', html, flags=re.DOTALL)

full_gallery = """
<!-- FULL BELLS & WHISTLES GALLERY - CONSOLIDATED TEMPLE -->
<section id="bells-gallery" style="background:#000;padding:0;border-top:4px solid gold;border-bottom:4px solid gold">
  <div style="background:#111;text-align:center;padding:12px;color:#ffd700;font-weight:bold;letter-spacing:3px;font-size:12px">BELLS & WHISTLES • THE VISUAL TESTIMONY • DREAM STELE 2026</div>
  
  <!-- ROW 1: OUT OF AFRICA + DREAM STELE -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;background:gold">
    <div style="background:#000;position:relative">
      <img src="assets/02-out-of-africa.jpg" style="width:100%;display:block" alt="OUT OF AFRICA I CALLED MY SON">
      <div style="position:absolute;bottom:0;left:0;right:0;background:rgba(0,0,0,0.8);padding:6px;color:#ffd700;font-size:10px;text-align:center">OUT OF AFRICA I CALLED MY SON • Isaiah 19:19</div>
    </div>
    <div style="background:#000;position:relative">
      <img src="assets/03-dream-stele.jpg" style="width:100%;display:block" alt="DREAM STELE 2026">
      <div style="position:absolute;bottom:0;left:0;right:0;background:rgba(0,0,0,0.8);padding:6px;color:#ffd700;font-size:10px;text-align:center">DREAM STELE 2026 • TUTMOSE IV UNSEALED</div>
    </div>
  </div>
  
  <!-- ROW 2: MICDOM REGALIA + EBOOK QR -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;background:gold;margin-top:2px">
    <div style="background:#000;position:relative">
      <img src="assets/01-micdom-regalia.jpg" style="width:100%;display:block" alt="MICDOM PHARAOH REGALIA">
      <div style="position:absolute;bottom:0;left:0;right:0;background:rgba(0,0,0,0.8);padding:6px;color:#ffd700;font-size:10px;text-align:center">MICDOM PHARAOH • COLONEL LAW48</div>
    </div>
    <div style="background:#000;position:relative">
      <img src="assets/04-ebook-qr.jpg" style="width:100%;display:block" alt="GET EBOOK QR">
      <div style="position:absolute;bottom:0;left:0;right:0;background:gold;padding:8px;color:#000;font-size:11px;font-weight:bold;text-align:center">SCAN TO ENSHRINE →</div>
    </div>
  </div>
</section>
"""

# Insert after glamour throne
if 'id="book-glamour"' in html:
    html = re.sub(r'(<section id="book-glamour".*?</section>)', r'\1' + "\n" + full_gallery, html, flags=re.DOTALL, count=1)
else:
    # fallback before BUSINESS REGISTRY
    html = html.replace("BUSINESS REGISTRY", full_gallery + "\nBUSINESS REGISTRY")

Path("index.html").write_text(html)
print("FULL GALLERY RESTORED - 4 images + throne")
