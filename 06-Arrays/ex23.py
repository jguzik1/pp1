def bubblesort(array):
    for i in range(len(array)-1):
        for k in range(len(array)-1):
            if array[k] > array[k+1]:
                nast = array[k+1]
                array[k+1] = array[k]
                array[k] = nast
    return array



arr = [4,36,12,28,9,44,5]

newarr = bubblesort(arr)

print(newarr)
