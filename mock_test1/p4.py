def f(number, even):
    sum = 0
    if even:
        for digit in str(number):
            digit = int(digit)
            if digit % 2 == 0:
                sum += digit
    elif even == False:
        for digit in str(number):
            digit = int(digit)
            if digit % 2 != 0:
                sum += digit
    return sum

liczba = 13115
wartosc = True
print(f(liczba, wartosc))
