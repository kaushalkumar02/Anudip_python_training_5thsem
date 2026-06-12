'''Function-Based Temperature Converter 
Problem Statement 
Daily temperatures recorded in Celsius are given below. 
Sample Data 
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31] 
Tasks 
Create functions to: 
1. Convert Celsius to Fahrenheit.  
2. Display all temperatures in Fahrenheit.  
3. Find the highest Fahrenheit temperature.  
4. Find the lowest Fahrenheit temperature.  
5. Calculate the average Fahrenheit temperature.  
Sample Output 
Temperatures in Fahrenheit: 
77.0 
86.0 
95.0 
104.0 
82.4 
89.6 
100.4 
71.6 
80.6 
87.8 
Highest Temperature: 104.0°F 
Lowest Temperature: 71.6 
Average Temperature: 87.14°F'''
# Function-Based Temperature Converter

# List storing temperatures in Celsius
temperatures = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31]

# --------------------------------------------------
# Function to convert Celsius to Fahrenheit
# Formula: (C × 9/5) + 32
# --------------------------------------------------

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# --------------------------------------------------
# Function to display all temperatures
# in Fahrenheit
# --------------------------------------------------

def display_fahrenheit(temperature_list):

    print("Temperatures in Fahrenheit:")

    for temp in temperature_list:
        print(celsius_to_fahrenheit(temp))

# --------------------------------------------------
# Function to find the highest
# Fahrenheit temperature
# --------------------------------------------------

def highest_temperature(temperature_list):

    highest = celsius_to_fahrenheit(temperature_list[0])

    for temp in temperature_list:
        fahrenheit = celsius_to_fahrenheit(temp)

        if fahrenheit > highest:
            highest = fahrenheit

    return highest

# --------------------------------------------------
# Function to find the lowest
# Fahrenheit temperature
# --------------------------------------------------

def lowest_temperature(temperature_list):

    lowest = celsius_to_fahrenheit(temperature_list[0])

    for temp in temperature_list:
        fahrenheit = celsius_to_fahrenheit(temp)

        if fahrenheit < lowest:
            lowest = fahrenheit

    return lowest

# --------------------------------------------------
# Function to calculate the average
# Fahrenheit temperature
# --------------------------------------------------

def average_temperature(temperature_list):

    total = 0

    for temp in temperature_list:
        total += celsius_to_fahrenheit(temp)

    average = total / len(temperature_list)

    return average

# --------------------------------------------------
# Function Calls
# --------------------------------------------------

display_fahrenheit(temperatures)

print("\nHighest Temperature:", highest_temperature(temperatures), "°F")

print("Lowest Temperature:", lowest_temperature(temperatures), "°F")

print("Average Temperature:", round(average_temperature(temperatures), 2), "°F")