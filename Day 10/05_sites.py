facebook_fine = 150
instagram_fine = 100
reddit_fine = 50

number_tabs = int(input())
salary = int(input())

fine = 0

for _ in range(number_tabs):
    tab_name = input()
    if tab_name == 'Facebook':
        fine += facebook_fine
    elif tab_name == 'Instagram':
        fine += instagram_fine
    elif tab_name == 'Reddit':
        fine += reddit_fine
    if salary <= fine:
        print('You have lost your salary.')
        break
if salary > fine:
    print(f'{salary - fine}')