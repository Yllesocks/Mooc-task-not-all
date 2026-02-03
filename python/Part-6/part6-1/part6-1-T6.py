student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")



def create_dict(file):
	new_dict = {}
	with open(file) as new_file:
		for line in new_file:
			line = line.strip()
			parts = line.split(";")
			if parts[0] == "id":
				continue
			new_dict[parts[0]] = []
			for item in parts[1:]:
				if item.isdigit():
					new_dict[parts[0]].append(int(item))
				else:
					new_dict[parts[0]].append(item)
	return new_dict

def comb_dict(student_names, student_exercises, student_exams):
	print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
	for id, name in student_names.items():
		if id in student_exercises:
			grade = calculate_grade(sum(student_exercises[id]), sum(student_exams[id]))
			full_name = f"{name[0]} {name[1]}"
			print(f"{full_name:30}{grade[0]:<10}{grade[1]:<10}{grade[2]:<10}{grade[3]:<10}{grade[4]:<10}")

def calculate_grade(exercises, exam_points):
	point_exerc = int((exercises/40) * 10)
	total_points = point_exerc + exam_points
	grade = 5
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
	return [exercises, point_exerc, exam_points, total_points, grade]	

student_names = create_dict(student_info)
student_exercises = create_dict(exercise_data)
student_exams = create_dict(exam_points)
comb_dict(student_names, student_exercises, student_exams)
