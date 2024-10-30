import random
import json
import os
from xml.etree.ElementTree import indent

PATH = 'Manual.json'
phone_book = []
user_ids = set() # Хранилище ID

def unique_id():
    # Функция для генерации уникального ID
    while True:
        new_id = ''.join(random.choices('0123456789', k=8))
        if new_id not in user_ids:
            user_ids.add(new_id)
            return new_id

def open_file():
    if os.path.isfile(PATH):
        # Функция для чтения данных из JSON-файла и добавления их в указанный список
        with open(PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            phone_book.extend(data)
            return print('\nТелефонная книга успешно открыта\n')
    return print('\nТелефонная книга не найдена!\n')


def save_file():
    # Функция для сохранения данных в файле
    with open(PATH, "w", encoding="utf-8") as file:
        json.dump(phone_book, file, ensure_ascii=False, indent=4)
        return print('Файл успешно сохранен!')


def show_all_contacts():
    # Функция отображающая весь список контактов
    print('Список контактов:')
    for contact in phone_book:
        print_contact(contact)

def print_contact(cont):
    # Функция для вывода на печать словаря в одну строку
    print(f"{cont.get('id'):20}"
          f"{(cont.get('last_name')).title():20}"
          f"{(cont.get('name')).title():20}"
          f"{cont.get('phone_num'):20}"
          f"{cont.get('comment'):20}"
            )

def search_contacts():
    # Функция запуска поиска по значению с клавиатуры
    crit = input('Введите значение поиска: ')
    return search_criteria(crit)

def search_criteria(criteria):
    # Функция поиска по значение criteria
    for contact in phone_book:
        if criteria.lower() in contact.values():
            print_contact(contact)
            return contact
    else:
        print('Контакт не найден')


def create_contact():
    # Функция для добавления нового контакта
    new_contact = {}
    print('*' * 18 ,"Добавление нового контакта\n",
          "Поля отмеченные * обязательные для заполнения", sep='\n')
    last_name_inp, phone_num_inp = '', ''
    while last_name_inp is '':
        last_name_inp = input('Введите фамилию*: ')
    name_inp = input('Введите имя: ')
    while phone_num_inp is '':
        phone_num_inp = input('Введите номер телефона*: ')
    comm_input: str = input('Введите комментарий(не обязательное поле): ')
    new_contact = {
        'id' : unique_id(),
        'name': name_inp.lower() if name_inp != '' else 'Не заполнено',
        'last_name' : last_name_inp.lower(),
        'phone_num' : phone_num_inp,
        'comment' : comm_input if comm_input != '' else 'Не заполнено'
    }
    print('\nНовый контакт успешно добавлен!\n')

    return phone_book.append(new_contact)


def change_contact():
    # Функция изменения контакта по ключу
    chg_id = input('Ведите ID контакта для изменения: ')
    chg_key = input('Доступные поля для изменения - имя, фамилия, телефон и комментарий.\nУкажите поле: ')
    if chg_key.lower() == 'имя':
        chg_key = 'name'
    elif chg_key.lower() == 'фамилия':
        chg_key = 'last_name'
    elif chg_key.lower() == 'телефон':
        chg_key = 'phone_num'
    elif chg_key.lower() == 'комментарий':
        chg_key = 'comment'
    else:
        print('Указанное поле не найдено!')
        return user_menu()

    chg_value = input('Введите новое значение: ')
    for d in phone_book:
        if d.get('id') == chg_id:
            d[chg_key] = chg_value
            print('Контакт успешно обновлен.')


def delete_contact():
    # Функция удаления контакта по ID
    delete_id = input('Ведите ID контакта для удаления из телефонной книги: ')
    for contact in phone_book:
        if delete_id in contact.values():
            print('Контакт удалён из справочника')
            return phone_book.remove(contact)

def user_menu():
    # Функция стартового меню
    select = {
        '1': open_file,
        '2': save_file,
        '3': show_all_contacts,
        '4': create_contact,
        '5': search_contacts,
        '6': change_contact,
        '7': delete_contact,
    }
    print('''
Телефонный справочник
Доступные команды:
1 - Открыть файл
2 - Сохранить файл
3 - Показать все контакты
4 - Создать новый контакт
5 - Поиск контакта
6 - Изменить существующий контакт
7 - Удалить контакт
        ''')
    while True:
        inp = input("Введите номер команды (1-7) или 'q' для выхода: ")
        if inp.lower() == 'q':  # Выход из меню
            print("Выход из меню.")
            break
        action = select.get(inp)
        if action:
            action()  # Вызываем функцию, если она найдена
        else:
            print("Неверная команда, попробуйте снова.")

user_menu()
