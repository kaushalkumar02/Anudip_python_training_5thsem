'''Library Book Issue Tracker 
Problem Statement 
A library stores the number of times books were issued during a month. 
Sample Data 
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25] 
Tasks 
1. Find the maximum number of issues.  
2. Find the minimum number of issues.  
3. Calculate the average number of issues.  
4. Count books issued more than 15 times.  
5. Create a list of books issued fewer than 10 times.  
Sample Output 
Maximum Issues: 30 
 
Minimum Issues: 5 
 
Average Issues: 16.5 
 
Books Issued More Than 15 Times: 5 
 
Books Issued Fewer Than 10 Times: 
[8, 5] 
 
Problem 14: Shopping Cart Billing System 
Problem Statement 
The prices of products purchased by a customer are stored in a tuple. 
Sample Data 
prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200) 
Tasks 
1. Calculate the total bill amount.  
2. Find the most expensive product.  
3. Find the least expensive product.  
4. Count products costing more than ₹1,000.  
5. Create a list of products eligible for discount (price > ₹800).  
Sample Output 
Total Bill Amount: ₹8,248 
 
Most Expensive Product: ₹1,500 
 
Least Expensive Product: ₹250 
Products Costing More Than ₹1,000: 3 
Discount Eligible Products: 
[1250, 999, 1500, 850, 1200]'''


# Library Book Issue Tracker

# List storing the number of times books were issued
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]

# --------------------------------------------------
# Task 1: Find the maximum number of issues
# --------------------------------------------------

maximum_issues = book_issues[0]

for issues in book_issues:
    if issues > maximum_issues:
        maximum_issues = issues

print("Maximum Issues:", maximum_issues)

# --------------------------------------------------
# Task 2: Find the minimum number of issues
# --------------------------------------------------

minimum_issues = book_issues[0]

for issues in book_issues:
    if issues < minimum_issues:
        minimum_issues = issues

print("\nMinimum Issues:", minimum_issues)

# --------------------------------------------------
# Task 3: Calculate the average number of issues
# --------------------------------------------------

total_issues = 0

for issues in book_issues:
    total_issues += issues

average_issues = total_issues / len(book_issues)

print("\nAverage Issues:", average_issues)

# --------------------------------------------------
# Task 4: Count books issued more than 15 times
# --------------------------------------------------

count = 0

for issues in book_issues:
    if issues > 15:
        count += 1

print("\nBooks Issued More Than 15 Times:", count)

# --------------------------------------------------
# Task 5: Create a list of books issued fewer than 10 times
# --------------------------------------------------

less_than_10 = []

for issues in book_issues:
    if issues < 10:
        less_than_10.append(issues)

print("\nBooks Issued Fewer Than 10 Times:")
print(less_than_10)