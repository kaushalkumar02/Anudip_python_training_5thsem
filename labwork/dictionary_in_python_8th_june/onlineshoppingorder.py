# --------------------------------------------------
# Problem Statement:
# An e-commerce company stores product sales data as:
# Perform analysis on the given sales dictionary.
# --------------------------------------------------

# Sample Data
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

# 1. Products sold more than 20 times
above_20 = [product for product, qty in sales.items() if qty > 20]

# 2. Best-selling product
best_product = max(sales, key=sales.get)
best_value = sales[best_product]

# 3. Least-selling product
least_product = min(sales, key=sales.get)
least_value = sales[least_product]

# 4. Total products sold
total_sold = sum(sales.values())

# 5. Products requiring promotion (sales < 15)
promotion_list = [product for product, qty in sales.items() if qty < 15]

# 6. Count products having sales between 10 and 30
between_10_30_count = sum(1 for qty in sales.values() if 10 <= qty <= 30)

# --------------------------------------------------
# Output Section
# --------------------------------------------------

print("Products Sold More Than 20 Times:")
print(" ".join(above_20))

print("\nBest Selling Product:")
print(f"{best_product} ({best_value})")

print("\nLeast Selling Product:")
print(f"{least_product} ({least_value})")

print("\nTotal Units Sold:")
print(total_sold)

print("\nProducts Requiring Promotion:")
print(promotion_list)

print("\nProducts Having Sales Between 10 and 30:")
print(between_10_30_count)