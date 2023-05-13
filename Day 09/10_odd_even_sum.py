number = int(input())
odd = 0
even = 0

for n in range(number):
    dynamic = int(input())

    if n % 2 == 0:
        even += dynamic
    else:
        odd += dynamic


if even == odd:
    print('Yes')
    print(f'Sum = {even}')
else:
    total = abs(odd - even)
    print(f'No')
    print(f'Diff = {total}')
