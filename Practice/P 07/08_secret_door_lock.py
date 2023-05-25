fn = int(input())
sn = int(input())
tn = int(input())
IS_PRIME = True

for one in range(2, fn + 1, 2):
    for two in range(2, sn + 1):
        for three in range(2, tn + 1, 2):
            for i in range(2, two + 1):
                if two % i == 0 and two != 2 or two == 9 or two == 8:
                    IS_PRIME = False
                if IS_PRIME:
                    print(f"{one} {two} {three}")
                    break
        IS_PRIME = True
