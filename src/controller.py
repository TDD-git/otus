import random
from view import PhonebookView
from model import PhonebookModel
import text


class PhonebookController:
    def __init__(self):
        self.model = PhonebookModel(text.PATH)
        self.view = PhonebookView()


    def app(self) -> None:
        """
        Запуск приложения. Реализация логики основного меню на рекурсии. Выход по команде Exit.
        """
        self.view.show_main_menu()
        user_choice = self.view.main_menu_user_choice()
        main_menu_controller = [
            self.open_file,
            self.save_file,
            self.show_all_contacts,
            self.create_contacts,
            self.search_contacts,
            self.change_contacts,
            self.delete_contacts,
            PhonebookController.exit_from_phonebook
        ]
        main_menu_controller[user_choice - 1]()
        self.app()


    def save_file(self):
        """
        Сохранение обновленного справочника в файл
        """
        self.view.message(text.pb_save)
        self.model.write_file(self.model.phone_book)


    def open_file(self):
        """
        Открытие файла
        """
        self.model.read_file()
        self.view.message(text.pb_open)


    def search_contacts(self) -> None:
        """
        Функция запуска поиска по значению с клавиатуры
        """
        criteria = self.view.user_input(text.search_contact_input)
        for contact in self.model.phone_book:
            if criteria.title() in contact.values():
                self.view.print_contact(contact)
        else:
            self.view.message(text.search_contact_error)


    def show_all_contacts(self) -> None:
        """
        Функция печати всех контактов справочника
        """
        return self.view.show_contacts(self.model.phone_book)


    def create_contacts(self):
        """
        Создание новой записи в справочнике. ID генерируется случайным образом.
        """
        new_contact = {}
        rand_id = ''.join(random.choices('0123456789', k=8))
        new_contact['id'] = rand_id
        new_contact.update(self.view.create_user())
        self.view.message(text.create_person_ok)
        self.model.phone_book.append(new_contact)
        return self.model.phone_book


    def change_contacts(self):
        """
        Изменение контакта в справочнике по ID. Указывается ключ словаря и значение для обновления
        """
        contact_id = self.view.user_input(text.change_contact_input_id)
        for contact_dict in self.model.phone_book:
            if contact_id == contact_dict['id']:
                key = self.view.user_input(text.change_contact_input_key).lower()
                new_value = self.view.user_input(text.change_contact_input_new_value)
                contact_dict[key] = new_value
                self.view.message(text.change_contact_OK)
                return self.model.phone_book
        else:
            self.view.message(text.change_contact_error_no_con)


    def delete_contacts(self) -> None:
        """
        Функция удаления контакта по ID
        """
        delete_id: str = self.view.user_input(text.delete_contact_id)
        for contact in self.model.phone_book:
            if delete_id in contact.values():
                self.view.message(text.delete_contact_ok)
                return self.model.phone_book.remove(contact)


    @staticmethod
    def exit_from_phonebook():
        """
        Функция завершения программы
        """
        exit()

