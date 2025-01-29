import text

class PhonebookView:

    @staticmethod
    def message(msg: str):
        """
        Печать значения msg
        :param msg:
        """
        print('\n' + '=' * len(msg))
        print(msg)
        print('=' * len(msg) + '\n')


    @staticmethod
    def show_main_menu():
        """
        Динамическая печать пунктов меню из модуля text
        """
        for i, row in enumerate(text.main_menu):
            print(f'\t{i}. {row}' if i else row)


    def user_input(self, msg: str) -> str:
        """
        Функция запроса ввода с клавиатуры. Текст подставляется в controller
        :param msg:
        """
        return input(msg)


    def show_contacts(self, contacts):
        """Функция перебора значения справочника. Используется перед выводом на печать"""
        for contact in contacts:
            self.print_contact(contact)


    @staticmethod
    def print_contact(contact):
        """
        Печать одного словаря в формате f-строки
        """
        print('=' * 100)
        print(f"{contact.get('id'):20}"
              f"{(contact.get('фамилия')).title():20}"
              f"{(contact.get('имя')).title():20}"
              f"{contact.get('номер'):20}"
              f"{contact.get('комментарий'):20}"
              )
        print('=' * 100)


    @staticmethod
    def main_menu_user_choice():
        """
        Вывод меню в консоль
        """
        while True:
            user_choice = input(text.main_menu_choice)
            if user_choice.isdigit() and 0 < int(user_choice) < len(text.main_menu):
                return int(user_choice)
            else:
                print(text.main_menu_user_choice_error_not_digit)


    def create_user(self):
        """
        Создание нового пользователя
        """
        name = self.user_input(text.create_name)
        lastname = self.user_input(text.create_lastname)
        phone_n = self.user_input(text.create_number)
        comment = self.user_input(text.create_comment)
        person = {
            'имя': name,
            'фамилия': lastname,
            'номер': phone_n,
            'комментарий': comment if comment != '' else 'Нет комментариев'
        }
        return person
