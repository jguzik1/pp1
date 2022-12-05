def median(array):
    import math
    if len(array) % 2 != 0:
        mediana = array[math.floor(len(array)/2)]
    else:
        x = array[int(len(array)/2 - 1)]
        y = array[int(len(array)/2)]
        mediana = int((x+y)/2)
    return mediana
        


a = [1,0,9,4,6]
b = [6,8,3,1,0,5]

print(median(a))
print(median(b))