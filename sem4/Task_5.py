# Задача 5. 
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, 
# у которых "х" в одинаковых степенях). 
# Пример того, что будет в итоговом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

import sympy

f_path_file1 = 'file1.txt'
f_path_file2 = 'file2.txt'
f_path_file3 = 'file3.txt'

with open(f_path_file1, 'r') as file_1:
    polynom1: str = file_1.read().replace('= 0', '+')

with open(f_path_file2, 'r') as file_2:
    polynom2: str = file_2.read().split('=')[0]

x = sympy.symbols('x')

polynom_sum = sympy.powsimp(polynom1 + polynom2)

with open(f_path_file3, 'w') as file_3:
    file_3.writelines(f'{str(polynom_sum)} = 0')