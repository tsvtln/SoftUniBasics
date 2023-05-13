num_jury = int(input())
FINISHED = False
grade_sum = 0
final_grade = 0
total_tasks = 0
grade_cur_task = 0
total_grade = 0


while not FINISHED:
    task_name = input()
    if task_name == 'Finish':
        FINISHED = True
        continue
    for i in range(num_jury):
        grade = float(input())
        grade_sum += grade
        total_tasks += 1
        total_grade += grade
    grade_cur_task = grade_sum / num_jury
    # total_grade += grade_cur_task
    print(f"{task_name} - {grade_cur_task:.2f}.")
    grade_sum = 0

final_grade = total_grade / total_tasks
print(f"Student's final assessment is {final_grade:.2f}.")
