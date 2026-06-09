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
present = 0
absent = 0

for ch in attendance:
    if ch == "P":
        present = present + 1
    elif ch == "A":
        absent = absent + 1

# 2. Attendance percentage
total_days = len(attendance)
percentage = (present / total_days) * 100

# 3. Longest Present streak
max_p = 0
current_p = 0

for ch in attendance:
    if ch == "P":
        current_p = current_p + 1
        if current_p > max_p:
            max_p = current_p
    else:
        current_p = 0

# 4. Longest Absent streak
max_a = 0
current_a = 0

for ch in attendance:
    if ch == "A":
        current_a = current_a + 1
        if current_a > max_a:
            max_a = current_a
    else:
        current_a = 0

# 5. Check 75% rule
if percentage < 75:
    status = "Below 75% (Attendance Low)"
else:
    status = "Above 75% (OK)"

# OUTPUT
print("Attendance:", attendance)
print("Present Days:", present)
print("Absent Days:", absent)
print("Attendance Percentage:", percentage)
print("Longest Present Streak:", max_p)
print("Longest Absent Streak:", max_a)
print("Status:", status)
