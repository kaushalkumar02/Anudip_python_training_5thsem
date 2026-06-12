# Problem 1: Cyber Security Login Audit System
# Problem Statement:
# A file named login_logs.txt contains user login attempts
# in the following format:
# username,status
# anuj,Success
# rahul,Failed
# anuj,Failed
# priya,Failed
# rahul,Failed
# neha,Success
# anuj,Failed
# karan,Failed
# rahul,Success
# priya,Failed
# Tasks:
# 1. Count successful and failed login attempts.
# 2. Identify users with more than 2 failed attempts.
# 3. Create a dictionary storing the number of failures per user.
# 4. Create a set of users who logged in successfully.
# 5. Display users whose accounts should be reviewed.
# Sample Output:
# Successful Login Attempts: 3
# Failed Login Attempts: 7
# Failure Count per User:
# anuj : 2
# rahul : 2
# priya : 2
# karan : 1
# Users with Successful Logins:
# {'anuj', 'neha', 'rahul'}
# Accounts Requiring Review:
# None
# Function to analyze login records
def analyze_login_logs():
    try:
        # Open file in read mode
        file = open("login_logs.txt", "r")

        # Read all lines from file
        records = file.readlines()

        # Close file
        file.close()

        # Initialize counters
        success_count = 0
        failed_count = 0

        # Dictionary to store failure count per user
        failure_dict = {}

        # Set to store successful users
        successful_users = set()

        # Process each record
        for record in records:

            # Remove extra spaces and newline character
            record = record.strip()

            # Split username and status
            username, status = record.split(",")

            # Check login status
            if status == "Success":

                # Increase successful login count
                success_count += 1

                # Add user to successful users set
                successful_users.add(username)

            elif status == "Failed":

                # Increase failed login count
                failed_count += 1

                # Store failure count in dictionary
                if username in failure_dict:

                    failure_dict[username] += 1

                else:

                    failure_dict[username] = 1

        # Create list for accounts requiring review
        review_accounts = []

        # Check users having more than 2 failed attempts
        for user, count in failure_dict.items():

            if count > 2:

                review_accounts.append(user)

        # Display results
        print("Successful Login Attempts:", success_count)

        print("Failed Login Attempts:", failed_count)

        print("\nFailure Count per User:")

        for user, count in failure_dict.items():

            print(user, ":", count)

        print("\nUsers with Successful Logins:")

        print(successful_users)

        print("\nAccounts Requiring Review:")

        if len(review_accounts) > 0:

            print(review_accounts)

        else:

            print("None")

    except FileNotFoundError:

        # Handle file not found error
        print("Error: login_logs.txt file not found.")

    except Exception as e:

        # Handle unexpected errors
        print("Error:", e)

    finally:

        # Always executes
        print("\nCyber Security Login Audit Completed.")


# Function Call
analyze_login_logs()