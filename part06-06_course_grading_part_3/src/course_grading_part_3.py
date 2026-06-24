# each row contains the information for a single student
# width of name should be 30 characters
# others should be 10
# {word:10} justifies to the left
# {number:<10} justifies to the left
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

# if False: 
#     student_file = input("Student information: ")
#     exercise_file = input("Exercises completed: ")
#     exam_file = input("Exam points: ")
# else:
#     student_file = "students2.csv"
#     exercise_file = "exercises2.csv"
#     exam_file = "exam_points2.csv"

names = {}

with open(student_file) as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1] + " " + parts[2]

# print(names)

exercises = {}

with open(exercise_file) as new_file:

    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        scores = [int(x) for x in parts]
        exercises[parts[0]] = sum(scores[1:])

exercise_points = {}

with open(exercise_file) as new_file:

    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        scores = [int(x) for x in parts]
        exercise_points[parts[0]] = int(sum(scores[1:])/40 * 10)

exams = {}

with open(exam_file) as new_file:

    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exam_points = [int(x) for x in parts]
        exams[parts[0]] = sum(exam_points[1:])

def grade(total_points):
    thresholds = [(28, 5), (24, 4), (21, 3), (18, 2), (15, 1), (0, 0)]
    for threshold, grade_value in thresholds:
        if total_points >= threshold:
            return grade_value

column1 = "name"
column2 = "exec_nbr"
column3 = "exec_pts."
column4 = "exm_pts."
column5 = "tot_pts."
column6 = "grade"
print(f"{column1:30}{column2:10}{column3:10}{column4:10}{column5:10}{column6:10}")

for id, name in names.items():
    if id in exercises:
        exec_nbr = exercises[id]
        total = exercise_points[id]
        exam_total = exams[id]
        total_points = exercise_points[id] + exams[id]
        print(f"{name:30}{exec_nbr:<10}{total:<10}{exam_total:<10}{total_points:<10}{grade(total_points):<10}")
    else:
        print(f"{name} 0 exercises completed")