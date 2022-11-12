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

#______________________________________________________________________


#while True:
#
#	try:
#		a = int(input('\nPodaj pierwsza liczbe: '))	
#		b = int(input('\nPodaj druga liczbe: '))
#	except:
#		print("\nPodalesz zla liczbe.")
#		continue
#
#	y = input('\nPodaj znak: ')
#
#	print()
#
#	if b == 0 and y == '/':
#		print("Nie mozna delic na 0!")
#		continue
#
#	if y == '+':
#		print(a, "+", b, "=", a+b)
#	
#	elif y == '-':
#		print(a, "-", b, "=", a-b)
#	
#	elif y == '*':
#		print(a, "*", b, "=", a*b)
#	
#	elif y == '/':
#		print(a, "/", b, "=", a/b)
#	
#	elif y == '%':
#		print(a, "%", b, "=", a%b)
#	
#	elif y == '//':
#		print(a, "//", b, "=", a//b)
#	
#	elif y == '**':
#		print(a, "**", b, "=", a**b)
#
#	else:
#		print("Podalesz zly znak.")
#		continue
#
#	print()
#
#	x = input('Kontynujemy?(y/n): ')
#
#	if x == 'y':
#		print()
#		continue
#
#	elif x == 'n':
#		break

#______________________________________________________________________


#while True:
#	a = input("Podaj liczbe")
#
#	try:
#		print(float(a) / 2)
#	#except ValueError as e:
#	#	print(e)
#
#	except:
#		print("Podales zla liczbe.")





#import random
#
#def Czy_zgadles(a):
#	b = random.randint(0, 10)
#
#	print(b)
#
#	if a == b:
#		return True
#		
#	else:
#		return False
#
#
#x = False
#
#while x == False:
#
#	a = input("Podaj liczbe: ")
#
#	x = Czy_zgadles(a)
#
#	print(x)




#tablica = "zwykly tekst, zwykly tekst"
#
#print(tablica[0])
#print(tablica.split(',')[0])
#print(tablica[:-1])
#print(tablica.replace(',,',','))



zero = [" xxxx ",
        "x    x",
        "x    x",
        "x    x",
        "x    x",
        "x    x",
        " xxxx "]


one = ["  x ",
       " xx ",
       "x x ",
       "  x ",
       "  x ",
       "  x ",
       "xxxx"]


two = [" xxxx ",
       "x    x",
       "    x ",
       "   x  ",
       "  x   ",
       " x    ",
       "xxxxxx"]


three = [" xxxx ",
         "x   x ",
         "   x  ",
         "  xxx ",
         "     x",
         "x    x",
         " xxxx "]


four = ["x    x",
	"x    x",
	"x    x",
	"xxxxxx",
	"     x",
	"     x",
	"     x"]


five = ["xxxxxx",
	"x     ",
	"x     ",
	"xxxxx ",
	"     x",
	"x    x",
	" xxxx "]


six = [" xxxx ",
       "x    x",
       "x     ",
       "xxxxx ",
       "x    x",
       "x    x",
       " xxxx "]


seven = ["xxxxxx",
	 "x    x",
	 "    x ",
	 "   x  ",
	 "  x   ",
	 " x    ",
	 "x     "]


eight = [" xxxx ",
	 "x    x",
	 "x    x",
	 " xxxx ",
	 "x    x",
	 "x    x",
	 " xxxx "]


nine = [" xxxx ",
	"x    x",
	"x    x",
	" xxxxx",
	"     x",
	"x    x",
	" xxxx "]


dot = [" ",
       " ",
       " ",
       " ",
       " ",
       " ",
       "x"]


plus = ["       ",
	"   x   ",
	"   x   ",
	"x x x x",
	"   x   ",
	"   x   ",
	"       "]


equal = ["       ",
	 "       ",
	 " xxxxx ",
	 "       ",
	 " xxxxx ",
	 "       ",
	 "       "]


x = input("podaj liczbe: ")

for i in range(7):
	tekst = ""
	for k in range(len(x)):
	
		if x[k] == "0":
			tekst += zero[i]
	
		if x[k] == "1":
			tekst += one[i]
	
		if x[k] == "2":
			tekst += two[i]
	
		if x[k] == "3":
			tekst += three[i]
	
		if x[k] == "4":
			tekst += four[i]
	
		if x[k] == "5":
			tekst += five[i]
	
		if x[k] == "6":
			tekst += six[i]
	
		if x[k] == "7":
			tekst += seven[i]
	
		if x[k] == "8":
			tekst += eight[i]
	
		if x[k] == "9":
			tekst += nine[i]

		if x[k] == ".":
			tekst += dot[i]

		if x[k] == "+":
			tekst += plus[i]

		if x[k] == "=":
			tekst += equal[i]

		tekst += "  "

	print(tekst)