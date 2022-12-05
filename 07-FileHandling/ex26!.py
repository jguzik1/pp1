import re
with open("07-FileHandling/forests.txt","r",encoding="UTF-8") as f:
    content = f.readlines()
    a = "[A-Za-z0-9]{6,}"
    words = re.findall(a, content)
    print(words)