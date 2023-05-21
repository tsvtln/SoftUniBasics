money_inherited = float(input())
year_to_live = int(input())
ivancho_age = 18
current_year = 1800
for years in range(current_year, year_to_live + 1):
    if current_year % 2 == 0:
        money_inherited -= 12000
    else:
        money_inherited -= 12000 + (50 * ivancho_age)
    current_year += 1
    ivancho_age += 1
if money_inherited >= 0:
    print(f"Yes! He will live a carefree life and will have {money_inherited:.2f} dollars left.")
else:
    print(f'He will need {abs(money_inherited):.2f} dollars to survive.')
