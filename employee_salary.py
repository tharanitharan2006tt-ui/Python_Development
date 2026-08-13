class Employee:
    def __init__(self, emp_name, basic_salary):
        self.emp_name = emp_name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        if self.basic_salary > 50000:
            bonus = 5000
        else:
            bonus = 2000

        total_salary = self.basic_salary + bonus

        print("Employee Name :", self.emp_name)
        print("Basic Salary  :", self.basic_salary)
        print("Bonus         :", bonus)
        print("Total Salary  :", total_salary)


name = input("Enter Employee Name: ")
salary = float(input("Enter Basic Salary:"))

emp = Employee(name, salary)
emp.calculate_salary()