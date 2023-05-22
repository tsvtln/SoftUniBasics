previous_summ = 0
summ = 0
diff = 0
HAS_DIFFERENCE = False
entries = int(input())

for numbers in range(entries):
    num_one = int(input())
    num_two = int(input())
    summ = num_one + num_two

    if summ != previous_summ and numbers != 0:
        diff = abs(summ-previous_summ)
        HAS_DIFFERENCE = True

    if numbers == 0:
        diff = summ

    previous_summ = summ

if HAS_DIFFERENCE:
    print(f"No, maxdiff={diff}")
else:
    print(f"Yes, value={diff}")


