budget = float(input())
season = input()
destination = ''
location = ''
spent = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        spent += budget * 0.3
        location = 'Camp'
    elif season == 'winter':
        spent += budget * 0.7
        location = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        spent += budget * 0.4
        location = 'Camp'
    elif season == 'winter':
        spent += budget * 0.8
        location = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    location = 'Hotel'
    spent += budget * 0.9
print(f'Somewhere in {destination}')
print(f'{location} - {spent:.2f}')
