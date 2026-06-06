# Problem Statement:
# Create an attendance tracker for 30 students.
# Take roll number and attendance status (Present/Absent) from user.
# Store data in a dictionary where:
# Key = Roll Number
# Value = Attendance (Present/Absent)
# Display roll numbers of students who are Present.

# Dictionary to store attendance
attendance = {}

# Input for 30 students
for i in range(5):
    roll_no = int(input("Enter Roll Number: "))
    status = input("Enter Attendance (Present/Absent): ").strip().capitalize()
    
    # Store data in dictionary
    attendance[roll_no] = status

print("\nStudents Present (Roll Numbers):")

# Display only present students
for roll_no, status in attendance.items():
    if status == "Present":
        print(roll_no)