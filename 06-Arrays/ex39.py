array = [[0 for a in range(5)]for b in range(5)]
insert = 1
for a in range(len(array)):
    for b in range(len(array[a])): 
        array[a][b] = insert
        insert += 1


print(array)