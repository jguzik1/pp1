array1 = [2, 3, 7, 5, 4]

print(array1)

print(len(array1))

print(array1[0])

print(array1[1])

print(array1[-1])

print(array1[len(array1)-2])

print(array1[0] + array1[len(array1)-1])

middle = len(array1)//2

print(array1[middle])

for a in array1:
    print(a, end=" ")
print()

for a in range(0, middle + 1):
    print(array1[a], end=" ")
