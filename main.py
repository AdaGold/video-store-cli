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
        # print("Not a valid selection, please select again")
        choice = input("Make your selection using the option number: ")

    if choice in valid_choices:
        print("")
        print("")
        return choice

def run_cli(play=True):

    customer = Customer(url="http://127.0.0.1:5000")

    options = list_options()

    while play==True:
        choice = make_choice(options)

        if choice == "1":
            title = input("Please enter titlen: ")
            release_date = input("Please enter release_date: ")
            inventory = input("Please enter total inventory: ")
            available_inventory = input("Please enter available inventory: ")
        elif choice == "2":
            update_video_params = input("Please enter title, release date, and total inventory for Reel update:  ")
        
        elif choice == "3":
            video_to_delete = input("Please enter Reel id for deletion: ")

        elif choice == "4":
            pass #not sure what to do here

        elif choice == "5":
            video_id = input("Please enter Reel id.")
        
        elif choice == "6":
            customer_name = input("Please enter customer name:  ")
            postal_code = input("Please enter customer postal code:  ")
            phone_number = input("Please enter customer phone number:  ")
            respone = customer.create_customer(customer_name=customer_name, postal_code=postal_code, phone_number=phone_number)
            print(f"Customer profile '{customer_name}' has been created.")
            
        elif choice == "7":
            customer_name = input("Please enter customer name:  ")
            postal_code = input("Please enter customer postal code:  ")
            phone_number = input("Please enter customer phone number:  ")
            response = customer.update_customer_info(customer_name=customer_name, postal_code=postal_code, phone_number=phone_number)
            print(f"Customer profile '{customer_name}' has been updated. ")

        elif choice == "8":
            customer_id = input("Please enter to Customer id for deletion: ")
            response = customer.delete_customer(customer_id=customer_id)
            print(f"Customer id '{customer_id}' has been deleted")

        elif choice== "9":
        #print_stars()
            for customer in customer.all_customers():
                print(customer)
        elif choice =="10":
            customer_id = input("Please enter valid customer ID:  ")
                # if customer_id.isnumeric():
                #     customer_id = int(customer_id)
                #     customer.get_customer(customer_id=customer_id)
        elif choice == "11":
            checkout_params = input("Please enter Customer id and Video id for checkout:  ")
        
        elif choice == "12":
            checkin_params = input("Please enter customer id and Reel id for check-in: ")
    

# def main():
#     print("WELCOME TO RETRO VIDEO STORE")
#     #look up snowman project
#     list_options()
#     customer = Customer() 
#     print(customer.all_customers())
    

if __name__ == "__main__":
    run_cli()
    #main()