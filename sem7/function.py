import database as db


def new_contact():
    last_name = input("Введите Фамилию: ").upper()
    first_name = input("Введите Имя: ").upper()
    second_name = input("Введите Отчество: ").upper()
    phone_number = input("Введите телефон: ").upper()
    status = input("Введите статус: ").upper()
    return last_name, first_name,second_name, phone_number, status 

def print_contact(contact):
    if len(contact) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Телефон".center(20), "Статус".center(20))
        print("-"*100)
        for person in contact:
            print(person[0].center(20), person[1].center(20), person[2].center(20), person[3].center(20), person[4].center(20))
    else:
        print("Нет контактов")

def search_contact(word, contact):
    if len(contact) > 0:
        for person in contact:
            if word in person:
                print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Телефон".center(20), "Статус".center(20))
                print("-"*100)
                print(person[0].center(20), person[1].center(20), person[2].center(20), person[3].center(20), person[4].center(20))
            else:
                return None

def output_list():
    with open(db.path, 'r', encoding='utf-8') as file:
        contact_list = []
        for i in file:
            temp = i.strip().split(' ')
            contact_list.append(temp)
    return contact_list

def add_contact(contact):
    with open(db.path, 'a+', encoding='utf-8') as file:
        file.write(' '.join(contact).upper())
        file.write(f"\n")
