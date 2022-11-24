def compare(array1, array2):

    if len(array1) != len(array2):
        return False

    for a in range(len(array1)):
        if array1[a] != array2[a]:
            return False

    return True


print(compare([3,2,1],[3,2]))