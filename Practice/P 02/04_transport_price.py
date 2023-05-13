taxi_day_start = 0.7
taxi_day_pkm = 0.79
taxi_night_pkm = 0.90

bus_night_day = 0.09

train_night_day = 0.06

n = int(input())
don = input()

if n < 20:
    if don == 'day':
        fare = taxi_day_start + (taxi_day_pkm * n)
        print(f'{fare:.2f}')
    elif don == 'night':
        fare = taxi_day_start + (taxi_night_pkm * n)
        print(f'{fare:.2f}')

elif n < 100:
    fare = bus_night_day * n
    print(f'{fare:.2f}')

else:
    fare = train_night_day * n
    print(f'{fare:.2f}')
