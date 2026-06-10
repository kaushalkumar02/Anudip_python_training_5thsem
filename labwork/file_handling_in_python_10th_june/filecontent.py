# ==========================================================
# Class Work: File Handling in Python
#
# Program Name: File Content Analyzer
#
# Problem Statement:
# A publishing company maintains articles in text files
# and wants to generate basic statistics about the content.
#
# Requirements:
# 1. Total number of vowels
# 2. Total number of characters
# 3. Total number of lines
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
    count = 0

    for ch in data:
        count += 1

    return count


# Function to count lines
def count_lines(data):
    count = 1

    for ch in data:
        if ch == "\n":
            count += 1

    return count


# Main Function
def file_analyzer():

    try:
        file = open("article.txt", "r")

        data = file.read()

        file.close()

        vowels = count_vowels(data)
        characters = count_characters(data)
        lines = count_lines(data)

        print("\nFile Analysis Report")
        print("-" * 35)
        print("Total Number of Vowels    :", vowels)
        print("Total Number of Characters:", characters)
        print("Total Number of Lines     :", lines)

    except FileNotFoundError:
        print("Error: article.txt file not found!")
        print("Please create article.txt in the same folder.")


# Function Call
file_analyzer()