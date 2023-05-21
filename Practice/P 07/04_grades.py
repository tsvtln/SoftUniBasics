number_of_students = int(input())

# for average grade
grade_2_to_299 = 0
grade_3_to_399 = 0
grade_4_to_499 = 0
grade_5_or_above = 0

# for number of grades
number_of_2 = 0
number_of_3 = 0
number_of_4 = 0
number_of_5 = 0

for grades in range(number_of_students):
    grade_of_student = float(input())
    if grade_of_student <= 2.99:
        grade_2_to_299 += grade_of_student
        number_of_2 += 1
    elif grade_of_student <= 3.99:
        grade_3_to_399 += grade_of_student
        number_of_3 += 1
    elif grade_of_student <= 4.99:
        grade_4_to_499 += grade_of_student
        number_of_4 += 1
    else:
        grade_5_or_above += grade_of_student
        number_of_5 += 1

# calculation of percentages
top_students = number_of_5 / number_of_students * 100
between_4_and_499 = number_of_4 / number_of_students * 100
between_3_and_399 = number_of_3 / number_of_students * 100
fail = number_of_2 / number_of_students * 100
average_grade = (grade_2_to_299 + grade_3_to_399 + grade_4_to_499 + grade_5_or_above) / number_of_students

# prints
print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_499:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_399:.2f}%")
print(f"Fail: {fail:.2f}%")
print(f"Average: {average_grade:.2f}")
