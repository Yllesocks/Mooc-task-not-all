student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students = {}
with open(student_info) as file:
    next(file)
    for line in file:
        id_, first, last = line.strip().split(";")
        students[id_] = f"{first} {last}"

with open(exercise_data) as file:
    next(file)
    for line in file:
        parts = line.strip().split(";")
        id_ = parts[0]
        exercises = map(int, parts[1:])
        total = sum(exercises)

        print(students[id_], total)