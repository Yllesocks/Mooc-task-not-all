def summary(students: dict):
    print(f"students {len(students)}")

    most_courses = 0
    most_courses_student = ""
    best_average = 0
    best_average_student = ""

    for name, courses in students.items():
        count = len(courses)

        if count > most_courses:
            most_courses = count
            most_courses_student = name

        if count > 0:
            average = sum(courses.values()) / count
            if average > best_average:
                best_average = average
                best_average_student = name

    print(f"most courses completed {most_courses} {most_courses_student}")
    print(f"best average grade {best_average} {best_average_student}")

def add_student(students: dict, name: str):
    if name not in students:
        students[name] = {}

def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    courses = students[name]
    print(f"{name}:")
    
    if len(courses) == 0:
        print(" no completed courses")
    else:
        print(f" {len(courses)} completed courses:")
        total = 0
        for course, grade in courses.items():
            print(f"  {course} {grade}")
            total += grade
        print(f" average grade {total / len(courses)}")

def add_course(students: dict, name: str, course: tuple):
    course_name, grade = course
    
    if grade == 0 or name not in students:
        return

    courses = students[name]

    if course_name not in courses or grade > courses[course_name]:
        courses[course_name] = grade
