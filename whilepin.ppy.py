correct_pin = 1234
attempt = 0
while attempt < 3:
    pin=int(input("enter your pin "))
    if pin == correct_pin:
        print("login successful")
        break
    else:
        print("try again")
    attempt += 1