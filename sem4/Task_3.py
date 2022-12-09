# Задача 3. 
# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

import random
n = int(input('Введите размер списка: '))

list = []
for i in range(n):
    list.append(random.randint(0, 5))
print(list)

uniqueList = []

for i in list:
    if list.count(i) < 2:
        uniqueList.append(i)
        
print(uniqueList)
