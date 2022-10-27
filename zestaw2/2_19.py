L = [7,8,19,33,67,90,120,345,876]

for i in range(len(L)):
    L[i]=str(L[i]).zfill(3)

napis=' '.join(L)
print("Otrzymany napis:",napis)
