import json
favourite = {
    "Type" : "Film",
    "Title" : "Shrek",
    "Production_year" : 2001,
    "Is_awesome" : True,
    "How_many_rewatches" : "Countless"
}

with open("08-DictionariesStacksAndQueues/12.json", "w", encoding="UTF-8") as f:
    json.dump(favourite, f, indent= 4)