# while True:
#     text = input()
#     if text == 'Stop':
#         break
#     else:
#         print(text)

text = input()
is_false = True
while is_false:
    if text == 'Stop':
        is_false = False
        break
    print(text)
    text = input()


