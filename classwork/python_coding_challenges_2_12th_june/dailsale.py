# Problem 17: Daily Sales Performance Analyzer

# Problem Statement:
# Daily sales figures (in ₹) for 10 days are stored in a list.
#
# Sample Data
# sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000]
#
# Tasks:
# 1. Find the highest sales.
# 2. Find the lowest sales.
# 3. Calculate average sales.
# 4. Count days with sales above ₹20,000.
# 5. Display sales figures below average.
#
# Sample Output
# Highest Sales: ₹30,000
# Lowest Sales: ₹15,000
# Average Sales: ₹22,100
# Days with Sales Above ₹20,000: 5
# Sales Below Average: [15000, 18000, 17000, 21000, 19000]

try:

    # Store daily sales data in a list
    sales = [15000, 22000, 18000, 25000, 30000,
             17000, 28000, 26000, 21000, 19000]

    # Find highest sales value
    highest_sales = max(sales)

    # Find lowest sales value
    lowest_sales = min(sales)

    # Calculate total sales
    total_sales = sum(sales)

    # Calculate average sales
    average_sales = total_sales / len(sales)

    # Initialize counter for sales above ₹20,000
    above_20000_count = 0

    # Initialize list for sales below average
    below_average_sales = []

    # Traverse sales list
    for amount in sales:

        # Count sales greater than ₹20,000
        if amount > 20000:
            above_20000_count += 1

        # Store sales below average
        if amount < average_sales:
            below_average_sales.append(amount)

    # Display results
    print("Highest Sales: ₹", highest_sales)
    print("Lowest Sales: ₹", lowest_sales)
    print("Average Sales: ₹", average_sales)
    print("Days with Sales Above ₹20,000:", above_20000_count)
    print("Sales Below Average:", below_average_sales)

except Exception as e:

    # Handle unexpected errors
    print("Error:", e)

finally:

    # Always executed
    print("Daily sales performance analysis completed.")