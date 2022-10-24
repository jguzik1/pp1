h_age = int(input('''Enter the dog's age in human years: '''))
d_age = 0

for a in range(1, h_age + 1):
    if a <=2 :
        d_age += 10.5
    else:
        d_age += 4

print(f'''The dog;s age in dog's years is {d_age} years''')
