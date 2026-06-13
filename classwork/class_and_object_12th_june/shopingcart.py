# Problem Statement:
# Create a Product class containing product name,
# quantity, and price per unit.
# Implement methods to:
# • Calculate total price.
# • Update quantity.
# • Display product details.
# Sample Output:
# Product Name : Laptop
# Quantity     : 2
# Unit Price   : ₹45000
# Total Price  : ₹90000
#============================================================================

# Product Class
class Product:

    # Constructor to initialize product details
    #=======================================================================
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    # Method to calculate total price
    #=====================================================================
    def calculate_total_price(self):
        return self.quantity * self.unit_price

    # Method to update quantity
    #==========================================================================
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    # Method to display product details
    #====================================================================
    def display_details(self):
        print("\nProduct Details")
        print("-" * 30)
        print("Product Name :", self.name)
        print("Quantity     :", self.quantity)
        print("Unit Price   : ₹", self.unit_price)
        print("Total Price  : ₹", self.calculate_total_price())

#==================================================
# Main Program
#==================================================
# Accept product name
product_name = input("Enter Product Name: ")

# Accept quantity
quantity = int(input("Enter Quantity: "))

# Accept unit price
unit_price = float(input("Enter Unit Price: ₹"))

# Create Product Object
product = Product(product_name, quantity, unit_price)

# Display product details
product.display_details()

# Update quantity
new_quantity = int(input("\nEnter New Quantity: "))
product.update_quantity(new_quantity)

# Display updated details
print("\nAfter Updating Quantity")
product.display_details()