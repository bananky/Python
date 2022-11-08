def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        pierwszy = 0
        drugi = 1
        for i in range(n-1):
            liczony = pierwszy + drugi
            pierwszy = drugi
            drugi = liczony
    return liczony

print(Fibonacci(9))

