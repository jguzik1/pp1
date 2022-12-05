array = [5,1,9,6,1]

largest = array[0]
second_largest = 0

for number in array:
    if number < largest and number > second_largest:
        second_largest = number
    elif number > largest:
        largest = number

print(f"largest {largest} second largest {second_largest}")