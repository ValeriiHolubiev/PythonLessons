from random import randint

lista = []
lista_p = []
lista_np = []

def wypelnij_liste(lista):
    for i in range(100):
        lista.append(randint(1,100))

wypelnij_liste(lista)

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista_p.append(lista[i])
    else:
        lista_np.append(lista[i])

print("Glowna lista:",lista)
print("Lista parzystych:",lista_p)
print("Lista nieparzystych: ",lista_np)

