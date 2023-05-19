from re import sub

NOT_ENDED = True
word = ''
temp_word = ''
CS, OS, NS = False, False, False
while NOT_ENDED:
    symbol = input()
    if symbol == 'End':
        NOT_ENDED = False
        continue
    symbol = sub(r'[^a-zA-Z]', '', symbol)
    if symbol == '':
        continue
    elif symbol != '':
        if symbol == 'c' and CS:
            temp_word += symbol
        elif symbol == 'o' and OS:
            temp_word += symbol
        elif symbol == 'n' and NS:
            temp_word += symbol
        elif symbol != 'n' and symbol != 'o' and symbol != 'c':
            temp_word += symbol

        if symbol == 'c' and not CS:
            CS = True
        elif symbol == 'o' and not OS:
            OS = True
        elif symbol == 'n' and not NS:
            NS = True
        if CS and OS and NS:
            word += f'{temp_word} '
            CS, NS, OS = False, False, False
            temp_word = ''

print(word)
