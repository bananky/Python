height=int(input("Podaj wysokosc: "))
width=int(input("Podaj szerokosc: "))

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

print(result)