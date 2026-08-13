currest_pin = 1234
balance = 5000
attempt = 0
while attempt < 3:
    pin = int(input("enter the pin number: "))
    if pin == currest_pin:
        amount = int(input("enter the amount: "))
        if amount <= balance:
            balance -= amount
            print("withrovel sussesfully")
            print("new balance: ", balance)
        else:
            print("insufficient funds")
        break
    else:
        attempt += 1
        print("wrong pin number")