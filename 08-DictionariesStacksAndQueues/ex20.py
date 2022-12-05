import stack
number = int(input("> "))
converted = ""
while number > 0:
    if number % 2 == 0:
        stack.push(0)
    else:
        stack.push(1)
    number = number // 2

for a in range(len(stack.stack)-1,-1,-1):
    converted += str(stack.stack[a])

converted = int(converted)
print(converted)