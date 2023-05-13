cake_wight = int(input())
cake_length = int(input())

cake_sum = cake_wight * cake_length

while True:
    piece_size = input()
    if piece_size == 'STOP':
        print(f'{cake_sum} pieces are left.')
        break
    if piece_size != 'STOP':
        piece_size = int(piece_size)
    cake_sum -= piece_size
    if cake_sum < 0:
        print(f'No more cake left! You need {abs(cake_sum)} pieces more.')
        break

