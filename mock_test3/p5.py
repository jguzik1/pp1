class C():
    def __init__(self,array):
        self.intigers = array
        self.sum = 0
        self.combined = ''
        for number in self.intigers:
            self.sum += number
        self.combined = ''
        for a in range(len(self.intigers)-1):
            self.combined += str(array[a]) + "+"
        self.combined += str(array[-1]) + "=" + str(self.sum)
    
    def __str__(self):
        return self.combined

        




arr1 = [5,12]
arr2 = [6,0,15]
test = C(arr1)
print(test)
