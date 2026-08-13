pin =  int(input("enter your pin: "))
pin = "1234"
if pin == "1234":
    print("pin is correct")
else:
    print("pin is incorrect")

age = int(input("enter your age: "))
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")


#logical operator
username = "tharanitharan"
password = "1234"
if username == "tharanitharan" and password == "1234":
    print("login successful")
else:
    print("login failed")
#nested if
user = int(input("enter your username: "))
if user == "tharanitharan":
    pwd = (input("enter your password: "))
    if pwd == "1234":
        print("login successful")
    else:
        print("incorrect password")
else:
    print("incorrect username")
#elif
tem = int(input("enter your tem number: "))
if tem >= 25:
    print("too hot")
elif tem >= 20:
    print("hot")
elif tem >= 10:
    print("cold")
else:
    print("nothing")