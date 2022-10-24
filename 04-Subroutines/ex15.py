from mymath import *


rand = generate_number()
wrong = True

while wrong:
    guess = read_number()
    if guess == rand:
        wrong = False

print("You won")