filename = input("File name: ")
with open(filename,'r',encoding="UTF-8") as f:
    content = f.readlines()
    lines = len(content)

print(f'File {filename} has {lines} lines')