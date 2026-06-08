# --------------------------------------------------
# Problem Statement:
# Analyze product prices and perform the following:
# 1. Display products costing more than ₹5000.
# 2. Count products costing less than ₹3000.
# 3. Find the most expensive product.
# 4. Create a list of products priced between
#    ₹2000 and ₹10000.
# 5. Calculate the total value of all products.
# --------------------------------------------------
# Sample Data
prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# --------------------------------------------------
# Validation Section
# --------------------------------------------------

is_valid = True

# Check whether prices is a dictionary
if not isinstance(prices, dict):
    print("Invalid data: Prices should be stored in a dictionary.")
    is_valid = False

# Validate product names and prices
if is_valid:
    for product, price in prices.items():

        # Product name must be a string
        if not isinstance(product, str):
            print("Invalid product name found.")
            is_valid = False
            break

        # Price must be numeric
        if not isinstance(price, (int, float)):
            print(f"Invalid price for {product}.")
            is_valid = False
            break

        # Price cannot be negative
        if price < 0:
            print(f"Negative price found for {product}.")
            is_valid = False
            break

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

if is_valid:

    # Products costing more than ₹5000
    costly_products = [
        product for product, price in prices.items()
        if price > 5000
    ]

    # Count products costing less than ₹3000
    below_3000_count = sum(
        1 for price in prices.values()
        if price < 3000
    )

    # Most expensive product
    expensive_product = max(prices, key=prices.get)
    highest_price = prices[expensive_product]

    # Products priced between ₹2000 and ₹10000
    mid_range_products = [
        product for product, price in prices.items()
        if 2000 <= price <= 10000
    ]

    # Total value of all products
    total_value = sum(prices.values())

    # --------------------------------------------------
    # Output Section
    # --------------------------------------------------

    print("Products costing more than ₹5000:")
    print(costly_products)

    print("\nNumber of products costing less than ₹3000:")
    print(below_3000_count)

    print("\nMost expensive product:")
    print(f"{expensive_product} - ₹{highest_price}")

    print("\nProducts priced between ₹2000 and ₹10000:")
    print(mid_range_products)

    print("\nTotal value of all products:")
    print(f"₹{total_value}")