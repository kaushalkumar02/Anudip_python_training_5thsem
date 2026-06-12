# Problem 19: Word Frequency Analyzer

# Problem Statement:
# A text file contains the following paragraph.
#
# Sample Input/Data (article.txt)
# Python is easy to learn.
# Python is powerful.
# Python supports multiple programming paradigms.
# Programming with Python is enjoyable.
#
# Tasks:
# 1. Count the total number of words.
# 2. Count the frequency of each word.
# 3. Find the most frequently occurring word.
# 4. Display words appearing only once.
# 5. Display all unique words.
#
# Sample Output
# Total Words: 16
# Most Frequent Word: Python (4 times)
# Words Appearing Once:
# easy to learn powerful supports multiple paradigms with enjoyable
# Unique Words Count: 12

try:

    # Open article file in read mode
    file = open("article.txt", "r")

    # Read complete file content
    content = file.read()

    # Close file
    file.close()

    # Convert text into lowercase for accurate counting
    content = content.lower()

    # Remove punctuation marks
    content = content.replace(".", "")

    # Split text into words
    words = content.split()

    # Count total words
    total_words = len(words)

    # Create dictionary to store word frequencies
    frequency = {}

    # Count frequency of each word
    for word in words:

        if word in frequency:

            frequency[word] += 1

        else:

            frequency[word] = 1

    # Find most frequent word
    most_frequent_word = ""
    highest_count = 0

    for word, count in frequency.items():

        if count > highest_count:

            highest_count = count
            most_frequent_word = word

    # Find words appearing only once
    words_once = []

    for word, count in frequency.items():

        if count == 1:

            words_once.append(word)

    # Find all unique words
    unique_words = set(words)

    # Display results
    print("Total Words:", total_words)

    print("Word Frequency Dictionary:")
    print(frequency)

    print("Most Frequent Word:",
          most_frequent_word.capitalize(),
          "(" + str(highest_count) + " times)")

    print("Words Appearing Once:")
    print(" ".join(words_once))

    print("Unique Words Count:", len(unique_words))

    print("Unique Words:")
    print(unique_words)

except FileNotFoundError:

    print("Error: article.txt file not found.")

except Exception as e:

    print("Error:", e)

finally:

    print("Word frequency analysis completed.")