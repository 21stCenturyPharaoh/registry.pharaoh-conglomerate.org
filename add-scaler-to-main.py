from pathlib import Path
html=Path("index.html").read_text()
scaler_block='''
<!-- BUSINESS REGISTRY SCALER V26.3 -->
<div style="background:radial-gradient(ellipse at center,#1a1500,#000);border-top:4px solid gold;border-bottom:4px solid gold;padding:20px 14px;text-align:center">
<h2 style="font-family:'Cinzel',serif;color:#ffd700;margin:0;font-size:14px">BUSINESS REGISTRY SCALER V26.3</h2>
<h3 style="color:#fff;margin:8px 0;font-size:13px;font-family:'Cinzel'">JOIN FREE. SELL MORE. EARN MORE. BUILD THE NETWORK.</h3>
<p style="font-size:10px;color:#ccc;margin:10px 0">Join once. Access multiple business channels. Sell qualifying products. Generate qualified customers. Refer businesses. Refer professional services. Earn commission assigned to each qualifying offer.</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin:12px 0">
<div style="background:#000;border:1px solid gold;border-radius:8px;padding:8px"><b style="color:#ffd700;font-size:10px">10% STANDARD</b><br><span style="font-size:8px;color:#aaa">$100 → $10</span></div>
<div style="background:#000;border:1px solid gold;border-radius:8px;padding:8px"><b style="color:#ffd700;font-size:10px">15% HIGH-TICKET</b><br><span style="font-size:8px;color:#aaa">$1,299 → $194.85</span></div>
<div style="background:#000;border:1px solid gold;border-radius:8px;padding:8px"><b style="color:#ffd700;font-size:10px">$25 / $50 / 10%</b><br><span style="font-size:8px;color:#aaa">Lead / Service / Corporate</span></div>
</div>
<div style="background:rgba(255,215,0,0.08);border-radius:10px;padding:10px;text-align:left;max-width:600px;margin:0 auto">
<p style="font-size:9px;color:#fff;margin:0">Example: Tech Blessing Solar Power Station<br>Price: $1,299 | Rate: 15% | Commission: $194.85 | Tracking: Registry Affiliate Link | Status: Available</p>
</div>
<a href="/affiliate-engine/" style="display:block;background:linear-gradient(180deg,#ffd700,#b89600);color:#000;padding:12px;border-radius:10px;font-family:'Cinzel';font-weight:900;text-align:center;text-decoration:none;font-size:11px;margin-top:12px">ENTER AFFILIATE ENGINE → SEE MATH</a>
<p style="font-size:8px;color:#666;margin-top:8px">4 Layers: Registry $49-$999 • Affiliate • Corporate Services • Commerce • Portfolio: Mosetta → V2 → Drug Store → Gabe's → Tech Blessing → Mama's → Derrina → Fe's → Corporate</p>
</div>
'''
html=html.replace('<!-- WORKER INTERFACES', scaler_block + '\n<!-- WORKER INTERFACES')
# fallback if comment missing
if scaler_block not in html:
    html=Path("index.html").read_text()
    html=html.replace('⚙️ WORKER INTERFACES', scaler_block + '\n<div style="padding:18px;background:#111;border-bottom:3px solid gold">\n<h2 style="color:#ffd700;margin:0 0 12px 0;font-size:13px;text-align:center">⚙️ WORKER INTERFACES')

Path("index.html").write_text(html)
print("Added scaler")
