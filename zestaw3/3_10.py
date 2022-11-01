dictionary = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
              'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

def roman2int(s):
    i = 0
    result = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in dictionary:
            result += dictionary[s[i:i + 2]]
            i += 2
        else:
            result += dictionary[s[i]]
            i += 1
    return result

x=input("Podaj liczbe do konwersji: ")

print(roman2int(x))

