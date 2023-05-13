students = int(input())
dvoikari = 0
troikari = 0
chetvorki = 0
petici = 0
total_grades = 0


for i in range(1, students+1):
    grade = float(input())
    total_grades += grade

    if 2.0 <= grade <= 2.99:
        dvoikari += 1
    if 3.0 <= grade <= 3.99:
        troikari += 1
    if 4.0 <= grade <= 4.99:
        chetvorki += 1
    if grade >= 5.0:
        petici += 1

print(f"Top students: {(petici/students)*100:.2f}%")
print(f"Between 4.00 and 4.99: {(chetvorki/students)*100:.2f}%")
print(f"Between 3.00 and 3.99: {(troikari/students)*100:.2f}%")
print(f"Fail: {(dvoikari/students)*100:.2f}%")
print(f"Average: {total_grades/students:.2f}")
