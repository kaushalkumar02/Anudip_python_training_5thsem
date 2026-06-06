# Problem Statement:
# A bus seat list is given where 1 = booked seat and 0 = available seat.
# Tasks:
# 1. Count booked and available seats
# 2. Find first available seat
# 3. Store all available seat numbers
# 4. Check if bus occupancy is more than 70%

seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

booked = 0
available = 0
available_seats = []
first_available = None

# traverse all seats
for i in range(len(seats)):

    # count booked seats
    if seats[i] == 1:
        booked += 1

    # process available seats
    else:
        available += 1
        available_seats.append(i + 1)

        # store first available seat only
        if first_available is None:
            first_available = i + 1

# calculate occupancy percentage
occupancy = (booked / len(seats)) * 100

# display results
print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seats)
print("Bus Occupancy:", int(occupancy), "%")

# check occupancy level
if occupancy > 70:
    print("Status: More Than 70% Occupied")
else:
    print("Status: Not More Than 70% Occupied")