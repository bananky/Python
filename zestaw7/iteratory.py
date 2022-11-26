import itertools
import random

#a
iter1 = itertools.cycle(["0","1"])
for i in iter1:
    print(i,end=", ")
#b
iter2 = iter(lambda:random.choice(["N", "E", "S", "W"]),0 )
for i in iter2:
    print(i, end=", ")
#c
iter3 = itertools.cycle(range(0,7))
for i in iter3:
    print(i, end=", ")