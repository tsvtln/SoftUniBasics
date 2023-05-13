season = input()
km_per_month = float(input())
ppkm = 0

if km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        ppkm = 0.75
    elif season == 'Summer':
        ppkm = 0.90
    elif season == 'Winter':
        ppkm = 1.05
elif 5000 < km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        ppkm = 0.95
    elif season == 'Summer':
        ppkm = 1.10
    elif season == 'Winter':
        ppkm = 1.25
elif 10000 < km_per_month <= 20000:
    ppkm = 1.45

money_made = (km_per_month * 4) * ppkm
money_made -= money_made * 0.10
print(f'{money_made:.2f}')
