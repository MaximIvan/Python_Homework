# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# 0,56 -> 11

number = float(input('Введите число: '))
modNum = abs(number)
num = str(modNum)
sum = 0
num = num.replace('.', '')

for i in num:
    sum += int(i)
print(f'{number} -> {sum}')

