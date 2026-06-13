# Problem Statement:
# Design a MovieTicket class containing:
# • Movie Name
# • Ticket Price
# • Number of Seats Available
# Implement methods to:
# • Book tickets.
# • Cancel tickets.
# • Display booking details.
# • Update seat availability.
# Do not allow booking if requested seats exceed availability.
# Sample Output:
# Booking Successful.
# Tickets Booked : 4
# Amount Payable : ₹800
# Seats Remaining: 46
# MovieTicket Class
#----------------------------------------------------------
class MovieTicket:

    # Constructor to initialize movie details
    #--------------------------------------------------------
    def __init__(self, movie_name, ticket_price, seats_available):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.seats_available = seats_available

    # Method to book tickets
    #--------------------------------------------------
    def book_tickets(self, tickets):
        if tickets <= self.seats_available:
            self.seats_available = self.seats_available - tickets
            amount = tickets * self.ticket_price

            print("\nBooking Successful.")
            print("Tickets Booked :", tickets)
            print("Amount Payable : ₹", amount)
            print("Seats Remaining:", self.seats_available)
        else:
            print("\nBooking Failed.")
            print("Requested seats exceed availability.")

    # Method to cancel tickets
    #----------------------------------------------------------
    def cancel_tickets(self, tickets):
        self.seats_available = self.seats_available + tickets
        print("\nTicket Cancellation Successful.")
        print("Seats Available:", self.seats_available)

    # Method to display movie details
    #--------------------------------------------------------------
    def display_details(self):
        print("\nMovie Details")
        print("-" * 30)
        print("Movie Name      :", self.movie_name)
        print("Ticket Price    : ₹", self.ticket_price)
        print("Seats Available :", self.seats_available)

#--------------------------------------------------------
# Main Program
#--------------------------------------------------------
# Accept movie details
movie_name = input("Enter Movie Name: ")
ticket_price = float(input("Enter Ticket Price: ₹"))
seats_available = int(input("Enter Available Seats: "))

# Create object
movie = MovieTicket(movie_name, ticket_price, seats_available)

# Display movie details
movie.display_details()

# Book tickets
tickets = int(input("\nEnter Number of Tickets to Book: "))
movie.book_tickets(tickets)

# Display updated details
movie.display_details()