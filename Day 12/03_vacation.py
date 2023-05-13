mn = float(input())  # needed money for excursion
mo = float(input())  # money owned

days_spent = 0
days_count = 0

while not days_spent == 5:
    sposv = input()  # spend or save
    msposv = float(input())  # money spent or saved
    if sposv == 'spend':
        mo -= msposv
        days_spent += 1
        days_count += 1
        if mo < 0:
            mo = 0
    elif sposv == 'save':
        days_spent = 0
        days_count += 1
        mo += msposv
    if mo >= mn:
        print(f"You saved the money for {days_count} days.")
        break
if days_spent == 5:
    print(f"You can't save the money.\n{days_count}")