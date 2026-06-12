'''Disaster Relief Resource Allocation 
Problem Statement 
Relief materials available at different warehouses are stored as dictionaries. 
resources = { 
"Warehouse1": ["Food", "Medicine", "Blankets"],
    "Warehouse2": ["Water", "Food", "Tents"], 
    "Warehouse3": ["Medicine", "Tents", "Clothes"], 
    "Warehouse4": ["Food", "Water", "Medicine"] 
} 
Tasks 
1. Display all unique relief items.  
2. Find warehouses containing medicines.  
3. Count how many warehouses stock each resource.  
4. Identify the most widely available resource.  
5. Display resources available in all warehouses.  
Sample Output 
Unique Resources: 
{'Food', 'Medicine', 'Blankets', 'Water', 'Tents', 'Clothes'} 
 
Warehouses with Medicines: 
Warehouse1 
Warehouse3 
Warehouse4 
 
Resource Availability: 
Food : 3 
Medicine : 3 
Blankets : 1 
Water : 2 
Tents : 2 
Clothes : 1 
 
Most Widely Available Resources: 
Food 
Medicine 
 
Resources Available in All Warehouses: 
None 
'''
# Disaster Relief Resource Allocation

# Dictionary storing resources in warehouses
resources = {
    "Warehouse1": ["Food", "Medicine", "Blankets"],
    "Warehouse2": ["Water", "Food", "Tents"],
    "Warehouse3": ["Medicine", "Tents", "Clothes"],
    "Warehouse4": ["Food", "Water", "Medicine"]
}

# Function to analyze resources
def analyze_resources(resources):

    try:
        # Set to store all unique resources
        unique_resources = set()

        # Dictionary to store resource availability count
        resource_count = {}

        # List to store warehouses having medicines
        medicine_warehouses = []

        # Process each warehouse
        for warehouse in resources:

            items = resources[warehouse]

            # Check for medicine availability
            if "Medicine" in items:
                medicine_warehouses.append(warehouse)

            # Process resources
            for item in items:

                unique_resources.add(item)

                if item in resource_count:
                    resource_count[item] += 1
                else:
                    resource_count[item] = 1

        # Display unique resources
        print("Unique Resources:")
        print(unique_resources)

        # Display warehouses containing medicines
        print("\nWarehouses with Medicines:")
        for warehouse in medicine_warehouses:
            print(warehouse)

        # Display resource availability
        print("\nResource Availability:")
        for item in resource_count:
            print(item, ":", resource_count[item])

        # Find maximum availability
        max_count = max(resource_count.values())

        print("\nMost Widely Available Resources:")
        for item in resource_count:
            if resource_count[item] == max_count:
                print(item)

        # Find resources available in all warehouses
        common_resources = set(resources["Warehouse1"])

        for warehouse in resources:
            common_resources = common_resources.intersection(
                set(resources[warehouse])
            )

        print("\nResources Available in All Warehouses:")

        if len(common_resources) > 0:
            for item in common_resources:
                print(item)
        else:
            print("None")

    except Exception as e:
        print("Error:", e)


# Function Call
analyze_resources(resources)