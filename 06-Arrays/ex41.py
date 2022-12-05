array = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]

for block in array:
    for number in block:
        print(number,end=" ")
    print()

print()

for a in range(len(array[0])):
    print(array[0][a],end=" ")
    print(array[1][a],end=" ")
    print(array[2][a])

print()

array[0], array[-1] = array[-1], array[0]


for block in array:
    for number in block:
        print(number,end=" ")
    print()

print()

for a in range(len(array[0])):
    print(array[0][a],end=" ")
    print(array[1][a],end=" ")
    print(array[2][a])