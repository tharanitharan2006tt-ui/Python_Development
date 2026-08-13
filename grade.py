# Function to calculate grade
def calculate_grade(mark):
    if mark >= 90:
        print("Grade: A")
    elif mark >= 75:
        print("Grade: B")
    elif mark >= 50:
        print("Grade: C")
    else:
        print("fail")


student_name = input("Enter Student Name: ")
mark = int(input("Enter Student Mark: "))

grade = calculate_grade(mark)

print("Student Name :", student_name)
print("Mark         :", mark)
print("Result       :", grade)