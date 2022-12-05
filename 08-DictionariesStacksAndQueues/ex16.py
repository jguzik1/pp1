import json
with open("08-DictionariesStacksAndQueues\students.json", "r", encoding="UTF-8") as students:
    content = json.load(students)

new_content = []
for student in content:
    student.pop("gender")
    student.pop("age")
    student.pop("year_of_study")
    student.pop("email")
    new_content.append(student)

    
with open("08-DictionariesStacksAndQueues\limited.json", "w", encoding="UTF-8") as limited:
    json.dump(new_content, limited,indent= 4)