def in_range(start, end, number):
    if number <= end and number >= start:
        return True
    return False


print(in_range(5,15,20))