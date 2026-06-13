# Problem Statement:
# Design a Vehicle class containing:
# • Vehicle Number
# • Vehicle Type
# • Rent per Day
#
# Implement methods to:
# • Accept vehicle details.
# • Calculate total rental amount based on the number of days rented.
# • Display the bill.
#
# Sample Output:
# Vehicle Type : Car
# Days Rented  : 5
# Total Rent   : ₹10000
#-------------------------------------------------------------------

# Vehicle Class
class Vehicle:

    # Constructor to initialize vehicle details
    #-------------------------------------------------------------------
    def __init__(self, vehicle_no, vehicle_type, rent_per_day):
        self.vehicle_no = vehicle_no
        self.vehicle_type = vehicle_type
        self.rent_per_day = rent_per_day

    # Method to calculate total rent
    #-----------------------------------------------------------------------
    def calculate_rent(self, days):
        return self.rent_per_day * days

    # Method to display bill
    #----------------------------------------------------------------------
    def display_bill(self, days):
        total_rent = self.calculate_rent(days)

        print("\nVehicle Rental Bill")
        print("-" * 30)
        print("Vehicle Number :", self.vehicle_no)
        print("Vehicle Type   :", self.vehicle_type)
        print("Rent Per Day   : ₹", self.rent_per_day)
        print("Days Rented    :", days)
        print("Total Rent     : ₹", total_rent)

#----------------------------------------------------------------------
# Main Program
#-----------------------------------------------------------------------
# Accept vehicle number
vehicle_no = input("Enter Vehicle Number: ")

# Accept vehicle type
vehicle_type = input("Enter Vehicle Type: ")

# Accept rent per day
rent_per_day = float(input("Enter Rent Per Day: ₹"))

# Accept number of days rented
days = int(input("Enter Number of Days Rented: "))

# Create Vehicle Object
vehicle = Vehicle(vehicle_no, vehicle_type, rent_per_day)

# Display rental bill
vehicle.display_bill(days)