# Duck Typing Example

# -----------------------------
# Example 1: IDE Duck Typing
# -----------------------------

class Vscode:
    def execute(self):
        print("Code is running in VS Code")


class Pycharm:
    def execute(self):
        print("Code is running in PyCharm")


class Common:
    def coding(self, ide):
        ide.execute()


# Object creation
vs = Vscode()
py = Pycharm()

c = Common()

c.coding(vs)
c.coding(py)


# -----------------------------
# Example 2: Payment Duck Typing
# -----------------------------

class CreditCard:
    def payment(self, amount):
        print(f"Your paid Rs.{amount} using Credit Card")


class Upi:
    def payment(self, amount):
        print(f"Your paid Rs.{amount} using UPI")


class Paypal:
    def payment(self, amount):
        print(f"Your paid Rs.{amount} using PayPal")


class Pay:
    def paid(self, platform, amount):
        platform.payment(amount)


# Object creation
c = CreditCard()
u = Upi()
p = Paypal()

pay = Pay()

pay.paid(u, 100)
pay.paid(c, 3000)
pay.paid(p, 5000)


# Function using Duck Typing
def paying(platform, amount):
    platform.payment(amount)


paying(u, 100)
paying(c, 500)
paying(p, 1000)

#*args - multiple argument
def add(*args):
    return sum(args)
print(add(1, 2, 3, 4, 5))
print(add(10, 20, 30, 40, 50))
#*kwarg.items():
def student(**kwargs):
    for a,b in kwargs.items():
        print(f"{a} : {b}")
student(rollno = 55,name = "tharanitharan", age = 21,loaction = "palani")