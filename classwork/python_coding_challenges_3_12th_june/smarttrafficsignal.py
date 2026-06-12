# Problem 10: Smart Traffic Signal Optimization System

# Problem Statement:
# Vehicle counts recorded at a junction every 15 minutes
# are stored as follows:
#
# traffic = [120, 95, 140, 180, 75, 60, 200, 160, 110, 85]
#
# Tasks:
# 1. Classify traffic conditions:
#    Low (< 80 vehicles)
#    Moderate (80–150 vehicles)
#    High (> 150 vehicles)
#
# 2. Count occurrences of each traffic condition.
#
# 3. Find the peak traffic interval.
#
# 4. Create separate lists for each traffic category.
#
# 5. Recommend whether manual traffic control is required
#    (more than 3 High traffic intervals).
#
# Sample Output:
# Traffic Conditions:
# 120 → Moderate
# 95 → Moderate
# 140 → Moderate
# 180 → High
# 75 → Low
# 60 → Low
# 200 → High
# 160 → High
# 110 → Moderate
# 85 → Moderate
#
# Low Traffic Intervals: 2
# Moderate Traffic Intervals: 5
# High Traffic Intervals: 3
#
# Peak Traffic Count: 200 vehicles
#
# Low Traffic List: [75, 60]
# Moderate Traffic List: [120, 95, 140, 110, 85]
# High Traffic List: [180, 200, 160]
#
# Manual Traffic Control Required: No


# Function to analyze traffic data
def analyze_traffic():

    try:

        # Store traffic data in a list
        traffic = [120, 95, 140, 180, 75,
                   60, 200, 160, 110, 85]

        # Create lists for traffic categories
        low_traffic = []
        moderate_traffic = []
        high_traffic = []

        # Counters for each category
        low_count = 0
        moderate_count = 0
        high_count = 0

        print("Traffic Conditions:")

        # Classify traffic conditions
        for vehicles in traffic:

            # Low Traffic
            if vehicles < 80:

                print(vehicles, "→ Low")

                low_traffic.append(vehicles)

                low_count += 1

            # Moderate Traffic
            elif vehicles <= 150:

                print(vehicles, "→ Moderate")

                moderate_traffic.append(vehicles)

                moderate_count += 1

            # High Traffic
            else:

                print(vehicles, "→ High")

                high_traffic.append(vehicles)

                high_count += 1

        # Find peak traffic count
        peak_traffic = max(traffic)

        # Display category counts
        print("\nLow Traffic Intervals:", low_count)

        print("Moderate Traffic Intervals:", moderate_count)

        print("High Traffic Intervals:", high_count)

        # Display peak traffic
        print("\nPeak Traffic Count:",
              peak_traffic, "vehicles")

        # Display traffic category lists
        print("\nLow Traffic List:", low_traffic)

        print("Moderate Traffic List:",
              moderate_traffic)

        print("High Traffic List:",
              high_traffic)

        # Check if manual traffic control is required
        print("\nManual Traffic Control Required:")

        if high_count > 3:

            print("Yes")

        else:

            print("No")

    except Exception as e:

        # Handle unexpected errors
        print("Error:", e)

    finally:

        # Always executes
        print("\nTraffic Analysis Completed.")


# Function Call
analyze_traffic()