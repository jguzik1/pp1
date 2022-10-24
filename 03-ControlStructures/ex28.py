last = 0
sum = 1

for i in range(51):
    if i == 0:
        print("0")
    elif i == 1:
        print("1")
    else:
        sum += last
        last = sum
        print(sum, end=" ")