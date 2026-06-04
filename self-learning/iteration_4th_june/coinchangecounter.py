# Program to calculate minimum number of notes for given amount

amt = int(input("Enter amount: "))

notes = [500, 200, 100, 50, 20, 10]

for n in notes:
    count = amt // n
    amt = amt % n
    if count > 0:
        print(n, "x", count)