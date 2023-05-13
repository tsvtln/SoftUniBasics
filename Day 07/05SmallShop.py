product = input()
city = input()
quantity = float(input())

# Prices Sofia
if city == 'Sofia':
    if product == 'coffee':
        price = 0.50
    elif product == 'water':
        price = 0.80
    elif product == 'beer':
        price = 1.20
    elif product == 'sweets':
        price = 1.45
    elif product == 'peanuts':
        price = 1.60
# final_price = price * quantity
# print(final_price)

elif city == 'Plovdiv':
    if product == 'coffee':
        price = 0.40
    elif product == 'water':
        price = 0.70
    elif product == 'beer':
        price = 1.15
    elif product == 'sweets':
        price = 1.30
    elif product == 'peanuts':
        price = 1.50

# Prices Plovdiv
# coffee = 0.40
# water = 0.70
# beer = 1.15
# sweets = 1.30
# peanuts = 1.50

# Prices Varna
# coffee = 0.45
# water = 0.70
# beer = 1.10
# sweets = 1.35
# peanuts = 1.55

elif city == 'Varna':
    if product == 'coffee':
        price = 0.45
    elif product == 'water':
        price = 0.70
    elif product == 'beer':
        price = 1.10
    elif product == 'sweets':
        price = 1.35
    elif product == 'peanuts':
        price = 1.55

final_price = price * quantity
print(final_price)
