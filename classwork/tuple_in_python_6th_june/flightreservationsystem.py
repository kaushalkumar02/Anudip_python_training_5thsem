# ------------------------------------------------------------
# Problem Statement:
# Flight Reservation System
#
# A flight reservation system stores passenger records as tuples.
# Each record contains:
# 1. Passenger ID
# 2. Destination
# 3. Booking Status
#
# Tasks:
# 1. Display all passengers whose booking status is Confirmed.
# 2. Count the number of passengers travelling to Delhi.
# 3. Count Confirmed, Waiting, and Cancelled bookings separately.
# 4. Create a list containing passenger IDs with Waiting status.
# 5. Determine which destination has the highest number of bookings.
# ------------------------------------------------------------

# Passenger booking records
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# 1. Display all confirmed passengers
print("Confirmed Passengers:")

for passenger_id, destination, status in bookings:
    if status == "Confirmed":
        print(passenger_id, destination)

# 2. Count passengers travelling to Delhi
delhi_count = 0

for passenger_id, destination, status in bookings:
    if destination == "Delhi":
        delhi_count += 1

print("\nPassengers Travelling to Delhi:", delhi_count)

# 3. Count booking statuses
confirmed_count = 0
waiting_count = 0
cancelled_count = 0

for passenger_id, destination, status in bookings:
    if status == "Confirmed":
        confirmed_count += 1

    elif status == "Waiting":
        waiting_count += 1

    elif status == "Cancelled":
        cancelled_count += 1

print("\nConfirmed:", confirmed_count)
print("Waiting:", waiting_count)
print("Cancelled:", cancelled_count)

# 4. Create a list of waiting passengers
waiting_list = []

for passenger_id, destination, status in bookings:
    if status == "Waiting":
        waiting_list.append(passenger_id)

print("\nWaiting List:", waiting_list)

# 5. Find the destination with the highest number of bookings
destination_count = {}

for passenger_id, destination, status in bookings:
    if destination in destination_count:
        destination_count[destination] += 1
    else:
        destination_count[destination] = 1

most_booked_destination = max(
    destination_count,
    key=destination_count.get
)

print("\nMost Booked Destination:", most_booked_destination)