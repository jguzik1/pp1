with open("07-FileHandling/allcountries.txt", "r", encoding="UTF-8") as f:
    content = f.readlines()
    counter = 0
    for line in content:
        print(line)
        counter += 1
        if counter == 5:
            a = input()
            counter = 0