def energy_gels(fruit: str, size: str, amount: int):
    if size == 'small':
        watermelon, mango, ananas, raspberry = 112, 73.32, 84.2, 40
    elif size == 'big':
        watermelon, mango, ananas, raspberry = 143.5, 98, 124, 76
    if fruit == 'Watermelon':
        price = watermelon * amount
    elif fruit == 'Mango':
        price = mango * amount
    elif fruit == 'Pineapple':
        price = ananas * amount
    else:
        price = raspberry * amount
    if 400 <= price <= 1000:
        price -= price * 0.15
    elif price > 1000:
        price /= 2
    return f'{price:.2f} lv.'


fruit_entry = input()
size_entry = input()
amount_entry = int(input())
print(energy_gels(fruit_entry, size_entry, amount_entry))
