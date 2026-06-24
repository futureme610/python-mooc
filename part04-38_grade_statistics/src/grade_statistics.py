def exam_input():
    question = (input("Exam points and exercises completed: "))


    if question == "":
        return "", ""
    
    else:
        question_list = question.split()
        exam = question_list[0]
        ex = question_list[1]
        return int(exam), int(ex)

def statistics(average, pass_percent):
    print("Statistics: ")
    print(f"Points average: {average}")
    print(f"Pass percentage: {pass_percent}")

def grades(total1, total2, total3, total4, total5, total_fail):
    print("Grade distribution: ")
    print(f"5: {'*' * total5}")
    print(f"4: {'*' * total4}")
    print(f"3: {'*' * total3}")
    print(f"2: {'*' * total2}")
    print(f"1: {'*' * total1}")
    print(f"0: {'*' * total_fail}")



exam_total = 0
no_exams = 0 
exams_passed = 0
grade_1 = 0
grade_2 = 0
grade_3 = 0
grade_4 = 0
grade_5 = 0
fail = 0

while True:
    exam, exercise = exam_input()

    if exam == "":
        percent_passed = round((exams_passed/no_exams)*100, 1)
        average_score = (exam_total/no_exams)
        statistics(average_score, percent_passed)
        grades(grade_1, grade_2, grade_3, grade_4, grade_5, fail)
        break

    else:
        current_exam = exam + exercise//10
        exam_total += current_exam
        if exam < 10:
            fail += 1

        elif current_exam > 14:
            exams_passed += 1
            if current_exam <= 17:
                grade_1 += 1
            elif current_exam <= 20:
                grade_2 += 1
            elif current_exam <= 23:
                grade_3 += 1
            elif current_exam <= 27:
                grade_4 += 1
            elif current_exam <= 30:
                grade_5 += 1
            
        else: 
            fail += 1
        no_exams += 1
    