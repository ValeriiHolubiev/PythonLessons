#Функция map служит для применения к какой либо функции в качестве параметра каждый элемент из списка.

# def Summa(x):
# 	return x + x

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for item in map(Summa, list):
# 	print(item)




#Функция filtr служит для отфильтровывания значений равных false

# def Czy_liczba_Parzysta(x):
# 	return x % 2 == 0

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in filter(Czy_liczba_Parzysta, number_list):
# 	print(number)




#Функция лямбда нужна для создания "анонимных" функций. Оба варианта кода приведут к одному и тому же результату.


#1

# def Cube(number):
# 	return number ** 3

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(list(map(Cube, list1)))


# #2

# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(list(map(lambda number: number ** 3, list2)))

