def keypad():
    for x in range(1,10,3):
        for a in range(3):
            print(x + a, end=" ")
        print()



def keypad2(length):
    for i in range(1, length + 1):
        print(i, end=" ")
        if i % 3 == 0:
            print()

a = int(input("a: "))

keypad2(a)