import csv
with open("07-FileHandling\students.txt", "r") as f:
    contents = csv.reader(f, delimiter=",")
    for line in contents:
        try:
            if int(line[2]) < 30:
                print(line[0], line[1], line[4])
        except:
            print("",end="")