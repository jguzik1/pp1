with open("07-FileHandling/allcountries.txt","r",encoding="UTF-8") as f1:
    with open("07-FileHandling\copylines.txt","w",encoding="UTF-8") as f2:
        for line in f1:
            f2.writelines(line)