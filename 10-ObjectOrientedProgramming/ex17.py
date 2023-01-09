class Statistics():
    numbers =[]
    def __init__(self,array):
        self.numbers = array
        self.max = -999999999999
        self.min = 999999999999
        self.ar_mean = 0
        self.medi = -999999999999

    def append(self):
        '''adds new number to array'''
        number = int(input("> "))
        self.numbers.append(number)

    def display_arr(self):
        '''displays array of numbers'''
        for number in self.numbers:
            print(number,end=" ")
        print()

    def greatest(self):
        '''determines greatest number in array'''
        for number in self.numbers:
            if number > self.max:
                self.max = number

    def lowest(self):
        '''determines smallest number in array'''
        for number in self.numbers:
            if number < self.min:
                self.min = number

    def arythmetic_mean(self):
        '''calculates arithmetic mean of numbers'''
        sum = 0
        for number in self.numbers:
            sum += number
        self.ar_mean = sum/len(self.numbers)

    def median(self):
        '''determines median'''
        sorted = self.numbers.sort()
        if len(self.numbers) % 2 != 0:
            self.medi = self.numbers[int(len(self.numbers)/2)]
        else:
            self.medi = (self.numbers[int(len(self.numbers)/2)]+self.numbers[int(len(self.numbers)/2-1)])/2

    def display_results(self):
        print(f"Minimum: {self.min}")
        print(f'Maximum: {self.max}')
        print(f'Arithmetic mean: {self.ar_mean}')
        print(f'Median: {self.medi}')

arr1 = [12, 37, 6, 9, 17]
test = Statistics(arr1)

test.append()
test.display_arr()
test.greatest()
test.lowest()
test.arythmetic_mean()
test.median()
test.display_results()
