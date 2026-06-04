pin = 1234

while True:
    user_pin = int(input("Enter PIN: "))

    if user_pin == pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN. Try Again.")