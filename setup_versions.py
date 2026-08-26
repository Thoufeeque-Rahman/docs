import json
import copy

with open('docs.json', 'r') as f:
    data = json.load(f)

# If versions already exists, just print
if "versions" in data:
    print("Already has versions")
else:
    original_tabs = data["navigation"].get("tabs", [])
    
    # Create English version of tabs
    en_tabs = copy.deepcopy(original_tabs)
    for tab in en_tabs:
        tab["version"] = "English"
        
    # Create Malayalam version of tabs
    ml_tabs = copy.deepcopy(original_tabs)
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
        
    data["versions"] = ["English", "Malayalam"]
    data["navigation"]["tabs"] = en_tabs + ml_tabs
    
    with open('docs.json', 'w') as f:
        json.dump(data, f, indent=2)
