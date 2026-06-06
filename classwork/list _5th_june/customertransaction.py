# Store all transactions (positive = deposit, negative = withdrawal)
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Initialize variables
balance = 0
deposits = []
withdrawals = []

# To track largest values
largest_deposit = 0
largest_withdrawal = 0

# To count transactions
deposit_count = 0
withdrawal_count = 0

# Process each transaction
for t in transactions:

    # Add to total balance
    balance += t

    # If deposit
    if t > 0:
        deposits.append(t)
        deposit_count += 1

        # Update largest deposit
        if t > largest_deposit:
            largest_deposit = t

    # If withdrawal
    else:
        withdrawals.append(t)
        withdrawal_count += 1

        # Update largest withdrawal (most negative value)
        if t < largest_withdrawal:
            largest_withdrawal = t

# Display final results
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)