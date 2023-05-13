budget = int(input())
season = input()
people = int(input())
# Spring", "Summer", "Autumn" или "Winter"
rent = 0
discount = 0
final_price = 0
final_price2 = 0
discount_2 = 0

if season == 'Spring':
    rent += 3000
    if people <= 6:
        discount = 0.10
        # if people % 2 == 0:
        #     discount_2 += 0.05
    elif 7 <= people <= 11:
        discount = 0.15
        # if people % 2 == 0:
        #     discount_2 += 0.05
    elif people >= 12:
        discount = 0.25
        # if people % 2 == 0:
        #     discount_2 += 0.05
elif season == 'Summer' or season == 'Autumn':
    rent += 4200
    if people <= 6:
        discount = 0.10
        # if people % 2 == 0 and not season == 'Autumn':
        #     discount_2 += 0.05
    elif 7 <= people <= 11:
        discount = 0.15
        # if people % 2 == 0 and not season == 'Autumn':
        #     discount_2 += 0.05
    elif people >= 12:
        discount = 0.25
        # if people % 2 == 0 and not season == 'Autumn':
        #     discount_2 += 0.05
elif season == 'Winter':
    rent += 2600
    if people <= 6:
        discount = 0.10
        # if people % 2 == 0:
        #     discount_2 += 0.05
    elif 7 <= people <= 11:
        discount = 0.15
        # if people % 2 == 0:
        #     discount_2 += 0.05
    elif people >= 12:
        discount = 0.25
        # if people % 2 == 0:
        #     discount_2 += 0.05

if people % 2 == 0 and not season == 'Autumn':
    discount_2 = 0.05
    final_price = rent - (rent * discount)
    final_price2 = final_price - (final_price * discount_2)
    money_left = budget - final_price2
else:
    final_price = rent - (rent * discount)
    final_price2 = final_price
    money_left = budget - final_price2


if budget >= final_price2:
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(money_left):.2f} leva.')