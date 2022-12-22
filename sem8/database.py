path = "sem8\phone_book.txt"

def add_contact(contact):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(' '.join(contact).upper())
        file.write(f"\n")

def output_list():
    with open(path, 'r', encoding='utf-8') as file:
        contact_list = []
        for i in file:
            temp = i.strip().split(' ')
            contact_list.append(temp)
    return contact_list

def clear_db():
    with open(path, 'w', encoding='utf-8') as file:
        file.write("")

def exp_csv():
    with open(path, 'r', encoding='utf-8') as file:    
        contact_list_csv = []
        for i in file:
            temp = i.strip().split(' ')
            contact_list_csv.append(temp)
    with open('sem8\phone_book.csv', 'w', encoding='utf-8') as new_format:
        new_format.write(str(f'{contact_list_csv}\n'))