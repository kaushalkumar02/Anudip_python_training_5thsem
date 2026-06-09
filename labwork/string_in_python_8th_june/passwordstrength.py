# Problem Statement:
# Password Strength Analyzer
# A user enters a password: Python@2026!
# The program should:
# 1. Count uppercase letters
# 2. Count lowercase letters
# 3. Count digits
# 4. Count special characters
# 5. Display all digits separately
# 6. Display all special characters separately
# 7. Determine password strength (Strong / Medium / Weak)
# Rules for Strong password:
# - Minimum length 8
# - At least 1 uppercase letter
# - At least 1 lowercase letter
# - At least 1 digit
# - At least 1 special character

password = "Python@2026!"

# 1. Count uppercase letters
upper = 0
# 2. Count lowercase letters
lower = 0
# 3. Count digits
digits = 0
# 4. Count special characters
special = 0

# lists for digits and special characters
digit_list = []
special_list = []

# loop through password
for ch in password:
    if ch.isupper():
        upper = upper + 1

    elif ch.islower():
        lower = lower + 1

    elif ch.isdigit():
        digits = digits + 1
        digit_list.append(ch)

    else:
        special = special + 1
        special_list.append(ch)

# 5. Conditions for strong password
length_ok = len(password) >= 8
upper_ok = upper >= 1
lower_ok = lower >= 1
digit_ok = digits >= 1
special_ok = special >= 1

# 6. Determine strength
if length_ok and upper_ok and lower_ok and digit_ok and special_ok:
    strength = "Strong"
elif length_ok and (upper + lower + digits >= 3):
    strength = "Medium"
else:
    strength = "Weak"

# OUTPUT
print("Password:", password)
print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)
print("Digits:", digits)
print("Special Characters:", special)
print("Digits Found:", digit_list)
print("Special Characters Found:", special_list)
print("Password Strength:", strength)
