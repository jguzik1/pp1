a = int(input('a: '))
b = int(input('b: '))

for k in range(1, a + 1):
    if k == 1 or k == a:
        print("x" * b)
    else:
        print("x", end="")
        print(" " * (b - 2), end="")
        print("x")
