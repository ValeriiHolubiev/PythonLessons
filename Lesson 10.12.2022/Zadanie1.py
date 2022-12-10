from random import randint

lista = []

for i in range(100):
    lista.append(randint(1, 100))

lista.sort()

print(lista)

for i in range(len(lista)):
    if lista[i] == lista[i-1]:
        lista.remove(lista[i])

print(lista)
