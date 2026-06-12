# Problem 3: E-Commerce Coupon Fraud Detection

# Problem Statement:
# A file named coupons.txt contains coupon usage records.
#
# Sample Input/Data (coupons.txt)
# SAVE50
# WELCOME20
# SAVE50
# FESTIVE10
# SAVE50
# WELCOME20
# NEWUSER
# FESTIVE10
# SAVE50
# NEWUSER
#
# Tasks:
# 1. Count the usage frequency of each coupon.
# 2. Identify coupons used more than 3 times.
# 3. Create a set of unique coupons.
# 4. Display the most frequently used coupon.
# 5. Save suspicious coupon records into fraud_report.txt.
#
# Sample Output:
# Coupon Usage Frequency:
# SAVE50 : 4
# WELCOME20 : 2
# FESTIVE10 : 2
# NEWUSER : 2
#
# Suspicious Coupons:
# SAVE50
#
# Unique Coupons:
# {'SAVE50', 'WELCOME20', 'FESTIVE10', 'NEWUSER'}
#
# Most Frequently Used Coupon:
# SAVE50
#
# Fraud Report Generated Successfully


# Function to analyze coupon usage
def coupon_fraud_detection():

    try:

        # Open coupon file in read mode
        file = open("coupons.txt", "r")

        # Read all coupon records
        coupons = file.readlines()

        # Close file
        file.close()

        # Remove newline characters
        coupons = [coupon.strip() for coupon in coupons]

        # Dictionary to store coupon frequency
        coupon_frequency = {}

        # Count coupon usage frequency
        for coupon in coupons:

            if coupon in coupon_frequency:

                coupon_frequency[coupon] += 1

            else:

                coupon_frequency[coupon] = 1

        # Create set of unique coupons
        unique_coupons = set(coupons)

        # List to store suspicious coupons
        suspicious_coupons = []

        # Variables for most frequent coupon
        most_used_coupon = ""
        highest_count = 0

        # Check frequency details
        for coupon, count in coupon_frequency.items():

            # Find suspicious coupons
            if count > 3:

                suspicious_coupons.append(coupon)

            # Find most frequently used coupon
            if count > highest_count:

                highest_count = count
                most_used_coupon = coupon

        # Create fraud report file
        report_file = open("fraud_report.txt", "w")

        report_file.write("Suspicious Coupon Report\n")
        report_file.write("-------------------------\n")

        # Save suspicious coupon details
        for coupon in suspicious_coupons:

            report_file.write(coupon + "\n")

        report_file.close()

        # Display results
        print("Coupon Usage Frequency:")

        for coupon, count in coupon_frequency.items():

            print(coupon, ":", count)

        print("\nSuspicious Coupons:")

        if len(suspicious_coupons) > 0:

            for coupon in suspicious_coupons:

                print(coupon)

        else:

            print("None")

        print("\nUnique Coupons:")

        print(unique_coupons)

        print("\nMost Frequently Used Coupon:")

        print(most_used_coupon)

        print("\nFraud Report Generated Successfully")

    except FileNotFoundError:

        print("Error: coupons.txt file not found.")

    except Exception as e:

        print("Error:", e)

    finally:

        print("\nCoupon Fraud Detection Completed.")


# Function Call
coupon_fraud_detection()