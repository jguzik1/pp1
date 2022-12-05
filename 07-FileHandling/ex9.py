file = open('07-FileHandling/numbers.txt', 'r')


sum = 0

for liczba in file:
    sum += int(liczba)

file.close()
print(sum)