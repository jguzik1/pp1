import stack
import re
expression = str(input("> "))
temp = 0
for a in expression:
    temp = 0
    if a == "(" or ")":
        continue
    elif a == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
        stack.push(int(a))
    elif a == "=":
        stack.display()
    else:
        match a:
            case "+":
                temp = stack.pop() + stack.pop()
                stack.push(temp)
            case "-":
                temp = stack.pop() - stack.pop()
                stack.push(temp)
            case "*":
                temp = stack.pop() * stack.pop()
                stack.push(temp)
            case "/":
                temp = stack.pop() / stack.pop()
                stack.push(temp)