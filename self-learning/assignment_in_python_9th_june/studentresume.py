'''Student Resume Analyzer 
Problem Statement 
A student enters a resume as plain text (Name, Skills, Education, Projects, Achievements). 
The system should: 
1. Count total words.  
2. Count total characters.  
3. Extract email IDs.  
4. Extract phone numbers.  
5. Count skills mentioned.  
6. Find repeated keywords.  
7. Identify the most frequently used word.  
8. Generate a skill frequency report.  
9. Detect duplicate skills.  
10. Create a summary dashboard.  
Expected Output 
Resume Analysis Report 
 
Total Words: 420 
Total Characters: 2650 
 
Email Found: 1 
Phone Numbers Found: 1 
 
Most Frequent Skill: Python 
 
Top 5 Keywords: 
Python 
SQL 
React 
Java 
Communication '''


# ==========================================
# STUDENT RESUME ANALYZER
# ==========================================

print("Enter Resume Text:")
print("Type END in a new line to finish\n")

resume = ""

while True:

    line = input()

    if line == "END":
        break

    resume += line + " "

# ==========================================
# TOTAL WORDS
# ==========================================

words = resume.split()

total_words = len(words)

# ==========================================
# TOTAL CHARACTERS
# ==========================================

total_characters = len(resume)

# ==========================================
# EXTRACT EMAIL IDS
# ==========================================

emails = []

for word in words:

    if "@" in word and "." in word:

        emails.append(word)

# ==========================================
# EXTRACT PHONE NUMBERS
# ==========================================

phone_numbers = []

for word in words:

    clean_word = word.strip(".,()-+")

    if clean_word.isdigit():

        if len(clean_word) == 10:

            phone_numbers.append(clean_word)

# ==========================================
# SKILL LIST
# ==========================================

skills_list = [
    "python",
    "java",
    "sql",
    "react",
    "html",
    "css",
    "javascript",
    "c",
    "c++",
    "django",
    "flask",
    "mongodb",
    "mysql",
    "communication",
    "leadership",
    "excel",
    "powerbi",
    "machine",
    "learning",
    "aws"
]

# ==========================================
# SKILL FREQUENCY
# ==========================================

skill_frequency = {}

for word in words:

    word = word.lower().strip(".,()[]{}")

    if word in skills_list:

        if word in skill_frequency:

            skill_frequency[word] += 1

        else:

            skill_frequency[word] = 1

# ==========================================
# TOTAL SKILLS MENTIONED
# ==========================================

total_skills = 0

for count in skill_frequency.values():

    total_skills += count

# ==========================================
# REPEATED KEYWORDS
# ==========================================

word_frequency = {}

for word in words:

    word = word.lower().strip(".,()[]{}")

    if word in word_frequency:

        word_frequency[word] += 1

    else:

        word_frequency[word] = 1

# ==========================================
# MOST FREQUENT WORD
# ==========================================

most_frequent_word = ""

highest_count = 0

for word, count in word_frequency.items():

    if count > highest_count:

        highest_count = count
        most_frequent_word = word

# ==========================================
# DUPLICATE SKILLS
# ==========================================

duplicate_skills = []

for skill, count in skill_frequency.items():

    if count > 1:

        duplicate_skills.append(skill)

# ==========================================
# MOST FREQUENT SKILL
# ==========================================

most_frequent_skill = ""

highest_skill_count = 0

for skill, count in skill_frequency.items():

    if count > highest_skill_count:

        highest_skill_count = count
        most_frequent_skill = skill

# ==========================================
# TOP 5 KEYWORDS
# ==========================================

temp = word_frequency.copy()

print("\nTop 5 Keywords")

for i in range(5):

    highest_word = ""
    highest = 0

    for word, count in temp.items():

        if count > highest:

            highest = count
            highest_word = word

    if highest_word != "":

        print(highest_word)

        del temp[highest_word]

# ==========================================
# REPORT
# ==========================================

print("\n===================================")
print("RESUME ANALYSIS REPORT")
print("===================================")

print("Total Words :", total_words)

print("Total Characters :", total_characters)

print("\nEmail IDs Found :", len(emails))

for email in emails:

    print(email)

print("\nPhone Numbers Found :", len(phone_numbers))

for number in phone_numbers:

    print(number)

print("\nTotal Skills Mentioned :", total_skills)

print("Most Frequent Word :", most_frequent_word)

print("Most Frequent Skill :", most_frequent_skill)

print("\nRepeated Keywords")

for word, count in word_frequency.items():

    if count > 1:

        print(word, "->", count)

print("\nSkill Frequency Report")

for skill, count in skill_frequency.items():

    print(skill, "->", count)

print("\nDuplicate Skills")

for skill in duplicate_skills:

    print(skill)

print("\nSummary Dashboard")

print("Words :", total_words)

print("Characters :", total_characters)

print("Emails :", len(emails))

print("Phone Numbers :", len(phone_numbers))

print("Most Frequent Skill :", most_frequent_skill)

print("Vocabulary Size :", len(word_frequency))