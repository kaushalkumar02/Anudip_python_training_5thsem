# Problem Statement:
# Create a MobilePhone class to store:
# • Brand Name
# • Model Name
# • Price
# • Available Stock
#
# Implement methods to:
# • Display phone details.
# • Sell a specified quantity of phones.
# • Update stock after sale.
#
# Display an appropriate message if sufficient stock is unavailable.
#
# Sample Output:
# Sale Successful.
# Remaining Stock: 12

#-------------------------------------------------------------------------
# MobilePhone Class
class MobilePhone:
#--------------------------------------------------------------------------
    # Constructor to initialize phone details
    def __init__(self, brand, model, price, stock):
        self.brand = brand
        self.model = model
        self.price = price
        self.stock = stock

    # Method to display phone details
    #----------------------------------------------
    def display_details(self):
        print("\nMobile Phone Details")
        print("-" * 30)
        print("Brand Name     :", self.brand)
        print("Model Name     :", self.model)
        print("Price          : ₹", self.price)
        print("Available Stock:", self.stock)

    # Method to sell phones
    #--------------------------------------------------------
    def sell_phone(self, quantity):
        if quantity <= self.stock:
            self.stock = self.stock - quantity
            print("\nSale Successful.")
            print("Remaining Stock:", self.stock)
        else:
            print("\nInsufficient Stock Available.")

#------------------------------------------------------
# Main Program
#-----------------------------------------------
# Accept phone details
brand = input("Enter Brand Name: ")
model = input("Enter Model Name: ")
price = float(input("Enter Price: ₹"))
stock = int(input("Enter Available Stock: "))

# Create MobilePhone object
phone = MobilePhone(brand, model, price, stock)

# Display phone details
phone.display_details()

# Accept quantity to sell
quantity = int(input("\nEnter Quantity to Sell: "))

# Sell phones
phone.sell_phone(quantity)

# Display updated details
phone.display_details()