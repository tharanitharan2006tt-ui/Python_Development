# Sample users dictionary
users = {
    "tharani": 1234,
    "admin": 5678
}

def login():
    try:
        username = input("Enter your username: ")
        password = int(input("Enter your password: "))

        if username not in users:
            raise ValueError("User does not exist")

        if users[username] != password:
            raise ValueError("Incorrect password")

    except ValueError as e:
        print("Login failed:", e)

    else:
        print("Login successful")

    finally:
        print("Authentication completed")


# Function call
login()

def checkout():
    try:
        cart_total = 5000  # Example cart total

        payment = int(input("Enter a payment amount ₹: "))

        if payment < 0:
            raise ValueError("Payment cannot be negative")

        elif payment < cart_total:
            raise ValueError("Insufficient payment. Kindly pay the full amount.")

        elif payment >= 10000:
            raise ValueError("Payment limit is exceeded")

    except ValueError as i:
        print("ERROR:", i)

    else:
        print("Payment completed successfully")

    finally:
        print("thank you for shopping with us")


checkout()
