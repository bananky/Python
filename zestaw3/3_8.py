import random

s = random.getstate()

first = [random.randint(0, 10) for i in range(10)]
second = [random.randint(0, 10) for j in range(10)]

print("Pierwsza sekwencja: ", first)
print("Druga sekwencja: ", second)

same = set()

for i in first:
    for j in second:
        if i == j:
            same.add(i)

print("Wspólne elementy: ", same)

allElements = set(first).union(second)
print("Wszystkie elementy: ", allElements)
