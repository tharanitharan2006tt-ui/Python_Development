class employee:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary
    def calculate(self):
        return self.base_salary #normal employee get base salary
class Developer(employee):
    def calculate(self):
        return self.base_salary + 20000
class Manager(employee):
    def calculate(self):
        return self.base_salary + 50000


dev = Developer("tharani", 20000)
mgr = Manager("tharani", 50000)
em = employee("tharani", 100000)
print(em.name,"salary")
print(em.base_salary,"salary",em.calculate())
print(dev.name,"salary",dev.calculate())
print(mgr.name,"salary",mgr.calculate())


class Notification:
    def send(self,message):
        return ("sending notification")
class Email(Notification):
    def send(self,message):
        return ("sending email :"+message)
class Text_message(Notification):
    def send(self,message):
        return ("sending text_mass :"+message)
class Whatsapp(Notification):
    def send(self,message):
        return ("sending whatsapp massage :"+message)
email = Email()
text_message = Text_message()
whatsapp = Whatsapp()
print(email.send  ("hi"))
print(text_message.send ("hi"))
print(whatsapp.send ("hi"))