money_needed = int(input())
END, CARD, ERROR = False, False, False
transaction_num, collected_money, card_payment, card_payment_num, cash_payment, cash_payment_num = 0, 0, 0, 0, 0, 0


while not END:
    price_of_product = input()
    if price_of_product == 'End':
        END = True
        continue

    elif price_of_product != 'End':
        price_of_product = float(price_of_product)
        transaction_num += 1

    if transaction_num % 2 == 0:
        CARD = True
    elif transaction_num % 2 != 0:
        CARD = False

    if price_of_product > 100:
        if not CARD:
            print(f'Error in transaction!')
            ERROR = True
        elif CARD:
            collected_money += price_of_product
            card_payment += price_of_product
            card_payment_num += 1
            ERROR = False
    elif price_of_product < 10:
        if CARD:
            print(f'Error in transaction!')
            ERROR = True
        elif not CARD:
            collected_money += price_of_product
            cash_payment += price_of_product
            cash_payment_num += 1
            ERROR = False
    elif 11 <= price_of_product <= 99:
        collected_money += price_of_product
        if CARD:
            card_payment += price_of_product
            card_payment_num += 1
            ERROR = False
        elif not CARD:
            cash_payment += price_of_product
            cash_payment_num += 1
            ERROR = False

    if collected_money >= money_needed:
        END = True
    if not ERROR:

        print(f'Product sold!')

if collected_money >= money_needed:
    print(f"Average CS: {cash_payment / cash_payment_num:.2f}")
    print(f'Average CC: {card_payment / card_payment_num:.2f}')

if collected_money < money_needed:
    print("Failed to collect required money for charity.")
