# Problem Statement:
# Passenger count at each bus stop is recorded in a list.
# passengers = [12, 18, 25, 30, 28, 15, 8]
# Write a program to:
# • Find the busiest stop
# • Display stops with fewer than 10 passengers
# • Calculate average passengers
# • Determine whether any stop exceeded 25 passengers

# Passenger data for each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Initialize variables
max_passengers = passengers[0]
busiest_stop = 1
low_passenger_stops = []
exceeded_25 = False

total = 0

# Loop through all stops
for i in range(len(passengers)):
    total += passengers[i]

    # Find busiest stop
    if passengers[i] > max_passengers:
        max_passengers = passengers[i]
        busiest_stop = i + 1

    # Stops with fewer than 10 passengers
    if passengers[i] < 10:
        low_passenger_stops.append(i + 1)

    # Check if any stop exceeded 25 passengers
    if passengers[i] > 25:
        exceeded_25 = True

# Calculate average passengers
average = total / len(passengers)

# Display results
print("Busiest Stop:", busiest_stop, "with", max_passengers, "passengers")
print("Stops with fewer than 10 passengers:", low_passenger_stops)
print("Average passengers:", round(average, 2))

if exceeded_25:
    print("Yes, at least one stop exceeded 25 passengers")
else:
    print("No stop exceeded 25 passengers")