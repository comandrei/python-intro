students = []
with open("students.csv", "r") as input_file:
    for line in input_file:
        student = line.split(',')[0]
        students.append(student)

for student in students:
    print student
