from pathlib import Path
p=Path("index.html")
t=p.read_text()
t=t.replace("https://soloist.ai","https://hermes-toth-agent.pages.dev/?v=27.4")
p.write_text(t)
print("TOTH now points to BOUND Hermes V27.4")
