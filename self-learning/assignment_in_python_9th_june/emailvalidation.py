'''An organization has collected 20 email addresses from users. 
Create a program to analyze these email addresses. 
Requirements 
For each email: 
1. Extract username.  
2. Extract domain.  
3. Extract extension.  
4. Count digits in username.  
5. Count special characters.  
6. Check if email is valid:  
o Exactly one '@'  
o Contains '.'  
o No spaces  
7. Display invalid emails.  
8. Count emails belonging to each domain.  
Sample Input 
rahul123@gmail.com 
priya@outlook.com 
anuj@company.in 
Challenge 
Generate a domain report: 
gmail.com     -> 8 users 
outlook.com   -> 5 users 
yahoo.com     -> 3 users 
company.in    -> 4 users '''

# ==========================================
# EMAIL VALIDATION AND DOMAIN ANALYTICS
# ==========================================

# Dictionary to store domain counts
domain_count = {}

# List to store invalid emails
invalid_emails = []

# ==========================================
# INPUT 20 EMAILS
# ==========================================

for i in range(1, 21):

    print(f"\nEnter Email {i}")

    email = input("Email: ")

    print("\n========== EMAIL REPORT ==========")

    # --------------------------------------
    # Email Validation
    # --------------------------------------

    at_count = email.count("@")
    dot_count = email.count(".")
    space_count = email.count(" ")

    if at_count == 1 and dot_count >= 1 and space_count == 0:

        print("Valid Email")

        # ----------------------------------
        # Extract Username
        # ----------------------------------

        username = email[:email.index("@")]

        # ----------------------------------
        # Extract Domain
        # ----------------------------------

        domain = email[email.index("@") + 1:]

        # ----------------------------------
        # Extract Extension
        # ----------------------------------

        extension = domain[domain.rindex(".") + 1:]

        # ----------------------------------
        # Count Digits in Username
        # ----------------------------------

        digit_count = 0

        for ch in username:

            if ch.isdigit():

                digit_count += 1

        # ----------------------------------
        # Count Special Characters
        # ----------------------------------

        special_count = 0

        for ch in username:

            if not ch.isalnum():

                special_count += 1

        # ----------------------------------
        # Count Domain Users
        # ----------------------------------

        if domain in domain_count:

            domain_count[domain] += 1

        else:

            domain_count[domain] = 1

        # ----------------------------------
        # Display Details
        # ----------------------------------

        print("Username :", username)
        print("Domain :", domain)
        print("Extension :", extension)
        print("Digits In Username :", digit_count)
        print("Special Characters :", special_count)

    else:

        print("Invalid Email")

        invalid_emails.append(email)

# ==========================================
# DISPLAY INVALID EMAILS
# ==========================================

print("\n================================")
print("INVALID EMAILS")
print("================================")

for email in invalid_emails:

    print(email)

# ==========================================
# DOMAIN ANALYTICS REPORT
# ==========================================

print("\n================================")
print("DOMAIN ANALYTICS REPORT")
print("================================")

for domain, count in domain_count.items():

    print(domain, "->", count, "users")