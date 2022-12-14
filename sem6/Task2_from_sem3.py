# Задача: предложить улучшения кода для уже решённых задач (3-5 задача):

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задача 2 из семинара 3. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math
list1 = list(map(int, input('Введите числа через пробел: ').split()))
print(f'{list1} => {list([a*b for a, b in zip(list1[0:math.ceil(len(list1)/2)],list1[::-1])])}')



