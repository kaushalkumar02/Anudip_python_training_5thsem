# List of student marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# list for passed students (marks >= 40)
passed = []

# counter for failed students
failed_count = 0

# finding highest and lowest without max/min
highest = marks[0]
lowest = marks[0]

# list for merit students (marks > 75)
merit = []

# loop through all marks
for m in marks:

    # check pass or fail
    if m >= 40:
        passed.append(m)
    else:
        failed_count += 1

    # update highest mark
    if m > highest:
        highest = m

    # update lowest mark
    if m < lowest:
        lowest = m

    # check merit condition
    if m > 75:
        merit.append(m)

# output results
print("Passed Students:", passed)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit)