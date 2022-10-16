a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

h = (a + b + c) / 2

p = (h * (h - a) * (h - b) * (h - c)) ** (1/2)

print(f'pole: {p}')