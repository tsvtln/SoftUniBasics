dog_food = 2.50
cat_food = 4
dog_pack = int(input())
cat_pack = int(input())

price_dog = dog_food * dog_pack
price_cat = cat_pack * cat_food
price = price_cat + price_dog

print(f"{price} lv.")
