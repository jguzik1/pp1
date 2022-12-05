def f(dictionary,x,y):
    sum = 0
    for arr in dictionary:
        for number in dictionary[arr]:
            if number >= x and number <= y:
                sum += number
    
    return sum
        




print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10))