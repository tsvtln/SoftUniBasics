# inputs
price_vac = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

# prices
puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2
final_price = 0

total_count = number_trucks + number_minions + number_bears + number_dolls + number_puzzles
# final_price += (number_puzzles * puzzle) + (number_minions * minion) + (number_bears * bear) + (number_dolls * doll) +\
#                (number_trucks * truck)
final_price = number_puzzles * 2.60 + number_minions * 8.20 + number_bears * 4.10 + number_dolls * 3 + number_trucks * 2

if total_count >= 50:
    final_price -= 0.25 * final_price

# naem = 0.10 * final_price

final_price -= 0.10 * final_price
# money_left = final_price - price_vac

if price_vac <= final_price:
    money_left = final_price - price_vac
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_left = price_vac - final_price
    print(f'Not enough money! {money_left:.2f} lv needed.')
