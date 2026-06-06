# ------------------------------------------------------------
# Problem Statement:
# Employee Performance Evaluation System
#
# A company stores employee details in a tuple.
# Each employee record contains:
# 1. Employee ID
# 2. Employee Name
# 3. Performance Score
#
# Tasks:
# 1. Display details of employees scoring 80 or above.
# 2. Count the number of employees who need improvement
#    (score below 60).
# 3. Find the employee with the highest score.
# 4. Create a list containing the names of all employees
#    scoring above 75.
# 5. Display the performance category for each employee:
#    - 90 and above  -> Excellent
#    - 75 to 89      -> Good
#    - 60 to 74      -> Average
#    - Below 60      -> Needs Improvement
# ------------------------------------------------------------

# Employee records stored in a tuple
employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# 1. Display employees scoring 80 or above
print("Employees Scoring 80 or Above:")
for emp_id, name, score in employees:
    if score >= 80:
        print(emp_id, name, score)

# 2. Count employees needing improvement
improvement_count = 0

for emp_id, name, score in employees:
    if score < 60:
        improvement_count += 1

print("\nEmployees Needing Improvement:", improvement_count)

# 3. Find employee with highest score
highest_performer = max(employees, key=lambda employee: employee[2])

print("\nHighest Performer:")
print(
    highest_performer[0],
    highest_performer[1],
    highest_performer[2]
)

# 4. Create list of employees scoring above 75
high_performers = []

for emp_id, name, score in employees:
    if score > 75:
        high_performers.append(name)

print("\nHigh Performers:", high_performers)

# 5. Display performance category for each employee
print("\nPerformance Categories:")

for emp_id, name, score in employees:

    if score >= 90:
        category = "Excellent"

    elif score >= 75:
        category = "Good"

    elif score >= 60:
        category = "Average"

    else:
        category = "Needs Improvement"

    print(name, "->", category)