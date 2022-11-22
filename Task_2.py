# Задача №2.
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

r = range(0, 2)
for x in r:
    for y in r:
        for z in r:
            a = (not (x or y or z)) == (not x and not y and not z)
            print(f'при {x}, {y}, {z} -> не ({x} или {y} или {z}) = (не {x} и не {y} и не {z})  - {a}')