degrees = int(input())
time = input()

if 10 <= degrees <= 18 and time == 'Morning':
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif 10 <= degrees <= 18 and time == 'Afternoon':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif 10 <= degrees <= 18 and time == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif 18 < degrees <= 24 and time == 'Morning':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif 18 < degrees <= 24 and time == 'Afternoon':
    outfit = 'T-Shirt'
    shoes = 'Sandals'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif 18 < degrees <= 24 and time == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif degrees >= 25 and time == 'Morning':
    outfit = 'T-Shirt'
    shoes = 'Sandals'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif degrees >= 25 and time == 'Afternoon':
    outfit = 'Swim Suit'
    shoes = 'Barefoot'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif degrees >= 25 and time == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'
    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
