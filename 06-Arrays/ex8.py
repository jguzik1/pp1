arr = [-15, 8, -31, 47, -2, 19]

min = arr[0]
max = arr[0]

for number in arr:
    if number < min:
        min = number
    elif number > max:
        max = number

print(f'min: {min},  max: {max}')