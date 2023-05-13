# age = int(input())
# price_washing_machine = float(input())
# toy_price = int(input())
#
# money_saved = 0
# toys_sold = 0
#
# for i in range(2, age + 1, 2):
#     money_saved += i * 10 - (i // 2)
#     toys_sold += (i // 2) * toy_price
#
# money_saved += (age // 2) * toy_price
#
# if money_saved >= price_washing_machine:
#     print(f"Yes! {money_saved - price_washing_machine:.2f}")
# else:
#     print(f"No! {price_washing_machine - money_saved:.2f}")

age = int(input())
price_washing_machine = float(input())
toy_price = int(input())

toys = 0
money_saved = 0
mpy = 10

for i in range(1, age + 1):
    if i % 2 == 0:
        money_saved += mpy - 1
        mpy += 10
    else:
        toys += 1

toys_profit = toys * toy_price
total_profit = toys_profit + money_saved

if total_profit >= price_washing_machine:
    print(f'Yes! {total_profit - price_washing_machine:.2f}')
else:
    print(f'No! {price_washing_machine - total_profit:.2f}')