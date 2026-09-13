from pathlib import Path
p=Path("index.html")
html=p.read_text()

new_hero = """
<!-- NEW HERO: THE SPHINX SPEAKS -->
<section id="pharaoh-sphinx" style="background:#0a0a0a;color:#f5e6a6;padding:32px 18px;border-top:4px solid gold;border-bottom:4px solid gold">
<h2 style="font-size:28px;text-align:center;margin:0 0 10px 0">About Pharaoh M. Sirleaf; Lǎobǎn: THE SPHINX SPEAKS 🦁👁️</h2>
<h3 style="text-align:center;color:#ffd700;margin:0 0 18px 0">The Book That Started The Movement — The Dream Stele Is Enshrined</h3>

<p style="line-height:1.6">For 1400 years scholars said "Allah knows best" about <b>Alif Lam Mim</b>.</p>
<p style="line-height:1.6">The Dream Stele of Thutmose IV says a prince slept at the feet of the Sphinx and was given a kingdom for clearing the sand.【8694333543931631134†L6-L9】</p>
<p style="line-height:1.6"><b>I, Pharaoh M. Sirleaf;</b> a legally blind Priest of The Most High YHVH/Yeshua — after The Essene Order of Melchizedek — slept at the feet of the Sphinx; in this case, The Ruach Ha Kodesh! He spoke.</p>

<div style="background:#111;border:1px solid gold;padding:12px;margin:16px 0;border-radius:8px">
<p style="margin:4px 0"><b>Alif</b> - Kemet (Blackness)</p>
<p style="margin:4px 0"><b>Lam</b> - Cush (Land of Cham / Liberia)</p>
<p style="margin:4px 0"><b>Mim</b> - The Waters (The Atlantic Covenant)</p>
</div>

<p style="line-height:1.6">This is the <b>UNSEALING OF THE PROPHETS — The Mama Hajah Seal (Model 21) — Sept 21, 7x3 Completion.</b></p>
<p style="line-height:1.6">From Giza to Monrovia — <b>Isaiah 19:19 — An Altar in the midst of Egypt.</b></p>

<div style="margin:18px 0">
<p>📖 <b>GET THE EBOOK:</b></p>
<a href="https://registry.pharaoh-conglomerate.org/mama-hajah-seal" style="color:#ffd700;display:block">👉 registry.pharaoh-conglomerate.org/mama-hajah-seal</a>
<a href="https://www.amazon.com/s?k=UNSEALING+THE+PROPHETS+Pharaoh+Momolu" style="color:#ffd700;display:block">👉 Amazon: UNSEALING THE PROPHETS Pharaoh Momolu</a>
</div>

<div style="margin:16px 0">
<iframe width="100%" height="215" src="https://www.youtube.com/embed/1ePOgjtA2q8" frameborder="0" allowfullscreen style="border:1px solid gold;border-radius:8px"></iframe>
<p style="font-size:12px;color:#aaa">00:00 Dream (Thutmose IV) • 00:12 Sphinx Speaks • 00:28 Alif Lam Mim Unsealed • 00:45 Clearing Sand (Model21) • 01:10 Altar in Liberia • 01:30 The Book</p>
</div>

<p style="font-size:12px;color:#ccc">#UnsealingTheProphets #TheSphinxSpeaks #AlifLamMim #PharaohMomolu #DreamStele #Kemet #Cush #Liberia</p>

<hr style="border:0;border-top:1px solid #333;margin:22px 0">

<h3>About MICDOM AI RECORDS — Liberia's 1st AI Label</h3>
<p style="line-height:1.6;font-size:14px">Micdom AI Records is Liberia's 1st AI Record Label, 100% Liberian Operated prophetic arts imprint. Official cultural & audio-visual arm of Registry@Pharaoh Conglomerate. Owned by Human Rights Angels Registry Inc. (US C-Corp EIN 880836464) DBA Registry@Pharaoh / Micdom AI Records. Pharaoh Conglomerate is legacy public name now consolidated under Registry@Pharaoh.</p>
<p style="font-size:13px;line-height:1.5">We don't sell $5 MP3s. We sell citizenship to Pharaoh-Chain 0x504841. 107 Acres. One Chain. Zero Heidelberg. Tiers: FREE Diamond Listener • $7/mo Citizen • $48/mo Imhotep Initiate [LAW 48] • $107/mo Sovereign Builder [107 Acres] • $5048 Lifetime COLONEL|LAW48</p>
<p style="font-size:12px">Contact: m.sirleaf@pharaoh-conglomerate.org | WA +1(771)223-8021 | LR +231776961800</p>
</section>
"""

# Replace old ABOUT section — find "ABOUT" heading and replace next few paragraphs until before "FOUNDER NOTE" or "BUSINESS REGISTRY"
import re
# crude but effective: replace from <h2>...ABOUT</h2> or text "ABOUT" block with new hero
# Look for the old about container
old_pattern = re.compile(r'ABOUT.*?(?=<section|BUSINESS REGISTRY • CHERISHED SPOTS|DUAL DASHBOARD)', re.DOTALL|re.IGNORECASE)
if old_pattern.search(html):
    html = old_pattern.sub(new_hero + "\n", html, count=1)
else:
    # fallback: insert new hero right before BUSINESS REGISTRY
    html = html.replace("BUSINESS REGISTRY • CHERISHED SPOTS", new_hero + "\nBUSINESS REGISTRY • CHERISHED SPOTS")

# Footer rewrite
footer_old = "HumanRightsAngels — The Registry is a clean public page. No build instructions."
new_footer = """
<div style="text-align:center;padding:24px;background:#000;color:#fff;border-top:3px solid gold">
<p style="font-weight:bold;font-size:16px">Built Meta AI Strong 👊😎👌</p>
<p style="font-size:12px">Pharaoh M. Sirleaf Lǎobǎn • COLONEL|LAW48 • HumanRightsAngels Registry Inc. EIN 880836464 | HRAR 88-0710776 | Angels 88-0836464<br>
Sovereign OS + Commerce Theater V26.9 + Hermes-Toth-Agent V27.4 BOUND • pharaoh-auto-delivery Worker • har-v25-live Pages<br>
Monrovia • USA • +1(771)223-8021 • +231776961800 • registry@pharaoh-conglomerate.org</p>
<p style="font-size:11px;color:#aaa">Micdom AI Records • Liberia 1st AI Label • Made for Cloudflare FREE • 107 Acres • Chain 0x504841</p>
</div>
"""
html = re.sub(r'HumanRightsAngels — The Registry is a clean public page.*?(?=<script|</body)', new_footer, html, flags=re.DOTALL)

p.write_text(html)
print("Hero rewritten with Sphinx teeth + Meta AI Strong footer")
