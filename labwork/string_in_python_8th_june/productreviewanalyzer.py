# Problem Statement:
# Product Review Analyzer
# A customer submits a review:
# "This product is excellent excellent excellent and very useful"
# Tasks:
# 1. Count total words
# 2. Create word frequency dictionary
# 3. Find most frequently used word
# 4. Find words appearing only once
# 5. Count words having more than 5 characters
# 6. Display words in reverse order
# 7. Create list of unique word
review = "This product is excellent excellent excellent and very useful"
# Split into words
words = review.split()
# 1. Total words
total_words = len(words)
# 2. Word frequency dictionary
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
# 3. Most frequent word
most_frequent = max(freq, key=freq.get)
# 4. Words appearing only once
once_words = [word for word in freq if freq[word] == 1]

# 5. Words having more than 5 characters
long_words = [word for word in words if len(word) > 5]

# 6. Words in reverse order
reverse_words = words[::-1]

# 7. Unique words list
unique_words = list(freq.keys())

# Output
print("Review:", review)
print("Total Words:", total_words)

print("\nWord Frequencies:")
for word, count in freq.items():
    print(word, "->", count)

print("\nMost Frequent Word:", most_frequent)
print("Words Appearing Once:", once_words)
print("Words Longer Than 5 Characters:", long_words)
print("Words in Reverse Order:", reverse_words)
print("Unique Words:", unique_words)