euro = 1.94
veg_prc = float(input())
fruit_prc = float(input())
total_weight_veg = float(input())
total_weight_fruit = float(input())

# price = ((veg_prc * fruit_prc) / euro) + (((fruit_prc * total_weight_fruit) / euro))
total_price_stuff = (veg_prc * total_weight_veg) + (fruit_prc * total_weight_fruit)
price = total_price_stuff / euro
print("%0.2f" % price)
