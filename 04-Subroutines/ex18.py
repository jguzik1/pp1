def sum_of_digits(liczba):
    liczba = str(liczba)
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma

print(sum_of_digits(7182))