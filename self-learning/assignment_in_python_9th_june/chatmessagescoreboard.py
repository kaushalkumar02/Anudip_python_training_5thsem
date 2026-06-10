'''Chat Message Analytics Dashboard 
Problem Statement 
A messaging application wants to analyze chat messages. 
Store at least 20 chat messages in a list. 
Requirements 
For each message: 
1. Count total words.  
2. Count total characters.  
3. Count vowels and consonants.  
4. Find longest word.  
5. Find shortest word.  
6. Count occurrence of each word.  
7. Display repeated words.  
8. Display words starting with vowels.  
9. Display words longer than 5 characters.  
10. Create a dictionary containing word frequencies.  
Challenge 
Generate a report showing: 
Most Frequently Used Word 
Longest Message 
Shortest Message 
Average Words Per Message'''


# ==========================================
# CHAT MESSAGE ANALYTICS DASHBOARD
# ==========================================

# Store 20 chat messages

messages = []

for i in range(1, 21):

    msg = input(f"Enter Message {i}: ")

    messages.append(msg)

# Dictionary for word frequencies

word_frequency = {}

# Variables for challenge

total_words_all = 0

longest_message = messages[0]
shortest_message = messages[0]

# ==========================================
# ANALYZE EACH MESSAGE
# ==========================================

for msg in messages:

    print("\n================================")
    print("MESSAGE :", msg)
    print("================================")

    words = msg.split()

    # --------------------------------------
    # Total Words
    # --------------------------------------

    total_words = len(words)

    print("Total Words :", total_words)

    total_words_all += total_words

    # --------------------------------------
    # Total Characters
    # --------------------------------------

    total_characters = len(msg)

    print("Total Characters :", total_characters)

    # --------------------------------------
    # Vowels and Consonants
    # --------------------------------------

    vowels = 0
    consonants = 0

    for ch in msg:

        if ch.isalpha():

            if ch.lower() in "aeiou":

                vowels += 1

            else:

                consonants += 1

    print("Vowels :", vowels)
    print("Consonants :", consonants)

    # --------------------------------------
    # Longest Word
    # --------------------------------------

    if len(words) > 0:

        longest_word = words[0]

        for word in words:

            if len(word) > len(longest_word):

                longest_word = word

        print("Longest Word :", longest_word)

    # --------------------------------------
    # Shortest Word
    # --------------------------------------

        shortest_word = words[0]

        for word in words:

            if len(word) < len(shortest_word):

                shortest_word = word

        print("Shortest Word :", shortest_word)

    # --------------------------------------
    # Word Frequency
    # --------------------------------------

    for word in words:

        word = word.lower()

        if word in word_frequency:

            word_frequency[word] += 1

        else:

            word_frequency[word] = 1

    # --------------------------------------
    # Repeated Words
    # --------------------------------------

    print("Repeated Words :")

    repeated_found = False

    for word in words:

        if words.count(word) > 1:

            print(word)

            repeated_found = True

    if repeated_found == False:

        print("None")

    # --------------------------------------
    # Words Starting With Vowels
    # --------------------------------------

    print("Words Starting With Vowels :")

    for word in words:

        if word[0].lower() in "aeiou":

            print(word)

    # --------------------------------------
    # Words Longer Than 5 Characters
    # --------------------------------------

    print("Words Longer Than 5 Characters :")

    for word in words:

        if len(word) > 5:

            print(word)

    # --------------------------------------
    # Longest Message
    # --------------------------------------

    if len(msg) > len(longest_message):

        longest_message = msg

    # --------------------------------------
    # Shortest Message
    # --------------------------------------

    if len(msg) < len(shortest_message):

        shortest_message = msg

# ==========================================
# DISPLAY WORD FREQUENCY DICTIONARY
# ==========================================

print("\n================================")
print("WORD FREQUENCY DICTIONARY")
print("================================")

print(word_frequency)

# ==========================================
# MOST FREQUENTLY USED WORD
# ==========================================

max_frequency = 0
most_used_word = ""

for word, count in word_frequency.items():

    if count > max_frequency:

        max_frequency = count
        most_used_word = word

# ==========================================
# AVERAGE WORDS PER MESSAGE
# ==========================================

average_words = total_words_all / len(messages)

# ==========================================
# FINAL REPORT
# ==========================================

print("\n================================")
print("CHAT ANALYTICS REPORT")
print("================================")

print("Most Frequently Used Word :",most_used_word)

print("Frequency :",max_frequency)

print("\nLongest Message :")
print(longest_message)

print("\nShortest Message :")
print(shortest_message)

print("\nAverage Words Per Message :",round(average_words, 2))