def amount_to_pay(money):
    coins = 0
    money = int(money)
    while money > 0:
        if money >= 5:
            coins += 1
            money -= 5
        elif money >= 2:
            coins += 1
            money -= 2
        else:
            coins += 1
            money -= 1
    return coins


print(amount_to_pay(9))