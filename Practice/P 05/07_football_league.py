stadium_capacity, number_of_fans = int(input()), int(input())
sector_a, sector_b, sector_v, sector_g = 0, 0, 0, 0

for fans in range(number_of_fans):
    sector = input()
    if sector == 'A':
        sector_a += 1
    elif sector == 'B':
        sector_b += 1
    elif sector == 'V':
        sector_v += 1
    else:
        sector_g += 1

avg_a = (sector_a / number_of_fans) * 100
avg_b = (sector_b / number_of_fans) * 100
avg_v = (sector_v / number_of_fans) * 100
avg_g = (sector_g / number_of_fans) * 100
avg_stadium = (number_of_fans / stadium_capacity) * 100

print(f'{avg_a:.2f}%\n{avg_b:.2f}%\n{avg_v:.2f}%\n{avg_g:.2f}%\n{avg_stadium:.2f}%')
