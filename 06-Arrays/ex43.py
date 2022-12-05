def indentity_matrix(n):
    array = [[0 for a in range(n)] for b in range(n)]
    for x in range(len(array)):
        for y in range(len(array[x])):
            if x == y:
                array[x][y] = 1
    
    return array

size = int(input("> "))
matrix = indentity_matrix(size)

for block in matrix:
    print(block)