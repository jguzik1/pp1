array1 = [1,2,3,4,5,6]
array2 = [2, 3, 5, 6]

count = 0

for number2 in array2:
    for number1 in array1:
        if number2 == number1:
            count += 1
            break

if count == len(array2):
    print('this array is a subset')
else:
    print("this array is not a subset")