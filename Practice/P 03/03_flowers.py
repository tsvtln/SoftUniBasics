hrisantemas = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

hrisantemas_prz_summer_spring = 2
roses_prz_summer_spring = 4.10
tulips_prz_summer_spring = 2.50

hrisantemas_prz_winter_autumn = 3.75
roses_prz_winter_autumn = 4.50
tulips_prz_winter_autumn = 4.15

flowers_price = 0
taof = roses + tulips + hrisantemas  # total amount of flwrs

if holiday == 'Y':
    # if season == 'Summer' or season == 'Spring':
    #     hrisantemas_prz_summer_spring += hrisantemas_prz_summer_spring * 0.15
    #     roses_prz_summer_spring += roses_prz_summer_spring * 0.15
    #     tulips_prz_summer_spring += tulips_prz_summer_spring * 0.15
    # elif season == 'Winter' or season == 'Autumn':
    #     hrisantemas_prz_winter_autumn += hrisantemas_prz_winter_autumn * 0.15
    #     roses_prz_winter_autumn += roses_prz_winter_autumn * 0.15
    #     tulips_prz_winter_autumn += tulips_prz_winter_autumn * 0.15
    if season == 'Summer' or season == 'Spring':
        flowers_price = (hrisantemas * hrisantemas_prz_summer_spring) + (roses * roses_prz_summer_spring) \
                        + (tulips * tulips_prz_summer_spring)
    elif season == 'Winter' or season == 'Autumn':
        flowers_price = (hrisantemas * hrisantemas_prz_winter_autumn) + (roses * roses_prz_winter_autumn) \
                        + (tulips * tulips_prz_winter_autumn)
    flowers_price += flowers_price * 0.15
    if tulips >= 7 and season == 'Spring':
        flowers_price -= flowers_price * 0.05
    if roses >= 10 and season == 'Winter':
        flowers_price -= flowers_price * 0.10
    if taof > 20:
        flowers_price -= flowers_price * 0.20

elif holiday == 'N':
    if season == 'Summer' or season == 'Spring':
        flowers_price = (hrisantemas * hrisantemas_prz_summer_spring) + (roses * roses_prz_summer_spring) \
                        + (tulips * tulips_prz_summer_spring)
    elif season == 'Winter' or season == 'Autumn':
        flowers_price = (hrisantemas * hrisantemas_prz_winter_autumn) + (roses * roses_prz_winter_autumn) \
                        + (tulips * tulips_prz_winter_autumn)
    if tulips >= 7 and season == 'Spring':
        flowers_price -= flowers_price * 0.05
    if roses >= 10 and season == 'Winter':
        flowers_price -= flowers_price * 0.10
    if taof > 20:
        flowers_price -= flowers_price * 0.20

flowers_price += 2
print(f'{flowers_price:.2f}')