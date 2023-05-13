exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
is_on_time = ''

# convert to minutes
exam_hour_to_min = exam_hour * 60
exam_total_minutes = exam_hour_to_min + exam_minutes

arrival_hour_to_min = arrival_hour * 60
arrival_total_minutes = arrival_hour_to_min + arrival_minutes

# calculate minutes left
minutes_left = exam_total_minutes - arrival_total_minutes

# Late, On time, Early
if arrival_total_minutes == exam_total_minutes:
    is_on_time = 'On time'
    print(f'{is_on_time}')
# elif (exam_hour and exam_minutes) == (arrival_hour and arrival_minutes):
#     is_on_time = 'on time'
#     print(f'{is_on_time}')
elif 0 < minutes_left <= 30:
    is_on_time = 'On time'
    print(f'{is_on_time}')
    print(f'{minutes_left} minutes before the start')
    # if minutes_left > 60:
        # time = minutes_left * 60
        # hour = time // 60
        # minutes = time % 60
        # print('')

elif minutes_left > 30 and not arrival_total_minutes > exam_total_minutes:
    is_on_time = 'Early'
    time = exam_total_minutes - arrival_total_minutes
    hour = time // 60
    minutes = time % 60
    print(f'{is_on_time}')
    if minutes < 10 and hour != 0:
        print(f'{hour}:0{minutes} hours before the start')
    elif hour != 0 and minutes >= 10:
        print(f'{hour}:{minutes} hours before the start')
    elif minutes < 10 and hour == 0:
        print(f'{minutes} minutes before the start')
    elif minutes >= 10 and hour == 0:
        print(f'{minutes} minutes before the start')
    # elif minutes < 10 and hour == 0:
    #     print(f'{hour}:{minutes} hours before the start')

elif arrival_total_minutes > exam_total_minutes:
    is_on_time = 'Late'
    time = arrival_total_minutes - exam_total_minutes
    hour = time // 60
    minutes = time % 60
    print(f'{is_on_time}')
    # print(f'{abs(time)} minutes after the start')
    if minutes < 10 and hour != 0:
        print(f'{hour}:0{minutes} hours after the start')
    elif hour != 0 and minutes >= 10:
        print(f'{hour}:{minutes} hours after the start')
    elif minutes < 10 and hour == 0:
        print(f'{minutes} minutes after the start')
    elif minutes >= 10 and hour == 0:
        print(f'{minutes} minutes after the start')
