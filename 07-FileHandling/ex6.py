file = open('07-FileHandling\countries.txt', 'r', encoding='UTF-8')
file_content = file.read()
print(file_content)
file.close()