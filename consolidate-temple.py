from pathlib import Path
p=Path("index.html")
html=p.read_text()

# Remove all duplicate glamour/sphinx injections we added
import re
# Keep only first Sphinx Speaks + first Glamour, delete extras
# Count occurrences
parts = html.split("<!-- GLAMOUR BOOK THRONE")
if len(parts) > 2:
    # Keep first glamour + rebuild rest without glamour markers
    html = parts[0] + "<!-- GLAMOUR BOOK THRONE" + parts[1].split("BUSINESS REGISTRY")[0] + "BUSINESS REGISTRY" + "".join([x.split("BUSINESS REGISTRY")[-1] if "BUSINESS REGISTRY" in x else "" for x in parts[2:]])
    # Actually simpler: remove duplicate glamour sections entirely and re-inject once cleanly at the end
    html = re.sub(r'<!-- GLAMOUR BOOK THRONE.*?BUSINESS REGISTRY', 'BUSINESS REGISTRY', html, flags=re.DOTALL)

parts = html.split("<!-- NEW HERO: THE SPHINX SPEAKS")
if len(parts) > 2:
    # Keep only first Sphinx hero
    html = parts[0] + "<!-- NEW HERO: THE SPHINX SPEAKS" + parts[1] + "".join([x.split("</section>")[-1] if "</section>" in x else x for x in parts[2:]])

# Now ensure single clean structure order: Sovereign Wing -> Sphinx Speaks -> Glamour Throne -> Commerce Theater -> Footer

clean_glamour = """
<!-- GLAMOUR BOOK THRONE - CONSOLIDATED -->
<section id="book-glamour" style="background:#000;color:#f5e6a6;padding:0;border-top:4px solid gold;border-bottom:4px solid gold">
  <div style="position:relative">
    <img src="assets/pharaoh_book_sunset.webp" style="width:100%;display:block" alt="THE UNSEALING - Sphinx Beaming">
    <div style="position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(0,0,0,0.95));padding:50px 16px 16px 16px">
      <h2 style="margin:0;color:#ffd700;font-size:28px;text-shadow:0 2px 15px #000;letter-spacing:1px">THE UNSEALING OF THE PROPHETS</h2>
      <p style="margin:6px 0 0 0;font-size:13px;color:#fff">MAMA HAJAH SEAL 21 • Sept 21 7x3 Completion • GIZA TO MONROVIA • Isaiah 19:19</p>
    </div>
  </div>
  <div style="padding:16px;background:#0a0a0a;text-align:center">
    <a href="https://registry.pharaoh-conglomerate.org/mama-hajah-seal" style="display:block;background:gold;color:#000;padding:14px;font-weight:bold;text-decoration:none;border-radius:8px;margin:0 0 10px 0">📖 GET THE EBOOK & REGISTRY →</a>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
      <a href="https://www.amazon.com/s?k=UNSEALING+THE+PROPHETS+Pharaoh+Momolu" style="background:#111;border:1px solid gold;color:#ffd700;padding:10px;border-radius:6px;text-decoration:none;font-size:12px">Amazon<br><b>Kindle $0.00 Unlimited<br>$9.99 Buy</b></a>
      <a href="https://youtu.be/1ePOgjtA2q8?si=8Y3K-tzoILC3Q1wE" style="background:#111;border:1px solid gold;color:#ffd700;padding:10px;border-radius:6px;text-decoration:none;font-size:12px">🎧 Watch Trailer<br><b>The Sphinx Speaks</b></a>
    </div>
    <p style="font-size:10px;color:#666;margin:10px 0 0 0">Payment +231 776961800 Mama Hajah • Office +1 771 223-8021 • registry@pharaoh-conglomerate.org</p>
  </div>
</section>
"""

# Ensure glamour is right after Sphinx section, before Commerce
if 'id="book-glamour"' in html:
    # Remove existing glamour to re-insert in correct spot
    html = re.sub(r'<section id="book-glamour".*?</section>', '', html, flags=re.DOTALL)

# Find where Sphinx section ends
sphinx_end = html.find("</section>", html.find("THE SPHINX SPEAKS"))
if sphinx_end!= -1:
    sphinx_end += len("</section>")
    html = html[:sphinx_end] + "\n" + clean_glamour + "\n" + html[sphinx_end:]
else:
    # fallback before BUSINESS REGISTRY
    html = html.replace("BUSINESS REGISTRY", clean_glamour + "\nBUSINESS REGISTRY")

# Final footer ensure Built Meta AI Strong
html = html.replace("Built Meta AI Strong 👊😎👌", "Built Meta AI Strong 👊😎👌")
if "Built Meta AI Strong" not in html:
    html = html.replace("</body>", '<div style="text-align:center;padding:20px;background:#000;color:#fff;border-top:3px solid gold"><p style="font-weight:bold">Built Meta AI Strong 👊😎👌</p><p style="font-size:11px">Pharaoh Conglomerate • COLONEL|LAW48 • EIN 880836464 • Monrovia • registry.pharaoh-conglomerate.org</p></div></body>')

Path("index.html").write_text(html)
print("CONSOLIDATED: One Sphinx + One Glamour Throne + Commerce Theater")
