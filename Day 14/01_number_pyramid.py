num = int(input())
current = 1
inbtc = False

for f in range(1, num + 1):
    for z in range(1, f + 1):
        if current > num:
            inbtc = True
            break
        print(current, end=' ')
        current += 1
    if inbtc:
        break
    print()