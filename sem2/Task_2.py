# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число: '))
i = 1
r = []
count = 1
while i <= n:
    for j in range(1, i + 1):
        count *= j
    r.append(count)
    count = 1
    i += 1
print(f'тогда: {r}', end='')
