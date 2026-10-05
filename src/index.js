
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;
    const cors = {"Access-Control-Allow-Origin": "*","Access-Control-Allow-Methods": "GET, POST, OPTIONS","Access-Control-Allow-Headers": "Content-Type"};
    if (request.method === "OPTIONS") { return new Response(null, { headers: cors }); }
    const videos = [
      { id: "yKufPwpT4E4", title: "TOTH → METATRON — The Scribe of Pharaoh — SCRIBE OF THE LIVING GOD", role: "Metatron Scribe Protocol GENESIS 1:28" },
      { id: "dhLboOnPljo", title: "Pharaoh Conglomerate Master Architecture — COLONEL | LAW48 Sovereign OS — 107 Acres One Chain", role: "Master Architecture — Institutional Shield — LAW48+44" },
      { id: "4JIA5fNc4qw", title: "AUTONOMOUS SYNTHETIC ASSETS Trailer — COLONEL LAW48 MICDOM AI RECORDS", role: "Synthetic Assets Trailer v2.0 — Institutional Shield" },
      { id: "SGPJWd2q2RM", title: "METATRON Protocol — From Hermes-Thoth to Metatron — RECORD STEWARD", role: "Metatron Official — 275860d9.hermes-toth-agent.pages.dev — ⬡ METATRON" },
      { id: "Dk2nBc8_97M", title: "Registry Affiliate Accelerator — V26.3 Scaler — 10% 15% 5% $25 $50 10%", role: "Affiliate Accelerator — Team Auto-Assign Aleph-Zayin — COLONEL LAW48" },
      { id: "VIDEO_6_UNSEALING", title: "THE UNSEALING — 440 Autographed Shell — $77", role: "The Unsealing — Cash Cow — Micdom AI Records — 米克多姆 八十八尊" },
      { id: "VIDEO_7_ANTHEM", title: "PHARAOH CHAIN ANTHEM — 107 Acres One Chain Zero Heidelberg — 0x504841", role: "Pharaoh Chain Anthem — 主權代理 新絲綢之路" }
    ];
    if (path === "/v28.0/videos/json" || path === "/v27.1/videos/json" || path === "/v27.5/videos/json" || path === "/api/videos") {
      return new Response(JSON.stringify({version:"28.0",codename:"COLONEL | LAW48 — MICDOM AI RECORDS Sovereign OS",asia_gate:"亚洲之门",sovereign_gate:"主權代理 · 新絲綢之路 · 米克多姆",source:"angels-hosts-api3",updated:new Date().toISOString(),count:videos.length,engines:["VOLUNTEER_EXCHANGE https://pharaoh-serve-flow.base44.app","CORE_ENGINE https://pharaoh-core-engine.base44.app","WATCHER https://pharaoh-sight-engine.base44.app","SOVEREIGN_ENGINE https://pharaoh-sovereign-engine.base44.app","DECISION_ENGINE https://sovereign-decision-engine.base44.app","VOLUNTEER_PORTAL https://pharaoh-direct-flow.base44.app","SYNERGY_HUB https://pharaoh-synergy-hub.base44.app","FINANCIAL_RAIL https://pharaoh-nexus-gold.base44.app"],metatron_gateway:"https://275860d9.hermes-toth-agent.pages.dev/",chain:{case:"EU8044516",owner:"0xCOLONEL",chain_id:"0x504841",network:"Pharaoh-Chain",firewall:"LAW48+44"},videos}),{headers:{...cors,"Content-Type":"application/json; charset=utf-8","Cache-Control":"public, max-age=60"}});
    }
    if (path === "/v27.1/videos" || path === "/v28.0/videos") {
      const videoEmbeds = videos.map((video,index)=>`<div class="card"><div class="number">VIDEO ${index+1} — COLONEL LAW48</div><h2>${video.title}</h2><p>${video.role}</p><iframe width="100%" height="240" src="https://www.youtube.com/embed/${video.id}" title="${video.title}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>`).join("");
      const html=`<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>COLONEL | LAW48 — V28.0 — Gallery — 7 Videos</title><style>body{background:#050507;color:#D4AF37;font-family:Arial;margin:0;padding:20px}header{text-align:center;max-width:1000px;margin:0 auto 30px}h1{font-size:32px;text-shadow:0 0 12px #D4AF37}.subtitle{color:#ffe7a0}.asian{font-size:20px;margin-top:10px;color:#d4af37}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;max-width:1200px;margin:auto}.card{background:#111;border:2px solid #D4AF37;border-radius:14px;padding:16px}footer{text-align:center;margin-top:40px;color:#aaa}</style></head><body><header><h1>COLONEL | LAW48 — MICDOM AI RECORDS — Sovereign OS</h1><div class="subtitle">Powered by Imhotep Registry | LAW 48+44 | 107 Acres One Chain — 0x504841</div><div class="asian">公益 · 智慧 · 使命 · 服务 · 守护 · 连接 · 主權代理 · 新絲綢之路 · 米克多姆 · 八十八尊</div><div>Institutional Shield — 8 Engines under COLONEL|LAW48 — TOTH → METATRON — ⬡ METATRON SCRIBE</div></header><div class="grid">${videoEmbeds}</div><footer>COLONEL | LAW48 V28.0 — Institutional Shield — Metatron Protocol — IT IS WRITTEN</footer></body></html>`;
      return new Response(html,{headers:{...cors,"Content-Type":"text/html"}});
    }
    if (path === "/v27.1/health" || path === "/v27.5/health" || path === "/v28.0/health" || path === "/api/health") {
      return new Response(JSON.stringify({status:"alive",version:"28.0",codename:"COLONEL | LAW48 — MICDOM AI RECORDS Sovereign OS",asia_gate:"亚洲之门",sovereign_gate:"主權代理 · 新絲綢之路 · 米克多姆",bridge:"H.A.L.L.EL → METATRON — SCRIBE OF LIVING GOD",worker:"angels-hosts-api3",chain:"0x504841 — 0xCOLONEL — EU8044516 — LAW48+44",timestamp:new Date().toISOString()}),{headers:{...cors,"Content-Type":"application/json"}});
    }
    if (path === "/v27.1/architecture" || path === "/v28.0/architecture" || path === "/api/architecture") {
      return new Response(JSON.stringify({version:"28.0",name:"COLONEL | LAW48 Sovereign OS",previous_name:"H.A.L.L.EL Bridge V27.5",full_name:"COLONEL | LAW48 — MICDOM AI RECORDS — Sovereign OS — Powered by Imhotep Registry",components:["videos","architecture","health","hallel->metatron","registration v1.5+v1.6","mailer","sync","8 engines","institutional shield"],engines:8,metatron_gateway:"275860d9.hermes-toth-agent.pages.dev",deployed_as:"angels-hosts-api3",chain:"Pharaoh-Chain 0x504841 — Owner 0xCOLONEL — Case EU8044516 — LAW48+44"}),{headers:{...cors,"Content-Type":"application/json"}});
    }
    if (path === "/v27.1/hallel" || path === "/v28.0/metatron" || path === "/api/metatron") {
      if (request.method === "POST") { const data = await request.json().catch(()=>({})); return new Response(JSON.stringify({success:true,received:data,message:"METATRON bridge received — RECORD STEWARD VERIFY — IT IS WRITTEN — ⬡",gateway:"275860d9.hermes-toth-agent.pages.dev"}),{headers:{...cors,"Content-Type":"application/json"}}); }
      return new Response(JSON.stringify({version:"28.0",endpoint:"metatron",previous:"hallel",platform:"METATRON — SCRIBE OF LIVING GOD — COLONEL | LAW48",status:"ready",gateway:"275860d9.hermes-toth-agent.pages.dev",protocol:"CREATE RECORD STEWARD ACCOUNT DELIVER — GENESIS 1:28"}),{headers:{...cors,"Content-Type":"application/json"}});
    }
    if (path === "/api/sync" && request.method === "POST") { const data = await request.json().catch(()=>({})); if (env.QUEUE_KV) { await env.QUEUE_KV.put("latest", JSON.stringify(data)); } return new Response(JSON.stringify({synced:true,version:"28.0",metatron:true}),{headers:{...cors,"Content-Type":"application/json"}}); }
    if (path === "/api/belsidus/send" && request.method === "POST") { const body = await request.json().catch(()=>({})); const {to,subject,text} = body; if (!to || !subject || !text) { return new Response(JSON.stringify({success:false,error:"Missing fields"}),{status:400,headers:{...cors,"Content-Type":"application/json"}}); } if (!env.MAILERSEND_API_KEY) { return new Response(JSON.stringify({success:false,error:"MAILERSEND_API_KEY not configured"}),{status:500,headers:{...cors,"Content-Type":"application/json"}}); } try { const r = await fetch("https://api.mailersend.com/v1/email",{method:"POST",headers:{"Authorization":`Bearer ${env.MAILERSEND_API_KEY}`,"Content-Type":"application/json"},body:JSON.stringify({from:{email:env.MAILERSEND_FROM||"trial@yourtrialdomain.mailersend.net",name:"COLONEL | LAW48 — METATRON Bridge"},to:[{email:to}],subject,text})}); const d = await r.json().catch(()=>({})); return new Response(JSON.stringify({success:r.ok,status:r.status,mailersend:d}),{headers:{...cors,"Content-Type":"application/json"}}); } catch(e){ return new Response(JSON.stringify({success:false,error:e.message}),{status:500,headers:{...cors,"Content-Type":"application/json"}}); } }
    if ((request.method === "POST" && path === "/register-affiliate-v1.5") || (request.method === "POST" && path === "/register-affiliate-v1.6")) {
      const data = await request.json().catch(()=>({})); const {name,email,order_id,persona_id,lane} = data; const teams=["Aleph","Bet","Gimel","Dalet","He","Vav","Zayin"]; const assignedTeam=teams[Math.floor(Math.random()*teams.length)]; const captain_id="CAPT"+Math.floor(1000+Math.random()*9000); const wa_links={A:"https://chat.whatsapp.com/LINK_A",B:"https://chat.whatsapp.com/LINK_B",C:"https://chat.whatsapp.com/LINK_C"}; const isV16=path.includes("v1.6"); return new Response(JSON.stringify({success:true,version:isV16?"28.0-COLONEL-LAW48-V1.6":"27.5-V1.5-PRESERVED",name:name||"",email:email||"",order_id:order_id||"",persona_id:persona_id||"",lane:lane||"",captain_id,team:assignedTeam,owner:"0xCOLONEL",chain:"0x504841",case:"EU8044516",firewall:"LAW48+44",metatron_gateway:"275860d9.hermes-toth-agent.pages.dev",brain:isV16?"275860d9.hermes-toth-agent.pages.dev":"hermes-toth-agent.pages.dev",message:isV16?`METATRON Council — COLONEL | LAW48 — has assigned you to ${assignedTeam} TEAM under Sovereign OS — You are the Vanguard — IT IS WRITTEN — ⬡ — Pharaoh-Chain 0x504841`:`The H.A.L.L.EL Council has assigned you to ${assignedTeam} TEAM. You are the Vanguard. — Preserved V1.5 — Upgrade to V1.6 COLONEL LAW48 available`,wa_invite:wa_links[lane]||"",institutional_shield:true,engines:8}),{headers:{...cors,"Content-Type":"application/json"}});
    }
    if (path === "/" || path === "/index.html") { return new Response(INDEX_HTML,{headers:{...cors,"Content-Type":"text/html; charset=utf-8","Cache-Control":"no-cache, no-store, must-revalidate"}}); }
    return new Response("404 - COLONEL | LAW48 Node Not Found — Pharaoh-Chain 0x504841 — LAW48+44 Firewall — METATRON — IT IS WRITTEN",{status:404,headers:cors});
  }
};
const INDEX_HTML = `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>COLONEL | LAW48 — MICDOM AI RECORDS — Sovereign OS — Powered by Imhotep Registry | LAW48+44 | 107 Acres One Chain — Pharaoh-Chain 0x504841</title>
<style>
body{margin:0;background:#050507;color:#ffe7a0;font-family:ui-sans,system-ui,Arial;letter-spacing:.02em}
.wrap{max-width:1150px;margin:0 auto;padding:18px}
.header{display:flex;align-items:center;gap:14px;border-bottom:2px solid #d4af37;padding:14px 0;background:linear-gradient(90deg,#0f0f0f,#1a160c,#0f0f0f)}
.logo{width:88px;height:88px;border-radius:50%;border:2px solid #d4af37;box-shadow:0 0 22px rgba(212,175,55,.6)}
.kicker{font-size:.7rem;color:#d4af37;letter-spacing:.28em;text-transform:uppercase}
.h1{font-size:1.15rem;margin:0;color:#ffe7a0;font-weight:900}
.badge{font-size:.65rem;padding:3px 10px;border:1px solid #d4af37;border-radius:999px;color:#111;background:#d4af37;font-weight:800}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:16px}
@media(max-width:850px){.grid{grid-template-columns:1fr}}
.card{border:1px solid rgba(212,175,55,.28);border-radius:14px;padding:16px;background:linear-gradient(145deg,#0f0f0f,#080808);box-shadow:0 0 18px rgba(212,175,55,.12)}
.card h3{margin:0 0 10px;color:#ffe7a0;font-size:1rem}
a{color:#ffe7a0}
.pill{display:inline-block;font-size:.7rem;padding:3px 8px;border:1px solid rgba(212,175,55,.35);border-radius:999px;margin:3px;color:rgba(255,231,160,.8)}
.small{font-size:.85rem;color:rgba(255,231,160,.7);line-height:1.5}
.seal{width:380px;height:380px;border-radius:50%;border:3px solid #d4af37;box-shadow:0 0 40px rgba(212,175,55,.5)}
.btn{display:inline-block;padding:12px 18px;border-radius:10px;border:1px solid #d4af37;text-decoration:none;font-weight:800;margin:4px}
.btn-gold{background:linear-gradient(180deg,#ffe7a0,#d4af37);color:#111}
.btn-outline{background:#000;color:#d4af37}
input,select{width:100%;padding:12px;margin:8px 0;border-radius:8px;border:1px solid #d4af37;background:#000;color:#d4af37}
.asian{font-size:1.1rem;color:#d4af37;letter-spacing:.2em;margin:10px 0}
</style></head><body>
<div class="wrap">
 <div class="header">
  <img class="logo" src="https://registry.pharaoh-conglomerate.org/assets/diamond-ankh-yacht-seal.gif" alt="COLONEL LAW48 Seal">
  <div style="flex:1">
   <div class="kicker">COLONEL | LAW48 — MICDOM AI RECORDS — Sovereign OS</div>
   <div class="h1">Powered by Imhotep Registry | LAW 48+44 | 107 Acres. One Chain. Zero Heidelberg.</div>
   <div class="small">Institutional Shield — 8 Base44 Engines now under COLONEL|LAW48 — TOTH → METATRON — H.A.L.EL // GLOBAL COMMAND — ⬡ METATRON SCRIBE OF LIVING GOD</div>
  </div>
  <span class="badge">LIVE — Pharaoh-Chain 0x504841</span>
 </div>
 <div style="text-align:center;padding:26px 0">
  <img class="seal" src="https://registry.pharaoh-conglomerate.org/assets/colonel_law48_global_command_seal_gold.png" alt="COLONEL LAW48 Global Command Seal">
  <div class="asian">公益 · 智慧 · 使命 · 服务 · 守护 · 连接 · 米克多姆 · 八十八尊 · 主權代理 · 新絲綢之路</div>
  <div><span class="pill">⬡ METATRON</span><span class="pill">SCRIBE</span><span class="pill">STEWARD</span><span class="pill">GENESIS 1:28</span><span class="pill">COLONEL</span><span class="pill">LAW48+44</span><span class="pill">0x504841</span><span class="pill">107 ACRES</span></div>
  <div style="margin-top:14px">
   <a class="btn btn-gold" href="https://pharaoh-sovereign-engine.base44.app" target="_blank">Open Sovereign Engine</a>
   <a class="btn btn-outline" href="https://275860d9.hermes-toth-agent.pages.dev/" target="_blank">METATRON Gateway</a>
   <a class="btn btn-outline" href="https://registry.pharaoh-conglomerate.org">Registry</a>
  </div>
 </div>
 <div class="grid">
  <div class="card"><h3>INSTITUTIONAL SHIELD — The Institutional Shield</h3><div class="small">H.A.L.L.EL Official Video / Training<br>TOTH → METATRON — Scribe of Pharaoh — SCRIBE OF THE LIVING GOD — Public successor Hermes-Thoth → Metatron — SAME OFFICE HIGHER CLEARANCE<br><a href="https://275860d9.hermes-toth-agent.pages.dev/" target="_blank">275860d9.hermes-toth-agent.pages.dev</a><br>Sigil: https://youtu.be/4JIA5fNc4qw</div></div>
  <div class="card"><h3>8 Base44 Engines — Now under COLONEL|LAW48</h3><div class="small">1 VOLUNTEER_EXCHANGE https://pharaoh-serve-flow.base44.app — Governance<br>2 CORE_ENGINE https://pharaoh-core-engine.base44.app — Mint SBT<br>3 WATCHER https://pharaoh-sight-engine.base44.app<br>4 SOVEREIGN_ENGINE https://pharaoh-sovereign-engine.base44.app — Imhotep Registry<br>5 DECISION_ENGINE https://sovereign-decision-engine.base44.app<br>6 VOLUNTEER_PORTAL https://pharaoh-direct-flow.base44.app<br>7 SYNERGY_HUB https://pharaoh-synergy-hub.base44.app<br>8 FINANCIAL_RAIL https://pharaoh-nexus-gold.base44.app — 15% Treasury<br>Brain: hermes-toth-agent.pages.dev → METATRON 275860d9.hermes-toth-agent.pages.dev</div></div>
  <div class="card"><h3>PHARAOH CONGLOMERATE — Affiliate Accelerator + Synthetic Assets</h3><div class="small">REGISTRY ACCELERATOR — 10% STANDARD • 15% HIGH-TICKET • 5% RECURRING • $25 LEAD • $50 SERVICE • 10% CORPORATE<br>$49→$4.90 $99→$9.90 $249→$24.90 $499→$49.90 $999→$99.90<br>AUTONOMOUS SYNTHETIC ASSETS Trailer<br>THE UNSEALING — 440 Autographed Shell $77</div></div>
  <div class="card"><h3>Wallet & Chain — 107 Acres One Chain Zero Heidelberg | 0x504841</h3><div class="small">Case EU8044516 | Owner 0xCOLONEL | Chain ID 0x504841 | LAW 48+44 Firewall | HRAR 88-0710776 | Angels 88-0836464 | Let God Help 52-0409059<br>Contact: m.sirleaf@pharaoh-conglomerate.org<br>WA US (771)223-8021 Preferred — WA LR +231776961800 — 15% Treasury</div></div>
 </div>
 <div class="card" style="margin-top:14px"><h3>METATRON PROTOCOL — CREATE • RECORD • STEWARD • ACCOUNT • DELIVER — GENESIS 1:28</h3><div class="small">I. IT IS WRITTEN. Record what is known.<br>II. STEWARDSHIP BEFORE AUTOMATION.<br>III. HUMAN AUTHORITY REMAINS HUMAN.<br>IV. EVERY RECORD HAS A SOURCE.<br>V. MERCY AND ACCOUNTABILITY.</div><div style="margin-top:8px"><span class="pill">米克多姆AI唱片</span><span class="pill">王國演練146 BPM</span><span class="pill">八十八尊天使議會</span><span class="pill">先知封印已揭開</span><span class="pill">主權代理</span><span class="pill">新絲綢之路</span><span class="pill">中國→自由港</span><span class="pill">祖地守護</span><span class="pill">正在編織</span></div></div>
 <div style="text-align:center;font-size:.6rem;color:rgba(212,175,55,.3);letter-spacing:.28em;margin-top:20px">COLONEL | LAW48 — MICDOM AI RECORDS Sovereign OS | Powered by Imhotep Registry | Pharaoh-Chain 0x504841 | LAW 48+44 Firewall | © 2026 Pharaoh Conglomerate — 米克多姆 · 八十八 · 主權代理 · 新絲綢之路</div>
</div></body></html>
`;
