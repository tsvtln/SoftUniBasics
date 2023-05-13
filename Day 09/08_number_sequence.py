from sys import maxsize
number = int(input())
max_size = -maxsize
min_size = maxsize

for _ in range(number):
    dynamic = int(input())

    if dynamic > max_size:
        max_size = dynamic
    if dynamic < min_size:
        min_size = dynamic

print(f'Max number: {max_size}')
print(f'Min number: {min_size}')

