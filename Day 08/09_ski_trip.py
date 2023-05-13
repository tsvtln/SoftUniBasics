# rooms prices
room_for_one_person = 18
apartment = 25
president_apartment = 35

# vars
room_price = 0
stay = int(input())
nights = stay - 1
room_type = input()
score = str(input())
final_price = 0

if stay < 10:
    if room_type == 'room for one person':
        final_price = nights * room_for_one_person
    elif room_type == 'apartment':
        final_price = nights * apartment
        final_price -= final_price * 0.3
    elif room_type == 'president apartment':
        final_price = nights * president_apartment
        final_price -= final_price * 0.1

elif 10 <= stay <= 15:
    if room_type == 'room for one person':
        final_price = nights * room_for_one_person
    elif room_type == 'apartment':
        final_price = nights * apartment
        final_price -= final_price * 0.35
    elif room_type == 'president apartment':
        final_price = nights * president_apartment
        final_price -= final_price * 0.15
elif stay > 15:
    if room_type == 'room for one person':
        final_price = nights * room_for_one_person
    elif room_type == 'apartment':
        final_price = nights * apartment
        final_price -= final_price * 0.5
    elif room_type == 'president apartment':
        final_price = nights * president_apartment
        final_price -= final_price * 0.2

if score == 'positive':
    final_price += final_price * 0.25
elif score == 'negative':
    final_price -= final_price * 0.1

print(f'{final_price:.2f}')

