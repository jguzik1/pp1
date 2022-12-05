file = open('07-FileHandling/allcountries.txt', 'r')

file_content = file.read()

for line in file_content:
    print(line, end="")

file.close()