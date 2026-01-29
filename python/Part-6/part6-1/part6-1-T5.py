student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

students = {}
with open(student_info) as file:
    next(file)
    for line in file:
        id_, first, last = line.strip().split(";")
        students[id_] = f"{first} {last}"

exercise_points = {}
with open(exercise_data) as file:
    next(file)
    for line in file:
        parts = line.strip().split(";")
        id_ = parts[0]
        exercises_completed = sum(int(x) for x in parts[1:])
        points = exercises_completed // 4
        exercise_points[id_] = points

exam_points = {}
with open(exam_data) as file:
    next(file)
    for line in file:
        parts = line.strip().split(";")
        id_ = parts[0]
        exam_points[id_] = sum(int(x) for x in parts[1:])

for id_ in students:
    total_points = exercise_points[id_] + exam_points[id_]
    if total_points <= 14:
        grade = 0
    elif total_points <= 17:
        grade = 1
    elif total_points <= 20:
        grade = 2
    elif total_points <= 23:
        grade = 3
    elif total_points <= 27:
        grade = 4
    else:
        grade = 5
    print(students[id_], grade)