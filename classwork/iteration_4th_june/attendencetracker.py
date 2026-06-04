present = 0
absent = 0
i = 1

while i <= 30:
    status = input("Student " + str(i) + " Attendance (P/A): ")

    if status == "P" or status == "p":
        present = present + 1
    else:
        absent = absent + 1

    i = i + 1

print("No. of Students Present :", present)
print("No. of Students Absent :", absent)