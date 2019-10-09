import json
with open('Storage.json', 'r') as JSON:
    data = json.load(JSON)
    type(data)
    print(data["login"])