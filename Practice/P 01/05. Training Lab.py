w = float(input()) * 100
h = float(input()) * 100
coridor = 100
seat_w = 70
seat_h = 120
catedra = 160
door = 160

# seats_total = (w + h) - coridor - catedra - door / seat
h2 = (h - coridor) // seat_w
w2 = (w // seat_h)
result = h2 * w2 - 3
print(result)
