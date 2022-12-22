import database as db

def new_contact():
    last_name = input("Введите Фамилию: ")
    first_name = input("Введите Имя: ")
    second_name = input("Введите Отчество: ")
    phone_number = input("Введите телефон: ")
    status = input("Введите статус: ")
    return last_name, first_name, second_name, phone_number, status

def print_contact(contact):
    if len(contact) > 0:
        print("Фамилия".center(20), '|', "Имя".center(20), '|', "Отчество".center(20), '|', "Телефон".center(20), '|', "Статус".center(20))
        print("-"*100)
        for person in contact:
            print(person[0].center(20), '|', person[1].center(20), '|', person[2].center(20), '|', person[3].center(20), '|', person[4].center(20))
    else:
        print("Нет контактов")

def search_contact(word, contact_list):
    for person in contact_list:
        if word in person:
            print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Телефон".center(20), "Статус".center(20))
            print("-"*100)
            print(person[0].center(20), person[1].center(20), person[2].center(20), person[3].center(20), person[4].center(20))    
        else:
            return None

            