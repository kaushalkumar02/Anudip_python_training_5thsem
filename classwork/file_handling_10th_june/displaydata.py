# ==========================================================
# Class Work: File Handling in Python
# Program:
# Read the data from file and display:
# 1. Number of Vowels
# 2. Number of Characters
# 3. Number of Lines
# ==========================================================

# Function to count vowels
def count_vowels(data):
    count = 0

    for ch in data:
        if ch in "aeiouAEIOU":
            count += 1

    return count

# Function to count characters
def count_characters(data):
    return len(data)

# Function to count lines
def count_lines(data):
    return len(data.split("\n"))

# Main Function
def file_analysis():

    file = open("article.txt", "r")

    data = file.read()

    file.close()

    print("\nFile Analysis Report")
    print("-" * 30)
    print("Number of Vowels    :", count_vowels(data))
    print("Number of Characters:", count_characters(data))
    print("Number of Lines     :", count_lines(data))

# Function Call
file_analysis()