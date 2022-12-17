import function as func
import database as db


def start():
    print('\n\
    1 - Добавить контакт\n\
    2 - Вывести книгу на экран\n\
    3 - Найти контакт\n\
    4 - Очистить книгу')

    task = input("Выберите действие: ")
    action(task)


def action(task):
    if task == '1':
        input_data = func.new_contact()
        func.add_contact(input_data)


    if task == '2':
        all_list = func.output_list()
        if len(all_list) > 0:
            func.print_contact(all_list)
        else:
            print("Нет контактов")

    if task == '3':
        search = input("Введите данные для поиска: ").upper()
        data = func.output_list()
        person = func.search_contact(search, data)
        print(person)


    if task == '4':
        db.clear_db()
        print("- Справочник пуст\n")