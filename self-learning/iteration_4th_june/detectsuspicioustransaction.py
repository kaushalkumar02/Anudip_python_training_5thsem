# Program to detect suspicious transactions

high = 0
low = 0
total = 0

while True:
    amt = int(input("Enter transaction amount (-1 to stop): "))

    if amt == -1:
        break

    total = total + amt

    if amt > 50000:
        high = high + 1

    if amt < 1000:
        low = low + 1

print("High value transactions:", high)
print("Low value transactions:", low)
print("Total amount:", total)