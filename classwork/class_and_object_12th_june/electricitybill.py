# Problem Statement:
# Create an ElectricityBill class containing:
# • Consumer Name
# • Consumer Number
# • Units Consumed
# Implement methods to:
# • Calculate electricity charges using the following slab:
#   First 100 Units    : ₹5 per unit
#   Next 100 Units     : ₹7 per unit
#   Above 200 Units    : ₹10 per unit
# • Display the final bill.
# Sample Output:
# Consumer Name : Amit
# Units Consumed: 250
# Total Bill    : ₹1700
#------------------------------------------------------------
# ElectricityBill Class
class ElectricityBill:

    # Constructor to initialize consumer details
    #------------------------------------------------------
    def __init__(self, consumer_name, consumer_number, units):
        self.consumer_name = consumer_name
        self.consumer_number = consumer_number
        self.units = units

    # Method to calculate electricity bill
    #-------------------------------------------------------------
    def calculate_bill(self):

        if self.units <= 100:
            bill = self.units * 5

        elif self.units <= 200:
            bill = (100 * 5) + ((self.units - 100) * 7)

        else:
            bill = (100 * 5) + (100 * 7) + ((self.units - 200) * 10)

        return bill

    # Method to display final bill
    #-----------------------------------------------------
    def display_bill(self):
        print("\nElectricity Bill")
        print("-" * 30)
        print("Consumer Name  :", self.consumer_name)
        print("Consumer Number:", self.consumer_number)
        print("Units Consumed :", self.units)
        print("Total Bill     : ₹", self.calculate_bill())

#---------------------------------------------------------------------
# Main Program
#------------------------------------------------------------------
# Accept consumer details
consumer_name = input("Enter Consumer Name: ")
consumer_number = input("Enter Consumer Number: ")
units = int(input("Enter Units Consumed: "))

# Create object
bill = ElectricityBill(consumer_name, consumer_number, units)

# Display bill
bill.display_bill()