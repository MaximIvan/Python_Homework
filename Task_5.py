# Задача №5.
# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:
#  A (3,6); B (2,1) -> 5,09
#  A (7,-5); B (1,-1) -> 7,21

x1 = float(input('Введите значение Х точки А: '))
y1 = float(input('Введите значение Y точки А: '))
x2 = float(input('Введите значение Х точки В: '))
y2 = float(input('Введите значение Y точки В: '))



import math
dis = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
print(f'А ({int(x1)}, {int(y1)}); В ({int(x2)}, {int(y2)}) -> {round(dis, 2)}')
