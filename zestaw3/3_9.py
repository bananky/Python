sequence = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

result = []

for i in sequence:
    result.append(sum(i))

print(result)