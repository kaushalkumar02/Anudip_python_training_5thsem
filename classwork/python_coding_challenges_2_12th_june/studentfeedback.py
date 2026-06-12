'''Student Feedback Analysis System 
Problem Statement 
A training institute collects feedback from students after completing a Python course. The feedback 
comments are stored in a text file named feedback.txt. 
Sample Input/Data (feedback.txt) 
The sessions were very interactive and informative. 
Excellent teaching methodology and practical examples. 
The pace of the course was appropriate. 
More real-world projects should be included. 
The trainer explained concepts very clearly. 
Tasks 
1. Count the total number of lines.  
2. Count the total number of words.  
3. Count the total number of characters.  
4. Find the longest feedback comment.  
5. Find the shortest feedback comment.  
6. Count the total number of vowels present in the file.  
Sample Output 
Total Lines: 5 
 
Total Words: 35 
 
Total Characters: 220 
 
Longest Feedback: 
Excellent teaching methodology and practical examples. 
 
Shortest Feedback: 
The pace of the course was appropriate. 
 
Total Vowels: 76'''

# Student Feedback Analysis System

# Open the file in read mode
file = open("feedback.txt", "r")

# Read all lines from the file
lines = file.readlines()

# --------------------------------------------------
# Task 1: Count the total number of lines
# --------------------------------------------------

total_lines = len(lines)

print("Total Lines:", total_lines)

# --------------------------------------------------
# Task 2: Count the total number of words
# --------------------------------------------------

total_words = 0

for line in lines:
    words = line.split()
    total_words += len(words)

print("\nTotal Words:", total_words)

# --------------------------------------------------
# Task 3: Count the total number of characters
# --------------------------------------------------

total_characters = 0

for line in lines:
    total_characters += len(line)

print("\nTotal Characters:", total_characters)

# --------------------------------------------------
# Task 4: Find the longest feedback comment
# --------------------------------------------------

longest_feedback = lines[0].strip()

for line in lines:
    if len(line.strip()) > len(longest_feedback):
        longest_feedback = line.strip()

print("\nLongest Feedback:")
print(longest_feedback)

# --------------------------------------------------
# Task 5: Find the shortest feedback comment
# --------------------------------------------------

shortest_feedback = lines[0].strip()

for line in lines:
    if len(line.strip()) < len(shortest_feedback):
        shortest_feedback = line.strip()

print("\nShortest Feedback:")
print(shortest_feedback)

# --------------------------------------------------
# Task 6: Count the total number of vowels
# --------------------------------------------------

vowel_count = 0
vowels = "AEIOUaeiou"

for line in lines:
    for ch in line:
        if ch in vowels:
            vowel_count += 1

print("\nTotal Vowels:", vowel_count)

# Close the file
file.close()