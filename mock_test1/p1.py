def card_number(card):
    iteration = 0
    for number in str(card):
        iteration += 1
        if iteration <= 2 or iteration >=13:
            print(number, end="")
        else:
            print("*", end="")
    print()
            


card_number(1234567890123456)