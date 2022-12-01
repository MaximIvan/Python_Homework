# Задача №1.
# Написать программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# 6 - да
# 7 - да
# 1 - нет

work_day = range(1, 6)
holiday = range(6, 8)
number = int(input('Введите число: '))
if number in work_day:
    print(f'{number} - нет, рабочий')
elif number in holiday:
    print(f'{number} - да, выходный')