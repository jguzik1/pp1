def rand_element(array):
    import random
    rand = random.randint(0, len(array)-1)
    return array[rand]

arr = [15, 8, 31, 47, 2, 19]

print(rand_element(arr))