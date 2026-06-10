'''News Article Text Analyzer 
Problem Statement 
A news agency wants to analyze the content of an article. 
Use a paragraph containing at least 300 words. 
Requirements 
1. Count total characters.  
2. Count total words.  
3. Count total sentences.  
4. Count vowels and consonants.  
5. Find longest word.  
6. Find shortest word.  
7. Find the most frequent word.  
8. Create a dictionary of word frequencies.  
9. Display words appearing only once.  
10. Display words appearing more than 5 times.  
11. Count words starting with each alphabet.  
12. Display all unique words.  
Challenge 
Generate a complete text summary: 
Total Words 
Total Sentences 
Average Word Length 
Most Frequent Word 
Vocabulary Size '''

# ==========================================
# NEWS ARTICLE TEXT ANALYZER
# ==========================================

print("Enter News Article (Minimum 300 Words):")

article = input()

# ==========================================
# TOTAL CHARACTERS
# ==========================================

total_characters = len(article)

# ==========================================
# TOTAL WORDS
# ==========================================

words = article.split()

total_words = len(words)

# ==========================================
# TOTAL SENTENCES
# ==========================================

total_sentences = 0

for ch in article:

    if ch == "." or ch == "!" or ch == "?":

        total_sentences += 1

# ==========================================
# VOWELS AND CONSONANTS
# ==========================================

vowels = 0
consonants = 0

for ch in article:

    if ch.isalpha():

        if ch.lower() in "aeiou":

            vowels += 1

        else:

            consonants += 1

# ==========================================
# LONGEST WORD
# ==========================================

longest_word = words[0]

for word in words:

    if len(word) > len(longest_word):

        longest_word = word

# ==========================================
# SHORTEST WORD
# ==========================================

shortest_word = words[0]

for word in words:

    if len(word) < len(shortest_word):

        shortest_word = word

# ==========================================
# WORD FREQUENCY DICTIONARY
# ==========================================

word_frequency = {}

for word in words:

    word = word.lower()

    if word in word_frequency:

        word_frequency[word] += 1

    else:

        word_frequency[word] = 1

# ==========================================
# MOST FREQUENT WORD
# ==========================================

most_frequent_word = ""

max_frequency = 0

for word, count in word_frequency.items():

    if count > max_frequency:

        max_frequency = count
        most_frequent_word = word

# ==========================================
# WORDS APPEARING ONLY ONCE
# ==========================================

print("\nWORDS APPEARING ONLY ONCE")

for word, count in word_frequency.items():

    if count == 1:

        print(word)

# ==========================================
# WORDS APPEARING MORE THAN 5 TIMES
# ==========================================

print("\nWORDS APPEARING MORE THAN 5 TIMES")

for word, count in word_frequency.items():

    if count > 5:

        print(word, "->", count)

# ==========================================
# WORDS STARTING WITH EACH ALPHABET
# ==========================================

alphabet_count = {}

for word in words:

    first_letter = word[0].lower()

    if first_letter.isalpha():

        if first_letter in alphabet_count:

            alphabet_count[first_letter] += 1

        else:

            alphabet_count[first_letter] = 1

print("\nWORDS STARTING WITH EACH ALPHABET")

for letter, count in alphabet_count.items():

    print(letter, "->", count)

# ==========================================
# DISPLAY UNIQUE WORDS
# ==========================================

print("\nUNIQUE WORDS")

for word in word_frequency:

    print(word)

# ==========================================
# AVERAGE WORD LENGTH
# ==========================================

total_length = 0

for word in words:

    total_length += len(word)

average_word_length = total_length / total_words

# ==========================================
# VOCABULARY SIZE
# ==========================================

vocabulary_size = len(word_frequency)

# ==========================================
# COMPLETE REPORT
# ==========================================

print("\n====================================")
print("NEWS ARTICLE ANALYSIS REPORT")
print("====================================")

print("Total Characters :", total_characters)

print("Total Words :", total_words)

print("Total Sentences :", total_sentences)

print("Vowels :", vowels)

print("Consonants :", consonants)

print("Longest Word :", longest_word)

print("Shortest Word :", shortest_word)

print("Most Frequent Word :", most_frequent_word)

print("Frequency :", max_frequency)

print("Vocabulary Size :", vocabulary_size)

print("Average Word Length :",round(average_word_length, 2))

# ==========================================
# WORD FREQUENCY DICTIONARY
# ==========================================

print("\nWORD FREQUENCY DICTIONARY")

print(word_frequency)