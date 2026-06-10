'''Vehicle Registration Verification System 
Problem Statement 
A transport department wants to verify vehicle registration numbers. 
Store at least 20 vehicle numbers. 
Example 
MH12AB4589 
DL05XY9988 
KA03PQ1234 
Requirements 
For each registration number: 
1. Extract state code.  
2. Extract district code.  
3. Extract series.  
4. Extract vehicle number.  
5. Count letters and digits.  
6. Validate format:  
o First 2 characters = Alphabets  
o Next 2 characters = Digits  
o Next 2 characters = Alphabets  
o Last 4 characters = Digits  
7. Display invalid registrations.  
8. Count vehicles state-wise.  
Challenge 
Generate a state-wise report: 
MH -> 6 Vehicles 
DL -> 4 Vehicles 
KA -> 5 Vehicles 
UP -> 5 Vehicles '''


# ==========================================
# VEHICLE REGISTRATION VERIFICATION SYSTEM
# ==========================================

# List to store vehicle numbers

vehicles = []

# Dictionary for state-wise count

state_count = {}

# List for invalid registrations

invalid_registrations = []

# ==========================================
# INPUT 20 VEHICLE NUMBERS
# ==========================================

for i in range(1, 21):

    vehicle = input(f"Enter Vehicle Number {i}: ")

    vehicles.append(vehicle)

# ==========================================
# PROCESS EACH VEHICLE NUMBER
# ==========================================

for vehicle in vehicles:

    print("\n================================")
    print("Registration Number :", vehicle)
    print("================================")

    # --------------------------------------
    # Length Check
    # --------------------------------------

    valid = True

    if len(vehicle) != 10:

        valid = False

    else:

        # ----------------------------------
        # Extract Components
        # ----------------------------------

        state_code = vehicle[0:2]

        district_code = vehicle[2:4]

        series = vehicle[4:6]

        vehicle_number = vehicle[6:10]

        # ----------------------------------
        # Count Letters and Digits
        # ----------------------------------

        letters = 0
        digits = 0

        for ch in vehicle:

            if ch.isalpha():

                letters += 1

            elif ch.isdigit():

                digits += 1

        # ----------------------------------
        # Validation Rules
        # ----------------------------------

        if not vehicle[0:2].isalpha():

            valid = False

        if not vehicle[2:4].isdigit():

            valid = False

        if not vehicle[4:6].isalpha():

            valid = False

        if not vehicle[6:10].isdigit():

            valid = False

        # ----------------------------------
        # Display Extracted Data
        # ----------------------------------

        print("State Code :", state_code)

        print("District Code :", district_code)

        print("Series :", series)

        print("Vehicle Number :", vehicle_number)

        print("Letters :", letters)

        print("Digits :", digits)

    # --------------------------------------
    # Valid / Invalid Status
    # --------------------------------------

    if valid:

        print("Registration Status : Valid")

        # State-wise Count

        if state_code in state_count:

            state_count[state_code] += 1

        else:

            state_count[state_code] = 1

    else:

        print("Registration Status : Invalid")

        invalid_registrations.append(vehicle)

# ==========================================
# INVALID REGISTRATION REPORT
# ==========================================

print("\n================================")
print("INVALID REGISTRATIONS")
print("================================")

for vehicle in invalid_registrations:

    print(vehicle)

# ==========================================
# STATE-WISE REPORT
# ==========================================

print("\n================================")
print("STATE-WISE VEHICLE REPORT")
print("================================")

for state, count in state_count.items():

    print(state, "->", count, "Vehicles")