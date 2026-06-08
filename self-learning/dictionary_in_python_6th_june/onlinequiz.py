# --------------------------------------------------
# Problem Statement:
# Analyze online quiz scores and perform the following:
# 1. Display students scoring 15 or above.
# 2. Count students scoring below 10.
# 3. Find the top performer.
# 4. Create a list of students who passed
#    (marks >= 10).
# 5. Calculate the class average.
# --------------------------------------------------
# Sample Data
quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# --------------------------------------------------
# Validation Section
# --------------------------------------------------

is_valid = True

# Check whether quiz_scores is a dictionary
if not isinstance(quiz_scores, dict):
    print("Invalid data: Quiz scores should be stored in a dictionary.")
    is_valid = False

# Validate student IDs and scores
if is_valid:
    for student_id, score in quiz_scores.items():

        # Student ID must be a string
        if not isinstance(student_id, str):
            print("Invalid student ID found.")
            is_valid = False
            break

        # Score must be numeric
        if not isinstance(score, (int, float)):
            print(f"Invalid score for {student_id}.")
            is_valid = False
            break

        # Score must be between 0 and 20
        if score < 0 or score > 20:
            print(f"Score out of range for {student_id}.")
            is_valid = False
            break

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

if is_valid:

    # Students scoring 15 or above
    high_scorers = [
        student_id for student_id, score in quiz_scores.items()
        if score >= 15
    ]

    # Count students scoring below 10
    below_10_count = sum(
        1 for score in quiz_scores.values()
        if score < 10
    )

    # Find top performer
    top_performer = max(quiz_scores, key=quiz_scores.get)
    highest_score = quiz_scores[top_performer]

    # Students who passed (>= 10)
    passed_students = [
        student_id for student_id, score in quiz_scores.items()
        if score >= 10
    ]

    # Calculate class average
    class_average = sum(quiz_scores.values()) / len(quiz_scores)

    # --------------------------------------------------
    # Output Section
    # --------------------------------------------------

    print("Students scoring 15 or above:")
    print(high_scorers)

    print("\nNumber of students scoring below 10:")
    print(below_10_count)

    print("\nTop performer:")
    print(f"{top_performer} - {highest_score}")

    print("\nStudents who passed:")
    print(passed_students)

    print("\nClass Average:")
    print(f"{class_average:.2f}")