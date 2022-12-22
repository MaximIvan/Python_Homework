from datetime import datetime

def status_log(data):
    time = datetime.now().strftime('%m.%d.%Y - %H:%M')
    with open('sem8\log.txt', 'a+', encoding='utf-8') as log:
        log.write(f"{[time]} - {data}\n")