# =====================================================
# PROBLEM STATEMENT:
# Student Performance System using Dictionary
# =====================================================
# -----------------------------------------------------
# STUDENT DATA STORE (Dictionary)
# Use: Store 30 students with ID as key and details as value
# -----------------------------------------------------
students = {
    "S101": {"name": "Aman", "marks": 85},
    "S102": {"name": "Riya", "marks": 92},
    "S103": {"name": "Rahul", "marks": 67},
    "S104": {"name": "Sneha", "marks": 74},
    "S105": {"name": "Vikas", "marks": 88},
    "S106": {"name": "Neha", "marks": 45},
    "S107": {"name": "Karan", "marks": 56},
    "S108": {"name": "Pooja", "marks": 78},
    "S109": {"name": "Amit", "marks": 91},
    "S110": {"name": "Sonia", "marks": 69},
    "S111": {"name": "Raj", "marks": 82},
    "S112": {"name": "Meena", "marks": 73},
    "S113": {"name": "Yash", "marks": 64},
    "S114": {"name": "Isha", "marks": 95},
    "S115": {"name": "Deepak", "marks": 58},
    "S116": {"name": "Anjali", "marks": 87},
    "S117": {"name": "Mohit", "marks": 49},
    "S118": {"name": "Kavya", "marks": 76},
    "S119": {"name": "Nikhil", "marks": 81},
    "S120": {"name": "Tanya", "marks": 90},
    "S121": {"name": "Rohit", "marks": 66},
    "S122": {"name": "Simran", "marks": 72},
    "S123": {"name": "Arjun", "marks": 59},
    "S124": {"name": "Divya", "marks": 84},
    "S125": {"name": "Harsh", "marks": 77},
    "S126": {"name": "Kriti", "marks": 93},
    "S127": {"name": "Sahil", "marks": 52},
    "S128": {"name": "Manish", "marks": 68},
    "S129": {"name": "Priya", "marks": 80},
    "S130": {"name": "Ayesha", "marks": 86}
}
# -----------------------------------------------------
# DISPLAY ALL STUDENTS
# Use: Show complete student list
# -----------------------------------------------------

print("\n--- ALL STUDENTS ---")

for sid in students:
    print(sid, "=>", students[sid])

# -----------------------------------------------------
# SEARCH STUDENT
# Use: Find student using ID
# -----------------------------------------------------
sid = input("\nEnter Student ID to search: ")
if sid in students:
    print("Student Found:", students[sid])
else:
    print("Student not found")
# -----------------------------------------------------
# ADD NEW STUDENT
# Use: Insert new student record in dictionary
# -----------------------------------------------------
print("\n--- ADD STUDENT ---")
new_id = input("Enter ID: ")
name = input("Enter Name: ")
marks = int(input("Enter Marks: "))
students[new_id] = {"name": name, "marks": marks}
print("Student Added Successfully")
# -----------------------------------------------------
# UPDATE MARKS
# Use: Modify existing student marks
# -----------------------------------------------------

print("\n--- UPDATE MARKS ---")
uid = input("Enter Student ID: ")
if uid in students:
    new_marks = int(input("Enter new marks: "))
    students[uid]["marks"] = new_marks
    print("Marks Updated Successfully")
else:
    print("Student not found")
# -----------------------------------------------------
# DELETE STUDENT
# Use: Remove student record from dictionary
# -----------------------------------------------------

print("\n--- DELETE STUDENT ---")

did = input("Enter Student ID: ")

if did in students:
    del students[did]
    print("Student Deleted Successfully")
else:
    print("Student not found")
# -----------------------------------------------------
# TOPPER AND LOWEST SCORER
# Use: Find highest and lowest marks student
# -----------------------------------------------------

topper_id = ""
lowest_id = ""

top_marks = -1
low_marks = 101

for i in students:
    if students[i]["marks"] > top_marks:
        top_marks = students[i]["marks"]
        topper_id = i

    if students[i]["marks"] < low_marks:
        low_marks = students[i]["marks"]
        lowest_id = i

print("\nTopper:", students[topper_id])
print("Lowest:", students[lowest_id])
# -----------------------------------------------------
# CLASS AVERAGE
# Use: Calculate average marks of all students
# -----------------------------------------------------

total = 0

for i in students:
    total = total + students[i]["marks"]

avg = total / len(students)

print("\nClass Average =", avg)

# -----------------------------------------------------
# PASS AND FAIL COUNT
# Use: Count students based on passing marks
# -----------------------------------------------------
pass_count = 0
fail_count = 0

for i in students:
    if students[i]["marks"] >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("\nPass Students:", pass_count)
print("Fail Students:", fail_count)

# -----------------------------------------------------
# GRADES ASSIGNMENT
# Use: Assign grade based on marks range
# -----------------------------------------------------

print("\n--- GRADES ---")

for i in students:
    m = students[i]["marks"]

    if m >= 90:
        print(students[i]["name"], "=> A")
    elif m >= 75:
        print(students[i]["name"], "=> B")
    elif m >= 50:
        print(students[i]["name"], "=> C")
    else:
        print(students[i]["name"], "=> F")

# -----------------------------------------------------
# SCHOLARSHIP STUDENTS
# Use: Find students scoring above 85
# -----------------------------------------------------

print("\n--- SCHOLARSHIP STUDENTS ---")

for i in students:
    if students[i]["marks"] > 85:
        print(i, students[i])