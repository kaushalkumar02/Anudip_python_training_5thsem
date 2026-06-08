# --------------------------------------------------
# Problem Statement:
# Analyze bus route passenger data and perform the following:
# 1. Display stops having more than 20 passengers.
# 2. Count stops with fewer than 10 passengers.
# 3. Find the busiest stop.
# 4. Create a list of stops requiring an extra bus
#    (passengers > 25).
# 5. Calculate the average number of passengers.
# --------------------------------------------------

# Sample Data
passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# --------------------------------------------------
# Validation Section
# --------------------------------------------------

is_valid = True

# Check whether passengers is a dictionary
if not isinstance(passengers, dict):
    print("Invalid data: Passenger data should be stored in a dictionary.")
    is_valid = False

# Validate stop names and passenger counts
if is_valid:
    for stop, count in passengers.items():

        # Stop name must be a string
        if not isinstance(stop, str):
            print("Invalid stop name found.")
            is_valid = False
            break

        # Passenger count must be an integer
        if not isinstance(count, int):
            print(f"Invalid passenger count for {stop}.")
            is_valid = False
            break

        # Passenger count cannot be negative
        if count < 0:
            print(f"Negative passenger count found for {stop}.")
            is_valid = False
            break

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

if is_valid:

    # Stops having more than 20 passengers
    busy_stops = [
        stop for stop, count in passengers.items()
        if count > 20
    ]

    # Count stops with fewer than 10 passengers
    low_passenger_stops = sum(
        1 for count in passengers.values()
        if count < 10
    )

    # Find the busiest stop
    busiest_stop = max(passengers, key=passengers.get)
    highest_passengers = passengers[busiest_stop]

    # Stops requiring an extra bus
    extra_bus_stops = [
        stop for stop, count in passengers.items()
        if count > 25
    ]

    # Calculate average passengers
    average_passengers = sum(passengers.values()) / len(passengers)

    # --------------------------------------------------
    # Output Section
    # --------------------------------------------------

    print("Stops having more than 20 passengers:")
    print(busy_stops)

    print("\nNumber of stops with fewer than 10 passengers:")
    print(low_passenger_stops)

    print("\nBusiest stop:")
    print(f"{busiest_stop} - {highest_passengers} passengers")

    print("\nStops requiring an extra bus:")
    print(extra_bus_stops)

    print("\nAverage number of passengers:")
    print(f"{average_passengers:.2f}")