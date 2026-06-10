'''Assignment 1: Password Security Analyzer 
Problem Statement 
A cybersecurity company wants to analyze user passwords before allowing account creation. 
The system should accept at least 15 passwords and generate a security report. 
Requirements 
For each password: 
1. Count uppercase letters.  
2. Count lowercase letters.  
3. Count digits.  
4. Count special characters.  
5. Check minimum length (8 characters).  
6. Check if spaces exist.  
7. Determine password strength:  
o Strong  
o Medium  
o Weak  
8. Display repeated characters.  
9. Count vowels and consonants.  
10. Identify the most frequently occurring character.  
Challenge 
Generate a report showing: 
Total Passwords Analyzed 
Strong Passwords 
Medium Passwords 
Weak Passwords'''

# ==========================================
# PASSWORD SECURITY ANALYZER
# ==========================================

# Counters for summary report

strong_count = 0
medium_count = 0
weak_count = 0

# Analyze 15 passwords

for i in range(1, 16):

    print(f"\nEnter Password {i}")

    password = input("Password: ")

    # Counters

    uppercase = 0
    lowercase = 0
    digits = 0
    special = 0
    spaces = 0

    vowels = 0
    consonants = 0

    # ======================================
    # Count Character Types
    # ======================================

    for ch in password:
        if ch.isupper():
            uppercase += 1
        elif ch.islower():
            lowercase += 1
        elif ch.isdigit():
            digits += 1
        else:
            special += 1

        # Count vowels and consonants

        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    # ======================================
    # Check Minimum Length
    # ======================================

    if len(password) >= 8:
        length_status = "Valid"
    else:
        length_status = "Invalid"

    # ======================================
    # Determine Password Strength
    # ======================================

    if (
        len(password) >= 8
        and uppercase > 0
        and lowercase > 0
        and digits > 0
        and special > 0
        and spaces == 0
    ):

        strength = "Strong"
        strong_count += 1

    elif (
        len(password) >= 8
        and digits > 0
        and (uppercase > 0 or lowercase > 0)
    ):

        strength = "Medium"
        medium_count += 1

    else:

        strength = "Weak"
        weak_count += 1

    # ======================================
    # Find Repeated Characters
    # ======================================

    repeated = []

    for ch in password:

        if password.count(ch) > 1:

            if ch not in repeated:

                repeated.append(ch)

    # ======================================
    # Find Most Frequent Character
    # ======================================

    max_count = 0
    frequent_char = ""

    for ch in password:

        count = password.count(ch)

        if count > max_count:

            max_count = count
            frequent_char = ch

    # ======================================
    # Display Individual Password Report
    # ======================================

    print("\n========== PASSWORD REPORT ==========")

    print("Password :", password)

    print("Uppercase Letters :", uppercase)

    print("Lowercase Letters :", lowercase)

    print("Digits :", digits)

    print("Special Characters :", special)

    print("Length Status :", length_status)

    if spaces > 0:

        print("Spaces Present")

    else:

        print("No Spaces Present")

    print("Password Strength :", strength)

    print("Repeated Characters :", repeated)

    print("Vowels :", vowels)

    print("Consonants :", consonants)

    print("Most Frequent Character :", frequent_char)

# ==========================================
# FINAL SUMMARY REPORT
# ==========================================

print("\n======================================")
print("PASSWORD SECURITY SUMMARY REPORT")
print("======================================")

print("Total Passwords Analyzed :", 15)

print("Strong Passwords :", strong_count)

print("Medium Passwords :", medium_count)

print("Weak Passwords :", weak_count)