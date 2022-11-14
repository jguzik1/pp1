def binary_number(number):
    for digit in str(number):
        digit = int(digit)
        if digit != 0 and digit != 1:
            return False
    return True
    


print(binary_number(10112))