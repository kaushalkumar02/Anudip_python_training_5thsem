# Problem Statement:
# Student marks are stored in results.txt.
# File Format:
# S101,Anuj,85
# S102,Rahul,72
# S103,Priya,96
# S104,Neha,68
# S105,Amit,39
# S106,Sneha,54
# S107,Karan,91
# S108,Pooja,78
# S109,Rohit,47
# S110,Anjali,88
# Requirements:
# 1. Display all student records.
# 2. Search a student using Student ID.
# 3. Find topper and lowest scorer.
# 4. Calculate class average.
# 5. Count pass and fail students.
# 6. Generate grades:
#    A (90+)
#    B (75-89)
#    C (40-74)
#    F (<40)
# 7. Write grade reports into a new file.
# ==========================================================

# Function to display all student records
def display_records():

    file = open("results.txt", "r")

    print("\nStudent Records")
    print("-" * 40)

    for line in file:
        print(line.strip())

    file.close()


# Function to search student by ID
def search_student():

    student_id = input("Enter Student ID: ")

    file = open("results.txt", "r")

    found = False

    for line in file:

        data = line.strip().split(",")

        if data[0] == student_id:

            print("\nStudent Found")
            print("ID    :", data[0])
            print("Name  :", data[1])
            print("Marks :", data[2])

            found = True
            break

    if found == False:
        print("Student not found!")

    file.close()


# Function to find topper and lowest scorer
def topper_lowest():

    file = open("results.txt", "r")

    students = []

    for line in file:
        students.append(line.strip().split(","))

    file.close()

    topper = students[0]
    lowest = students[0]

    for student in students:

        if int(student[2]) > int(topper[2]):
            topper = student

        if int(student[2]) < int(lowest[2]):
            lowest = student

    print("\nTopper")
    print(topper[0], topper[1], topper[2])

    print("\nLowest Scorer")
    print(lowest[0], lowest[1], lowest[2])


# Function to calculate class average
def class_average():

    file = open("results.txt", "r")

    total = 0
    count = 0

    for line in file:

        data = line.strip().split(",")

        total = total + int(data[2])
        count = count + 1

    file.close()

    average = total / count

    print("Class Average =", average)


# Function to count pass and fail students
def pass_fail_count():

    file = open("results.txt", "r")

    pass_count = 0
    fail_count = 0

    for line in file:

        data = line.strip().split(",")

        if int(data[2]) >= 40:
            pass_count += 1
        else:
            fail_count += 1

    file.close()

    print("Pass Students :", pass_count)
    print("Fail Students :", fail_count)


# Function to generate grades
def generate_grades():

    file = open("results.txt", "r")

    print("\nGrade Report")
    print("-" * 40)

    for line in file:

        data = line.strip().split(",")

        marks = int(data[2])

        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        print(data[1], "->", grade)

    file.close()


# Function to write grades into new file
def write_grade_report():

    file = open("results.txt", "r")

    report = open("grades.txt", "w")

    for line in file:

        data = line.strip().split(",")

        marks = int(data[2])

        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        report.write(data[0] + "," +
                     data[1] + "," +
                     str(marks) + "," +
                     grade + "\n")

    file.close()
    report.close()

    print("Grade report written successfully to grades.txt")


# Main Menu
while True:

    print("\n===== Student Result Processing System =====")
    print("1. Display All Student Records")
    print("2. Search Student by ID")
    print("3. Find Topper and Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass and Fail Students")
    print("6. Generate Grades")
    print("7. Write Grade Report to File")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        display_records()

    elif choice == 2:
        search_student()

    elif choice == 3:
        topper_lowest()

    elif choice == 4:
        class_average()

    elif choice == 5:
        pass_fail_count()

    elif choice == 6:
        generate_grades()

    elif choice == 7:
        write_grade_report()

    elif choice == 8:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")