petrol = 2.22  # gasoline
diesel = 2.33
gas = 0.93
total_price = 0

# if discount card
petrol_disc = petrol - 0.18
diesel_disc = diesel - 0.12
gas_disc = gas - 0.08

type_of_fuel = input()
fuel_amount = float(input())
club_card = input()

if type_of_fuel == 'Gasoline':
    if club_card == 'Yes':
        total_price = fuel_amount * petrol_disc
        if 20 <= fuel_amount <= 25:
            total_price -= total_price * 0.08
            print(f'{total_price:.2f} lv.')
        elif fuel_amount > 25:
            total_price -= total_price * 0.1
            print(f'{total_price:.2f} lv.')
        else:
            print(f'{total_price:.2f} lv.')

    elif club_card == 'No':
        total_price = fuel_amount * petrol
        if 20 <= fuel_amount <= 25:
            total_price -= total_price * 0.08
            print(f'{total_price:.2f} lv.')
        elif fuel_amount > 25:
            total_price -= total_price * 0.1
            print(f'{total_price:.2f} lv.')
        else:
            print(f'{total_price:.2f} lv.')

elif type_of_fuel == 'Diesel':
    if club_card == 'Yes':
        total_price = fuel_amount * diesel_disc
        if 20 <= fuel_amount <= 25:
            total_price -= total_price * 0.08
            print(f'{total_price:.2f} lv.')
        elif fuel_amount > 25:
            total_price -= total_price * 0.1
            print(f'{total_price:.2f} lv.')
        else:
            print(f'{total_price:.2f} lv.')

    elif club_card == 'No':
        total_price = fuel_amount * diesel
        if 20 <= fuel_amount <= 25:
            total_price -= total_price * 0.08
            print(f'{total_price:.2f} lv.')
        elif fuel_amount > 25:
            total_price -= total_price * 0.1
            print(f'{total_price:.2f} lv.')
        else:
            print(f'{total_price:.2f} lv.')

elif type_of_fuel == 'Gas':
    if club_card == 'Yes':
        total_price = fuel_amount * gas_disc
        if 20 <= fuel_amount <= 25:
            total_price -= total_price * 0.08
            print(f'{total_price:.2f} lv.')
        elif fuel_amount > 25:
            total_price -= total_price * 0.1
            print(f'{total_price:.2f} lv.')
        else:
            print(f'{total_price:.2f} lv.')

    elif club_card == 'No':
        total_price = fuel_amount * gas
        if 20 <= fuel_amount <= 25:
            total_price -= total_price * 0.08
            print(f'{total_price:.2f} lv.')
        elif fuel_amount > 25:
            total_price -= total_price * 0.1
            print(f'{total_price:.2f} lv.')
        else:
            print(f'{total_price:.2f} lv.')
