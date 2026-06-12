'''Employee Salary Report Generator 
Problem Statement 
Employee details are stored in a text file named employees.txt. 
Sample Input/Data (employees.txt) 
EMP101,Anuj,45000 
EMP102,Rahul,52000 
EMP103,Priya,38000 
EMP104,Neha,61000 
EMP105,Amit,29000 
EMP106,Sneha,55000 
EMP107,Karan,47000 
EMP108,Pooja,72000 
EMP109,Rohit,33000 
EMP110,Anjali,68000 
Tasks 
1. Display employees earning more than ₹50,000.  
2. Find the highest-paid employee.  
3. Find the lowest-paid employee.  
4. Calculate the average salary.  
5. Generate salary categories:  
o High (≥ ₹60,000)  
o Medium (₹40,000 – ₹59,999)  
o Low (< ₹40,000)  
Sample Output 
Employees Earning Above ₹50,000: 
Rahul 
Neha 
Sneha 
Pooja 
Anjali 
 
Highest Paid Employee: 
Pooja (₹72,000) 
 
Lowest Paid Employee: 
Amit (₹29,000) 
 
Average Salary: ₹50,000 
 
High Salary: 
['Neha', 'Pooja', 'Anjali'] 
 
Medium Salary: 
['Anuj', 'Rahul', 'Sneha', 'Karan'] 
 
Low Salary: 
['Priya', 'Amit', 'Rohit']'''

# Employee Salary Report Generator

# Open the file in read mode
file = open("employees.txt", "r")

# Read all lines from the file
records = file.readlines()

# --------------------------------------------------
# Task 1: Display employees earning more than ₹50,000
# --------------------------------------------------

print("Employees Earning Above ₹50,000:")

for record in records:

    # Split the record into employee ID, name and salary
    emp_id, name, salary = record.strip().split(",")

    salary = int(salary)

    if salary > 50000:
        print(name)

# --------------------------------------------------
# Task 2: Find the highest-paid employee
# --------------------------------------------------

# Extract details from the first record
emp_id, name, salary = records[0].strip().split(",")

highest_name = name
highest_salary = int(salary)

# Compare salaries of all employees
for record in records:

    emp_id, name, salary = record.strip().split(",")
    salary = int(salary)

    if salary > highest_salary:
        highest_salary = salary
        highest_name = name

print("\nHighest Paid Employee:")
print(highest_name, f"(₹{highest_salary})")

# --------------------------------------------------
# Task 3: Find the lowest-paid employee
# --------------------------------------------------

# Extract details from the first record
emp_id, name, salary = records[0].strip().split(",")

lowest_name = name
lowest_salary = int(salary)

# Compare salaries of all employees
for record in records:

    emp_id, name, salary = record.strip().split(",")
    salary = int(salary)

    if salary < lowest_salary:
        lowest_salary = salary
        lowest_name = name

print("\nLowest Paid Employee:")
print(lowest_name, f"(₹{lowest_salary})")

# --------------------------------------------------
# Task 4: Calculate the average salary
# --------------------------------------------------

total_salary = 0

for record in records:

    emp_id, name, salary = record.strip().split(",")
    total_salary += int(salary)

average_salary = total_salary / len(records)

print("\nAverage Salary: ₹", average_salary)

# --------------------------------------------------
# Task 5: Generate salary categories
# High (≥ ₹60,000)
# Medium (₹40,000 – ₹59,999)
# Low (< ₹40,000)
# --------------------------------------------------

high_salary = []
medium_salary = []
low_salary = []

for record in records:

    emp_id, name, salary = record.strip().split(",")
    salary = int(salary)

    if salary >= 60000:
        high_salary.append(name)

    elif salary >= 40000:
        medium_salary.append(name)

    else:
        low_salary.append(name)

print("\nHigh Salary:")
print(high_salary)

print("\nMedium Salary:")
print(medium_salary)

print("\nLow Salary:")
print(low_salary)

# Close the file
file.close()