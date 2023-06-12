def card(allowance, gender, age, sport):
    prices = {
        'm': {
            'Gym': 42,
            'Boxing': 41,
            'Yoga': 45,
            'Zumba': 34,
            'Dances': 51,
            'Pilates': 39
        },
        'f': {
            'Gym': 35,
            'Boxing': 37,
            'Yoga': 42,
            'Zumba': 31,
            'Dances': 53,
            'Pilates': 37
        }
    }
    gender_var = prices.get(gender)
    gym_price = gender_var.get(sport)
    if age <= 19:
        gym_price -= gym_price * 0.2
    months = allowance // gym_price
    if months >= 1:
        return f'You purchased a {months:.0f} month pass for {sport}.'
    else:
        return f"You don't have enough money! You need ${gym_price - allowance:.2f} more."


allowance_entry, gender_entry, age_entry, sport_entry = float(input()), input(), int(input()), input()
print(card(allowance_entry, gender_entry, age_entry, sport_entry))
