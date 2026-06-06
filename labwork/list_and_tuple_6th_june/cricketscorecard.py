# ------------------------------------------------------------
# Problem Statement:
# Cricket Tournament Scorecard Analysis
# A batsman’s scores in different matches are stored in a list.
# Objective:
# Write a Python program to analyze the performance of the batsman
# using the given scores.
# Tasks:
# • Count half-centuries (50–99) and centuries (100+)
# • Find the highest score
# • Display all scores below 20
# • Calculate the average score
# ------------------------------------------------------------
# List of scores
scores = [45, 78, 12, 100, 67, 8, 90, 55]

# 1. Count half-centuries and centuries
half_centuries = 0
centuries = 0

for score in scores:
    if 50 <= score < 100:
        half_centuries += 1
    elif score >= 100:
        centuries += 1

print("Half-centuries:", half_centuries)
print("Centuries:", centuries)

# 2. Find the highest score
highest_score = max(scores)

print("\nHighest Score:", highest_score)

# 3. Display all scores below 20
print("\nScores below 20:")

for score in scores:
    if score < 20:
        print(score)

# 4. Calculate average score
total = 0

for score in scores:
    total += score

average = total / len(scores)

print("\nAverage Score:", average)