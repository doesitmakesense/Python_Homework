# Напишите функцию print_operation_table(operation, num_rows, num_columns),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
#
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
#
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
#
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
#
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.
#
# Пример
#
# На входе:
# print_operation_table(lambda x, y: x * y, 3, 3)
#
# На выходе:
# 1 2 3
# 2 4 6
# 3 6 9

def print_operation_table(operation, num_rows, num_columns):
    x, y = 1, 1
    if num_rows < 2:
        return print('ОШИБКА! Размерности таблицы должны быть больше 2!')

    for x in range(1, num_rows + 1):
        if y == 1:
            print(x, end='')
        else:
            print(operation(x, y), end='')
        for y in range(2, num_columns + 1):
            if x == 1:
                print(' ', end='')
                print(y, end='')
            else:
                print(' ', end='')
                print(operation(x, y), end='')
        if num_rows > x > 1:
            print(' ', end='')
        y = 1
        print('')


print_operation_table(lambda x, y: x * y, 3, 3)