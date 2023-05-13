x = float(input())  # visochina
y = float(input())  # duljina
h = float(input())  # visochina na pokriva

window = 2.25
door = 2.4
green_paint_per_liter = 3.4
red_paint_per_liter = 4.3

pokriv_shirochina = y
porkriv_visochina = h


# stranichni steni / green paint
total_sides = (2 * (x * y)) - (window * 2)

# zadna strana
zadna_strana = x * x

# predna strana
predna_strana = (x * x) - door

total_strani = predna_strana + zadna_strana
total_strani_steni = total_strani + total_sides

green_paint = total_strani_steni / green_paint_per_liter

print(f'{green_paint:.2f}')

pokriv_sides = 2 * (x * y)
pokriv_fronts = 2 * (x * h / 2)
total_pokriv = pokriv_sides + pokriv_fronts

red_paint = total_pokriv / red_paint_per_liter

print(f'{red_paint:.2f}')
