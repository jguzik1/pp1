import json
with open("08-DictionariesStacksAndQueues/11.json") as f:
    data = json.load(f)

for a, b in data.items():
    print(a,":",b)
