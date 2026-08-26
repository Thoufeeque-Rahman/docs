import json

with open('docs.json', 'r') as f:
    data = json.load(f)

if "versions" in data:
    del data["versions"]

if "tabs" in data.get("navigation", {}):
    en_tabs = [t for t in data["navigation"]["tabs"] if t.get("version") == "English"]
    if en_tabs:
        for t in en_tabs:
            if "version" in t:
                del t["version"]
        data["navigation"]["tabs"] = en_tabs

with open('docs.json', 'w') as f:
    json.dump(data, f, indent=2)
