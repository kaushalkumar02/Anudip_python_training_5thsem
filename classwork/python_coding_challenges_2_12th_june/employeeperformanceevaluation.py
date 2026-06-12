'''Employee Performance Evaluation System 
Problem Statement 
Employee performance scores are stored below. 
Sample Data 
performance = { 
    "EMP101": 92, 
    "EMP102": 78, 
    "EMP103": 45, 
    "EMP104": 88, 
    "EMP105": 97, 
    "EMP106": 56, 
    "EMP107": 81, 
    "EMP108": 64, 
    "EMP109": 39, 
    "EMP110": 73 
} 
Tasks 
1. Display employees scoring above 80.  
2. Count employees needing improvement (score < 60).  
3. Find the top performer.  
4. Calculate average performance score.  
5. Categorize employees:  
o Excellent (≥ 90)  
o Good (75–89)  
o Average (60–74)  
o Poor (< 60)  
Sample Output 
Employees Scoring Above 80: 
EMP101 
EMP104 
EMP105 
EMP107 
 
Employees Needing Improvement: 3 
 
Top Performer: 
EMP105 (97) 
 
Average Score: 71.3 
 
Excellent: 
['EMP101', 'EMP105'] 
 
Good: 
['EMP102', 'EMP104', 'EMP107'] 
 
Average: 
['EMP108', 'EMP110'] 
 
Poor: 
['EMP103', 'EMP106', 'EMP109'] 
'''

# Employee Performance Evaluation System

# Dictionary storing employee IDs and performance scores
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# --------------------------------------------------
# Task 1: Display employees scoring above 80
# --------------------------------------------------

print("Employees Scoring Above 80:")

for emp_id, score in performance.items():
    if score > 80:
        print(emp_id)

# --------------------------------------------------
# Task 2: Count employees needing improvement
# (Score less than 60)
# --------------------------------------------------

improvement_count = 0

for score in performance.values():
    if score < 60:
        improvement_count += 1

print("\nEmployees Needing Improvement:", improvement_count)

# --------------------------------------------------
# Task 3: Find the top performer
# --------------------------------------------------

top_employee = list(performance.keys())[0]
highest_score = performance[top_employee]

for emp_id, score in performance.items():

    if score > highest_score:
        highest_score = score
        top_employee = emp_id

print("\nTop Performer:")
print(top_employee, f"({highest_score})")

# --------------------------------------------------
# Task 4: Calculate average performance score
# --------------------------------------------------

total_score = 0

for score in performance.values():
    total_score += score

average_score = total_score / len(performance)

print("\nAverage Score:", round(average_score, 1))

# --------------------------------------------------
# Task 5: Categorize employees
# Excellent (≥ 90)
# Good (75 – 89)
# Average (60 – 74)
# Poor (< 60)
# --------------------------------------------------

excellent = []
good = []
average = []
poor = []

for emp_id, score in performance.items():

    if score >= 90:
        excellent.append(emp_id)

    elif score >= 75:
        good.append(emp_id)

    elif score >= 60:
        average.append(emp_id)

    else:
        poor.append(emp_id)

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average)

print("\nPoor:")
print(poor)