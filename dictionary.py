dic = {
    "name" : "tharani",
    "age" : 20,
    "city" : "palani"
}
print(dic)
print(type(dic))
student = {
    "name" : "tharani",
    "age" : 20,
    "city" : "palani"
}
print(student)
print(type(student))
# 1.get() -
print(student.get("name"))
print(student.get("email"))
#keys
print(student.keys())
#valus
print(student.values())
#items
print(student.items())
#update
student.update({"wmail":"tharanitharan2006tt@gmail.com"})
print(student)
#pop - spacific key remove
student.pop("age")
print(student)
#popitem()-last item remove
student.popitem()
print("after pop item ",student)
