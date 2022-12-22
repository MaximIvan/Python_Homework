import function as func
import database as db
from log import status_log


new_contact = 1
veiw_contact_list = 2
search_contact = 3
clear_phone_book = 4
exp_to_csv = 5
exit = 0

def start():
    while True:
        print('\n\
    1 - Добавить контакт\n\
    2 - Вывести книгу на экран\n\
    3 - Найти контакт\n\
    4 - Очистить телефонную книгу\n\
    5 - экспортировать данные в формате csv\n\
    0 - Выход')
        task = int(input("Выберите действие: "))
        action(task)
        if task == 0:
            print("Хорошего дня")
            break
          
def action(task):
    if task == 1:
        input_data = func.new_contact()
        db.add_contact(input_data)
        status_log(f"Добавлен новый контакт - {' '.join(input_data)}")

    if task == 2:
        all_list = db.output_list()
        if len(all_list) > 0:
            func.print_contact(all_list)
        else:
            print("Нет контактов")
        status_log("Просмотр контактов")

    if task == 3:
        search = input("Введите данные для поиска: ").upper()
        contact_list = db.output_list()
        func.search_contact(search, contact_list)  
        status_log(f"Поиск контакта - {' '.join(func.search_contact)}")

    if task == 4:
        db.clear_db()
        print("- Справочник пуст\n")
        status_log("- Очистка справочника")

    if task == 5:
        db.exp_csv()
        status_log("Экспорт данных в формате csv")

    

        












