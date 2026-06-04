# Program to calculate electricity bill using slabs

u = int(input("Enter units consumed: "))

bill = 0

if u <= 100:
    bill = u * 5

elif u <= 200:
    bill = (100 * 5) + ((u - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((u - 200) * 10)

if bill > 5000:
    bill = bill + (bill * 10 / 100)

print("Final Payable Amount =", bill)