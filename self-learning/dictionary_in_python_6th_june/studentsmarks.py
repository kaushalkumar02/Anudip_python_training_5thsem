# --------------------------------------------------
# Problem Statement:
# Analyze student marks and perform the following:
# 1. Display students scoring 80 or above.
# 2. Count the number of students who failed (marks < 40).
# 3. Find the highest scorer.
# 4. Create a list of students scoring between 60 and 75.
# 5. Assign grades:
#       A : marks >= 90
#       B : 75 - 89
#       C : 50 - 74
#       F : marks < 50
# -------------------------------------------------
# Sample Data
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# --------------------------------------------------
# Validation Section
# --------------------------------------------------

is_valid = True

# Check whether marks is a dictionary
if not isinstance(marks, dict):
    print("Invalid data: Marks should be stored in a dictionary.")
    is_valid = False

# Check each student name and mark
if is_valid:
    for student, score in marks.items():

        # Student name must be a string
        if not isinstance(student, str):
            print("Invalid student name found.")
            is_valid = False
            break

        # Marks must be numeric and between 0 and 100
        if not isinstance(score, (int, float)):
            print(f"Invalid marks for {student}.")
            is_valid = False
            break

        if score < 0 or score > 100:
            print(f"Marks out of range for {student}.")
            is_valid = False
            break

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

if is_valid:

    # Students scoring 80 or above
    high_scorers = [student for student, score in marks.items() if score >= 80]

    # Count failed students
    failed_count = sum(1 for score in marks.values() if score < 40)

    # Find highest scorer
    topper = max(marks, key=marks.get)
    highest_marks = marks[topper]

    # Students scoring between 60 and 75
    between_60_75 = [
        student for student, score in marks.items()
        if 60 <= score <= 75
    ]

    # Grade assignment
    grades = {}

    for student, score in marks.items():

        if score >= 90:
            grades[student] = "A"

        elif score >= 75:
            grades[student] = "B"

        elif score >= 50:
            grades[student] = "C"

        else:
            grades[student] = "F"

    # --------------------------------------------------
    # Output Section
    # --------------------------------------------------

    print("Students scoring 80 or above:")
    print(high_scorers)

    print("\nNumber of failed students:")
    print(failed_count)

    print("\nHighest scorer:")
    print(f"{topper} - {highest_marks}")

    print("\nStudents scoring between 60 and 75:")
    print(between_60_75)

    print("\nGrades:")
    for student, grade in grades.items():
        print(f"{student}: {grade}")