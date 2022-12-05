with open("07-FileHandling\intigers.txt","w") as f:
    for a in range(1,51):
        if a == 50:
            f.writelines(str(a))
        else:
            a = str(a) + "\n"
            f.writelines(a)