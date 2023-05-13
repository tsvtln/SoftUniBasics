detergent = int(input()) * 750
wash_count, used_detergent, total_plates, total_pans = 0, 0, 0, 0

END = False

while not END:
    number_of_dishes = input()
    wash_count += 1
    if number_of_dishes != 'End':
        number_of_dishes = int(number_of_dishes)
        if wash_count % 3 == 0:
            used_detergent = number_of_dishes * 15
            detergent -= used_detergent
            total_pans += number_of_dishes
        else:
            used_detergent = number_of_dishes * 5
            detergent -= used_detergent
            total_plates += number_of_dishes
    if detergent < 0 or number_of_dishes == 'End':
        END = True

if detergent >= 0:
    print(f"Detergent was enough!\n{total_plates} dishes and {total_pans} pots were "
          f"washed.\nLeftover detergent {detergent} ml.")
else:
    print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')
