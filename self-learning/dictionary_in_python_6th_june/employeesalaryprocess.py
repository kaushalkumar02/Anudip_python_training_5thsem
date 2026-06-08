# --------------------------------------------------
# Problem Statement:
# Analyze employee salary data and perform the following:
# 1. Display employees earning above ₹60,000.
# 2. Count employees earning below ₹40,000.
# 3. Find the highest-paid employee.
# 4. Create a list of employees eligible for a bonus
#    (salary > ₹50,000).
# 5. Calculate the average salary.
# -------------------------------------------------
# Sample Data
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# --------------------------------------------------
# Validation Section
# --------------------------------------------------

is_valid = True

# Check whether salary is a dictionary
if not isinstance(salary, dict):
    print("Invalid data: Salary records should be stored in a dictionary.")
    is_valid = False

# Validate employee IDs and salary values
if is_valid:
    for emp_id, emp_salary in salary.items():

        # Employee ID must be a string
        if not isinstance(emp_id, str):
            print("Invalid employee ID found.")
            is_valid = False
            break

        # Salary must be numeric
        if not isinstance(emp_salary, (int, float)):
            print(f"Invalid salary for {emp_id}.")
            is_valid = False
            break

        # Salary cannot be negative
        if emp_salary < 0:
            print(f"Negative salary found for {emp_id}.")
            is_valid = False
            break

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

if is_valid:

    # Employees earning above ₹60,000
    high_salary_employees = [
        emp_id for emp_id, emp_salary in salary.items()
        if emp_salary > 60000
    ]

    # Count employees earning below ₹40,000
    low_salary_count = sum(
        1 for emp_salary in salary.values()
        if emp_salary < 40000
    )

    # Highest-paid employee
    highest_paid_employee = max(salary, key=salary.get)
    highest_salary = salary[highest_paid_employee]

    # Employees eligible for bonus (salary > ₹50,000)
    bonus_eligible = [
        emp_id for emp_id, emp_salary in salary.items()
        if emp_salary > 50000
    ]

    # Average salary
    average_salary = sum(salary.values()) / len(salary)

    # --------------------------------------------------
    # Output Section
    # --------------------------------------------------

    print("Employees earning above ₹60,000:")
    print(high_salary_employees)

    print("\nNumber of employees earning below ₹40,000:")
    print(low_salary_count)

    print("\nHighest-paid employee:")
    print(f"{highest_paid_employee} - ₹{highest_salary}")

    print("\nEmployees eligible for bonus:")
    print(bonus_eligible)

    print("\nAverage Salary:")
    print(f"₹{average_salary:.2f}")