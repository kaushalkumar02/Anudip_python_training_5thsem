import random

secret = random.randint(1, 50)
n = 0
attempt = 0

while n != secret:
    n = int(input("Enter Number : "))
    attempt = attempt + 1

    if n > secret:
        print("High")
    elif n < secret:
        print("Low")
    else:
        print("Correct")

print("Total Attempts :", attempt)