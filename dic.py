#1
from os import name

student = {
    "name" : "tharani",
    "age" : 20,
    "course" : "b.sc(cs)"
}
#2
print(student.keys())
print(student.values())
student["name"] = "tharanitharan"
print(student)
student["city"] = "palani"
print(student)
print(student.pop("city"))
print(student)