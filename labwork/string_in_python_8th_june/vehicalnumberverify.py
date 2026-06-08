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
plate = "MH12AB4589"
# Extraction
state_code = plate[0:2]
district_code = plate[2:4]
series = plate[4:6]
vehicle_number = plate[6:10]
# Count letters and digits
letter_count = sum(1 for ch in plate if ch.isalpha())
digit_count = sum(1 for ch in plate if ch.isdigit())

# Validation rules
valid_state = state_code.isalpha()
valid_district = district_code.isdigit()
valid_series = series.isalpha()
valid_number = vehicle_number.isdigit()

is_valid = valid_state and valid_district and valid_series and valid_number

# Output
print("Vehicle Number:", plate)
print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)
print("Total Letters:", letter_count)
print("Total Digits:", digit_count)
print("Vehicle Number Status:", "Valid" if is_valid else "Invalid")