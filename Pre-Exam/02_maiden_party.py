party = float(input())
sexy = int(input())
rose = int(input())
keychains = int(input())
drawings = int(input())
fortunes = int(input())

summ_count = sexy + rose + drawings + keychains + fortunes

summ_money = fortunes * 22 + drawings * 18.2 + rose * 7.2 + sexy * 0.6 + keychains * 3.6

if summ_count >= 25:
    summ_money -= summ_money * 0.35

summ_money -= summ_money * 0.1

if party <= summ_money:
    print(f"Yes! {summ_money-party:.2f} lv left.")
else:
    print(f"Not enough money! {party-summ_money:.2f} lv needed.")