imie = str(input("Podaj imie: "))

klucz = int(input("Podaj klucz: "))

for i in range(len(imie)):

    if (97 <= (ord(imie[i]) + klucz) and (ord(imie[i]) + klucz) <= 122) or (65 <= (ord(imie[i]) + klucz) and (ord(imie[i]) + klucz) <= 90):
        a = chr(ord(imie[i]) + klucz)

    else:
        a = chr((ord(imie[i]) + klucz) - 26)
    print(a, end='')
