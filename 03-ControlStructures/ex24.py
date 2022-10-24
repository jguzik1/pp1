x = int(input('x: '))

for a in range(1, x + 1):
    if a <= x / 2:
        print("* " * a)
    else:
        print("* " * (x - a))