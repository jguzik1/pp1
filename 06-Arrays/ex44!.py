matrix = [[1,2,3],[4,5,6],[7,8,9]]

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

print(matrix)