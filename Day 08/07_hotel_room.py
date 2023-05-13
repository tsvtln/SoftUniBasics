month = (input())
stay = int(input())
studio_price = 0
apartment_price = 0
discount = 0
discount_apt = 0

if month == 'May' or month == 'October':
    studio_price += 50
    apartment_price += 65
    if 7 < stay < 14:
        discount += 0.05
        studio_price -= studio_price * discount
    elif stay > 14:
        discount += 0.3
        studio_price -= studio_price * discount
        apartment_price -= apartment_price * 0.1

elif month == 'June' or month == 'September':
    studio_price += 75.20
    apartment_price += 68.70
    if stay > 14:
        discount += 0.2
        studio_price -= studio_price * discount
        apartment_price -= apartment_price * 0.1

elif month == 'August' or month == 'July':
    studio_price += 76
    apartment_price += 77
    if stay > 14:
        apartment_price -= apartment_price * 0.1

# if (month == 'May' or month == 'October') and (14 > stay > 7):
#     discount += 0.05
# elif (month == 'May' or month == 'October') and (stay > 14):
#     discount += 0.3
# elif (month == 'June' or month == 'September') and (14 > stay):
#     discount += 0.2
# if 14 > stay:
#     discount_apt += 10

apt_price = stay * apartment_price
print(f"Apartment: {apt_price:.2f} lv.")
std_price = stay * studio_price
print(f"Studio: {std_price:.2f} lv.")
