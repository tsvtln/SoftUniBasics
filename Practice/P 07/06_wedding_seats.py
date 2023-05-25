last_sector = input()
A_rows = int(input())
seats_odd = int(input())
taken_seats = 0

# convert to numbers
last_sector = ord(last_sector)
sector_A = 65
seats = 97
last_seat = 96 + seats_odd

for seats_one in range(sector_A, last_sector + 1):
    for row in range(1, A_rows + 1):
        if row % 2 == 0:
            for seats_two in range(seats, last_seat + 3):
                print(f'{chr(seats_one)}{row}{chr(seats_two)}')
                taken_seats += 1
        else:
            for seats_two_t in range(seats, last_seat + 1):
                print(f'{chr(seats_one)}{row}{chr(seats_two_t)}')
                taken_seats += 1
    A_rows += 1
print(taken_seats)

