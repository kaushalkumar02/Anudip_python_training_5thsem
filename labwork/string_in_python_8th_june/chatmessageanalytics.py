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

# Split message into words
words = message.split()

# 1. Total characters (excluding spaces OR including spaces depends on requirement)
total_characters = len(message)

# 2. Total words
total_words = len(words)

# 3. Longest and shortest word
longest_word = max(words, key=len)
shortest_word = min(words, key=len)

# 4. Occurrences of "Python"
python_count = words.count("Python")

# 5. Words having more than 4 characters
long_words = [word for word in words if len(word) > 4]

# 6. Words starting with a vowel
vowels = "aeiouAEIOU"
vowel_start_words = [word for word in words if word[0] in vowels]

# 7. Count vowels and consonants
vowel_count = 0
consonant_count = 0

for ch in message:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Output
print("Message:", message)
print("Total Characters:", total_characters)
print("Total Words:", total_words)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Occurrences of Python:", python_count)
print("Words Longer Than 4 Characters:", long_words)
print("Words Starting With Vowel:", vowel_start_words)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)58