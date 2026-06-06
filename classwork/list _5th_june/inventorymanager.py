# Problem Statement:
# An inventory manager stores stock quantities as a list.
# Tasks:
# 1. Count out of stock products (0 quantity)
# 2. Show products needing restock (less than 10)
# 3. Count available products (greater than 0)
# 4. Create list of healthy stock (>= 15)

stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock = 0
restock = []
available = 0
healthy_stock = []

# traverse each stock item
for s in stock:

    # check out of stock
    if s == 0:
        out_of_stock += 1

    # check restock condition
    if s < 10:
        restock.append(s)

    # check available stock
    if s > 0:
        available += 1

    # check healthy stock
    if s >= 15:
        healthy_stock.append(s)

# display results
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock)
print("Available Products:", available)
print("Healthy Stock:", healthy_stock)