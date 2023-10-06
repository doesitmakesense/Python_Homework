# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1. UI (user interface) +
# 2. Создать файл +
# 3. Читать файл +
# 4. Вывод данных на экран: +
#     - считать файл +
#     - сохранить в переменной +
#     - вывести на экран +
# 5. Запись контакта: +
#     - запросить данные +
#     - сохранить в переменную +
#     - записать в файл +
# 6. Поиск контакта:
#     - запросить данные поиска +
#     - сохранить в переменную +
#     - считать файл +
#     - сохранить в переменную +
#     - произвести поиск +
#
#    ДЗ:
# 7. Возможность изменения и удаления данных:
#     - прочитать файл
#     - ввести данные для поиска
#     - сохранить контакт в переменную
#     - найти нужное для изменения поле
#     - запросить это изменение или удаление
#     - если удаление, то удалить и попрощаться
#     - если изменение, то запросить новую инфу
#     - и заменить
#     - вывести на экран и попрощаться
#     - с поиском по виду данных, как в поиске
# 8. Дополнительно: защита от дурака на виде при поиске данных +

def name_data():
    return input('Введите имя: ')


def surname_data():
    return input('Введите фамилию: ')


def patronymic_data():
    return input('Введите отчество: ')


def phone_number_data():
    return input('Введите номер телефона: ')


def address_data():
    return input('Введите адрес: ')


def input_contact():
    name = name_data()
    surname = surname_data()
    patronymic = patronymic_data()
    phone_number = phone_number_data()
    address = address_data()
    return f'{name} {surname} {patronymic}\n{phone_number}\n{address}'


def add_contact():
    contact = input_contact()
    with open('Phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(contact + '\n\n')


def read_file():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        return data.read()


def print_contacts():
    data = read_file()
    print()
    print(data)


def search_contact():
    choice = None
    while choice != '5':
        print('Варианты поиска:\n'
              '1. По имени\n'
              '2. По фамилии\n'
              '3. По отчеству\n'
              '4. По номеру телефона\n'
              '5. По адресу')
        choice = input('Выберите вариант поиска: ')
        while choice not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод')
            choice = input('Введите номер операции: ')
        i_choice = int(choice) - 1
        search = input('Введите данные для поиска: ')
        data_str = read_file().rstrip()
        if search not in data_str:
            print('Такого контакта нет')
        else:
            data_lst = data_str.split('\n\n')
            for contact_str in data_lst:
                contact_lst = contact_str.replace('\n', ' ').split()
                if search in contact_lst[i_choice]:
                    print(contact_str)
                    print()
                    choice_search = input('Этот ли контакт вы искали? 1 - да, 2 - нет: ')
                    if choice_search == '1':
                        return contact_str
            print('Нужный контакт не обнаружен')


def change_contact():
    print('Какую запись вы хотите изменить?')
    contact = search_contact()
    if contact:
        print(contact)
        new_contact = contact.replace('\n', ' ').split()
        print('Варианты замены:\n'
              '1. Имя\n'
              '2. Фамилия\n'
              '3. Отчество\n'
              '4. Номер телефона\n'
              '5. Адрес\n'
              '6. Весь контакт целиком')
        choice = input('Выберите вариант замены: ')
        while choice not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            choice = input('Введите номер операции: ')
        if choice != '6':
            i_choice = int(choice) - 1
            replacement = input('Введите обновленные данные: ')
            new_contact[i_choice] = replacement
            # new_contact = ' '.join(new_contact[:3]) + '\n' + '\n'.join(new_contact[3:])
            new_contact = f'{new_contact[0]} {new_contact[1]} {new_contact[2]}\n{new_contact[3]}\n{new_contact[4]}'
            print('')
            print('Обновленный контакт: ' + '\n' + new_contact + '\n')
        else:
            new_contact = input_contact()
        data = read_file()
        with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact, new_contact)
            data2.write(data)


def delete_contact():
    print('Какую запись вы хотите удалить?')
    contact = search_contact()
    if contact:
        print(contact)
        data = read_file()
        with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact + '\n\n', '')
            data2.write(data)


def user_interface():
    with open('Phonebook.txt', 'a', encoding='utf-8'):  # создаем файл если его нет
        pass
    cmd = None
    while cmd != '6':
        print('Меню:\n'
              '1. Запись контакта\n'
              '2. Вывести данные на экран\n'
              '3. Поиск контакта\n'
              '4. Изменить данные\n'
              '5. Удалить данные\n'
              '6. Выход')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        match cmd:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                change_contact()
            case '5':
                delete_contact()
            case '6':
                print('До свидания))')


user_interface()
