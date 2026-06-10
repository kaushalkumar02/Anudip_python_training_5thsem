# Problem Statement:
# A railway coach has seats represented as follows:
# seats = [
#     "Booked", "Available", "Booked", "Booked",
#     "Available", "Available", "Booked", "Available",
#     "Booked", "Booked", "Available", "Booked"
# ]
# Requirements:
# 1. count_seats(seats)
# 2. first_available(seats)
# 3. occupancy_percentage(seats)
# 4. display_available_seats(seats)
# ==========================================================
# List of seats
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]
# Function to count booked and available seats
def count_seats(seats):
    booked = 0
    available = 0

    for seat in seats:
        if seat == "Booked":
            booked = booked + 1
        else:
            available = available + 1

    return booked, available

# Function to find first available seat
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1

# Function to calculate occupancy percentage
def occupancy_percentage(seats):
    booked = 0

    for seat in seats:
        if seat == "Booked":
            booked = booked + 1

    percentage = (booked * 100) / len(seats)
    return percentage

# Function to display available seat numbers
def display_available_seats(seats):
    print("\nAvailable Seat Numbers:", end=" ")

    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1, end=" ")

# Main Program
booked, available = count_seats(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)

print("\nFirst Available Seat:", first_available(seats))

print("\nOccupancy Percentage:", round(occupancy_percentage(seats), 2), "%")

display_available_seats(seats)