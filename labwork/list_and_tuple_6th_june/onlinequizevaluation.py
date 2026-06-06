# Problem Statement:
# A quiz has correct answers and a student's answers stored in two lists.
# correct = ['A', 'C', 'B', 'D', 'A']
# student = ['A', 'B', 'B', 'D', 'C']
# Write a program to:
# • Calculate the score
# • Display incorrectly answered question numbers
# • Count correct and wrong answers
# • Determine pass/fail (minimum 60% required)
# Correct answers
correct = ['A', 'C', 'B', 'D', 'A']
# Student answers
student = ['A', 'B', 'B', 'D', 'C']
# Counters
correct_count = 0
wrong_count = 0
# List to store wrong question numbers
wrong_questions = []
# Loop through answers
for i in range(len(correct)):
    if student[i] == correct[i]:
        # Correct answer
        correct_count += 1
    else:
        # Wrong answer
        wrong_count += 1
        wrong_questions.append(i + 1)  # store question number (1-based)

# Calculate score in percentage
total_questions = len(correct)
score = (correct_count / total_questions) * 100

# Determine result (minimum 60% required)
if score >= 60:
    result = "Pass"
else:
    result = "Fail"

# Display results
print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)
print("Score:", round(score, 2), "%")
print("Wrong Question Numbers:", wrong_questions)
print("Result:", result)