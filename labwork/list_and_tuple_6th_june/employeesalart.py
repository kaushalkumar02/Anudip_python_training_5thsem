# ------------------------------------------------------------
# Problem Statement:
# Employee Salary Processing
# Employee data is stored as a list of tuples.
# Each tuple contains:
# 1. Employee Name
# 2. Employee Salary
# Objective:
# Write a Python program to analyze employee salary data.
# Tasks:
# • Display employees earning above ₹50,000
# • Find the highest-paid employee
# • Calculate total salary expenditure
# • Count employees earning below ₹40,000
# ------------------------------------------------------------

# Employee data (Name, Salary)
employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# 1. Display employees earning above ₹50,000
print("Employees earning above ₹50,000:")

for name, salary in employees:
    if salary > 50000:
        print(name, "->", salary)

# 2. Find highest-paid employee
highest_paid = max(employees, key=lambda emp: emp[1])

print("\nHighest Paid Employee:")
print(highest_paid[0], "->", highest_paid[1])

# 3. Calculate total salary expenditure
total_salary = 0

for name, salary in employees:
    total_salary += salary

print("\nTotal Salary Expenditure:", total_salary)

# 4. Count employees earning below ₹40,000
count_below_40000 = 0

for name, salary in employees:
    if salary < 40000:
        count_below_40000 += 1

print("\nEmployees earning below ₹40,000:", count_below_40000)