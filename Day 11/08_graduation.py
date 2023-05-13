name = input()
failed = 0
year = 0
total_grade = 0

while True:
    grade = float(input())
    year += 1
    if grade >= 4:
        total_grade += grade
    elif grade < 4:
        failed += 1
        year -= 1
    if failed == 2:
        print(f'{name} has been excluded at {year + 1} grade')
        break
    if year == 12:
        avg_grade = total_grade / year
        print(f'{name} graduated. Average grade: {avg_grade:.2f}')
        break

