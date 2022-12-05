array = [5,1,9,6,1]

max = array[0]
min = array[0]

for number in array:
    if number > max:
        max = number
    elif number < min:
        min = number

print(max - min)