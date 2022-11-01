size = input("Podaj dlugosc linijki: ")
if size.isdigit()==False:
    print("Podany zly format, wpisz liczbe")
else:
    ruler="|"
    numbers="0"
    for i in range(1,int(size)+1):
        ruler+="....|"
        numbers+=str(i).rjust(5)

    result= ruler + "\n" + numbers
    print(result)