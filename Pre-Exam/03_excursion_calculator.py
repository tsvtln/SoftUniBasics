number_of_people, season = int(input()), input()
price = 0

if season == 'spring':
    if number_of_people <= 5:
        price = 50 * number_of_people
    elif number_of_people > 5:
        price = 48 * number_of_people
elif season == 'summer':
    if number_of_people <= 5:
        price = 48.50 * number_of_people
    elif number_of_people > 5:
        price = 45 * number_of_people
    price -= price * 0.15
elif season == 'autumn':
    if number_of_people <= 5:
        price = 60 * number_of_people
    elif number_of_people > 5:
        price = 49.50 * number_of_people
elif season == 'winter':
    if number_of_people <= 5:
        price = 86 * number_of_people
    elif number_of_people > 5:
        price = 85 * number_of_people
    price += price * 0.08

print(f'{price:.2f} leva.')
