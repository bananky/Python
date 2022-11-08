def factorial(n):
    if n == 0:
        return 1
    prod = 1
    for i in range(1, n + 1):
        prod = prod * i
    return prod

print(factorial(6))