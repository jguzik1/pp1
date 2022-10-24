from re import I


x = int(input('x: '))
y = int(input('Y: '))

if x > 0 and y > 0:
    print(f'Point P({x}, {y}) is in the first quadrant')
elif x < 0 and y > 0:
    print(f'Point P({x}, {y}) is in the second quadrant')
elif x < 0 and y < 0:
    print(f'Point P({x}, {y}) is in the third quadrant')
else:
    print(f'Point P({x}, {y}) is in the fourth quadrant')