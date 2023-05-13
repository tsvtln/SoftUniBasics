fruit = str(input())
dow = str(input())
quantity = float(input())
price = 0

if dow == 'Monday' or dow == 'Tuesday' or dow == 'Wednesday' or dow == 'Thursday' or dow == 'Friday':
    if fruit == 'banana':
        price = quantity * 2.50
        print(f'{price:.2f}')
    elif fruit == 'apple':
        price = quantity * 1.20
        print(f'{price:.2f}')
    elif fruit == 'orange':
        price = quantity * 0.85
        print(f'{price:.2f}')
    elif fruit == 'grapefruit':
        price = quantity * 1.45
        print(f'{price:.2f}')
    elif fruit == 'kiwi':
        price = quantity * 2.70
        print(f'{price:.2f}')
    elif fruit == 'pineapple':
        price = quantity * 5.50
        print(f'{price:.2f}')
    elif fruit == 'grapes':
        price = quantity * 3.85
        print(f'{price:.2f}')
    else:
        print('error')
    # final_price = quantity * price
    # print(f'{final_price:.2f}')
    # else:
    # print('error')

elif dow == 'Saturday' or dow == 'Sunday':
    if fruit == 'banana':
        price = quantity * 2.70
        print(f'{price:.2f}')
    elif fruit == 'apple':
        price = quantity * 1.25
        print(f'{price:.2f}')
    elif fruit == 'orange':
        price = quantity * 0.90
        print(f'{price:.2f}')
    elif fruit == 'grapefruit':
        price = quantity * 1.60
        print(f'{price:.2f}')
    elif fruit == 'kiwi':
        price = quantity * 3.00
        print(f'{price:.2f}')
    elif fruit == 'pineapple':
        price = quantity * 5.60
        print(f'{price:.2f}')
    elif fruit == 'grapes':
        price = quantity * 4.20
        print(f'{price:.2f}')
    else:
        print('error')

# elif not fruit == 'banana' or fruit == 'apple' or fruit == 'orange' or fruit == 'grapefruit' \
#          or fruit == 'kiwi' or fruit == 'pineapple' or fruit == 'grapes':
#      print('error')
#
# final_price = quantity * price
# print(f'{final_price:.2f}')

# else:
# #     print('error')
# final_price = quantity * price
# print(f'{final_price:.2f}')
else:
    print('error')
    