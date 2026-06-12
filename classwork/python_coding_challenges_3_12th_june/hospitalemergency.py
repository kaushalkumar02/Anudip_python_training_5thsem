'''Hospital Emergency Triage System 
Problem Statement 
Patients arriving at the emergency ward are categorized as: 
patients = [ 
    ("P101", "Critical"), 
    ("P102", "Stable"), 
    ("P103", "Critical"), 
    ("P104", "Moderate"), 
    ("P105", "Stable"), 
    ("P106", "Critical"), 
    ("P107", "Moderate"), 
    ("P108", "Stable"), 
    ("P109", "Critical"), 
    ("P110", "Moderate") 
] 
Tasks 
1. Count patients in each category.  
2. Display IDs of critical patients.  
3. Create separate lists for Critical, Moderate, and Stable patients.  
4. Determine which category requires maximum attention.  
5. Save critical patient IDs to critical_patients.txt.  
Sample Output 
Patient Count by Category: 
Critical : 4 
Moderate : 3 
Stable : 3 
 
Critical Patients: 
P101 
P103 
P106 
P109 
 
Critical Patients List: 
['P101', 'P103', 'P106', 'P109'] 
 
Moderate Patients List: 
['P104', 'P107', 'P110'] 
 
Stable Patients List: 
['P102', 'P105', 'P108'] 
 
Category Requiring Maximum Attention: 
Critical 
 
Critical Patient Report Generated Successfully. '''

# Hospital Emergency Triage System

# List of patients with their categories
patients = [
    ("P101", "Critical"),
    ("P102", "Stable"),
    ("P103", "Critical"),
    ("P104", "Moderate"),
    ("P105", "Stable"),
    ("P106", "Critical"),
    ("P107", "Moderate"),
    ("P108", "Stable"),
    ("P109", "Critical"),
    ("P110", "Moderate")
]

# Function to analyze patient data
def triage_system(patient_data):

    try:
        # Lists for different categories
        critical_patients = []
        moderate_patients = []
        stable_patients = []

        # Counters
        critical_count = 0
        moderate_count = 0
        stable_count = 0

        # Process patient records
        for patient_id, category in patient_data:

            if category == "Critical":
                critical_patients.append(patient_id)
                critical_count += 1

            elif category == "Moderate":
                moderate_patients.append(patient_id)
                moderate_count += 1

            elif category == "Stable":
                stable_patients.append(patient_id)
                stable_count += 1

        # Display patient counts
        print("Patient Count by Category:")
        print("Critical :", critical_count)
        print("Moderate :", moderate_count)
        print("Stable :", stable_count)

        # Display critical patients
        print("\nCritical Patients:")
        for patient in critical_patients:
            print(patient)

        # Display lists
        print("\nCritical Patients List:")
        print(critical_patients)

        print("\nModerate Patients List:")
        print(moderate_patients)

        print("\nStable Patients List:")
        print(stable_patients)

        # Determine category requiring maximum attention
        print("\nCategory Requiring Maximum Attention:")

        if critical_count >= moderate_count and critical_count >= stable_count:
            attention_category = "Critical"

        elif moderate_count >= critical_count and moderate_count >= stable_count:
            attention_category = "Moderate"

        else:
            attention_category = "Stable"

        print(attention_category)

        # Save critical patient IDs to file
        try:
            file = open("critical_patients.txt", "w")

            file.write("Critical Patient IDs\n")
            file.write("--------------------\n")

            for patient in critical_patients:
                file.write(patient + "\n")

            file.close()

            print("\nCritical Patient Report Generated Successfully.")

        except PermissionError:
            print("Permission denied while creating the file.")

        except Exception as e:
            print("File Error:", e)

    except Exception as e:
        print("Error:", e)


# Function Call
triage_system(patients)