# Problem Statement:
# Chat Message Analytics System
# Message: "Python is awesome and Python is easy to learn"
# Tasks:
# 1. Count total characters
# 2. Count total words
# 3. Find longest word
# 4. Find shortest word
# 5. Count occurrences of "Python"
# 6. List words having more than 4 characters
# 7. Display words starting with a vowel
# 8. Count vowels and consonants

message = "Python is awesome and Python is easy to learn"

# split into words
words = message.split()

# 1. total characters
total_characters = 0
for ch in message:
    total_characters = total_characters + 1

# 2. total words
total_words = 0
for w in words:
    total_words = total_words + 1

# 3. longest word
longest_word = ""
for w in words:
    if len(w) > len(longest_word):
        longest_word = w

# 4. shortest word
shortest_word = words[0]
for w in words:
    if len(w) < len(shortest_word):
        shortest_word = w

# 5. occurrences of "Python"
python_count = 0
for w in words:
    if w == "Python":
        python_count = python_count + 1

# 6. words > 4 characters
long_words = []
for w in words:
    if len(w) > 4:
        long_words.append(w)

# 7. words starting with vowel
vowels = "aeiouAEIOU"
vowel_words = []
for w in words:
    if w[0] in vowels:
        vowel_words.append(w)

# 8. vowels and consonants count
vowel_count = 0
consonant_count = 0

for ch in message:
    if ch.isalpha():
        if ch in vowels:
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1

# OUTPUT
print("Message:", message)
print("Total Characters:", total_characters)
print("Total Words:", total_words)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Python Count:", python_count)
print("Words > 4 characters:", long_words)
print("Words starting with vowel:", vowel_words)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
