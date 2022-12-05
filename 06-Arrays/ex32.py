def f(arr):
    string = ""
    for i in range(len(arr)):
        if i == len(arr) - 1:
            string += str(arr[i])
        else:
            string += str(arr[i]) + ", "    
    return string




array = [5,4,3,2,6,5]

print(f(array))