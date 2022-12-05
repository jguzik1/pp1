import json
student = {
    "Name" : "Jan",
    "Surname" : "Kowalski",
    "Currently_active" : True,
    "Age" : 23,
    "Hobbies" : ["football", "Cycling"],
    "Degrees" : None
}

with open("08-DictionariesStacksAndQueues/13.json", "w", encoding="UTF-8") as f:
    json.dump(student, f, indent= 4)