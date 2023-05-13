numbers = int(input())
left = 0
right = 0

for _ in range(1, numbers + 1):
    left += int(input())
for _ in range(1, numbers +1):
    right += int(input())

if left == right:
    print(f'Yes, sum = {left}')
else:
    print(f'No, diff = {abs(left - right)}')
