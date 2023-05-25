a = int(input())
b = int(input())
max_password = int(input())
MAX_REACHED = False

# ASCII
symbol_one = 35  # to 55
symbol_two = 64  # to 96

# symbol_one + symbol_two + x(a) + y (b) + symbol_two + symbol_one

for x in range(1, a + 1):
    for y in range(1, b + 1):
        print(f"{chr(symbol_one)}{chr(symbol_two)}{x}{y}{chr(symbol_two)}{chr(symbol_one)}|", end='')
        symbol_one += 1
        if symbol_one > 55:
            symbol_one = 35
        symbol_two += 1
        if symbol_two > 96:
            symbol_two = 64
        max_password -= 1
        if max_password == 0:
            MAX_REACHED = True
        if MAX_REACHED:
            break
    if MAX_REACHED:
        break
