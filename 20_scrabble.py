# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
#
# Ввод:
# ноутбук
# Вывод:
# 12

# словарь, ключ - цифра, значения - буквы (можно несколько значений к одному ключу?)
# ищу значение, ключи собираю через какой-то конвертор сразу в инт в счетчик суммы
# вывожу счетчик
'''
data = {1: ('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'),
        2: ('Д', 'К', 'Л', 'М', 'П', 'У', 'D', 'G'),
        3: ('Б', 'Г', 'Ё', 'Ь', 'Я', 'B', 'C', 'M', 'P'),
        4: ('Й', 'Ы', 'F', 'H', 'V', 'W', 'Y'),
        5: ('Ж', 'З', 'Х', 'Ц', 'Ч', 'K'),
        8: ('Ш', 'Э', 'Ю', 'J', 'X'),
        10: ('Ф', 'Щ', 'Ъ', 'Q', 'Z')}

english_scores = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}
russian_scores = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10
}
string = list(input('Введите слово: ').upper())
sum = 0
for letter in string:
    if letter in english_scores:
        sum = sum + english_scores[letter]
    else:
        sum = sum + russian_scores[letter]
print(sum)

word = str(input())
sum_points = 0
for key, value in dict_with_letter.items():
    for letter in word.upper():
        if letter in value:
            sum_points += key
print(sum_points)
'''
data = {1: ('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'),
        2: ('Д', 'К', 'Л', 'М', 'П', 'У', 'D', 'G'),
        3: ('Б', 'Г', 'Ё', 'Ь', 'Я', 'B', 'C', 'M', 'P'),
        4: ('Й', 'Ы', 'F', 'H', 'V', 'W', 'Y'),
        5: ('Ж', 'З', 'Х', 'Ц', 'Ч', 'K'),
        8: ('Ш', 'Э', 'Ю', 'J', 'X'),
        10: ('Ф', 'Щ', 'Ъ', 'Q', 'Z')}

k = 'ноутбук'

word = k
sum_points = 0
for key, value in data.items():
    for letter in word.upper():
        if letter in value:
            sum_points += key
print(sum_points)