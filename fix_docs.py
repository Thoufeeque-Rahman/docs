import json
import copy

with open('docs.json', 'r') as f:
    data = json.load(f)

# Extract original tabs from the "en" language block
en_tabs = []
if "languages" in data["navigation"]:
    for lang in data["navigation"]["languages"]:
        if lang["language"] == "en":
            en_tabs = copy.deepcopy(lang.get("tabs", []))
            break
            
# Create new tabs array with versions
new_tabs = []
for tab in en_tabs:
    tab["version"] = "English"
    new_tabs.append(tab)

ml_tabs = copy.deepcopy(en_tabs)
def prefix_pages(obj):
    if isinstance(obj, dict):
        if "pages" in obj:
            obj["pages"] = ["ml/" + p if not p.startswith("ml/") else p for p in obj["pages"]]
        for k, v in obj.items():
            prefix_pages(v)
    elif isinstance(obj, list):
        for item in obj:
            prefix_pages(item)

for tab in ml_tabs:
    tab["version"] = "Malayalam"
    prefix_pages(tab)
    new_tabs.append(tab)

data["versions"] = ["English", "Malayalam"]
del data["navigation"]["languages"]
data["navigation"]["tabs"] = new_tabs

with open('docs.json', 'w') as f:
    json.dump(data, f, indent=2)
