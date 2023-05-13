from math import ceil, floor
days_gone = int(input())
food_left = int(input())
dog_fpd = float(input())
cat_fpd = float(input())
turtle_fpd_grams = float(input())

turtle_fpd = turtle_fpd_grams / 1000

total_food_consumed = (dog_fpd * days_gone) + (cat_fpd * days_gone) + (turtle_fpd * days_gone)

if total_food_consumed >= food_left:
    dif = total_food_consumed - food_left
    print(f'{ceil(dif)} more kilos of food are needed.')
else:
    dif = food_left - total_food_consumed
    print(f'{floor(dif)} kilos of food left.')
