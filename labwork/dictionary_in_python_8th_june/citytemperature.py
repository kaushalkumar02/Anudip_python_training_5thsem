# --------------------------------------------------
# Problem Statement:
# Daily temperatures of different cities are stored as:
# Perform analysis on the given temperature dictionary.
# --------------------------------------------------
# Sample Data
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

# 1. Cities having temperature above 40°C
above_40 = [city for city, temp in temperature.items() if temp > 40]

# 2. Hottest city
hottest_city = max(temperature, key=temperature.get)
hottest_temp = temperature[hottest_city]

# 3. Coolest city
coolest_city = min(temperature, key=temperature.get)
coolest_temp = temperature[coolest_city]

# 4. Average temperature
avg_temp = sum(temperature.values()) / len(temperature)

# 5. Pleasant cities (temperature < 35°C)
pleasant_cities = [city for city, temp in temperature.items() if temp < 35]

# 6. Cities between 35°C and 40°C
between_35_40_count = sum(1 for temp in temperature.values() if 35 <= temp <= 40)

# --------------------------------------------------
# Output Section
# --------------------------------------------------

print("Cities Above 40°C:", *above_40)

print("\nHottest City:")
print(f"{hottest_city} ({hottest_temp}°C)")

print("\nCoolest City:")
print(f"{coolest_city} ({coolest_temp}°C)")

print("\nAverage Temperature:")
print(f"{avg_temp:.1f}°C")

print("\nPleasant Cities:", pleasant_cities)

print("\nCities Between 35°C and 40°C:", between_35_40_count)