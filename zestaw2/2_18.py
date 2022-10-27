cyfra=92368276280329893272027628720101

cyfraStr=str(cyfra)
count=0

for i in range(len(cyfraStr)):
    if cyfraStr[i]=="0":
        count+=1

print("ilosc zer:",count)