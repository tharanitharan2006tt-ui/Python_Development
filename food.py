class FoodItem:
    def __init__(self, food_name, price, quantity):
        self.food_name = food_name
        self.price = price
        self.quantity = quantity

    def calculate_bill(self):
        bill = self.price * self.quantity

        if self.quantity > 5:
            discount = bill * 0.10
            bill -= discount

        delivery_charge = 40
        bill += delivery_charge

        return bill


class VegFoodItem(FoodItem):
    def __init__(self, food_name, price, quantity, vegtype):
        super().__init__(food_name, price, quantity)
        self.vegtype = vegtype

    def display(self):
        print(f"Food Name : {self.food_name}")
        print(f"Veg Type  : {self.vegtype}")
        print(f"Total Bill: Rs.{self.calculate_bill()}")


class NonVegFoodItem(FoodItem):
    def __init__(self, food_name, price, quantity, nonvegtype):
        super().__init__(food_name, price, quantity)
        self.nonvegtype = nonvegtype

    def display(self):
        print(f"Food Name : {self.food_name}")
        print(f"Meat Type : {self.nonvegtype}")
        print(f"Total Bill: Rs.{self.calculate_bill()}")


# Create Objects
v = VegFoodItem("Pizza", 600, 8, "Italian")
v.display()

print()

n = NonVegFoodItem("Chicken Biryani", 250, 6, "Chicken")
n.display()