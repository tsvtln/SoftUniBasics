budget = float(input())
number_vc = int(input())
number_processors = int(input())
number_ram = int(input())

price_vc = 250
price_processor = (number_vc * price_vc) * 0.35
price_ram = (number_vc * price_vc) * 0.10

price_calc = (price_vc * number_vc) + (price_processor * number_processors) + (price_ram * number_ram)

if number_vc > number_processors:
    price_calc -= price_calc * 0.15

if budget >= price_calc:
    print(f'You have {budget - price_calc:.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(budget - price_calc):.2f} leva more!')