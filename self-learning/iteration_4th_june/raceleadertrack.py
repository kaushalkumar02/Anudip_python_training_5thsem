# Program to find fastest and slowest racer and time difference

n = int(input("Enter number of racers: "))

t = int(input("Enter lap time of racer 1: "))

fast = t
slow = t
fast_pos = 1
slow_pos = 1

for i in range(2, n + 1):
    t = int(input(f"Enter lap time of racer {i}: "))

    if t < fast:
        fast = t
        fast_pos = i

    if t > slow:
        slow = t
        slow_pos = i

print("Fastest Racer Position:", fast_pos)
print("Slowest Racer Position:", slow_pos)
print("Difference:", slow - fast)