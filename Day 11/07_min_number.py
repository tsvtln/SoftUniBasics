from sys import maxsize
max_size = maxsize
while True:
    com = input()
    if com == 'Stop':
        break
    elif com != 'Stop':
        num = int(com)
        if max_size > num:
            max_size = num

print(max_size)
