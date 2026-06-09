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
# Product Review Analyzer

review = "This product is excellent excellent excellent and very useful"

# 1. Split sentence into words
words = review.split()

# 2. Total words
total_words = 0

for w in words:
    total_words = total_words + 1

# 3. Word frequency
freq = {}

for w in words:
    if w in freq:
        freq[w] = freq[w] + 1
    else:
        freq[w] = 1

# 4. Most frequent word
max_word = ""
max_count = 0

for w in freq:
    if freq[w] > max_count:
        max_count = freq[w]
        max_word = w

# 5. Words appearing only once
once_words = []

for w in freq:
    if freq[w] == 1:
        once_words.append(w)

# 6. Words having more than 5 characters
long_words = []

for w in words:
    if len(w) > 5:
        long_words.append(w)

# 7. Reverse words
reverse_words = []

for i in range(len(words)-1, -1, -1):
    reverse_words.append(words[i])

# 8. Unique words
unique_words = []

for w in words:
    if w not in unique_words:
        unique_words.append(w)

# OUTPUT
print("Total Words:", total_words)
print("Word Frequency:", freq)
print("Most Frequent Word:", max_word)
print("Words Appearing Once:", once_words)
print("Words > 5 letters:", long_words)
print("Reverse Order:", reverse_words)
print("Unique Words:", unique_words)
