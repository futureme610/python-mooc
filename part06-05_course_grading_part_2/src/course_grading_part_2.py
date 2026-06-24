#program should ask the user for the names of the files.
#the program should process the files and print out a grade for each student

#exercise points are based on the percentage completed: 40 (100%) = 10 points
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")
# if False: 
#     student_file = input("Student information: ")
#     exercise_file = input("Exercises completed: ")
#     exam_file = input("Exam points: ")
# else:
#     student_file = "students1.csv"
#     exercise_file = "exercises1.csv"
#     exam_file = "exam_points1.csv"

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
        exercises[parts[0]] = int(sum(scores[1:])/40 * 10)

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
        
for id, name in names.items():
    if id in exercises:
        total = exercises[id]
        exam_total = exams[id]
        total_points = exercises[id] + exams[id]
        print(f"{name} {grade(total_points)}")
    else:
        print(f"{name} 0 exercises completed")