#a
from sre_constants import NEGATE


print('a.', 5 + 10 * 5)
#b
print('b.', 3 - 2 + 1)
#c
print('c.', 2 + -3)
#d
print('d.', 2 ** 8)
#e
print('e.', 4 + 4 / 2 ** 2)
#f
print('f.', 4 % 3 % 2 % 1)
#g
print('g.', 1 + 2 % 3 ** 4 * 5)
#h
print('h.', True != False)
#i
print('i.', 2 <= 3 or False)
#j
print('j.', not True or not False and not True)
#k
print('k.', 2 < 3 and 4 < 5 or not 6 < 7)
#l
print('l.', 2 % 3 < 4 / 5 and 6 + 7 < 8 or not 9 + 10 == 19)
#m
print('m.', 0b11111 >> 1 >> 1 >> 1)
#n
print('n.', 0x11 + 0b11 + 11)
#o
print('o.', 2 << 3 >> 4)