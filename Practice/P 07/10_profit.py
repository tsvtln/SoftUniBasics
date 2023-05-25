coins_1, coins_2, bill_5, summ = int(input()), int(input()), int(input()), int(input())

for ones in range(coins_1 + 1):
    for twos in range(coins_2 + 1):
        for fives in range(bill_5 + 1):
            if summ == ones + twos * 2 + fives * 5:
                print(f"{ones} * 1 lv. + {twos} * 2 lv. + {fives} * 5 lv. = {summ} lv.")
