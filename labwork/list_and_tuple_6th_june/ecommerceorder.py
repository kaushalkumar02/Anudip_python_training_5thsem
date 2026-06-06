# ------------------------------------------------------------
# Problem Statement:
# E-Commerce Order Analysis
# An online store records orders as a list of tuples.
# Each tuple contains:
# 1. Product Name
# 2. Product Price
# Tasks:
# • Display all products costing more than ₹1000
# • Find the most expensive product
# • Calculate the total order value
# • Count products costing below ₹1000
# ------------------------------------------------------------
# List of orders (Product Name, Price)
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]
# 1. Display all products costing more than ₹1000
print("Products costing more than ₹1000:")
for product, price in orders:
    if price > 1000:
        print(product, "->", price)
# 2. Find the most expensive product
most_expensive = max(orders, key=lambda item: item[1])
print("\nMost Expensive Product:")
print(most_expensive[0], "->", most_expensive[1])
# 3. Calculate total order value
total_value = 0
for product, price in orders:
    total_value += price
print("\nTotal Order Value:", total_value)
# 4. Count products costing below ₹1000
count_below_1000 = 0
for product, price in orders:
    if price < 1000:
        count_below_1000 += 1
print("\nProducts costing below ₹1000:", count_below_1000)