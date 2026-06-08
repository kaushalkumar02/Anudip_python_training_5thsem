# --------------------------------------------------
# Problem Statement:
# Employee performance scores are stored as:
# Perform analysis on the given performance dictionary.
# --------------------------------------------------
# Sample Data
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
# Processing Section
# --------------------------------------------------

# 1. Employees scoring above 80
above_80 = [emp for emp, score in performance.items() if score > 80]

# 2. Count employees needing improvement (< 60)
need_improvement_count = sum(1 for score in performance.values() if score < 60)

# 3. Top performer
top_emp = max(performance, key=performance.get)
top_score = performance[top_emp]

# 4. Average performance score
avg_score = sum(performance.values()) / len(performance)

# 5. Performance categories
excellent = [emp for emp, score in performance.items() if score >= 90]
good = [emp for emp, score in performance.items() if 75 <= score <= 89]
average = [emp for emp, score in performance.items() if 60 <= score <= 74]
poor = [emp for emp, score in performance.items() if score < 60]

# --------------------------------------------------
# Output Section
# --------------------------------------------------

print("Employees Scoring Above 80:")
print(" ".join(above_80))

print("\nTop Performer:")
print(f"{top_emp} ({top_score})")

print("\nEmployees Needing Improvement:")
print(need_improvement_count)

print("\nAverage Score:")
print(round(avg_score, 1))

print("\nExcellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Poor:", poor)