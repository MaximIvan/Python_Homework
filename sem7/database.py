path = "phone_book.txt"

def clear_db():
    with open(path, 'w', encoding='utf-8') as file:
        file.write("")