'''Airport Baggage Screening System 
Problem Statement 
Passenger baggage weights (in kg) are stored as tuples: 
baggage = ( 
("P101", 18), 
("P102", 32), 
("P103", 24), 
("P104", 36), 
("P105", 28), 
("P106", 20), 
("P107", 41), 
("P108", 26), 
("P109", 19), 
("P110", 34) 
) 
Tasks 
1. Display passengers carrying baggage above 30 kg.  
2. Count passengers within and exceeding limits.  
3. Calculate excess baggage charges (₹500 per kg above 30 kg).  
4. Create a list of passengers requiring manual inspection.  
5. Find the passenger carrying the heaviest baggage.  
Sample Output 
Passengers Exceeding 30 kg Limit: 
P102 
P104 
P107 
P110 
Passengers Within Limit: 6 
Passengers Exceeding Limit: 4 
Excess Baggage Charges: 
P102 : ₹1000 
P104 : ₹3000 
P107 : ₹5500 
P110 : ₹2000 
Passengers Requiring Manual Inspection: 
['P102', 'P104', 'P107', 'P110']'''


# Airport Baggage Screening System

# Tuple containing passenger ID and baggage weight
baggage = (
    ("P101", 18),
    ("P102", 32),
    ("P103", 24),
    ("P104", 36),
    ("P105", 28),
    ("P106", 20),
    ("P107", 41),
    ("P108", 26),
    ("P109", 19),
    ("P110", 34)
)

# Function to analyze baggage details
def baggage_screening(data):

    within_limit = 0
    exceeding_limit = 0

    # Dictionary to store excess baggage charges
    charges = {}

    # List for passengers requiring manual inspection
    inspection_list = []

    # Assume first passenger has the heaviest baggage
    heaviest_passenger = data[0][0]
    max_weight = data[0][1]

    print("Passengers Exceeding 30 kg Limit:")

    # Process each passenger
    for passenger_id, weight in data:

        # Find passenger with heaviest baggage
        if weight > max_weight:
            max_weight = weight
            heaviest_passenger = passenger_id

        # Check baggage limit
        if weight > 30:
            print(passenger_id)

            exceeding_limit += 1

            # Calculate excess baggage charge
            excess_weight = weight - 30
            charges[passenger_id] = excess_weight * 500

            # Add passenger to inspection list
            inspection_list.append(passenger_id)

        else:
            within_limit += 1

    # Display counts
    print("\nPassengers Within Limit:", within_limit)
    print("Passengers Exceeding Limit:", exceeding_limit)

    # Display charges
    print("\nExcess Baggage Charges:")
    for passenger in charges:
        print(passenger, ": ₹", charges[passenger], sep="")

    # Display inspection list
    print("\nPassengers Requiring Manual Inspection:")
    print(inspection_list)

    # Display heaviest baggage details
    print("\nPassenger Carrying Heaviest Baggage:")
    print(heaviest_passenger, "-", max_weight, "kg")


# Exception handling
try:
    baggage_screening(baggage)

except Exception as e:
    print("Error:", e)