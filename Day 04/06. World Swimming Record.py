record_in_sec = float(input())
distance = float(input())
time_to_swim = float(input())

slower = (distance // 15) * 12.5
time_ivan = distance * time_to_swim + slower
# final_time = time_ivan - record_in_sec

if time_ivan < record_in_sec:
    print(f'Yes, he succeeded! The new world record is {time_ivan:.2f} seconds.')
else:
    final_time = time_ivan - record_in_sec
    print(f'No, he failed! He was {final_time:.2f} seconds slower.')
