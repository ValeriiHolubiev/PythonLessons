lista = []

licznik = 0

for i in range(6):
    lista.append(input("Podaj imie: "))

for i in range(len(lista)):
    if lista[i][-1] == "a":
        licznik += 1

print(lista)

print("Illosc imion damskich:", licznik)

