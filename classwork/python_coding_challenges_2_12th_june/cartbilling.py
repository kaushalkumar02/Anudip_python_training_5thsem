'''Online Shopping Inventory System 
Problem Statement 
An online store maintains stock quantities of products. 
Sample Data 
inventory = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products with stock below 15 units.  
2. Find the product with maximum stock.  
3. Find the product with minimum stock.  
4. Calculate total stock available.  
5. Create a list of products requiring restocking (<10 units).  
Sample Output 
Products with Stock Below 15: 
Monitor 
Printer 
Tablet 
 
Highest Stock Product: 
Mouse (45 units) 
 
Lowest Stock Product: 
Printer (8 units) 
 
Total Stock Available: 213 
 
Products Requiring Restocking: 
['Printer']'''




#creating dictionary of stock data

inventory = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 

#Display products with stock below 15 units. 
("Products with Stock Below 15:") 

for item,stock in inventory.items():
    if stock<15:
        print(item)


#Find the product with maximum stock.  

product_max = list(inventory.keys())[0]
max_stock = inventory[product_max]

for item, stock in inventory.items():
    if stock > max_stock:
        max_stock = stock
        product_max = item

print("Highest Stock Product:")
print(product_max, max_stock, "units")

#Find the product with minimum stock.  

product_min = list(inventory.keys())[0]
min_stock = inventory[product_min]

for item, stock in inventory.items():
    if stock < min_stock:
        min_stock = stock
        product_min = item

print("Minimum Stock Product:")
print(product_min, min_stock, "units")

#Calculate total stock available. 

total=sum(inventory.values())

print("Total Stock Available:",total)

#Create a list of products requiring restocking (<10 units).  

restock=[]

for item,stock in inventory.items():
    if stock<10:
        restock.append(item)
print("Products Requiring Restocking: ")
print(restock)