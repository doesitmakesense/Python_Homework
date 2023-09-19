# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
#
# 5
# 1 2 3 4 5
# 6
# -> 5
'''
n = int(input('Напишите, сколько будет элементов в списке: '))
x = int(input('Напишите, какое число ищем: '))

list_1 = [i for i in range(1, n + 1)]

if x > n:
    print('Вы ввели число большее, чем элементов в списке')
    n = int(input('Напишите, сколько будет элементов в списке: '))
    x = int(input('Напишите, какое число ищем: '))

diff = 0
for i in range(len(list_1)):
    if abs(list_1[i] - x == 0):
        print(f'Самое близкое число к {x}: {list_1[i]}')
        break
    else:
        diff += 1
'''
# 2
from random import randint

n = int(input('Напишите, сколько будет элементов в списке: '))
d = int(input('Напишите максимальное значение: '))
x = int(input('Напишите, какое число ищем: '))

list_1 = [randint(1, d) for i in range(1, n + 1)]
print(list_1)

if x > n:
    print('Вы ввели число большее, чем элементов в списке')

diff = abs(x - list_1[0])
closest = list_1[0]
for i in range(len(list_1)):
    if abs(x - list_1[i]) < diff:
        diff = abs(list_1[i] - x)
        closest = list_1[i]

print(f'Самое близкое число к {x}: {closest}')


# 3
list_1 = [1, 2, 3, 4, 5]
k = 6

diff = abs(k - list_1[0])
closest = list_1[0]
for i in range(len(list_1)):
    if abs(k - list_1[i]) < diff:
        diff = abs(list_1[i] - k)
        closest = list_1[i]

print(f'{closest}')
