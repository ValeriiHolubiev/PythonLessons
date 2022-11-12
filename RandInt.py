import random

def Czy_zgadles(a):

	if a == random.randint(0, 10):
		return True

	else:
		return False


x = False

while x == False:

	a = int(input("Podaj liczbe: "))

	x = Czy_zgadles(a)