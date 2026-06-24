#write a program which asks the users for the names of these two files, 
# reads the files, and then prints out the total number
# of exercises completed by the students
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")

# if False: 
#     student_file = input("Student information: ")
#     exercise_file = input("Exercises completed: ")
# else:
#     student_file = "students1.csv"
#     exercise_file = "exercises1.csv"

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
        int_list = [int(x) for x in parts]
        exercises[parts[0]] = sum(int_list[1:])

# print(exercises)

for id, name in names.items():
    if id in exercises:
        total = exercises[id]
        print(f"{name} {total}")
    else:
        print(f"{name} 0 exercises completed")