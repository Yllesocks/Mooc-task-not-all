points = []
grades = [0, 0, 0, 0, 0, 0] 

while True:
    line = input("Exam points and exercises completed: ")
    if line == "":
        break

    exam_points, exercises = map(int, line.split())
    exercise_points = exercises // 10
    total_points = exam_points + exercise_points
    points.append(total_points)
    if exam_points < 10:
        grade = 0
    elif total_points <= 14:
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

    grades[grade] += 1

print("Statistics:")
average = sum(points) / len(points)
print(f"Points average: {average:.1f}")
passed = sum(grades[1:])
pass_percentage = passed / len(points) * 100
print(f"Pass percentage: {pass_percentage:.1f}")

print("Grade distribution:")
for grade in range(5, -1, -1):
    print(f"  {grade}: {'*' * grades[grade]}")
