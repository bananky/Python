def odwracanie_iteracyjne(L, left, right):
    counter = 0
    for i in range(left, right + 1):

        if counter >= (right - left + 1) / 2:
            break
        help = L[i]
        L[i] = L[right - counter]
        L[right - counter] = help
        counter = counter + 1


def odwracanie_rekurencyjne(L, left, right):
    if left == right:
        return
    help = L[left]
    L[left] = L[right]
    L[right] = help
    return odwracanie_rekurencyjne(L, left + 1, right - 1)


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odwracanie_iteracyjne(lista, 3, 7)
print(lista)

odwracanie_rekurencyjne(lista, 3, 7)
print(lista)
