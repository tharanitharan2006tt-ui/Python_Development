# Parent Class
class FoodItem:
    def __init__(self, food_name, price, quantity):
        self.food_name = food_name
        self.price = price
        self.quantity = quantity

    def calculate_bill(self):
        total = self.price * self.quantity

        # 10% discount if quantity > 5
        if self.quantity > 5:
            discount = total * 0.10
            total -= discount

        # Add delivery charge
        total += 40

        return total


# Child Class - Veg Food
class VegFood(FoodItem):
    def __init__(self, food_name, price, quantity, veg_type):
        super().__init__(food_name, price, quantity)
        self.veg_type = veg_type

    def display(self):
        print("\n----- Veg Food Details -----")
        print("Food Name:", self.food_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Veg Type:", self.veg_type)
        print("Final Bill: ₹", self.calculate_bill())


# Child Class - Non Veg Food
class NonVegFood(FoodItem):
    def __init__(self, food_name, price, quantity, meat_type):
        super().__init__(food_name, price, quantity)
        self.meat_type = meat_type

    def display(self):
        print("\n----- Non-Veg Food Details -----")
        print("Food Name:", self.food_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Meat Type:", self.meat_type)
        print("Final Bill: ₹", self.calculate_bill())


# Creating Objects
veg = VegFood("Masala Dosa", 80, 6, "South Indian")
nonveg = NonVegFood("Chicken Biryani", 250, 4, "Chicken")

# Display Details
veg.display()
nonveg.display()