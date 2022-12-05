import random
with open("07-FileHandling\intigers.txt","w") as f:
    for a in range(50):
        if a == 49:
            rand = str(random.randint(100,999))
            f.writelines(rand)
        else:
            rand = str(random.randint(100,999)) + "\n"
            f.writelines(rand)