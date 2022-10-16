import random

dice = [1, 2, 3, 4, 5, 6]

x = random.choice(dice)

guess = int(input('number 1-6: '))

if guess == x:
    print(True)
else:
    print("try again")