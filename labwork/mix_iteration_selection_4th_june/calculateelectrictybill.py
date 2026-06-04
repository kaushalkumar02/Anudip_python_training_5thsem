units = int(input("Enter Units Consumed: "))

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Units Consumed:", units)
print("Total Bill:", bill)

if units <= 100:
    print("Category: Low Consumption")
elif units <= 200:
    print("Category: Medium Consumption")
else:
    print("Category: High Consumption")