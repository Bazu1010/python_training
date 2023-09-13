 # Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
 # A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


student_marks = int(input("Enter your marks: "))

if student_marks > 80 and student_marks <= 100:
    print("Grade: A")
elif student_marks >= 70 and student_marks < 80:
    print("Grade: B+")
elif student_marks >= 60 and student_marks < 70:
    print("Grade: B")
elif student_marks >= 50 and student_marks < 60:
    print("Grade C")
elif student_marks >= 40 and student_marks < 50:
    print("Grade: D")
elif student_marks < 40:
    print("Grade E")
else:
    print("Enter valid marks: 0-100")

