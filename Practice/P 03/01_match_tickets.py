VIP = 499.99
Normal = 249.99
transport_fees = 0
total_fees = 0
money_left = 0

budget = float(input())
type_of_pass = input()
number_of_people = int(input())

if number_of_people <= 4:
    transport_fees = budget * 0.75
elif number_of_people <= 9:
    transport_fees = budget * 0.6
elif number_of_people <= 24:
    transport_fees = budget * 0.5
elif number_of_people <= 49:
    transport_fees = budget * 0.4
elif number_of_people > 49:
    transport_fees = budget * 0.25

if type_of_pass == 'VIP':
    total_fees = transport_fees + VIP * number_of_people
    if total_fees <= budget:
        money_left = budget - total_fees
        print(f'Yes! You have {money_left:.2f} leva left.')
    else:
        money_left = total_fees - budget
        print(f'Not enough money! You need {money_left:.2f} leva.')
elif type_of_pass == 'Normal':
    total_fees = transport_fees + Normal * number_of_people
    if total_fees <= budget:
        money_left = budget - total_fees
        print(f'Yes! You have {money_left:.2f} leva left.')
    else:
        money_left = total_fees - budget
        print(f'Not enough money! You need {money_left:.2f} leva.')
