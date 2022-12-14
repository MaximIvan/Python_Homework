# Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задача 1 из семинара 2.
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# 0,56 -> 11

number = float(input('Введите число: '))
modNum = abs(number)
num = str(modNum)

sum = sum(map(int, num.replace('.', '')))
print(f'{number} -> {sum}')