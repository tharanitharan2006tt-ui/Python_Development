def atm_withdraw():
    balance = 5000

    try:
        amount = int(input("Enter the withdrawal amount: "))
        if amount > balance:
            raise ValueError("Insufficient balance.")
        elif amount <= 0:
            raise ValueError("Invalid amount. Must be greater than 0.")
    except ValueError as e:
        print("Transaction Failed:", e)
    else:
        balance -= amount
        print("Withdrawal Successful!")
        print("Remaining Balance:", balance)
    finally:
        print("Thank you for using our ATM service.")
atm_withdraw()