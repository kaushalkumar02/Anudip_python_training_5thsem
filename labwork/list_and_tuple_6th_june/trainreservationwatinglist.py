# Problem Statement:
# Passenger records in a train reservation system are stored as tuples.
# passengers = [
#     ("Anuj", "Confirmed"),
#     ("Rahul", "Waiting"),
#     ("Priya", "Confirmed"),
#     ("Amit", "Waiting"),
#     ("Neha", "Confirmed")
# ]
# Write a program to:
# • Display all waiting-list passengers
# • Count confirmed and waiting passengers
# • Check whether a specific passenger has a confirmed ticket
# • Create separate lists for confirmed and waiting passengers
# Passenger data (Name, Status)
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# Lists to store separated data
confirmed_list = []
waiting_list = []

# Counters
confirmed_count = 0
waiting_count = 0

# Separate passengers based on status
for name, status in passengers:
    if status == "Confirmed":
        confirmed_list.append(name)
        confirmed_count += 1
    else:
        waiting_list.append(name)
        waiting_count += 1

# Display waiting list passengers
print("Waiting List Passengers:")
for name in waiting_list:
    print("-", name)

print()

# Display counts
print("Confirmed Passengers:", confirmed_count)
print("Waiting Passengers:", waiting_count)

print()

# Check specific passenger status
search_name = input("Enter passenger name to check status: ")

found = False
for name, status in passengers:
    if name.lower() == search_name.lower():
        print(f"{name} has a {status} ticket.")
        found = True
        break

if not found:
    print("Passenger not found in records.")