
        # Problem Statement:
# Create a Student class to store the student's name, roll number,
# and marks obtained in three subjects.
#
# Implement methods to:
# 1. Accept student details.
# 2. Calculate the total marks.
# 3. Calculate the percentage.
# 4. Display the complete student report.
#
# Sample Output:
# Name       : Ananya
# Roll No    : 101
# Total Marks: 255
# Percentage : 85.0%

# Student Class
class Student:
    # --------------------------------------------------------------
    # Constructor to initialize student details
    def __init__(self, name, roll_no, mark1, mark2, mark3):
        self.__name = name
        self.__roll_no = roll_no
        self.__mark1 = mark1
        self.__mark2 = mark2
        self.__mark3 = mark3
# --------------------------------------------------------------
    # Method to calculate total marks
    def calculate_total(self):
        return self.__mark1 + self.__mark2 + self.__mark3
# --------------------------------------------------------------
    # Method to calculate percentage
    def calculate_percentage(self):
        return self.calculate_total() / 3
# --------------------------------------------------------------
    # Method to display student report
    def display_report(self):
        print("\nStudent Report")
        print("-" * 30)
        print("Name       :", self.__name)
        print("Roll No    :", self.__roll_no)
        print("Total Marks:", self.calculate_total())
        print("Percentage :", round(self.calculate_percentage(), 2), "%")


# Main Program

# Input validation for student name
while True:
    name = input("Enter Student Name: ").strip()
    if name:
        break
    print("Error: Name cannot be empty.")

# Input validation for roll number
while True:
    try:
        roll_no = int(input("Enter Roll Number: "))
        if roll_no > 0:
            break
        print("Error: Roll number must be positive.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# Input validation for marks
while True:
    try:
        mark1 = float(input("Enter Marks in Subject 1: "))
        mark2 = float(input("Enter Marks in Subject 2: "))
        mark3 = float(input("Enter Marks in Subject 3: "))

        # Marks should be between 0 and 100
        if (0 <= mark1 <= 100 and
            0 <= mark2 <= 100 and
            0 <= mark3 <= 100):
            break

        print("Error: Marks must be between 0 and 100.")

    except ValueError:
        print("Error: Please enter valid numeric marks.")

# Create Student Object
student = Student(name, roll_no, mark1, mark2, mark3)

# Display Student Report
student.display_report()
