def f(array2D):
    array1D = []
    sum = 0
    for a in range(len(array2D[0])):
        sum = 0
        for b in range(len(array2D)):
            sum += array2D[b][a]
        array1D.append(sum)
    return array1D

print(f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]))