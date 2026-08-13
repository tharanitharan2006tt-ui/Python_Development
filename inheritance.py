class BankAccount:
    def __init__(self, acc_no, acc_holder, balance):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Your deposited Rs.{amount} and your balance is Rs.{self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Your withdrawn Rs.{amount} and your balance is Rs.{self.balance}")
        else:
            print("You don't have enough money")


class SavingsAccount(BankAccount):
    def __init__(self, acc_no, acc_holder, balance, interest_rate):
        super().__init__(acc_no, acc_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Rs.{interest} added to your account as interest")
        print(f"New Balance: Rs.{self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, acc_no, acc_holder, balance, overdraft):
        super().__init__(acc_no, acc_holder, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if self.balance + self.overdraft >= amount:
            self.balance -= amount
            print(f"Your withdrawn Rs.{amount} and your balance is Rs.{self.balance}")
        else:
            print("Overdraft limit exceeded")


# Creating objects
s1 = SavingsAccount(101, "John", 10000, 5)
s1.deposit(2000)
s1.withdraw(3000)
s1.calculate_interest()

print()

c1 = CurrentAccount(102, "David", 5000, 2000)
c1.withdraw(6000)
c1.withdraw(2000)
c1.overdraft(7000)