# Problem 18: Student Attendance Percentage Calculator

# Problem Statement:
# The attendance status of a student for 15 days is represented as follows:
#
# Sample Data
# attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A',
#               'P', 'P', 'P', 'P', 'A', 'P', 'P')
#
# Tasks:
# 1. Count present days.
# 2. Count absent days.
# 3. Calculate attendance percentage.
# 4. Determine whether attendance is below 75%.
# 5. Display the attendance status.
#
# Sample Output
# Present Days: 11
# Absent Days: 4
# Attendance Percentage: 73.33%
# Attendance Status: Below 75%

try:

    # Store attendance data in a tuple
    attendance = ('P', 'P', 'A', 'P', 'P', 'P', 'A', 'A',
                  'P', 'P', 'P', 'P', 'A', 'P', 'P')

    # Count present days
    present_days = attendance.count('P')

    # Count absent days
    absent_days = attendance.count('A')

    # Count total days
    total_days = len(attendance)

    # Calculate attendance percentage
    attendance_percentage = (present_days / total_days) * 100

    # Display attendance details
    print("Present Days:", present_days)
    print("Absent Days:", absent_days)
    print("Attendance Percentage:", round(attendance_percentage, 2), "%")

    # Check attendance status
    if attendance_percentage < 75:

        print("Attendance Status: Below 75%")

    else:

        print("Attendance Status: Above 75%")

except Exception as e:

    # Handle unexpected errors
    print("Error:", e)

finally:

    # This block always executes
    print("Attendance calculation completed.")