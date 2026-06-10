# Problem Statement:
# A company stores employee details in a text file
# named employees.txt.
# File Format:
# EMP101,Anuj,45000
# EMP102,Rahul,52000
# EMP103,Priya,38000
# EMP104,Neha,61000
# EMP105,Amit,29000
# EMP106,Sneha,55000
# EMP107,Karan,47000
# EMP108,Pooja,72000
# EMP109,Rohit,33000
# EMP110,Anjali,68000
# Requirements:
# 1. Display all employee records.
# 2. Search employee details using Employee ID.
# 3. Calculate the average salary.
# 4. Find the highest-paid and lowest-paid employee.
# 5. Display employees earning above ₹50,000.
# 6. Add a new employee record to the file.
# 7. Generate salary categories:
#    High   (₹60,000 and above)
#    Medium (₹40,000–₹59,999)
#    Low    (Below ₹40,000)
# ==========================================================

# Function to display all employee records
def display_records():

    file = open("employees.txt", "r")

    print("\nEmployee Records")
    print("-" * 40)

    for line in file:
        print(line.strip())

    file.close()


# Function to search employee by ID
def search_employee():

    emp_id = input("Enter Employee ID: ")

    file = open("employees.txt", "r")

    found = False

    for line in file:

        data = line.strip().split(",")

        if data[0] == emp_id:

            print("\nEmployee Details")
            print("Employee ID :", data[0])
            print("Name        :", data[1])
            print("Salary      :", data[2])

            found = True
            break

    if found == False:
        print("Employee not found!")

    file.close()


# Function to calculate average salary
def average_salary():

    file = open("employees.txt", "r")

    total_salary = 0
    count = 0

    for line in file:

        data = line.strip().split(",")

        total_salary = total_salary + int(data[2])
        count = count + 1

    file.close()

    average = total_salary / count

    print("Average Salary =", average)


# Function to find highest and lowest paid employee
def highest_lowest_salary():

    file = open("employees.txt", "r")

    employees = []

    for line in file:

        data = line.strip().split(",")

        employees.append(data)

    file.close()

    highest = employees[0]
    lowest = employees[0]

    for emp in employees:

        if int(emp[2]) > int(highest[2]):
            highest = emp

        if int(emp[2]) < int(lowest[2]):
            lowest = emp

    print("\nHighest Paid Employee")
    print("ID     :", highest[0])
    print("Name   :", highest[1])
    print("Salary :", highest[2])

    print("\nLowest Paid Employee")
    print("ID     :", lowest[0])
    print("Name   :", lowest[1])
    print("Salary :", lowest[2])


# Function to display employees earning above 50000
def employees_above_50000():

    file = open("employees.txt", "r")

    print("\nEmployees Earning Above ₹50,000")
    print("-" * 40)

    for line in file:

        data = line.strip().split(",")

        if int(data[2]) > 50000:
            print(data[0], data[1], data[2])

    file.close()


# Function to add new employee
def add_employee():

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Employee Salary: ")

    file = open("employees.txt", "a")

    file.write("\n" + emp_id + "," + name + "," + salary)

    file.close()

    print("Employee Record Added Successfully.")


# Function to generate salary categories
def salary_categories():

    file = open("employees.txt", "r")

    print("\nSalary Categories")
    print("-" * 40)

    for line in file:

        data = line.strip().split(",")

        salary = int(data[2])

        if salary >= 60000:
            category = "High"

        elif salary >= 40000:
            category = "Medium"

        else:
            category = "Low"

        print(data[1], "->", category)

    file.close()


# Main Program
while True:

    print("\n===== Employee Payroll Management System =====")
    print("1. Display All Employee Records")
    print("2. Search Employee by ID")
    print("3. Calculate Average Salary")
    print("4. Find Highest and Lowest Paid Employee")
    print("5. Display Employees Earning Above ₹50,000")
    print("6. Add New Employee Record")
    print("7. Generate Salary Categories")
    print("8. Exit")

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        display_records()

    elif choice == 2:
        search_employee()

    elif choice == 3:
        average_salary()

    elif choice == 4:
        highest_lowest_salary()

    elif choice == 5:
        employees_above_50000()

    elif choice == 6:
        add_employee()

    elif choice == 7:
        salary_categories()

    elif choice == 8:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice! Please try again.")