array1 = [1,2,3,4,5]

array1[0] -= 1

array1[-1] += 4

middle = len(array1)//2

array1[middle] *= 2

for a in range(len(array1)):
    array1[a] += 3

print(array1)