def f(player1, player2):
    values = {
    
        "A" : 10,
        "K" : 10,
        "Q" : 10,
        "J" : 10,
        "T" : 10,
        "1" : 1,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
    }
    p1_sum = 0
    p2_sum = 0
    for letter1 in player1:
        p1_sum += values[letter1]
    for letter2 in player2:
        p2_sum += values[letter2]
    if p1_sum > p2_sum:
        return True
    else:
        return False

print(f("987","AT4"))