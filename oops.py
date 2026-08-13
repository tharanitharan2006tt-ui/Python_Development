#class - keyword classname
class Student:
    def student_details(self,roll_no,name,domain):
        print(f"Student roll number is {roll_no} and name is {name} and domain is {domain}")
    x = 10
    #def student_name(self):
    #print(self.name):
#object creation
S = Student()
S.student_details(1,"tharani","python")
print(S.x)
#S.student_name()
x = Student()
x.student_details(2,"dharun","python")
#class employees
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def employee_salary(self,new_salary):
        self.salary = new_salary
        print(self.salary)
E = Employee("tharani",100)
E.employee_salary(10)
a = Employee("dharun",200)
a.employee_salary(20)
