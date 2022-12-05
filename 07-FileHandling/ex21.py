with open("07-FileHandling\intigers.txt", 'w') as f:
    for a in range(1,11):
        x = str(a) + " "
        y = str(a ** 2) + " "
        z = str(a ** 3) + " "
        joined = x + y + z + "\n"
        f.writelines(joined)