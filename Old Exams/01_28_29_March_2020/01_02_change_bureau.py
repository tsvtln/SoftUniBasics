def change_bureau(bitcoins: float, juans: float, comission: float) -> float:
    leva = bitcoins * 1168
    dollars = juans * 0.15
    leva += dollars * 1.76
    euro = leva / 1.95
    euro -= euro * (comission / 100)
    return euro


bitcoins_entry = float(input())
juans_entry = float(input())
comission_entry = float(input())
print(f'{change_bureau(bitcoins_entry, juans_entry, comission_entry):.2f}')
