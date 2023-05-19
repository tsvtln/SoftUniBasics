numbers = int(input())
cicles = 0
sum_of_digits = 0
for i in range(numbers):
    digit = int(input())
    cicles += 1
    sum_of_digits += digit
print(f'{sum_of_digits / cicles:.2f}')
