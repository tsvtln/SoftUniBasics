budget = float(input())
season = input()

car_class = ''
car_type = ''
price = 0

if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.65
elif budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.80
elif budget > 500:
    car_class = 'Luxury class'
    car_type = 'Jeep'
    price = budget * 0.90

print(f'{car_class}')
print(f'{car_type} - {price:.2f}')
