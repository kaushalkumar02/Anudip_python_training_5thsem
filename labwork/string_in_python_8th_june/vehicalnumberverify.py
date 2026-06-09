# Problem Statement:
# Vehicle Number Plate Verification System
# A vehicle number plate is entered: MH12AB4589
# Tasks:
# 1. Extract state code
# 2. Extract district code
# 3. Extract vehicle series
# 4. Extract vehicle number
# 5. Count letters and digits separately
# 6. Verify format:
#    - First 2 characters must be alphabets
#    - Next 2 must be digits
#    - Next 2 must be alphabets
#    - Last 4 must be digits
# 7. Display whether number plate is valid or invalid
# Vehicle Number Plate Verification System

plate = "MH12AB4589"

# 1. Extract parts using slicing
state_code = plate[0:2]
district_code = plate[2:4]
series = plate[4:6]
vehicle_number = plate[6:10]

# 2. Count letters and digits
letter_count = 0
digit_count = 0

for ch in plate:
    if ch.isalpha():
        letter_count = letter_count + 1
    elif ch.isdigit():
        digit_count = digit_count + 1

# 3. Validate format step by step
if state_code.isalpha():
    valid_state = True
else:
    valid_state = False

if district_code.isdigit():
    valid_district = True
else:
    valid_district = False

if series.isalpha():
    valid_series = True
else:
    valid_series = False

if vehicle_number.isdigit():
    valid_number = True
else:
    valid_number = False

# 4. Final validation
if valid_state and valid_district and valid_series and valid_number:
    status = "Valid"
else:
    status = "Invalid"

# 5. Output
print("Vehicle Number Plate:", plate)
print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)
print("Total Letters:", letter_count)
print("Total Digits:", digit_count)
print("Status:", status)
