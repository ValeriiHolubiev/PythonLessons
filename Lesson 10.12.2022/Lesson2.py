from random import randint

lista = []

X = int(input("Podaj cyfre : "))

def main(lista):
    for i in range(100):
        lista.append(randint(100, 100000))

def suma(lista, X):
    main(lista)
    S = 0
    licznik_X = 0


    for i in range(len(lista)):
        print(lista[i], end = "; ")

        while lista[i] > 0:
            S += lista[i] % 10

            if lista[i] % 10 == X:
                licznik_X += 1

            lista[i] = lista[i] // 10

        print("Suma cyfr =", str(S) + ';', "Illosc cyfr",X,"=",licznik_X)

        S = 0
        licznik_X = 0

suma(lista, X)

