'''Space Mission Telemetry Analyzer 
Problem Statement 
Sensor readings are stored in telemetry.txt. 
101 
98 
105 
110 
112 
95 
90 
88 
120 
102 
Tasks 
1. Read all sensor readings.  
2. Display abnormal readings (< 90 or > 110).  
3. Calculate average sensor value.  
4. Count normal and abnormal readings.  
5. Store abnormal readings in alerts.txt.  
Sample Output 
Abnormal Sensor Readings: 
88 
120 
 
Average Sensor Value: 
102.1 
 
Normal Readings: 8 
Abnormal Readings: 2 
 
Alert File Generated Successfully.'''


# Space Mission Telemetry Analyzer

# Function to analyze telemetry data
def telemetry_analyzer():

    try:
        # Open telemetry file
        file = open("telemetry.txt", "r")

        # Read all readings
        readings = file.readlines()

        file.close()

        # List to store sensor values
        sensor_values = []

        # List to store abnormal readings
        abnormal_readings = []

        total = 0
        normal_count = 0
        abnormal_count = 0

        # Process readings
        for reading in readings:

            reading = reading.strip()

            # Skip empty lines
            if reading == "":
                continue

            value = int(reading)

            sensor_values.append(value)

            total += value

            # Check whether reading is normal or abnormal
            if value < 90 or value > 110:
                abnormal_readings.append(value)
                abnormal_count += 1
            else:
                normal_count += 1

        # Calculate average
        average = total / len(sensor_values)

        # Display abnormal readings
        print("Abnormal Sensor Readings:")

        if len(abnormal_readings) > 0:
            for value in abnormal_readings:
                print(value)
        else:
            print("None")

        print("\nAverage Sensor Value:")
        print(round(average, 1))

        print("\nNormal Readings:", normal_count)
        print("Abnormal Readings:", abnormal_count)

        # Store abnormal readings in alerts.txt
        try:
            alert_file = open("alerts.txt", "w")

            alert_file.write("Abnormal Sensor Readings\n")
            alert_file.write("------------------------\n")

            for value in abnormal_readings:
                alert_file.write(str(value) + "\n")

            alert_file.close()

            print("\nAlert File Generated Successfully.")

        except Exception as e:
            print("Error while creating alert file:", e)

    except FileNotFoundError:
        print("Error: telemetry.txt file not found.")

    except ValueError:
        print("Error: File contains invalid sensor data.")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except Exception as e:
        print("Unexpected Error:", e)


# Function Call
telemetry_analyzer()