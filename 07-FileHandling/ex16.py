with open("07-FileHandling/allcountries.txt", "r", encoding="UTF-8") as f:
    content = f.readlines()

with open("07-FileHandling\copy.txt", "w", encoding="UTF-8") as a:
    a.writelines(content)