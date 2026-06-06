# Problem Statement:
# Product IDs and their quality status are stored in a list of tuples.
# products = [
#     (101, "Pass"),
#     (102, "Fail"),
#     (103, "Pass"),
#     (104, "Fail"),
#     (105, "Pass")
# ]
# Write a program to:
# • Display failed product IDs
# • Count passed and failed products
# • Calculate pass percentage
# • Stop checking if 3 failures are found
# Product data (Product ID, Status)
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]
# Counters
pass_count = 0
fail_count = 0
# List for failed product IDs
failed_products = []
# Counter to stop after 3 failures
failure_limit = 3
# Loop through products
for product_id, status in products:
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1
        failed_products.append(product_id)

        # Stop checking if 3 failures are found
        if fail_count == failure_limit:
            break

# Total processed products
total = pass_count + fail_count

# Calculate pass percentage
pass_percentage = (pass_count / total) * 100

# Display results
print("Failed Product IDs:", failed_products)
print("Passed Products:", pass_count)
print("Failed Products:", fail_count)
print("Pass Percentage:", round(pass_percentage, 2), "%")