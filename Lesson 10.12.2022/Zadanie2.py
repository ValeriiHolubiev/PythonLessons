imie = str(input("Podaj imie: "))

klucz = int(input("Podaj klucz: "))

for i in range(len(imie)):

    x = (ord(imie[i]) + klucz)

    if (97 <= x and x <= 122) or (65 <= x and x <= 90):
        a = chr(x)

    else:
        x -= 26

    print(a, end='')
