arr = ["Shrek", "Hulk", "Top Gun", "Batman", "Puss in the boots"]

file = open("11.txt", 'w', encoding="UTF-8")

for title in arr:
    file.write(title)
    file.write("\n")

file.close()