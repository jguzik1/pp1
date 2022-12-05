#def f(first_letter,last_letter):
first_letter = "w"
last_letter = "d"
with open("09-Test2/test.txt","r",encoding="UTF-8") as file:
    content = file.readlines()
    word = content.split()

