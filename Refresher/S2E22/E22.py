student_attendance = {"Rolf":96, "Bob":30, "Anne":100}

for student in student_attendance:
    print(f'{student} attended {student_attendance[student]}')
print('----------------------------')
for student, attendance in student_attendance.items():
    print(f'{student} attendance of {attendance}')