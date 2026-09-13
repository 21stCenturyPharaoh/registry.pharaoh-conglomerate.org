from pathlib import Path
p=Path("index.html")
html=p.read_text()

glamour_section = """
<!-- GLAMOUR BOOK THRONE + BELLS & WHISTLES -->
<section id="book-glamour" style="background:#000;color:#f5e6a6;padding:0;border:3px solid gold;margin:0">
  <div style="position:relative">
    <img src="assets/pharaoh_book_sunset.webp" style="width:100%;display:block" alt="THE UNSEALING OF THE PROPHETS - Glamour Throne">
    <div style="position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(0,0,0,0.9));padding:40px 16px 16px 16px">
      <h2 style="margin:0;color:#ffd700;font-size:26px;text-shadow:0 2px 10px #000">THE UNSEALING OF THE PROPHETS</h2>
      <p style="margin:4px 0 0 0;font-size:14px">GIZA TO MONROVIA • MAMA HAJAH SEAL 21 • Sept 21 7x3 Completion</p>
    </div>
  </div>
  
  <div style="padding:18px;background:#0a0a0a">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:16px">
      <img src="assets/pharaoh_book_sunset.webp" style="width:100%;border:1px solid gold;border-radius:6px" alt="Dream Stele">
      <div style="border:1px solid gold;border-radius:6px;padding:10px;background:#111">
        <p style="margin:0 0 6px 0;font-weight:bold;color:#ffd700">OUT OF AFRICA I CALLED MY SON</p>
        <p style="margin:0;font-size:12px;line-height:1.4">From Kemet (Blackness) → Cush (Liberia) → The Waters (Atlantic Covenant). Isaiah 19:19 altar in midst of Egypt.</p>
      </div>
    </div>

    <a href="https://registry.pharaoh-conglomerate.org/mama-hajah-seal" style="display:block;background:gold;color:#000;text-align:center;padding:14px;font-weight:bold;text-decoration:none;border-radius:8px;margin:8px 0">📖 GET THE EBOOK & REGISTRY →</a>
    
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:10px 0">
      <a href="https://www.amazon.com/s?k=UNSEALING+THE+PROPHETS+Pharaoh+Momolu" style="background:#111;border:1px solid #333;color:#fff;text-align:center;padding:10px;border-radius:6px;text-decoration:none;font-size:13px">Amazon Kindle<br><b>$0.00 Unlimited<br>$9.99 Buy</b></a>
      <a href="https://youtu.be/1ePOgjtA2q8" style="background:#111;border:1px solid #333;color:#fff;text-align:center;padding:10px;border-radius:6px;text-decoration:none;font-size:13px">🎧 Watch<br><b>The Unsealing Trailer</b></a>
    </div>

    <p style="font-size:11px;color:#888;text-align:center;margin:12px 0 0 0">Payment: +231 776961800 Mama Hajah • Office: +1 771 223-8021 • registry@pharaoh-conglomerate.org<br>#UnsealingTheProphets #TheSphinxSpeaks #AlifLamMim #DreamStele2026</p>
  </div>
</section>
"""

# Insert after SPHINX SPEAKS section or before BUSINESS REGISTRY
if "BUSINESS REGISTRY" in html:
    html = html.replace("BUSINESS REGISTRY", glamour_section + "\nBUSINESS REGISTRY")
else:
    html = html.replace("</section>", "</section>\n" + glamour_section, 1)

Path("index.html").write_text(html)
print("Glamour throne injected prominently!")
