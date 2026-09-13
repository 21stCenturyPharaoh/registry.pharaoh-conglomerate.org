import re
html = open("index.html").read()
html = re.sub(r'<script[^>]*>(?:(?!</script>).)*createRoot(?:(?!</script>).)*</script>', '', html, flags=re.S)
html = re.sub(r'<div id="root"></div>', '', html)
open("index.html", "w").write(html)
print("Removed only the React script + empty root div")
