file = open('numbers.txt', 'r')


sum = 0

for liczba in file:
    sum += int(liczba)

file.close()
print(sum)