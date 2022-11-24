file = open('countries.txt', 'r')

linia = 1
for line in file:
    print(linia, end=" ")
    linia += 1
    print(line, end="")


file.close()