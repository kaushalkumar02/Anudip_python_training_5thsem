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

employee_id = "EMP2026ANUJ458"

# Count uppercase letters
uppercase_count = sum(1 for ch in employee_id if ch.isupper())

# Count digits
digit_count = sum(1 for ch in employee_id if ch.isdigit())

# Extract joining year
joining_year = employee_id[3:7]

# Extract employee name
employee_name = employee_id[7:-3]

# Validation checks
starts_with_emp = employee_id.startswith("EMP")
year_valid = employee_id[3:7].isdigit() and len(employee_id[3:7]) == 4
ends_with_3_digits = employee_id[-3:].isdigit()

is_valid = starts_with_emp and year_valid and ends_with_3_digits

# List of digits
digit_list = [int(ch) for ch in employee_id if ch.isdigit()]

# Sum of digits
digit_sum = sum(digit_list)

# Result status
status = "Valid" if is_valid else "Invalid"

# Output
print("Employee ID:", employee_id)
print("Uppercase Letters:", uppercase_count)
print("Digits:", digit_count)
print("Joining Year:", joining_year)
print("Employee Name:", employee_name)
print("Digit List:", digit_list)
print("Sum of Digits:", digit_sum)
print("ID Status:", status)