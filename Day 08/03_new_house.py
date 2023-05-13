# flowers prices
# rose = 5
# dahlia = 3.80
# tulip = 2.80
# narcis = 3
# gladiola = 2.50
Roses = ''
Dahlias = ''
Tulips = ''
Narcissus = ''
Gladiolus = ''
final_price = 0
flower_price = 0

# inputs
flower_type = input()
flower_count = int(input())
budget = int(input())

if flower_type == 'Roses':
    flower_price += 5
elif flower_type == 'Dahlias':
    flower_price += 3.80
elif flower_type == 'Tulips':
    flower_price += 2.80
elif flower_type == 'Narcissus':
    flower_price += 3
elif flower_type == 'Gladiolus':
    flower_price += 2.50

final_price += flower_count * flower_price

if flower_type == 'Roses' and flower_count > 80:
    final_price -= final_price * 0.10
elif flower_type == 'Dahlias' and flower_count > 90:
    final_price -= final_price * 0.15
elif flower_type == 'Tulips' and flower_count > 80:
    final_price -= final_price * 0.15
elif flower_type == 'Narcissus' and flower_count < 120:
    final_price += final_price * 0.15
elif flower_type == 'Gladiolus' and flower_count < 80:
    final_price += final_price * 0.20

money_left = budget - final_price
diff = abs(budget - final_price)
# abs_value = abs(money_left)
# + "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left."
# - "Not enough money, you need {нужната сума} leva more.".

if budget >= final_price:
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {money_left:.2f} leva left.')
elif budget < final_price:
    print(f'Not enough money, you need {diff:.2f} leva more.')
