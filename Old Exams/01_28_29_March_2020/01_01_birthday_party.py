def calculate_budget(integer_value: int):
    cake, animator = integer_value * 0.2, integer_value / 3
    drinks = cake - cake * 0.45
    total = integer_value + cake + animator + drinks
    return total


rent = int(input())
print(calculate_budget(rent))
