import itertools
import random

#a
print(itertools.cycle('0 1'))
#b
print(iter(random.choice(("N", "E", "S", "W")) ))
#c
print(itertools.cycle(range(0,7)))