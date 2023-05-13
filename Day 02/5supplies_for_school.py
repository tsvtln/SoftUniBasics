pencils = 5.80
markers = 7.20
detergent = 1.20

num_pencils = int(input())
num_markers = int(input())
liters_detergent = int(input())
discount = int(input()) / 100

price_pencils = num_pencils * pencils
price_markers = num_markers * markers
price_detergent = liters_detergent * detergent
# Цена за всички материали => 11.60 + 21.60 + 4.80 = 38.00 лв.
final_price1 = price_pencils + price_markers + price_detergent
final_price2 = final_price1 - (final_price1 * discount)

print(final_price2)
