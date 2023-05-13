hour = int(input())
minutes = int(input())

summary = hour * 60 + minutes + 15
minutes_2 = summary % 60
hours_2 = summary // 60

if minutes_2 < 10 and hours_2 == 24:
    print(f'{hours_2 * 0}:0{minutes_2}')
elif minutes_2 < 10:
    print(f'{hours_2}:0{minutes_2}')
elif minutes_2 > 10 and hours_2 == 24:
    print(f'{hours_2 * 0}:{minutes_2}')
elif minutes_2 > 10:
    print(f'{hours_2}:{minutes_2}')
else:
    print(f'{hours_2}:{minutes_2}')
