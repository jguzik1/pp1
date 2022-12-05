array = [[-38, 19], [5,40],[-7,11],[29,16]]

min = array[0][0]
min_x = 0
min_y = 0
max = array[0][0]
max_x = 0
max_y = 0

for a in range(len(array)):
    for b in range(len(array[a])):
        if array[a][b] < min:
            min = array[a][b]
            min_x = a
            min_y = b
        if array[a][b] > max:
            max = array[a][b]
            max_x = a
            max_y = b

print(f'min {min} lokalizacja: {min_x} {min_y} // max {max} lokalizacja: {max_x} {max_y}')