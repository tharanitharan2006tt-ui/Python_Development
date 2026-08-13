# Abstract Class for Discount
from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass


# No Discount
class NoDiscount(Discount):
    def apply(self, price):
        return price


# Percentage Discount
class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, price):
        return price - (price * self.percentage / 100)


# Fixed Amount Discount
class FixedAmount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return price - self.amount if price > self.amount else 0


# Product Class
class Product:
    def __init__(self, name, price, discount: Discount):
        self.name = name
        self.price = price
        self.discount = discount

    def final_price(self):
        return self.discount.apply(self.price)

    def display(self):
        print("Product :", self.name)
        print("Original Price :", self.price)
        print("Final Price :", self.final_price())


# No Discount
p1 = Product("Thor", 100, NoDiscount())
p1.display()
p1.final_price()

print("------------------")

# 20% Discount
p2 = Product("Laptop", 50000, PercentageDiscount(20))
p2.display()

print("------------------")

# Fixed Amount Discount
p3 = Product("Mobile", 20000, FixedAmount(3000))
p3.display()

print("------------------")

p4 = Product("TV", 10000, FixedAmount(1000))
p4.display()
