young_cyclist = int(input())
old_cyclist = int(input())
track_type = input()
fee = 0
organisation_fee = 0
young_fee = 0
old_fee = 0
total_cyclists = 0

if track_type == 'trail':
    young_fee = 5.50 * young_cyclist
    old_fee = 7 * old_cyclist
    fee = young_fee + old_fee
elif track_type == 'cross-country':
    total_cyclists = old_cyclist + young_cyclist
    old_fee = 9.50 * old_cyclist
    young_fee = 8 * young_cyclist
    fee = old_fee + young_fee
    if total_cyclists >= 50:
        fee -= fee * 0.25
elif track_type == 'downhill':
    young_fee = 12.25 * young_cyclist
    old_fee = 13.75 * old_cyclist
    fee = young_fee + old_fee
elif track_type == 'road':
    young_fee = 20 * young_cyclist
    old_fee = 21.50 * old_cyclist
    fee = young_fee + old_fee
organisation_fee = fee * 0.05
fee -= organisation_fee
print(f'{fee:.2f}')
