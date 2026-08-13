class Demo:
    def __init__(self):
        self.__name = "tharani"
        self.__age = 20
        self.email = "tharanitharan2006tt@gmail.com"
    def get_details(self):
        print(self.__name)
        print(self.__age)


d = Demo()
print(d.email)


class ATM:
    def __init__(self):
        self.__name = "tharani"
        self.__pin = 20
    def modify_pin(self, old_pin):
        if self.__pin == old_pin:
            new_pin = int(input("Enter new pin number: "))
            self.__pin = new_pin
            prin("your pin is changed!")
        else:
            print("incorrect pin number")
    def grt_pin(self):
        return self.__pin
pin = ATM()
new = int(input("Enter new pin number: "))
pin.modify_pin(new)
print(pin.grt_pin())
