def make_ruler(n):
    ruler = "|"
    numbers = "0"
    for i in range(1, int(n) + 1):
        ruler += "....|"
        numbers += str(i).rjust(5)

    result = ruler + "\n" + numbers
    return result

def make_grid(height,width):
    result = ""

    for i in range(height * 2 + 1):
        if i % 2 == 0:
            result += "+"
            for j in range(width):
                result += "---+"
            result += "\n"
        else:
            result += "|"
            for j in range(width):
                result += "   |"
            result += "\n"

    return result


print(make_ruler(13))
print(make_grid(4,5))
