import thermomether
import random
th = thermomether.Thermometer()
a = random.random() * 100
while a > 42.0 or a < 34.0:
    a = random.random() * 100
    
a = round(a,2)

th.turn_on()
th.measure(a)
th.display()
