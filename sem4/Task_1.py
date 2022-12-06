# Задача 1. 
# Вычислить число c заданной точностью d

# Пример:
# при d = 0.001, π = 3.141   
# Ввод: 0.01
# Вывод: 3.14

#   Ввод: 0.001
#   Вывод: 3.141

# import math
# print(round(math.pi, 4))

import sympy
# print(sympy.pi.evalf(5))

d = input('Задайте точность: ')

count = -1
for i in d:
    count += 1
print(f'при d = {d}, π = {sympy.pi.evalf(count)}')
