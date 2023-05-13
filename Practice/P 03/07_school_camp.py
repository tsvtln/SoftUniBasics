season = input()
group_type = input()
num_of_students = int(input())
num_of_days = int(input())

price_per_day = 0
final_price = 0
sport_type = ''

if group_type == 'boys' or group_type == 'girls':
    if season == 'Winter':
        price_per_day = 9.60
    elif season == 'Spring':
        price_per_day = 7.20
    elif season == 'Summer':
        price_per_day = 15
elif group_type == 'mixed':
    if season == 'Winter':
        price_per_day = 10
    elif season == 'Spring':
        price_per_day = 9.50
    elif season == 'Summer':
        price_per_day = 20
final_price = (price_per_day * num_of_students) * num_of_days
if num_of_students >= 50:
    final_price -= final_price * 0.5
elif 50 > num_of_students >= 20:
    final_price -= final_price * 0.15
elif 20 >= num_of_students >= 10:
    final_price -= final_price * 0.05

if group_type == 'girls':
    if season == 'Winter':
        sport_type = 'Gymnastics'
    elif season == 'Spring':
        sport_type = 'Athletics'
    elif season == 'Summer':
        sport_type = 'Volleyball'
elif group_type == 'boys':
    if season == 'Winter':
        sport_type = 'Judo'
    elif season == 'Spring':
        sport_type = 'Tennis'
    elif season == 'Summer':
        sport_type = 'Football'
elif group_type == 'mixed':
    if season == 'Winter':
        sport_type = 'Ski'
    elif season == 'Spring':
        sport_type = 'Cycling'
    elif season == 'Summer':
        sport_type = 'Swimming'

print(f'{sport_type} {final_price:.2f} lv.')
