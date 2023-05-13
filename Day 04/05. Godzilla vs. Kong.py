budget = float(input())
statists = int(input())
price_clothing = float(input())

decor = budget * 0.10
if statists > 150:
    price_clothing -= price_clothing * 0.10
clothing = statists * price_clothing
sum_resources = clothing + decor

if budget < sum_resources:
    print("Not enough money!")
    print(f'Wingard needs {sum_resources - budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget - sum_resources:.2f} leva left.')
