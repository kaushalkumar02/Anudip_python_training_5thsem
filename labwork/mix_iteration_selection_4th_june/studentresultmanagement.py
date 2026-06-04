m1 = int(input("Enter Subject 1 Marks: "))
m2 = int(input("Enter Subject 2 Marks: "))
m3 = int(input("Enter Subject 3 Marks: "))
m4 = int(input("Enter Subject 4 Marks: "))
m5 = int(input("Enter Subject 5 Marks: "))

total = m1 + m2 + m3 + m4 + m5
percent = total / 5

fail = 0
if m1 < 40: fail += 1
if m2 < 40: fail += 1
if m3 < 40: fail += 1
if m4 < 40: fail += 1
if m5 < 40: fail += 1

print("Total Marks:", total)
print("Percentage:", percent)

if percent >= 90:
    grade = "A+"
elif percent >= 75:
    grade = "A"
elif percent >= 60:
    grade = "B"
elif percent >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
print("Subjects Failed:", fail)