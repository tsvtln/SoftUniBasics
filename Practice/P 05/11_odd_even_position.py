from sys import maxsize
entries = int(input())

odd_sum = 0
odd_min = maxsize
odd_max = -maxsize
even_sum = 0
even_min = maxsize
even_max = -maxsize

for numbers in range(1, entries + 1):
    if numbers % 2 == 0:
        even_entry = float(input())
        even_sum += even_entry
        if even_max < even_entry:
            even_max = even_entry
        if even_min > even_entry:
            even_min = even_entry
    else:
        odd_entry = float(input())
        odd_sum += odd_entry
        if odd_max < odd_entry:
            odd_max = odd_entry
        if odd_min > odd_entry:
            odd_min = odd_entry

# print(f'OddSum={odd_sum:.2f}, OddMin={odd_min:.2f}, OddMax={odd_max:.2f}, EvenSum={even_sum:.2f}, '
#       f'EvenMin={even_min:.2f}, EvenMax={even_max:.2f}')

print(f'OddSum={odd_sum:.2f},')
if entries == 0:
    print(f'OddMin=No,')
else:
    print(f'OddMin={odd_min:.2f},')

if entries == 0:
    print(f'OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},')

print(f'EvenSum={even_sum:.2f},')

if entries == 0 or entries == 1:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={even_min:.2f},')


if entries == 1 or entries == 0:
    print(f'EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')
