student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
students = {}
with open(student_info) as f:
    student_list = f.readlines()
    for student in student_list:
        student = student.replace("\n", "")
        student = student.split(";")
        if student[0] == "id":
            continue
        students[student[0]] = student[1] + " " + student[2]
exercises = {}
with open(exercise_data) as f:
    exercise_list = f.readlines()
    for exercise in exercise_list:
        exercise = exercise.replace("\n", "")
        exercise = exercise.split(";")
        if exercise[0] == "id":
            continue
        exercises[exercise[0]] = sum([int(x) for x in exercise[1:]])
exam_points = {}
results = {}
with open(exam_data) as f:
    exam_list = f.readlines()
    for exam in exam_list:
        exam = exam.replace("\n", "")
        exam = exam.split(";")
        if exam[0] == "id":
            continue
        exam_points[exam[0]] = sum([int(x) for x in exam[1:]])
        results[exam[0]] = exam_points[exam[0]] + exercises[exam[0]]//4
    grades = {}
    for student, result in results.items():
        if result <= 14:
            grades[student] = 0
        elif result <= 17:
            grades[student] = 1
        elif result <= 20:
            grades[student] = 2
        elif result <= 23:
            grades[student] = 3
        elif result <= 27:
            grades[student] = 4
        else:
            grades[student] = 5     
    message = f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n"
    for id in students:
        message += f"{students[id]:30}{exercises[id]:<10}{exercises[id]//4:<10}{exam_points[id]:<10}{results[id]:<10}{grades[id]:<10}\n"
    print(message)
                 
  
    
