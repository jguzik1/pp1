def bubble_sort(arr):
    for a in range(len(arr)):
        for b in range(len(arr)-1-a):
            if arr[b] > arr[b+1]:
                arr[b], arr[b+1] = arr[b+1], arr[b]
    return arr





arr = [15, 8, 31, 47, 2, 19]

print(bubble_sort(arr))
