def minmax(array):
    min = array[0]
    max = array[0]
    for number in array:
        if number > max:
            max = number
        elif number < min:
            min = number
    return [min, max]

arr = [4,2,8,4,7,9,5]

print(minmax(arr))