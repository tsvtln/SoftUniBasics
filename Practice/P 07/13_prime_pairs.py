fp, sp, diff_fp, diff_sp = int(input()), int(input()), int(input()), int(input())

for a in range(fp, fp + diff_fp + 1):
    for b in range(sp, sp + diff_sp + 1):
        PRIME_ONE, PRIME_TWO = True, True
        for c in range(2, a):
            if a % c == 0:
                PRIME_ONE = False
                break
        for d in range(2, b):
            if b % d == 0:
                PRIME_TWO = False
                break
        if PRIME_ONE and PRIME_TWO:
            print(f"{a}{b}")
