while True:
    x = input("Podaj liczbę:")
    if x.isdigit():
        print(float(x)**3)
    elif x=="stop":
        break
    else:
        print("Podany znak nie jest liczba")

