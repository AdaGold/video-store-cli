from customer import Customer 

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


# HOME PAGE 
# DISPLAY OPTIONS FOR USER TO PICK FROM

# PRINT GREETING
def welcome_greeting():
    print("Welcome to the Video Management System.")

def print_options():
    print("1. Customers")
    print("2. Videos")
    print("3. Rentals")
    print("4. Quit")

CUSTOMERS = 1
VIDEOS = 2
RENTALS = 3
QUIT = 4

def main():
    
    
    # while the main function is running. Quit will break out of while loop
    while(True): 
        welcome_greeting() 
        print_options() 
        # Add a check that user_input is integer and only 1-4 options
        user_input = input("Please choose from the following options: ")
        
        if user_input == CUSTOMERS:
            print("customer works")
            # customer = Customer()
            # customer.menu()
            #customer.menu # customer class and method called menu
        elif user_input == VIDEOS:
            print("Video function call here")
        elif user_input == RENTALS:
            print("rental function call here")
        else:
            user_input == QUIT
            break
        
        # elif type(user_input) != int or type(user_input) != float:
        #     print("The variable is not a number")

# __name__ is a built-in variable which evaluates to the name of the current module 
if __name__ == "__main__":
    main()