# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# Пример:
# [1.1, 1.2, 3.1, 10.01] => 0.19

import random

number = int(input('Введите размер списка '))
list = []

for i in range(number):
    list.append(round(random.uniform(0.1, 10.5), 2))

min = list[0]
max = 0
for i in list:
    if i % 1 > max:
        max = i % 1
    if i % 1 < min:
        min = i % 1
dif = max - min
print(f'{list} => {round(dif, 2)}')