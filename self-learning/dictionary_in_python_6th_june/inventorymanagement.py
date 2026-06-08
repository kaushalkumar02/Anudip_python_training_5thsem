# --------------------------------------------------
# Problem Statement:
# Analyze inventory data and perform the following:
# 1. Display products with stock less than 10.
# 2. Count products having stock more than 50.
# 3. Find the product with the minimum stock.
# 4. Create a list of products that require restocking
#    (stock < 20).
# 5. Calculate the total inventory count.
# --------------------------------------------------
# Sample Data
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# --------------------------------------------------
# Validation Section
# --------------------------------------------------

is_valid = True

# Check whether inventory is a dictionary
if not isinstance(inventory, dict):
    print("Invalid data: Inventory should be a dictionary.")
    is_valid = False

# Validate product names and stock values
if is_valid:
    for product, stock in inventory.items():

        # Product name must be string
        if not isinstance(product, str):
            print("Invalid product name found.")
            is_valid = False
            break

        # Stock must be an integer
        if not isinstance(stock, int):
            print(f"Invalid stock value for {product}.")
            is_valid = False
            break

        # Stock cannot be negative
        if stock < 0:
            print(f"Negative stock found for {product}.")
            is_valid = False
            break

# --------------------------------------------------
# Processing Section
# --------------------------------------------------

if is_valid:

    # Products with stock less than 10
    low_stock_products = [
        product for product, stock in inventory.items()
        if stock < 10
    ]

    # Count products having stock more than 50
    products_above_50 = sum(
        1 for stock in inventory.values()
        if stock > 50
    )

    # Product with minimum stock
    min_stock_product = min(inventory, key=inventory.get)
    min_stock = inventory[min_stock_product]

    # Products requiring restocking (stock < 20)
    restock_products = [
        product for product, stock in inventory.items()
        if stock < 20
    ]

    # Total inventory count
    total_inventory = sum(inventory.values())

    # --------------------------------------------------
    # Output Section
    # --------------------------------------------------

    print("Products with stock less than 10:")
    print(low_stock_products)

    print("\nNumber of products having stock more than 50:")
    print(products_above_50)

    print("\nProduct with minimum stock:")
    print(f"{min_stock_product} - {min_stock}")

    print("\nProducts requiring restocking:")
    print(restock_products)

    print("\nTotal inventory count:")
    print(total_inventory)