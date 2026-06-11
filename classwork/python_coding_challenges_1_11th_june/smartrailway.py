#program to create smart railway reservation system
#Problem Statement
#  A railway reservation system stores the booking status of seats in a train coach.
#  Sample Data seats = 
# {     1: "Booked",  
#    2: "Available", 
#     3: "Booked", 
#     4: "Available",
#      5: "Booked", 
#     6: "Booked",
#      7: "Available",
#      8: "Booked",
#      9: "Available",
#      10: "Booked" }
#  Tasks
#  1. Display all available seat numbers.
#   2. Count booked and available seats.
#   3. Reserve the first available seat.
#   4. Cancel booking for a given seat number.
#   5. Store the updated reservation status in reservations.txt.
#   6. Display occupancy percentage.
#Sample Output 
# Available Seats: 2 4 7 9 
#  Booked Seats: 6 Available Seats:
#  4  Seat 2 Reserved Successfully.
#   Occupancy Percentage: 70.0%  Reservation Details Saved Successfully.    
# dislpay all available seat numbers
seats = {
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available",
    5: "Booked", 
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}
# 2. Count booked and available seats
booked_count = sum(1 for status in seats.values() if status == "Booked")
available_count = sum(1 for status in seats.values() if status == "Available")  
print("Available Seats:", end=" ")
for seat_num, status in seats.items():
    if status == "Available":
        print(seat_num, end=" ")
print()  # Print a newline after listing available seats
print(f"Booked Seats: {booked_count}")
print(f"Available Seats: {available_count}")
# 3. Reserve the first available seat
for seat_num, status in seats.items():
    if status == "Available":
        seats[seat_num] = "Booked"
        print(f"Seat {seat_num} Reserved Successfully.")
        break
# 4. Cancel booking for a given seat number
cancel_seat = int(input("Enter seat number to cancel booking: "))
if seats.get(cancel_seat) == "Booked":
    seats[cancel_seat] = "Available"
    print(f"Booking for Seat {cancel_seat} cancelled successfully.")
else:
    print("Invalid seat number or seat is already available.")
# 5. Store the updated reservation status in reservations.txt
with open("reservations.txt", "w") as file:
    for seat_num, status in seats.items():
        file.write(f"Seat {seat_num}: {status}\n")
print("Reservation Details Saved Successfully.")
# 6. Display occupancy percentage
total_seats = len(seats)
occupancy_percentage = (booked_count / total_seats) * 100 if total_seats > 0 else 0
print(f"Occupancy Percentage: {occupancy_percentage:.1f}%") 
#sample output
# Available Seats: 2 4 7 9
# Booked Seats: 6
# Available Seats: 4
# Seat 2 Reserved Successfully.
# Occupancy Percentage: 70.0%
# Reservation Details Saved Successfully.