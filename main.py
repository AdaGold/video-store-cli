import requests
from customer import Customer

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    run_cli()

def print_stars():
    print("\n**************************\n")

def list_options():
    options = {
        "1": "To manage customers, type 1",
        "2": "To manage videos, type 2",
        "3": "To manage rentals, type 3",
        "4": "To quit, type 4"
    }

    print("Please choose from the following menu options:")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()
    return options

def make_choices(options):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print_stars()
        print("What would you like to do? ")
        choice = input("Make your selections using the option number: ")

    # if choice in ['1', '2', '3', '4']:
    #     # print("You must select an option")
    #     choice = input("You must select an option:")

    return choice

def customer_options():
    options = {
        "1": "To list all Customers, type 1",
        "2": "To see information for one Customer, type 2",
        "3": "To add a new Customer, type 3",
        "4": "To edit a Customer, type 4",
        "5": "To delete a Customer, type 5",
        "6": "To return to the main menu, type 6"
    }
    print("Please choose from the following Customer menu options:")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()
    return options

def make_customer_choices(customer_choices, customer):
    # List all Customers
    if customer_choices == "1":
        print_stars()
        for cust in customer.list_customers():
            print(cust)

    # See information for one Customer
    elif customer_choices == "2":
        select_by = input("Would you like to select by name or id?: ")
        if select_by == "name":
            name = input("What is the name of your customer? ")
            customer.get_customer(name=name)
        elif select_by == "id":
            id = input("What is the id of your customer? ")
            if id.isnumeric():
                id = int(id)
                customer.get_customer(id=id)
        else:
            print("Could not select. Please enter name or id")
        
        if customer.selected_customer:
            print_stars()
            print("Selected Customer: ", customer.selected_customer)

    # Add a new Customer      
    elif customer_choices == "3":
        print("Let's create a new customer")
        name = input("What is the name of your customer? ")
        postal_code = input("What is postal code of your customer? ")
        phone = input("What is the phone number of your customer? ")
        response = customer.create_customer(name=name, \
                            postal_code=postal_code, phone=phone)
        # print("***** cli We're in choice !")
        print_stars()
        print(f"New customer name: {name} \nPostal Code: {postal_code}\
                \nPhone: {phone}")

    # Edit a Customer
    elif customer_choices == "4":
        # select_by = input("Would you like to select by name or id?: ")

        name = input("What is the name of your customer? ")
        customer.get_customer(name=name)
        # else:
        #     print("Could not select. Please enter name or id")
        
        if customer.selected_customer:
            print_stars()

            print(f"Let's update the customer {customer.selected_customer}")
            new_name = input("What is the new name of your customer? ")
            postal_code = input("What is the new postal code of your customer? ")
            phone = input("What is the new phone number of your customer? ")
            response = customer.update_customer(name=new_name, \
                            postal_code=postal_code, phone=phone)
            print_stars()
            print("Customer Updated: ", customer.selected_customer)
            print(f"Updated customer name: {name} \nPostal Code: {postal_code} \
                \nPhone: {phone}")
        else:
            print_stars()
            print("There is no customer by that name. Try again. ")

    # Delete a Customer
    elif customer_choices == "5":
        select_by = input("Would you like to select by name or id?: ")
        if select_by == "name":
            name = input("What is the name of your customer? ")
            customer.delete_customer(name=name)
        elif select_by == "id":
            id = input("What is the id of your customer? ")
            if id.isnumeric():
                id = int(id)
                customer.delete_customer(id=id)
        else:
            print("Could not select. Please enter name or id")

        print_stars()
        print("Task has been deleted.")

    # Return to Main menu
    elif customer_choices == "6":
        list_options()


def run_cli(play=True):

    customer = Customer(url="https://jen-retro-video-store.herokuapp.com")
    # customer = Customer()

    options = list_options()

    while play == True:
        choice = make_choices(options)

        if choice == "1":
            print_stars()
            cust_options = customer_options()
            customer_choices = make_choices(cust_options)

            make_customer_choices(customer_choices, customer)






if __name__ == "__main__":
    main()