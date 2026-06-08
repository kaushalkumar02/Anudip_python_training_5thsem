# --------------------------------------------------
# Problem Statement:
# Monthly electricity consumption (units) is stored as:
# Perform analysis on the given dictionary.
# --------------------------------------------------
# Sample Data
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

# 1. Houses consuming more than 400 units
above_400 = [house for house, u in units.items() if u > 400]

# 2. Highest-consuming house
max_house = max(units, key=units.get)
max_units = units[max_house]

# 3. Lowest-consuming house
min_house = min(units, key=units.get)
min_units = units[min_house]

# 4. Total units consumed
total_units = sum(units.values())

# 5. Consumption categories
low = [house for house, u in units.items() if u < 200]
medium = [house for house, u in units.items() if 200 <= u <= 400]
high = [house for house, u in units.items() if u > 400]

# 6. Energy-saving campaign (consumption > 300)
campaign_count = sum(1 for u in units.values() if u > 300)

# --------------------------------------------------
# Output Section
# --------------------------------------------------

print("Houses Consuming More Than 400 Units:", *above_400)

print("\nHighest Consumption:")
print(f"{max_house} ({max_units} units)")

print("\nLowest Consumption:")
print(f"{min_house} ({min_units} units)")

print("\nTotal Units Consumed:")
print(total_units)

print("\nLow Consumption:", low)
print("Medium Consumption:", medium)
print("High Consumption:", high)

print("\nEligible for Energy-Saving Campaign:", campaign_count)