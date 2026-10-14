import json, re, sys, urllib.request
url = "https://docs.google.com/forms/d/e/1FAIpQLScBwbItiUOAr9Sbn0hhCUy2zX_ApFcAP67Fk0u9vOXEAw5cZA/viewform"
html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read().decode("utf-8")
m = re.search(r"FB_PUBLIC_LOAD_DATA_\s*=\s*(.*?);\s*</script>", html, re.S)
data = json.loads(m.group(1))
out = []
for item in data[1][1]:
    title = item[1]
    for q in (item[4] or []):
        out.append({"title": title, "entry": q[0], "options": [o[0] for o in (q[1] or [])]})
json.dump(out, open("form-ids.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
