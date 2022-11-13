#import os
##lass Uczen:
##	imie = ""
##	nazwisko = ""
#	oceny_z_matematyki = []
#	oceny_z_informatyki = []
#	oceny_z_historii = []
#
#
#	def __init__(self, imie, nazwisko):
#		self.imie = imie
#		self.nazwisko = nazwisko
#
#
#	def srednia(self):
#		suma = 0
#
#		for i in self.oceny_z_matematyki:
#			suma += i
#
#		return suma / len(self.oceny_z_matematyki)
#
#
#	def najwiekszaOcena(self):
#		return max(self.oceny_z_matematyki)
#
#
#	def iloscPiatek(self):
#		k = 0
#
#		for i in self.oceny_z_matematyki:
#			if i == 5:
#				k += 1
#		return k
#
#	def informacje(self):
#		print("\nImie i nazwisko: " + self.imie, self.nazwisko)
#		print("\nOceny z matematyki: ", end = "")
#
#		for i in self.oceny_z_matematyki:
#			print(i, end = " ")
#
#		print("\n\nOceny z historii: ", end = "")
#
#		for i in self.oceny_z_historii:
#			print(i, end = " ")
#
#		print("\n\nOceny z informatyki: ", end = "")
#
#		for i in self.oceny_z_informatyki:
#			print(i, end = " ")
#
##Deklaracje
#print("Jak sie nazywa uczen?")
#uczen1 = Uczen(input("Imie:"), input("Nazwisko:"))
##uczen2 = Uczen("Ryszard", "Nowak")
#
#uczen1.oceny_z_matematyki = [1,2,1,3,4,5]
#uczen1.oceny_z_historii = [1,4,3,2,4,5]
#uczen1.oceny_z_informatyki = [4,2,3,4,5,5]
##uczen2.oceny_z_matematyki = [1,5,4,5,2,3]
#
#
#
##Przypisanie wartosci
##uczen1.imie = "Janek"
##uczen2.imie = "Ryszard"
#
##Wyswietlanie
##print(uczen1.imie, uczen1.nazwisko, uczen1.oceny_z_matematyki, uczen1.najwiekszaOcena(), uczen1.iloscPiatek())
##print(uczen2.imie, uczen2.nazwisko, uczen2.oceny_z_matematyki, uczen2.najwiekszaOcena(), uczen2.iloscPiatek())
#
##uczen1.informacje()
#
#while True:
#	print("I - Informacja.")
#	print("P - Ilosc piatek")
#	print("N - Najwieksza ocena")
#	print("X - Wyjscie")
#	a = input("Twoje dzialanie: ")
#
#	if a == "I":
#
#		informacje()
#
#	if a == "P":
#
#		iloscPiatek()
#
#	if a == "N":
#
#		najwiekszaOcena()
#
#	if a == "X":
#
#		break
#
#
#
#print()
#print()
#
#
#
##________________________________________^^^^DOROBIC^^^_____________________________________________________________________________________________________

