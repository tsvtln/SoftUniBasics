budget = float(input())
season = input()
price = 0
stay = ''
country = ''

if budget <= 1000:
    stay = 'Camp'
    if season == 'Summer':
        country = 'Alaska'
        price += budget - (budget * 0.65)
    elif season == 'Winter':
        country = 'Morocco'
        price += budget - (budget * 0.45)
elif 1000 < budget <= 3000:
    stay = 'Hut'
    if season == 'Summer':
        country = 'Alaska'
        price += budget - (budget * 0.8)
    elif season == 'Winter':
        country = 'Morocco'
        price += budget - (budget * 0.6)
elif budget > 3000:
    stay = 'Hotel'
    if season == 'Summer':
        country = 'Alaska'
        price += budget - (budget * 0.9)
    elif season == 'Winter':
        country = 'Morocco'
        price += budget - (budget * 0.9)
final_price = budget - price
print(f'{country} - {stay} - {final_price:.2f}')
