class C():
    def __init__(self):
        pass

    def m1(self,number):
        removed = ""
        for symbol in str(number):
            if symbol in ['0','2','4','6','8']:
                removed += str(symbol)
        return int(removed)

    def m2(self,number):
        number = str(number)
        for a in range(1,len(number)):
            if int(number[a]) < int(number[a-1]):
                return False
        return True

    def m3(self,number):
        number = str(number)
        arr = []
        for a in number:
            arr.append(a) 
        digits = ['0','1','2','3','4','5','6','7','8','9']
        for a in arr:
            if a in digits:
                digits.remove(a)
        combined = ''
        for a in digits:
            combined += a

        return combined
        








c = C()
print(c.m1(4231564))
print(c.m1(79381))
print(c.m2(125579))
print(c.m2(4557879))
print(c.m3(23557))
print(c.m3(12340))
