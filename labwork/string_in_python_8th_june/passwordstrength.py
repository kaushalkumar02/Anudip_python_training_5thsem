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

# Counters
upper_count = sum(1 for ch in password if ch.isupper())
lower_count = sum(1 for ch in password if ch.islower())
digit_count = sum(1 for ch in password if ch.isdigit())
special_count = sum(1 for ch in password if not ch.isalnum())

# Extract digits and special characters
digits_list = [ch for ch in password if ch.isdigit()]
special_list = [ch for ch in password if not ch.isalnum()]

# Strength check conditions
length_ok = len(password) >= 8
upper_ok = upper_count >= 1
lower_ok = lower_count >= 1
digit_ok = digit_count >= 1
special_ok = special_count >= 1

# Determine strength
if length_ok and upper_ok and lower_ok and digit_ok and special_ok:
    strength = "Strong"
elif length_ok and (upper_count + lower_count + digit_count >= 3):
    strength = "Medium"
else:
    strength = "Weak"

# Output
print("Password:", password)
print("Uppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)
print("Digits Found:", digits_list)
print("Special Characters Found:", special_list)
print("Password Strength:", strength)