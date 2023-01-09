def f(n):
    string = ""
    for a in range(n):
        if a % 5 == 0 and a not in [0, range(n)]:
            string += "-"
        string += "/"
    
    return string


print(f(16))