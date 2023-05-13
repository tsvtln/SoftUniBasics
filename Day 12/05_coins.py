noc = 0  # num of coins
change = float(input())

while change > 0:
    if change >= 2:
        noc += 1
        change -= 2
    elif change >= 1:
        noc += 1
        change -= 1
    elif change >= 0.5:
        noc += 1
        change -= 0.5
    elif change >= 0.2:
        noc += 1
        change -= 0.2
    elif change >= 0.1:
        noc += 1
        change -= 0.1
    elif change >= 0.05:
        noc += 1
        change -= 0.05
    elif change >= 0.02:
        noc += 1
        change -= 0.02
    elif change == 0.01:
        noc += 1
        change -= 0.01
    change = round(change, 2)

print(noc)
