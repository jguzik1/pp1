money = int(input('Enter the amount of PLN: '))

five = 0
two = 0
one = 0

while money > 0:
    if money >= 5:
        five += 1
        money -= 5
    elif money >= 2:
        two += 1
        money -= 2
    else:
        one += 1
        money -= 1

print(f'5 zł - {five}\n 2 zł - {two}\n 1 zł - {one}')