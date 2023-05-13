total = 0
while True:
    try:
        input_str = input()
        if input_str == str:
            continue
        increase = float(input_str)
        total += increase
        if increase < 0:
            total -= increase
            print('Invalid operation!')
            print(f'Total: {total:.2f}')
            break
        else:
            print(f'Increase: {increase:.2f}')
            continue
    except ValueError:
        if input_str == 'NoMoreMoney':
            print(f'Total: {total:.2f}')
            break




