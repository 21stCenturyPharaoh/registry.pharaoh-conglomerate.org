from pathlib import Path
html=Path("index.html").read_text()

oversight_fix='''
<!-- OVERSIGHT FIXED — CORRECT PRICE ARCHITECTURE + ROLES SEPARATED -->
<div style="background:#000;padding:20px 14px;border-top:4px solid gold;border-bottom:4px solid gold">
<h2 style="font-family:'Cinzel',serif;color:#ffd700;margin:0;text-align:center;font-size:14px">PRICE ARCHITECTURE — FIXED PLATFORM • GOVT FEES SEPARATE</h2>
<p style="font-size:9px;color:#aaa;text-align:center;margin:6px 0">USD + LD approx • Central Bank Liberia ref L$180-182 per US$1 • LD equiv approximate, may change with rate • Govt/third-party/RA charges NOT included unless expressly stated</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px">

<div style="background:#111;border:1px solid #444;border-radius:12px;padding:12px">
<b style="color:#fff;font-size:11px">🟢 REGISTRY BASIC</b><br><b style="color:#ffd700">$49 / ≈L$8,900</b><br><span style="font-size:8px;color:#aaa">Existing business enters ecosystem<br>• Registry profile • Biz desc • Website/social • Category • Registry ID • Basic digital profile • Affiliate eligibility review • Platform announcements</span><br><span style="font-size:7px;color:#666">Best for: existing businesses</span>
</div>

<div style="background:#111;border:1px solid #555;border-radius:12px;padding:12px">
<b style="color:#fff;font-size:11px">🔵 REGISTRY PROFESSIONAL</b><br><b style="color:#ffd700">$99 / ≈L$18,000</b><br><span style="font-size:8px;color:#aaa">Everything Basic +<br>• Enhanced profile • Strategic-partner consideration • Affiliate profile • Referral ops • Accelerator eligibility • Directory placement • Custom badge • Priority updates</span>
</div>

<div style="background:#111;border:2px solid #8c6b00;border-radius:12px;padding:12px">
<b style="color:#ffd700;font-size:11px">🟣 CORPORATE LAUNCH</b><br><b style="color:#ffd700">$249 / ≈L$45,000</b><br><span style="font-size:8px;color:#fff">Real corporate-services funnel begins<br>• Registry Professional • Document prep/coordination • Formation workflow • Info intake • Filing-package prep • RA coordination thru Unique Business Solutions Inc. • Digital profile • Domain/email assist • Affiliate onboarding • Accelerator onboarding</span><br><span style="font-size:7px;color:#ff6666">Govt filing fees & RA charges NOT included</span>
</div>

<div style="background:linear-gradient(180deg,#1a1500,#000);border:2px solid gold;border-radius:12px;padding:12px;box-shadow:0 0 15px rgba(255,215,0,0.3)">
<b style="color:#ffd700;font-size:11px">🟠 CORPORATE GROWTH — HERO</b><br><b style="color:#ffd700">$499 / ≈L$90,000</b><br><span style="font-size:8px;color:#fff">Build my company + put inside Registry@Pharaoh<br>• All Launch + Enhanced corporate profile • Website/landing deployment • Custom-domain assist • businessname@pharaoh-conglomerate.org routing • Automation • Affiliate campaign • Referral tracking • Strategic-partner matching • Biz-dev profile • Priority support</span><br><span style="font-size:7px;color:#ff6666">Govt/third-party/RA/domain/hosting separate</span>
</div>

</div>

<div style="background:radial-gradient(ellipse at center,#221a00,#000);border:2px solid gold;border-radius:12px;padding:14px;margin-top:12px;text-align:center">
<b style="color:#ffd700;font-size:12px;font-family:'Cinzel'">👑 CORPORATE ECOSYSTEM • $999 / ≈L$180,000</b><br><span style="font-size:8px;color:#fff">Premium — Launch + Growth + Priority placement + Advanced digital presence + Website + Domain/email routing + Accelerator config + Affiliate infra + Referral infra + Partner-network intro + Automation + Doc-management + Priority support + 1-year ecosystem membership</span><br><span style="font-size:7px;color:#ff6666">Govt charges, third-party professional charges, RA charges, domains, hosting upgrades, filing fees & pass-through expenses separately identified</span>
</div>

<div style="margin-top:14px;background:#0a0a0a;border:1px solid #332a00;border-radius:10px;padding:12px">
<b style="color:#ffd700;font-size:10px">CUSTOMER LIFECYCLE — REGISTRY IS ACQUISITION LAYER</b><br>
<span style="font-size:9px;color:#ccc">$49 → $249 Launch → $499 Growth (hero) → $99-299/yr renewal + becomes affiliate generating commissions<br>Registry → Corporate Services → Digital Infra → Accelerator → Affiliate Network</span>
</div>

<div style="margin-top:14px;display:grid;grid-template-columns:1fr;gap:8px">
<div style="background:#111;border-left:4px solid gold;padding:10px;border-radius:8px"><b style="color:#ffd700;font-size:10px">PHARAOH CONGLOMERATE</b><br><span style="font-size:8px;color:#aaa">Platform / Registry / Technology / Marketplace / Affiliate Network</span></div>
<div style="background:#111;border-left:4px solid #888;padding:10px;border-radius:8px"><b style="color:#fff;font-size:10px">UNIQUE BUSINESS SOLUTIONS INC. — Jeanette Waters CEO</b><br><span style="font-size:8px;color:#aaa">Strategic Corporate Services Partner — document prep, filing coordination, govt submissions, ongoing filings — example: our own workflow formation → filing → receipt/handling → ongoing support</span></div>
<div style="background:#111;border-left:4px solid #fff;padding:10px;border-radius:8px"><b style="color:#ffd700;font-size:10px">NORTHWEST REGISTERED AGENT — Powered by</b><br><span style="font-size:8px;color:#aaa">$125/year • Mail scanning • Business address • Domain • Website • Email • Phone • Wholesale Partner Portal • API option • Affiliate $100 RA / $150 formation • End client stays under our relationship while Northwest handles RA function<br>Registered Agent Services provided through participating qualified strategic partners, including Unique Business Solutions Inc., subject to jurisdictional availability and applicable terms. Registry@Pharaoh itself is NOT the Registered Agent.</span></div>
</div>

<div style="margin-top:12px;text-align:center">
<p style="font-size:8px;color:#666">BUSINESS OWNER ↓ PHARAOH REGISTRY "Put my biz in ecosystem" ↓ CORPORATE LAUNCH "Help establish/document" ↓ UNIQUE BUSINESS SOLUTIONS "Prepare/coordinate filings" ↓ GOVT/AUTHORITY "Official filing" ↓ PHARAOH DIGITAL INFRA Website•Domain•Email•Hosting ↓ ALGORITHM ACCELERATOR Automation•Leads•Matching ↓ AFFILIATE ENGINE Business promotes qualifying offers ↓ REVENUE Pharaoh+Partner+Business</p>
<p style="font-size:7px;color:#555">Form 990 is IRS return for qualifying tax-exempt orgs, C corps have different federal obligations — we offer tax filing/compliance support through qualified providers, not generic 990 filing. We won't bundle govt fees until destination jurisdiction known. Liberia has own official registry infrastructure.</p>
</div>

<a href="/affiliate-engine/" style="display:block;background:linear-gradient(180deg,#ffd700,#b89600);color:#000;padding:12px;border-radius:10px;font-family:'Cinzel';font-weight:900;text-align:center;text-decoration:none;font-size:11px;margin-top:12px">SEE AFFILIATE ENGINE $100 RA / $150 FORMATION →</a>
</div>
'''

html=html.replace('<!-- BUSINESS REGISTRY SCALER', oversight_fix + '\n<!-- BUSINESS REGISTRY SCALER')

Path("index.html").write_text(html)
print("Oversight fixed")
