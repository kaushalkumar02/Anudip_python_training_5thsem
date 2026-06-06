#Create dictionary for employee records

emp = {}

# Input records of 10 employees
for i in range(10):
    emp_id = input("Enter Employee ID : ")
    salary = int(input("Enter Salary : "))
    
    emp[emp_id] = salary

# Count employees having salary greater than 30000
count = 0

for sal in emp.values():
    if sal > 30000:
        count += 1

print("Total employees having salary greater than 30000 =", count)

# Display employees having salary below 20000
print("Employees having salary below 20000 :")

for eid, sal in emp.items():
    if sal < 20000:
        print(eid, ":", sal)