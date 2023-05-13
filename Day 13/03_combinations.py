n = int(input())
combos = 0
flag = False

for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            if x1 + x2 + x3 == n:
                # flag = True
                # break
                combos += 1
print(combos)
