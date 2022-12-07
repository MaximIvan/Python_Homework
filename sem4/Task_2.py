# Задача 2. 
# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input('Задайте натуральное число: '))
n_list = []
s_num = 2
res = n
while s_num <= n:
    if res % s_num == 0:
        n_list.append(s_num)
        res = res/s_num
        s_num = 2
    else:
        s_num +=1
print(f'Список простых множителей числа {n} -> {n_list}') 
