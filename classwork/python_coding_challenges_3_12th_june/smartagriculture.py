'''Smart Agriculture Crop Monitoring System 
Problem Statement 
Crop moisture levels (%) are stored as follows: 
moisture = { 
    "Field1": 55, 
    "Field2": 30, 
    "Field3": 72, 
    "Field4": 28, 
    "Field5": 64, 
    "Field6": 35, 
    "Field7": 80, 
    "Field8": 42, 
    "Field9": 25, 
    "Field10": 68 
} 
Tasks 
1. Identify fields requiring irrigation (< 40%).  
2. Classify fields into Low, Moderate, and High moisture categories.  
3. Count fields in each category.  
4. Find fields with the highest and lowest moisture levels.  
5. Generate an irrigation priority list.  
Sample Output 
Fields Requiring Irrigation: 
Field2 
Field4 
Field6 
Field9 
 
Low Moisture Fields: 
['Field2', 'Field4', 'Field6', 'Field9'] 
 
Moderate Moisture Fields: 
['Field1', 'Field5', 'Field8'] 
 
High Moisture Fields: 
['Field3', 'Field7', 'Field10'] 
 
Field with Highest Moisture: 
Field7 (80%) 
 
Field with Lowest Moisture: 
Field9 (25%) 
 
Irrigation Priority List: 
['Field9', 'Field4', 'Field2', 'Field6']'''

# Smart Agriculture Crop Monitoring System

# Dictionary storing moisture levels
moisture = {
    "Field1": 55,
    "Field2": 30,
    "Field3": 72,
    "Field4": 28,
    "Field5": 64,
    "Field6": 35,
    "Field7": 80,
    "Field8": 42,
    "Field9": 25,
    "Field10": 68
}

# Function to analyze crop moisture
def crop_monitoring(data):

    try:
        # Lists for categorization
        low_moisture = []
        moderate_moisture = []
        high_moisture = []

        # Fields requiring irrigation
        irrigation_fields = []

        # Assume first field has highest and lowest moisture
        fields = list(data.keys())

        highest_field = fields[0]
        lowest_field = fields[0]

        highest_moisture = data[highest_field]
        lowest_moisture = data[lowest_field]

        # Process all fields
        for field in data:

            moisture_level = data[field]

            # Fields requiring irrigation
            if moisture_level < 40:
                irrigation_fields.append(field)

            # Categorize moisture levels
            if moisture_level < 40:
                low_moisture.append(field)

            elif moisture_level <= 65:
                moderate_moisture.append(field)

            else:
                high_moisture.append(field)

            # Find highest moisture
            if moisture_level > highest_moisture:
                highest_moisture = moisture_level
                highest_field = field

            # Find lowest moisture
            if moisture_level < lowest_moisture:
                lowest_moisture = moisture_level
                lowest_field = field

        # Create irrigation priority list
        priority_list = sorted(
            irrigation_fields,
            key=lambda field: data[field]
        )

        # Display fields requiring irrigation
        print("Fields Requiring Irrigation:")
        for field in irrigation_fields:
            print(field)

        # Display categories
        print("\nLow Moisture Fields:")
        print(low_moisture)

        print("\nModerate Moisture Fields:")
        print(moderate_moisture)

        print("\nHigh Moisture Fields:")
        print(high_moisture)

        # Display counts
        print("\nCount of Low Moisture Fields:", len(low_moisture))
        print("Count of Moderate Moisture Fields:", len(moderate_moisture))
        print("Count of High Moisture Fields:", len(high_moisture))

        # Display highest and lowest moisture fields
        print("\nField with Highest Moisture:")
        print(highest_field, "(" + str(highest_moisture) + "%)")

        print("\nField with Lowest Moisture:")
        print(lowest_field, "(" + str(lowest_moisture) + "%)")

        # Display irrigation priority list
        print("\nIrrigation Priority List:")
        print(priority_list)

    except Exception as e:
        print("Error:", e)


# Function Call
crop_monitoring(moisture)