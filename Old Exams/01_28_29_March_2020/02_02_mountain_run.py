def speed_climbing(record, distance, time_per_meter):
    time_required = (time_per_meter * distance) + (distance // 50 * 30)
    if time_required < record:
        result = f'Yes! The new record is {time_required:.2f} seconds.'
    else:
        result = f'No! He was {time_required - record:.2f} seconds slower.'
    return result


record_entry = float(input())
distance_entry = float(input())
tpm_entry = float(input())
print(speed_climbing(record_entry, distance_entry, tpm_entry))
