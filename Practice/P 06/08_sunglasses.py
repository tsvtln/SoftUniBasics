n = int(input())

# Print the top row of the sunglasses
print('*' * (2 * n) + ' ' * n + '*' * (2 * n))

# Print the middle rows of the sunglasses
for i in range(n - 2):
    if i == (n - 1) // 2 - 1:
        print('*' + '/' * (2 * n - 2) + '*' + '|' * n + '*' + '/' * (2 * n - 2) + '*')
    else:
        print('*' + '/' * (2 * n - 2) + '*' + ' ' * n + '*' + '/' * (2 * n - 2) + '*')

# Print the bottom row of the sunglasses
print('*' * (2 * n) + ' ' * n + '*' * (2 * n))