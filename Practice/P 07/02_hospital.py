doctors = 7
untreated_patients = 0
treated_patients = 0
period = int(input())
for check_ins in range(1, period + 1):
    number_of_patients = int(input())
    if check_ins % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    # doctors_temp = doctors
    # while doctors_temp > 0 and number_of_patients > 0:
    #     number_of_patients -= 1
    #     treated_patients += 1
    #     doctors_temp -= 1
    if number_of_patients <= doctors:
        treated_patients += number_of_patients
    else:
        treated_patients += doctors
        untreated_patients += number_of_patients - doctors
print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
