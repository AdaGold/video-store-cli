import requests
from customer import Customer

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def list_options(): 
    options = {
        "1": "Add New Reel", 
        "2": "Edit Reel Information",
        "3": "Delete Reel", 
        "4": "Get All Reel Information", 
        "5": "Lookup Specific Reel", 
        "6": "Add Customer",
        "7": "Update Customer Information",
        "8": "Delete Customer",
        "9": "Get All Customers ",
        "10": "Get Specific Customer",
        "11": "Checkout Reel to Customer",
        "12": "Check-in Reel",
        "13": "Quit"
        }

    print("Welcome to the RAQIS REELS CLI")
    print("These are the actions you can perform")

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    return options

def make_choice(options):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("Not a valid selection, please select again")
        choice = input("Make your selection using the option number: ")

#     if choice in ['6','7','8']:
#         print("")
#         print("")
#         choice = "3"
    
#     return choice

def run_cli(play=True):

    customer = Customer(url="http://127.0.0.1:5000")

    options = list_options()

    while play==True:
        choice = make_choice(options)

    if choice=='8':
        #print_stars()
        for customer in customer.all_customers():
                print(customer)
    if choice =="10":
        customer_id = input("Please enter valid customer ID:  ")
        if customer_id.isnumeric():
            customer_id = int(customer_id)
            customer.get_customer(customer_id=customer_id)

    

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    #look up snowman project
    list_options()
    customer = Customer() 
    print(customer.all_customers())
    

if __name__ == "__main__":
    run_cli()