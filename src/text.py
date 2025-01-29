PATH: str = 'pb.json'

main_menu = [
    'Главное меню',
    'Открыть файл',
    'Сохранить файл',
    'Показать все контакты',
    'Создать контакт',
    'Найти контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход'
]

file_not_exist_error = 'Телефонная книга не найдена!'

pb_open = 'Телефонная книга успешно открыта!'


msg_error = 'Телефонная книга пуста!'

main_menu_choice = 'Выберите пункт меню: '

main_menu_user_choice_error_not_digit = 'Требуется указать число от 1 до {number}'.format(number=len(main_menu) - 1)

pb_save = 'Справочник успешно сохранен!'

search_contact_input = 'Укажите значение для поиска: '

search_contact_error = 'Указанный контакт не найден!'

change_contact_input_id = 'Укажите ID пользователя для изменения: '

change_contact_input_key = 'Укажите ключ (доступные поля: Имя, Фамилия, Номер): '

change_contact_input_new_value = 'Укажите новое значение: '

change_contact_OK = 'Контакт был успешно обновлен!'

change_contact_error_no_con = 'Контакт не найден! Повторите поиск'

create_name = 'Введите имя: '

create_lastname = 'Введите фамилию: '

create_number = 'Введите номер телефона: '

create_comment = 'Укажите комментарий: '

create_person_ok = 'Контакт успешно создан!'

delete_contact_id = 'Укажите ID для удаления контакта: '

delete_contact_ok = 'Контакт был успешно удален!'
