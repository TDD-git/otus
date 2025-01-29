import json
import os


class PhonebookModel:
    def __init__(self, file_name, phone_book=None):
        self.file_name = file_name
        #self._is_file_exist()
        if phone_book is None:
            self.phone_book = []


    # def _is_file_exist(self):
    #     """
    #     Проверка на существование файла
    #     """
    #     if not os.path.isfile(self.file_name):
    #         raise FileExistsError


    def read_file(self) -> list:
        """
        Функция для чтения данных из JSON-файла и добавления их в указанный список
        """
        with open(self.file_name, "r", encoding="UTF-8") as file:
            self.phone_book = json.load(file)
            return self.phone_book


    def write_file(self, data):
        """
        Запись обновленного справочника в файл
        """
        with open(self.file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4)