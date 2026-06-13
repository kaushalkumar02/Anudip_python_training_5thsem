# Problem Statement:
# Create an Employee class containing employee ID, employee name,
# and monthly salary.
#
# Implement methods to:
# • Display employee details.
# • Calculate annual salary.
# • Increase salary by a given percentage.
#
# Sample Output:
# Employee Name   : Rohan
# Monthly Salary  : ₹50000
# Annual Salary   : ₹600000
# Updated Salary  : ₹55000


# Employee Class
class Employee:

    # Constructor to initialize employee details
    def __init__(self, emp_id, name, monthly_salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__monthly_salary = monthly_salary

    # Method to display employee details
    def display_details(self):
        print("\nEmployee Details")
        print("-" * 30)
        print("Employee ID    :", self.__emp_id)
        print("Employee Name  :", self.__name)
        print("Monthly Salary : ₹", self.__monthly_salary)

    # Method to calculate annual salary
    def calculate_annual_salary(self):
        return self.__monthly_salary * 12

    # Method to increase salary by a given percentage
    def increase_salary(self, percentage):
        self.__monthly_salary += (self.__monthly_salary * percentage / 100)

    # Method to display salary information
    def display_salary_info(self):
        print("\nSalary Information")
        print("-" * 30)
        print("Annual Salary  : ₹", self.calculate_annual_salary())
        print("Updated Salary : ₹", round(self.__monthly_salary, 2))


# ---------------- Main Program ----------------

# Accept and validate Employee ID
while True:
    emp_id = input("Enter Employee ID: ").strip()

    # Check if Employee ID is empty
    if emp_id == "":
        print("Error: Employee ID cannot be empty.")
    else:
        break


# Accept and validate Employee Name
while True:
    name = input("Enter Employee Name: ").strip()

    # Check if name is empty
    if name == "":
        print("Error: Employee Name cannot be empty.")

    # Check if name contains only alphabets and spaces
    elif not all(ch.isalpha() or ch.isspace() for ch in name):
        print("Error: Name should contain only alphabets and spaces.")

    else:
        break


# Accept and validate Monthly Salary
while True:
    try:
        monthly_salary = float(input("Enter Monthly Salary: ₹"))

        # Salary must be positive
        if monthly_salary <= 0:
            print("Error: Salary must be greater than 0.")
        else:
            break

    except ValueError:
        print("Error: Please enter a valid numeric salary.")


# Accept and validate Increment Percentage
while True:
    try:
        percentage = float(input("Enter Salary Increment Percentage: "))

        # Percentage cannot be negative
        if percentage < 0:
            print("Error: Percentage cannot be negative.")
        else:
            break

    except ValueError:
        print("Error: Please enter a valid percentage.")


# Create Employee object
emp = Employee(emp_id, name, monthly_salary)

# Display employee details
emp.display_details()

# Increase salary by given percentage
emp.increase_salary(percentage)

# Display annual salary and updated salary
emp.display_salary_info()