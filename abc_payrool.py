from abc import abstractmethod,ABC


class Payroll(ABC):
    @abstractmethod
    def generate_salary(self):
        pass
class CompanyPayroll(Payroll):
    def __init__(self,name,basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def generate_salary(self):

        hra = self.basic_salary * 0.20
        pf = self.basic_salary * 0.12
        tax = self.basic_salary * 0.10

        gross_salary = self.basic_salary + hra
        net_salary = self.basic_salary - pf - tax

        print("___________salary slip_________")
        print("Employee name         :",self.name)
        print("Employee basic salary :",self.basic_salary)
        print("hra                   :",hra)
        print("pf Deduction          :",pf)
        print("tax Deduction         :",tax)
        print("Net Salary            :",net_salary)


employee = CompanyPayroll("Tharanitharan",100000)
employee.generate_salary()