# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint 
total = 121
print(
    'Правила игры:\n На столе лежит 121 конфета.\nИграют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.'
)
print('Кто будет играть?\nЕсли игрок против игрока, введите 1.\nЕсли игрок против бота введите 2')
choose = int(input())

if choose == 1:
    print('Как зовут первого игрока')
    player1 = input()
    print(f'Привет {player1}')
    print('Как зовут второго игрока')
    player2 = input()
    print(f'Привет {player2}')
    
    count_player = randint(1, 2)

    while total >= 0:
        if count_player == 1:
            print(f'{player1} Ваш ход')
            num = int(input())
            if 29 > num > 0: 
                total -= num
                print(f'Конфет осталось {total}')
                count_player += 1
                if total == 0:
                    print(f'Победитель {player1}')
                    break
            else:
                print('Задано неверное число, читай правила')
                count_player = 1
  
        if count_player == 2:
            print(f'{player2} Ваш ход')
            num = int(input())
        if 29 > num > 0:
            total -= num
            print(f'Конфет осталось {total}')
            count_player -= 1
            if total == 0:
                print(f'Победитель {player2}')
                break
        else:
            print('Задано неверное число, читай правила')
            count_player = 2

if choose == 2:
    print('Как зовут игрока')
    player1 = input()
    print(f'Привет {player1}')
    player2 = 'Стив'
    print(f'Бота зовут {player2}')
    
    count_player = randint(1, 2)

    while total >= 0:
        if count_player == 1:
            print(f'{player1} Ваш ход')
            num = int(input())
            if 29 > num > 0: 
                total -= num
                print(f'Конфет осталось {total}')
                count_player += 1
                if total == 0:
                    print(f'Победитель {player1}')
                    break
            else:
                print('Задано неверное число, читай правила')
                count_player = 1
  
        if count_player == 2:
            print(f'Ходит {player2}')
            num = randint(0, 29)
            print(num)
            total -= num
            print(f'Конфет осталось {total}')
            count_player -= 1
            if total == 0:
                print(f'Победитель {player2}')
                break
