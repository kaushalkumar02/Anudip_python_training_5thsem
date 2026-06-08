# --------------------------------------------------
# Problem Statement:
# Analyze electricity consumption data and perform the following:
# 1. Display houses consuming more than 300 units.
# 2. Count houses consuming less than 200 units.
# 3. Find the house with the highest consumption.
# 4. Create a list of houses eligible for an
#    energy-saving awareness campaign
#    (consumption > 400 units).
# 5. Categorize houses as:
#       Low    : < 200 units
#       Medium : 200 - 350 units
#       High   : > 350 units
# --------------------------------------------------

# Sample Data
units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# --------------------------------------------------
# Validation Section
# --------------------------------------------------

is_valid = True

# Check whether units is a dictionary
if not isinstance(units, dict):
    print("Invalid data: Electricity consumption data should be stored in a dictionary.")
    is_valid = False

# Validate house names and unit values
if is_valid:
    for house, consumption in units.items():

        # House name must be a string
        if not isinstance(house, str):
            print("Invalid house name found.")
            is_valid = False
            break

        # Consumption must be numeric
        if not isinstance(consumption, (int, float)):
            print(f"Invalid consumption value for {house}.")
            is_valid = False
            break

        # Consumption cannot be negative
        if consumption < 0:
            print(f"Negative consumption value found for {house}.")
            is_valid = False
            break

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

if is_valid:

    # Houses consuming more than 300 units
    above_300 = [
        house for house, consumption in units.items()
        if consumption > 300
    ]

    # Count houses consuming less than 200 units
    below_200_count = sum(
        1 for consumption in units.values()
        if consumption < 200
    )

    # House with highest consumption
    highest_house = max(units, key=units.get)
    highest_consumption = units[highest_house]

    # Houses eligible for awareness campaign
    awareness_campaign = [
        house for house, consumption in units.items()
        if consumption > 400
    ]

    # Categorize houses
    categories = {}

    for house, consumption in units.items():

        if consumption < 200:
            categories[house] = "Low"

        elif 200 <= consumption <= 350:
            categories[house] = "Medium"

        else:
            categories[house] = "High"

    # --------------------------------------------------
    # Output Section
    # --------------------------------------------------

    print("Houses consuming more than 300 units:")
    print(above_300)

    print("\nNumber of houses consuming less than 200 units:")
    print(below_200_count)

    print("\nHouse with highest consumption:")
    print(f"{highest_house} - {highest_consumption} units")

    print("\nHouses eligible for energy-saving awareness campaign:")
    print(awareness_campaign)

    print("\nHouse Categories:")
    for house, category in categories.items():
        print(f"{house}: {category}")