from math import ceil, floor
magnolya = 3.25
zumbul = 4
roses = 3.50
cactie = 8

magnolya_count = int(input())
zumbuls_count = int(input())
roses_count = int(input())
cactie_count = int(input())
price_of_gift = float(input())

total_price = (magnolya * magnolya_count) + (zumbul * zumbuls_count) + (roses * roses_count) + (cactie_count * cactie)
total_price -= total_price * 0.05

if total_price >= price_of_gift:
    dif = total_price - price_of_gift
    print(f'She is left with {floor(dif)} leva.')
else:
    dif = price_of_gift - total_price
    print(f'She will have to borrow {ceil(dif)} leva.')
