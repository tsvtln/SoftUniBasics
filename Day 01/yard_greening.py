size_price = 7.61

size_input = float(input())
price = size_input * size_price
discount = price * 0.18
final_price = price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
