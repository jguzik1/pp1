import random
class Arrays():
    @staticmethod
    def create(a, value):
        array1 = []
        for z in range(a):
            array1.append(value)
        return array1

    @staticmethod
    def create_rand(a,m,n):
        array2 = []
        for z in range(a):
            array2.append(random.randint(m,n))
        return array2

    @staticmethod
    def find(array2,min,max):
        counter = 0
        for number in array2:
            if number >= min and number <= max:
                counter += 1
        return counter

new_array = Arrays.create(12,3)
print(new_array)

newe_array2 = Arrays.create_rand(12,3,8)
print(newe_array2)

new_array3 = Arrays.find(newe_array2,8,8)

print(new_array3)