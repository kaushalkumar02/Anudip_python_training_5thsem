# Problem Statement:
# Email Address Validator
# A user enters an email address: rahul.sharma2026@gmail.com
# Tasks:
# 1. Extract username
# 2. Extract domain name
# 3. Extract extension
# 4. Count digits in username
# 5. Count special characters in username
# 6. Validate email:
#    - Exactly one '@' must exist
#    - At least one '.' must exist after '@'
# 7. Display whether email is Valid or Invalid

email = "rahul.sharma2026@gmail.com"

# Count @
at_count = 0

for ch in email:
    if ch == "@":
        at_count = at_count + 1

# Split email
parts = email.split("@")

if len(parts) == 2:
    username = parts[0]
    domain_part = parts[1]
else:
    username = ""
    domain_part = ""

# Extract domain and extension
domain_parts = domain_part.split(".")

if len(domain_parts) >= 2:
    domain = domain_parts[0]
    extension = domain_parts[1]
else:
    domain = ""
    extension = ""

# Count digits in username
digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count = digit_count + 1

# Count special characters in username
special_count = 0

for ch in username:
    if not ch.isalnum():
        special_count = special_count + 1

# Check '.' after @
dot_after_at = False

if "@" in email:
    index = email.index("@")
    if "." in email[index:]:
        dot_after_at = True

# Validate email
if at_count == 1 and dot_after_at == True:
    status = "Valid Email"
else:
    status = "Invalid Email"

# Output
print("Email:", email)
print("Username:", username)
print("Domain:", domain)
print("Extension:", extension)
print("Digits Found:", digit_count)
print("Special Characters Found:", special_count)
print("Email Status:", status)
