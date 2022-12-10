from random import randint

lista = []

def wypelnij_liste(lista):
    for i in range(100):
        lista.append(randint(1,100))

def Licznik(lista):
    licznik = 0
    for i in range(len(lista)):
        if lista[i] == X:
            licznik += 1
    return licznik

X = int(input("Podaj liczbe : "))

wypelnij_liste(lista)

lista.sort()

print(lista)

print("Podana liczba wystepuje", Licznik(lista), "razy.")
