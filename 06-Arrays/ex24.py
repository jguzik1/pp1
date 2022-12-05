array = [2, 3, 2, 5, 8, 1, 9, 8]

for element in array:
    count = 0
    for a in range(len(array)):
        if array [a] == element:
            count += 1
    if count == 1:
        print(element, end=" ")