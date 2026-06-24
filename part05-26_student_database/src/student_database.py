def add_student(students: list, name: str):
    # adds new student to the database
    students[name] = {
        "courses": [],
        "total_grade": 0,
        "course_count": 0,
        "average": 0
    }

def add_course(students: list, name: str, course: tuple):
    # adds a completed course to the information of a specific student.
    # the course data us a tuple consisting of the name of the course and the grade.   

    if course[1] != 0:
        found = False
        for existing_course in students[name]["courses"]:
            if existing_course[0] == course[0]: # same course name?
                found = True
                if course[1] > existing_course[1]:
                    students[name]["courses"].remove(existing_course)
                    students[name]["courses"].append(course)
                    students[name]["total_grade"] -= (existing_course[1])
                    students[name]["total_grade"] += course[1]
     
        if not found:
            students[name]["courses"].append(course)
            students[name]["total_grade"] += course[1]
            students[name]["course_count"] += 1
        
        students[name]["average"] = students[name]["total_grade"] / students[name]["course_count"]
    
def summary(students: list):
    total_students = len(students)
    print(f"students {total_students}")
    
    max_courses = 0
    max_courses_name = ""
    max_average = 0
    max_average_name = ""
    for name in students:
        if students[name]["course_count"] > max_courses:
            max_courses = students[name]["course_count"]
            max_courses_name = name

        if students[name]["average"] > max_average:
            max_average = students[name]["average"]
            max_average_name = name

    print(f"most courses completed {max_courses} {max_courses_name}")
    print(f"best average grade {max_average} {max_average_name}")                


def print_student(students: list, name:str):
    if name in students:
        print(f"{name}:")

        if students[name]["course_count"] != 0:
            print(f" {students[name]["course_count"]} completed courses: ")
        else:
            print(" no completed courses")
        for course in students[name]["courses"]:
            print(f"  {course[0]} {course[1]}")
        if students[name]["average"] > 0:
            print(f" average grade {students[name]["average"]}")

    else:
        print(f"{name}: no such person in the database")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)