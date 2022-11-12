#zmienna_int = 123
#zmienna_float = 123.0
#zmienna_str = 'tekst'
#kolekcja_int = [123, 300, 400, 500]
#kolekcja_str = ['123', '300', '400', 'asd']
#slownik = {'pierwszy':'123', 'drugi':'300', 'trzeci':200}
#slownik_zaawansowany = {'aaa':111, 'kolekcja':[10, 20, 30, 40, 50], 'slownik':{'ttt':123, 'yyy':'250'}}
#
##print(slownik_zaawansowany['kolekcja'][2])


#print(slownik['pierwszy'])




#a = 20
#b = 20
#c = 20
#
#if a==b and a==c:
#	print('a = b = c')
#else:
#	print('falsz')


#a = 1
#while a<=10:
#	print(a)
#	a+=1


#a = input("wpisz swoje imie: ")
#
#b = input("wpisz jakas liczbe: ")
#
#print("witaj, " + a + ", twoja liczba to:" + b)


#while True:
#	print("Jestem w programie")
#	a = input()
#	if a == 'x':
#		break
#	else:
#		continue
#	print("Dzieki za wprowadzanie danych")
#print("Jestem poza programem")


while True:

	a = int(input('Podaj pierwsza liczbe: '))
	b = int(input('Podaj druga liczbe: '))
	y = input('Podaj znak: ')
	
	if y == '+':
		print(a, "+", b, "=", a+b)
	
	if y == '-':
		print(a, "-", b, "=", a-b)
	
	if y == '*':
		print(a, "*", b, "=", a*b)
	
	if y == '/':
		print(a, "/", b, "=", a/b)
	
	if y == '%':
		print(a, "%", b, "=", a%b)
	
	if y == '//':
		print(a, "//", b, "=", a//b)
	
	if y == '**':
		print(a, "**", b, "=", a**b)

	print()

	x = input('Kontynujemy?(y/n): ')

	if x == 'y':
		continue

	elif x == 'n':
		break

