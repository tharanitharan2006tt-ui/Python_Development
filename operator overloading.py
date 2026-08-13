#operator overloading
class Book:
    def __init__(self,pages):
        self.pages = pages
    def __sub__(self,other):
        return self.pages - other.pages
    def __add__(self,other):
        return self.pages + other.pages
    def __mul__(self,other):
        return self.pages * other.pages
    def __truediv__(self, other):
        return self.pages / other.pages
    def __floordiv__(self,other):
        return self.pages // other.pages
    def __mod__(self,other):
        return self.pages % other.pages
b1 = Book(5)
b2 = Book(6)
print(b1 - b2)
print(b1 + b2)
print(b1 * b2)
print(b1 / b2)