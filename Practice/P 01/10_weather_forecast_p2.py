temp = float(input())

if 26 <= temp <= 35:
    print("Hot")
elif 20.1 <= temp <= 25.9:
    print("Warm")
elif 15 <= temp <= 20:
    print('Mild')
elif 12 <= temp <= 14.9:
    print('Cool')
elif 5 <= temp <= 11.9:
    print('Cold')
else:
    print('unknown')
    