from pathlib import Path
import re
html=Path("index.html").read_text()

businesses=[
("Gabe's Landscaping","rjKTcilqUAE","Landscaping • Liberia-US • Cherished Spot #1 — visual proof of accelerated local service"),
("The Drug Store (Dr Yancy)","3uyLmMQptjc","Community Pharmacy • Monrovia • health anchor in Registry"),
("V2'S Business Center","znWY5kR1Qnk","Printing • Scanning • Business services • tech bridge"),
("Tech Blessing CEO","aw8SScWL7Xk","Global • Liberia-US Bridge • Founder • +1 771 223-8021"),
("Mama's Mani Pedi Hair Fest","Gms9crSj2R0","Luxury nails, pedicure, hair & cultural fest • glam anchor"),
("Derrina's Affordable Evening Wear","XHqUB6k_coY","Elegant gowns • Liberian design • commerce theater fashion"),
("Fe's Business Center","3vznYuBpxsM","Office support, internet, docs • infrastructure"),
("Mosetta's Online Restaurant","nDP5ltiO-ow","Authentic Liberian cuisine • Palm butter, fufu, jollof • taste of Liberia"),
("Bendu K. Massaley & Ambassador Chris Collins","CA4P9W9eVDI","Diplomacy • Community Leadership • Registry Directors"),
]

grid=""
for name,vid,desc in businesses:
    grid+=f'''
<div style="background:#0a0a0a;border:1px solid gold;border-radius:12px;overflow:hidden">
<div style="position:relative;padding-bottom:177%;background:#000">
<iframe style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" src="https://www.youtube.com/embed/{vid}" allowfullscreen loading="lazy"></iframe>
</div>
<div style="padding:10px">
<b style="color:#ffd700;font-size:12px">{name}</b><br>
<span style="font-size:9px;color:#ffd700">SILENT VISUAL TESTIMONY — Part of Accelerator (see explainer above)</span><br>
<span style="font-size:10px;color:#aaa">{desc}</span><br>
<a href="https://youtube.com/shorts/{vid}" style="display:block;margin-top:8px;background:gold;color:#000;text-align:center;padding:8px;border-radius:6px;font-weight:900;font-size:10px;text-decoration:none">▶ WATCH SHORT</a>
</div>
</div>
'''

coherent=f'''
<section style="background:#000;border-top:4px solid gold;border-bottom:4px solid gold;padding:0">
<div style="background:#111;padding:16px;text-align:center;border-bottom:2px solid gold">
<h2 style="color:#ffd700;margin:0;font-size:14px">🏛️ BUSINESS MODEL EXPLAINED • WATCH FIRST</h2>
<p style="font-size:11px;color:#fff;margin:8px 0;line-height:1.6">For Visitors / Affiliates / Micdom AI Records Citizens: The 9 Shorts below are NOT random — they are SILENT visual proof of businesses INSIDE the Accelerator. Watch the 2 explainers first → then each Short = case study.</p>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0">
<div style="border-right:2px solid gold">
<div style="position:relative;padding-bottom:56.25%;background:#000"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" src="https://www.youtube.com/embed/Dk2nBc8_97M" allowfullscreen></iframe></div>
<div style="padding:12px;background:#0a0a0a"><b style="color:#ffd700;font-size:12px">1. REGISTRY ACCELERATOR EXPLAINER</b><br><span style="font-size:10px;color:#fff">HOW businesses get accelerated — onboarding, TOTH auto-delivery, WhatsApp Temple, AI Records citizenship. WATCH FIRST to understand Shorts below.</span><br><a href="https://youtu.be/Dk2nBc8_97M?si=19MueNb9Q7lkHXds" style="display:inline-block;margin-top:8px;background:gold;color:#000;padding:8px 12px;border-radius:6px;font-weight:900;font-size:10px;text-decoration:none">▶ ACCELERATOR</a></div>
</div>
<div>
<div style="position:relative;padding-bottom:56.25%;background:#000"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" src="https://www.youtube.com/embed/mHBJN0QA8Fo" allowfullscreen></iframe></div>
<div style="padding:12px;background:#0a0a0a"><b style="color:#ffd700;font-size:12px">2. REGISTRY EXPLAINER</b><br><span style="font-size:10px;color:#fff">WHAT is Pharaoh Conglomerate? Dream Stele 2026, Giza to Monrovia, 10 Cherished Spots, EIN 880836464. The full model for affiliates.</span><br><a href="https://youtu.be/mHBJN0QA8Fo?si=fWYJjXvKF2Pm34eA" style="display:inline-block;margin-top:8px;background:#111;border:1px solid gold;color:#ffd700;padding:8px 12px;border-radius:6px;font-weight:900;font-size:10px;text-decoration:none">▶ REGISTRY</a></div>
</div>
</div>
<div style="background:#111;padding:12px;text-align:center;border-top:2px solid gold"><p style="margin:0;font-size:11px;color:#ffd700;font-weight:700">⬇️ NOW 9 CHOICE BUSINESSES — Silent visual proof inside Accelerator above — each = Commerce Theater spot</p></div>
</section>

<section style="padding:16px;background:#0a0a0a;border-bottom:4px solid gold">
<h3 style="color:#ffd700;text-align:center">🏛️ 9 CHOICE BUSINESSES • SILENT TESTIMONY • INSIDE ACCELERATOR</h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px">
{grid}
</div>
</section>
'''

# Replace old business registry sections (both old 10 spots text and any previous injection)
html = re.sub(r'<section style="padding:16px;background:#0a0a0a[^>]*>\s*<h3 style="color:#ffd700">.*?(BUSINESS REGISTRY|CHOICE BUSINESSES|10 Cherished).*?</section>', '', html, flags=re.DOTALL)

# Insert before final footer (Built Meta AI Strong)
html = html.replace('<div style="text-align:center;padding:20px;background:#000;border-top:3px solid gold">', coherent + '\n<div style="text-align:center;padding:20px;background:#000;border-top:3px solid gold">')

Path("index.html").write_text(html)
print("Coherent push ready — 2 explainers + 9 shorts pegged!")
