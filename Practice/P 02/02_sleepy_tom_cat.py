norm = 30000
work_owner = 63
weekend_owner = 127

weekend_days = int(input())

work_days = 365 - weekend_days

# Реалното време за игра е 24 275 минути (345 * 63 + 20 *127).
# Разликата от нормата е 5 725 минути (30 000 – 24 275 = 5 725) или 95 часа и 25 минути.

total_play_time = (work_days * work_owner) + (weekend_days * weekend_owner)

if total_play_time > norm:
    dif = total_play_time - norm
    print('Tom will run away')
    H = dif // 60
    M = dif % 60
    print(f'{H} hours and {M} minutes more for play')
elif total_play_time <= norm:
    print('Tom sleeps well')
    dif = norm - total_play_time
    H = dif // 60
    M = dif % 60
    print(f'{H} hours and {M} minutes less for play')
