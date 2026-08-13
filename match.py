#match
status = int(input("enter your status "))
match status:
    case 100:
        print("you are blocked")
    case 200:
        print("you are not blocked")
    case _:
        print("unknown")
#match
operators = input("enter your operator(+,-,*,/)")
x = int(input("enter your number: "))
y = int(input("enter your number: "))
match operators:
    case "+":
        print(x+y)
    case "-":
        print(x-y)
    case "*":
        print(x*y)
    case "/":
        print(x/y)
    case _:
        print("unknown")

