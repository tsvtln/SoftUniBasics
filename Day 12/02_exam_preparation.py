number_of_bad_grades = int(input())
last_name = ''
problems = 0
sum_of_grades = 0
sum_of_bad_grades = 0

while True:
    name = input()
    if name == 'Enough':
        print(f'Average score: {sum_of_grades / problems:.2f}\nNumber of problems: '
              f'{problems}\nLast problem: {last_name}')
        break
    last_name = name
    problems += 1
    grade = int(input())
    if grade <= 4:
        sum_of_bad_grades += 1
        sum_of_grades += grade
        if sum_of_bad_grades == number_of_bad_grades:
            print(f'You need a break, {number_of_bad_grades} poor grades.')
            break
    elif grade > 4:
        sum_of_grades += grade
