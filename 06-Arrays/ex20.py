def star(n):
    stars = "*" * n
    return stars

arr = [12, 6, 4, 9, 10]

for liczba in arr:
    print(f'{liczba}: {star(liczba)}')

