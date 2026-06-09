# Problem Statement:
# Employee ID Validation and Analysis System
# A company generates employee IDs in the format: EMP2026ANUJ458
# Write a program to:
# 1. Count the number of uppercase letters
# 2. Count the number of digits
# 3. Extract the joining year
# 4. Extract the employee name
# 5. Check whether the ID follows rules:
#    - Starts with "EMP"
#    - Contains exactly 4 digits for the year
#    - Ends with exactly 3 digits
# 6. Create a list containing all digits
# 7. Find sum of all digits
# 8. Display whether ID is valid or invalid

emp_id = "EMP2026ANUJ458"

# 1. Count uppercase letters
upper_count = 0

# 2. Count digits
digit_count = 0

# list of digits
digit_list = []

for ch in emp_id:
    if ch.isupper():
        upper_count = upper_count + 1

    elif ch.isdigit():
        digit_count = digit_count + 1
        digit_list.append(ch)

# 3. Extract joining year (position fixed)
joining_year = emp_id[3:7]

# 4. Extract employee name
employee_name = emp_id[7:11]

# 5. Validation rules
rule1 = False
rule2 = False
rule3 = False

# starts with EMP
if emp_id[0:3] == "EMP":
    rule1 = True

# year is 4 digits
if emp_id[3:7].isdigit():
    rule2 = True

# last 3 digits
if emp_id[-3:].isdigit():
    rule3 = True

# final validation
if rule1 and rule2 and rule3:
    status = "Valid ID"
else:
    status = "Invalid ID"

# sum of digits
digit_sum = 0
for d in digit_list:
    digit_sum = digit_sum + int(d)

# OUTPUT
print("Employee ID:", emp_id)
print("Uppercase Letters:", upper_count)
print("Digits Count:", digit_count)
print("Joining Year:", joining_year)
print("Employee Name:", employee_name)
print("Digits List:", digit_list)
print("Sum of Digits:", digit_sum)
print("ID Status:", status)
