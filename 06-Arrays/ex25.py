def occurs(number, array):
    for element in array:
        if number == element:
            return True
    return False

a = int(input("> "))

arr = [15, 38, 7, 23, 14]

if occurs(a, arr):
    print(f'Number {a} appears in the array')
else:
    print(f'Number {a} does not appear in the array')