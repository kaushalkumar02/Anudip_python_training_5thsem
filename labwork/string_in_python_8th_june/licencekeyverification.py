# Problem Statement:
# License Key Verification System
# A software license key is entered: ABCD-EFGH-IJKL-MNOP
# Tasks:
# 1. Verify there are exactly 4 groups
# 2. Verify each group contains exactly 4 characters
# 3. Count total letters
# 4. Count vowels
# 5. Remove hyphens and display merged key
# 6. Create list of all groups
# 7. Display whether key format is valid
license_key = "ABCD-EFGH-IJKL-MNOP"

# 1. Split into groups
groups = license_key.split("-")

# 2. Check number of groups
if len(groups) == 4:
    group_check = True
else:
    group_check = False

# 3. Check each group length
length_check = True

for g in groups:
    if len(g) != 4:
        length_check = False

# 4. Count letters
letter_count = 0

for ch in license_key:
    if ch.isalpha():
        letter_count = letter_count + 1

# 5. Count vowels
vowel_count = 0
vowels = "AEIOUaeiou"

for ch in license_key:
    if ch in vowels:
        vowel_count = vowel_count + 1

# 6. Remove hyphens
merged_key = ""

for ch in license_key:
    if ch != "-":
        merged_key = merged_key + ch

# 7. Create list of groups (already done above)
group_list = groups

# 8. Final validation
if group_check and length_check:
    status = "Valid Key Format"
else:
    status = "Invalid Key Format"

# OUTPUT
print("License Key:", license_key)
print("Groups:", group_list)
print("Merged Key:", merged_key)
print("Total Letters:", letter_count)
print("Vowels:", vowel_count)
print("Status:", status)
print("License Key Status:", status)
