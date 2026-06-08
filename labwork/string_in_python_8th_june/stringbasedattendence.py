# Problem Statement:
# String-Based Attendance Tracker
# Attendance of a student for 15 days:
# "PPAPPPAAPPPPAPP"
# Rules:
# P = Present
# A = Absent
# Tasks:
# 1. Count Present and Absent days
# 2. Calculate attendance percentage
# 3. Find longest consecutive Present streak
# 4. Find longest consecutive Absent streak
# 5. Check if attendance is below 75%
attendance = "PPAPPPAAPPPPAPP"

# 1. Count Present and Absent
present_days = attendance.count("P")
absent_days = attendance.count("A")

# 2. Attendance percentage
total_days = len(attendance)
percentage = (present_days / total_days) * 100

# 3. Longest Present streak
max_p = 0
current_p = 0

# 4. Longest Absent streak
max_a = 0
current_a = 0

for ch in attendance:
    if ch == "P":
        current_p += 1
        current_a = 0
        max_p = max(max_p, current_p)
    else:
        current_a += 1
        current_p = 0
        max_a = max(max_a, current_a)

# 5. Attendance status
status = "Below 75%" if percentage < 75 else "Above 75%"

# Output
print("Attendance Record:", attendance)
print("Present Days:", present_days)
print("Absent Days:", absent_days)
print("Attendance Percentage: {:.2f}%".format(percentage))
print("Longest Present Streak:", max_p)
print("Longest Absent Streak:", max_a)
print("Attendance Status:", status)