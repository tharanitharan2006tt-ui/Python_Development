class Vehicele:
    def Rental(self):
        print("Rental details")
class car(Vehicele):
    def Rental(self):
        print("car rent 1 day 5000")
class Bike(Vehicele):
    def Rental(self):
        print("bike rent 1 day 500")
class Bus(Vehicele):
    def Rental(self):
        print("bus rent 1 day 5000")


Car = car()
Bike = Bike()
Bus = Bus()
Car.Rental()
Bike.Rental()
Bus.Rental()