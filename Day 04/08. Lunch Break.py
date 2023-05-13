from math import ceil
name_serial = input()
episod_time = int(input())
rest_time = int(input())

time_to_eat = rest_time / 8
time_to_rest = rest_time / 4

time_left_to_watch = rest_time - time_to_eat - time_to_rest

if time_left_to_watch >= episod_time:
    print(f'You have enough time to watch {name_serial} and left with {ceil(time_left_to_watch - episod_time)} '
          f'minutes free time.')
else:
    print(f"You don't have enough time to watch {name_serial}, you need {ceil(episod_time - time_left_to_watch)} "
          f"more minutes.")
