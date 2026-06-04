# Employee Salary Calculator

name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Salary: "))

hra = basic * 0.20
da = basic * 0.10
pf = basic * 0.12

gross = basic + hra + da
net = gross - pf

print("\nEmployee Name:", name)
print("Gross Salary:", gross)
print("Net Salary:", net)

if net > 50000:
    print("Grade: Senior")
elif net > 30000:
    print("Grade: Mid")
else:
    print("Grade: Junior")