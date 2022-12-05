array = [15, 8, 31, 47, 2, 19]
a = int(input("> "))

greater_count = 0

for number in array:
    if number > a:
        greater_count += 1

print(f'there are {greater_count} numbers greater than {a}')