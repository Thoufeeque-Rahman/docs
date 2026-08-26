import json

with open('docs.json', 'r') as f:
    data = json.load(f)

tabs = data["navigation"]["tabs"]
en_tabs = []
ml_tabs = []

for tab in tabs:
    if tab.get("version") == "English":
        del tab["version"]
        en_tabs.append(tab)
    elif tab.get("version") == "Malayalam":
        del tab["version"]
        ml_tabs.append(tab)

data["navigation"] = {
    "versions": [
        {
            "version": "English",
            "tabs": en_tabs
        },
        {
            "version": "Malayalam",
            "tabs": ml_tabs
        }
    ]
}

if "versions" in data:
    del data["versions"]

with open('docs.json', 'w') as f:
    json.dump(data, f, indent=2)
