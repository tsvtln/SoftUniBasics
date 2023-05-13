FINISHED = False
END = False
seats_taken, total_seats_taken, student_seats, standard_seats, kid_seats, free_seats = 0, 0, 0, 0, 0, 0

while not FINISHED:
    movie_name = input()
    if movie_name == 'Finish':
        FINISHED = True
        continue
    free_seats = int(input())
    while not END:
        ticket_type = input()
        if ticket_type == 'End':
            END = True
            continue
        seats_taken += 1
        total_seats_taken += 1
        if ticket_type == 'student':
            student_seats += 1
        elif ticket_type == 'standard':
            standard_seats += 1
        elif ticket_type == 'kid':
            kid_seats += 1
        if seats_taken >= free_seats:
            END = True

    pct_taken_seats = (seats_taken / free_seats) * 100
    print(f"{movie_name} - {pct_taken_seats:.2f}% full.")
    seats_taken = 0
    END = False

pct_student = (student_seats / total_seats_taken) * 100
pct_standard = (standard_seats / total_seats_taken) * 100
pct_kid = (kid_seats / total_seats_taken) * 100
print(f"Total tickets: {total_seats_taken}")
print(f"{pct_student:.2f}% student tickets.")
print(f"{pct_standard:.2f}% standard tickets.")
print(f"{pct_kid:.2f}% kids tickets.")
