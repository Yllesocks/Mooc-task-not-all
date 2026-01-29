student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

students = {}
with open(student_info) as file:
    next(file) 
    for line in file:
        id_, first, last = line.strip().split(";")
        students[id_] = f"{first} {last}"

exercises_done = {}
exercise_points = {}
with open(exercise_data) as file:
    next(file) 
    for line in file:
        parts = line.strip().split(";")
        id_ = parts[0]
        total = sum(int(x) for x in parts[1:])
        exercises_done[id_] = total
        exercise_points[id_] = total // 4

exam_points = {}
with open(exam_data) as file:
    next(file) 
    for line in file:
        parts = line.strip().split(";")
        id_ = parts[0]
        exam_points[id_] = sum(int(x) for x in parts[1:])

print()
print(f"{'name':30}{'exec_nbr':>10}{'exec_pts.':>10}{'exm_pts.':>10}{'tot_pts.':>10}{'grade':>10}")

for id_ in students:
    exec_nbr = exercises_done[id_]
    exec_pts = exercise_points[id_]
    exm_pts = exam_points[id_]
    tot_pts = exec_pts + exm_pts

    if tot_pts <= 14:
        grade = 0
    elif tot_pts <= 17:
        grade = 1
    elif tot_pts <= 20:
        grade = 2
    elif tot_pts <= 23:
        grade = 3
    elif tot_pts <= 27:
        grade = 4
    else:
        grade = 5
    print(f"{students[id_]:30}{exec_nbr:>10}{exec_pts:>10}{exm_pts:>10}{tot_pts:>10}{grade:>10}")