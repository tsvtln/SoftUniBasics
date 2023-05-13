from sys import maxsize
max_size = -maxsize
sum = 0

numbers = int(input())

for _ in range(numbers):
    current_number = int(input())
    if current_number > max_size:
        max_size = current_number
    sum += current_number

sum_of_rest = abs(sum - max_size)

if sum_of_rest == max_size:
    print(f'Yes ')
    print(f'Sum = {max_size}')
else:
    print('No')
    print(f'Diff = {abs(sum_of_rest - max_size)}')
