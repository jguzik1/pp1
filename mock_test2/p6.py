#def f(age, course, average):
import json
with open('09-Test2/test.json',"r",encoding="UTF-8")as file:
    content = json.load(file)
    for a in range(len(content)):
        for b in range(len(content[a])):
            print(b)