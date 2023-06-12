def energy_gels(fruit: str, size: str, amount: int):
    prices = {
        'small': {
            'Watermelon': 112,
            'Mango': 73.32,
            'Pineapple': 84.2,
            'Raspberry': 40
        },
        'big': {
            'Watermelon': 143.5,
            'Mango': 98,
            'Pineapple': 124,
            'Raspberry': 76
        }
    }

    fruit_prices = prices.get(size)
    price_per_unit = fruit_prices.get(fruit)
    price = price_per_unit * amount

    if 400 <= price <= 1000:
        price -= price * 0.15
    elif price > 1000:
        price /= 2

    return f'{price:.2f} lv.'


fruit_entry, size_entry, amount_entry = input(), input(), int(input())
print(energy_gels(fruit_entry, size_entry, amount_entry))
