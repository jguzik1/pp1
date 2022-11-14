def f(card_number):
    card_number = str(card_number)
    print(card_number[0,2], end="")
    print("*" * 10, end="")
    print(card_number[-4,-1])


f(1234567890123456)