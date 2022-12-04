# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

n = int(input('Введите размер списка чисел Фибоначчи: '))

num1 = num2 = 1
list = [num1, num2]
for i in range(2, n):
    num1,num2 = num2, num1 + num2
    list.append(num2)
num1 = num2 = 1
for i in range(-n, 1):
    num1,num2 = num2, num1 - num2 
    list.insert(0, num2)
print(list)