def f(arr):
    for a in range(len(arr[0])):
        for b in range(len(arr[0])):
            if arr[a][b] != arr[0][a] * arr[0][b]:
                return False
    
    return True



test = [[1,2,3],[2,4,6],[3,6,9]]
test2 = [[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]
test3 = [[1,2],[3,6]]
print(f(test3))