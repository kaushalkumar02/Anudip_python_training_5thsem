# Problem Statement:
# Attendance for 15 days is recorded using a list where:
# 'P' represents Present and 'A' represents Absent.
# attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
# Write a program to:
# • Count the number of present and absent days
# • Calculate the attendance percentage
# • Determine eligibility (minimum 75% attendance required)
# • Display the positions (day numbers) where the student was absent
# Attendance data
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
# Counters for present and absent days
present_count = 0
absent_count = 0
# List to store absent day numbers
absent_days = []

# Loop through attendance list
for i in range(len(attendance)):
    if attendance[i] == 'P':
        # If present, increase present counter
        present_count += 1
    else:
        # If absent, increase absent counter
        absent_count += 1
        # Store day number (index + 1)
        absent_days.append(i + 1)

# Total number of days
total_days = len(attendance)

# Calculate attendance percentage
attendance_percentage = (present_count / total_days) * 100

# Check eligibility (minimum 75% required)
if attendance_percentage >= 75:
    eligibility = "Eligible"
else:
    eligibility = "Not Eligible"

# Display results
print("Present Days:", present_count)
print("Absent Days:", absent_count)
print("Attendance Percentage:", round(attendance_percentage, 2), "%")
print("Eligibility Status:", eligibility)
print("Absent Days (Positions):", absent_days)