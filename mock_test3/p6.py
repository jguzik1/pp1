class C():
    def __init__(self,initial_value) -> None:
        self.counter = initial_value
        
    def m1(self):
        print(self.counter)
    
    def m2(self):
        self.counter += 1

    def m3(self):
        self.counter -= 1

    def m4(self,how_much_to_add):
        self.counter += how_much_to_add

c = C(5)

c.m1()
c.m2()
c.m1()
c.m4(-8)
c.m1()
c.m3()
c.m1()
c.m4(10)
c.m1() 
