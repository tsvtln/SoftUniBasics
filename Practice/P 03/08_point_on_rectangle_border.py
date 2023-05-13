x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

on_horizontal_side = x1 <= x <= x2 and (y == y1 or y == y2)
on_vertical_side = y1 <= y <= y2 and (x == x1 or x == x2)

if on_horizontal_side or on_vertical_side:
    print("Border")
else:
    print("Inside / Outside")
