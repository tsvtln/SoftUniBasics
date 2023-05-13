from math import pi
figure = input()
face = 0
if figure == 'square':
    side = float(input())
    face = side * side
elif figure == 'rectangle':
    side_1 = float(input())
    side_2 = float(input())
    face = side_1 * side_2
elif figure == 'circle':
    radius = float(input())
    face = pi * radius * radius
elif figure == 'triangle':
    side_1 = float(input())
    side_2 = float(input())
    face = side_1 * side_2 / 2

print(f'{face:.3f}')
