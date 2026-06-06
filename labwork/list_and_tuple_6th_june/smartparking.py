# ------------------------------------------------------------
# Problem Statement:
# Smart Parking System Analysis
# Parking slots are represented using a list where:
# 1 = Occupied slot
# 0 = Available slot
# Objective:
# Write a Python program to count the number of occupied
# and available parking slots.
# ------------------------------------------------------------

# Parking slot status list
slots = [1, 0, 1, 1, 0, 0, 1, 0]

# Initialize counters
occupied_count = 0
available_count = 0

# Loop through each slot and count status
for slot in slots:
    if slot == 1:
        occupied_count += 1
    elif slot == 0:
        available_count += 1

# Display results
print("Occupied Slots:", occupied_count)
print("Available Slots:", available_count)