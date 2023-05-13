movie_type = input()
rows = int(input())
collums = int(input())

if movie_type == 'Premiere':
    price = rows * collums * 12
    print(f'{price:.2f} leva')
elif movie_type == 'Normal':
    price = rows * collums * 7.50
    print(f'{price:.2f} leva')
elif movie_type == 'Discount':
    price = rows * collums * 5
    print(f'{price:.2f} leva')
else:
    (print('error'))
