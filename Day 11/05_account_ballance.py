# total = 0
# while True:
#     try:
#         increase = float(input())
#         total += increase
#         print(f'Increase: {increase:.2f}')
#     except ValueError:
#         pass
#     text = input()
#     if text == 'NoMoreMoney':
#         print(f'Total: {total:.2f}')
#         break
# total = 0
# increase = ''
# while increase != 'NoMoreMoney':
#     increase = float(input())
#     total += increase
#     print(f'Increase: {increase:.2f}')
# else:
#     print(f'Total: {total:.2f}')

total = 0
while True:
    com = input()
    if com == 'NoMoreMoney':
        break
    else:
        money = float(com)
        if money < 0:
            print('Invalid operation!')
            break
        else:
            total += money
            print(f'Increase: {money:.2f}')

print(f'Total: {total:.2f}')
