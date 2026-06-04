total = 0

while True:
    price = float(input("Enter Item Price: "))

    if price == 0:
        break

    total = total + price

print("Total Bill Amount: ₹", total)