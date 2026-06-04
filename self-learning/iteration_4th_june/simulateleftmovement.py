# Program to simulate lift movement

curr = 0
total = 0

while True:
    dest = int(input("Enter destination floor (-1 to stop): "))

    if dest == -1:
        break

    travel = abs(dest - curr)
    total = total + travel

    print("Travelled:", travel, "floors")

    curr = dest

print("Total Travelled:", total, "floors")