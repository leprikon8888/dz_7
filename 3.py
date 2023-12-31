'''Task 3 Реалізуйте просту програму для збереження контактів. Кожен контакт може мати ім'я як ключ та номер телефону /
як значення. Дозвольте користувачу додавати нові контакти, видаляти існуючі та отримувати номер телефону за ім'ям.
'''
tel_book = {}
while True:
    action = input('какое действие хотите выполнить?\n'
                       '1 - добавить контакт\n'
                       '2 - удалить контакт по имени\n'
                       '3 - просмотреть контакт по имени\n'
                       '4 - просмотреть контакт по номеру телефона \n'
                       '5 - просмотреть всю телефонную книгу\n'
                       '6 - закрыть программу\n'
                       'Введите действие -  ')
    if action == '1':
        name = (input('введите имя нового контакта - ')).title()
        number = int(input('введите номер нового контакта - '))
        if name not in tel_book:
            tel_book[name] = number
            print(f'Контакт успешно добавлен')
        else:
            print('этот контакт уже есть в книге')
        print(30*'*')

    elif action == '2':
        name = (input('введите имя контакта, который нужно удалить- ')).title()
        if name not in tel_book:
            print('контакт не найден в телефонной книге')
            print(30 * '*')
        else:
            del tel_book[name]
            print(f'контакт {name} удалён из телефонной книги')
            print(30 * '*')

    elif action == '3':
        name = (input('введите имя контакта, который нужно показать- ')).title()
        if name not in tel_book:
            print('контакт не найден в телефонной книге')
            print(30 * '*')
        else:
            print(f'искомый контакт - {name} : {tel_book[name]}')
            print(30 * '*')

    elif action == '4':
        number = int(input('введите номер телефона искомого контакта - '))
        for key, value in tel_book.items():
            if value == number:
                print (f'искомый контакт - {key}{value}')
                print(30 * '*')
            else:
                print('контакт не найден в телефонной книге')
                print(30 * '*')

    elif action == '5':
        if not len(tel_book):
            print('телефонная книга пуста, попробуем снова?')
            print(30 * '*')
        else:
            for key, value in tel_book.items():
                print(f'Имя контакта - {key}, номер телефона - {value}\n')
                print(30 * '*')

    elif action == '6':
        print('программа закрыта')
        break


    else:
        print('Что-то пошло не так, попробуем снова?')
        print(30 * '*')