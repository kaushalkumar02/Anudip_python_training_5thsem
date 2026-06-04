# Initial Balance = 10000
balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amt = int(input("Enter Deposit Amount: "))
        balance = balance + amt
        print("Amount Deposited")

    elif choice == 3:
        amt = int(input("Enter Withdraw Amount: "))
        if amt <= balance:
            balance = balance - amt
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Exit Successful")
        break

    else:
        print("Invalid Choice")