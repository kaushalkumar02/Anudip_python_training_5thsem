# Problem Statement:
# Daily expenses are recorded in expenses.txt.
#
# File Format:
# Food,450
# Travel,300
# Shopping,1200
# Electricity,850
# Internet,700
# Entertainment,600
# Medicine,400
# Education,1500
# Fuel,900
# Miscellaneous,250
#
# Requirements:
# 1. Display all expenses.
# 2. Calculate total expenditure.
# 3. Find the category with highest and lowest spending.
# 4. Display expenses greater than ₹800.
# 5. Add a new expense category.
# 6. Update an existing expense amount.
# 7. Generate a summary report in report.txt containing:
#    - Total Expenses
#    - Highest Expense Category
#    - Lowest Expense Category
#    - Categories spending more than ₹800
# ==========================================================

# Function to display all expenses
def display_expenses():

    file = open("expenses.txt", "r")

    print("\nExpense Records")
    print("-" * 30)

    for line in file:
        print(line.strip())

    file.close()


# Function to calculate total expenditure
def total_expense():

    file = open("expenses.txt", "r")

    total = 0

    for line in file:

        data = line.strip().split(",")

        total += int(data[1])

    file.close()

    print("Total Expenditure = ₹", total)


# Function to find highest and lowest expense
def highest_lowest_expense():

    file = open("expenses.txt", "r")

    expenses = []

    for line in file:
        expenses.append(line.strip().split(","))

    file.close()

    highest = expenses[0]
    lowest = expenses[0]

    for item in expenses:

        if int(item[1]) > int(highest[1]):
            highest = item

        if int(item[1]) < int(lowest[1]):
            lowest = item

    print("\nHighest Expense")
    print(highest[0], "₹", highest[1])

    print("\nLowest Expense")
    print(lowest[0], "₹", lowest[1])


# Function to display expenses above 800
def expenses_above_800():

    file = open("expenses.txt", "r")

    print("\nExpenses Greater Than ₹800")
    print("-" * 35)

    for line in file:

        data = line.strip().split(",")

        if int(data[1]) > 800:
            print(data[0], "₹", data[1])

    file.close()


# Function to add new expense
def add_expense():

    category = input("Enter Expense Category: ")
    amount = input("Enter Amount: ")

    file = open("expenses.txt", "a")

    file.write("\n" + category + "," + amount)

    file.close()

    print("Expense Added Successfully.")


# Function to update expense amount
def update_expense():

    category = input("Enter Category Name: ")

    file = open("expenses.txt", "r")

    expenses = []

    for line in file:
        expenses.append(line.strip().split(","))

    file.close()

    found = False

    for item in expenses:

        if item[0].lower() == category.lower():

            new_amount = input("Enter New Amount: ")

            item[1] = new_amount

            found = True

            print("Expense Updated Successfully.")
            break

    if found == False:
        print("Category not found!")

    file = open("expenses.txt", "w")

    for item in expenses:
        file.write(item[0] + "," + item[1] + "\n")

    file.close()


# Function to generate summary report
def generate_report():

    file = open("expenses.txt", "r")

    expenses = []

    total = 0

    for line in file:

        data = line.strip().split(",")

        expenses.append(data)

        total += int(data[1])

    file.close()

    highest = expenses[0]
    lowest = expenses[0]

    for item in expenses:

        if int(item[1]) > int(highest[1]):
            highest = item

        if int(item[1]) < int(lowest[1]):
            lowest = item

    report = open("report.txt", "w")

    report.write("Expense Summary Report\n")
    report.write("-" * 30 + "\n")

    report.write("Total Expenses : ₹" + str(total) + "\n")

    report.write("Highest Expense Category : " +
                 highest[0] + " ₹" + highest[1] + "\n")

    report.write("Lowest Expense Category : " +
                 lowest[0] + " ₹" + lowest[1] + "\n")

    report.write("\nCategories Spending More Than ₹800\n")

    for item in expenses:

        if int(item[1]) > 800:
            report.write(item[0] + " ₹" + item[1] + "\n")

    report.close()

    print("Report Generated Successfully in report.txt")


# Main Menu
while True:

    print("\n===== Daily Expense Tracker =====")
    print("1. Display All Expenses")
    print("2. Calculate Total Expenditure")
    print("3. Find Highest and Lowest Expense")
    print("4. Display Expenses Greater Than ₹800")
    print("5. Add New Expense Category")
    print("6. Update Expense Amount")
    print("7. Generate Summary Report")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        display_expenses()

    elif choice == 2:
        total_expense()

    elif choice == 3:
        highest_lowest_expense()

    elif choice == 4:
        expenses_above_800()

    elif choice == 5:
        add_expense()

    elif choice == 6:
        update_expense()

    elif choice == 7:
        generate_report()

    elif choice == 8:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")