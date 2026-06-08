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
num_groups = len(groups)

# 3. Check each group length
valid_groups = all(len(group) == 4 for group in groups)

# 4. Count letters
total_letters = sum(len(group) for group in groups)

# 5. Count vowels
vowels = "AEIOUaeiou"
vowel_count = 0

for ch in license_key:
    if ch.isalpha() and ch in vowels:
        vowel_count += 1

# 6. Merged key (remove hyphens)
merged_key = license_key.replace("-", "")

# 7. Format validity
is_valid = (num_groups == 4) and valid_groups

status = "Valid" if is_valid else "Invalid"

# Output
print("License Key:", license_key)
print("Groups:", groups)
print("Number of Groups:", num_groups)
print("Total Letters:", total_letters)
print("Total Vowels:", vowel_count)
print("Merged Key:", merged_key)
print("License Key Status:", status)