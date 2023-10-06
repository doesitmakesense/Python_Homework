# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
#
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


# def create_lst(n, diff, how_much):
#     lst = []
#     for i in range(how_much):
#         lst.append(n + i * diff)
#     return lst
#
#
# n = int(input('Введите первый элемент прогресии: '))
# diff = int(input('Введите шаг: '))
# how_much = int(input('Введите количество элементов: '))
# lst = create_lst(n, diff, how_much)
# print(lst)


a1 = 2
d = 3
n = 4

for i in range(n):
    print(a1 + i * d)

print([a1 + i * d for i in range(n)])

print(*list(range(a1, a1 + n * d, d)), sep='\n') # sep в столбик фигачит

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15











