array = [[1,2,3,4],[5,6,7,8]]

#rows
for a in range(len(array)):
    for b in range(len(array[a])):
        print(array[a][b], end=' ')
    print()

print()
# collumns

for a in range(len(array[1])):
    print(array[0][a], end=" ")
    print(array[1][a])