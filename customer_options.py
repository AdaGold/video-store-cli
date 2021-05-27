from menu_options import *

def get_customer_choice(rental):
    options = {
        "1": "List all customers", 
        "2": "Create a customer",
        "3": "Select a customer", 
        "4": "Update selected customer", 
        "5": "Delete selected customer", 
        "6": "Delete all customers",
        "7": "Back to main menu"
        }
    
    print("\nThese are the actions you can perform: \n")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    valid_choices = options.keys()
    customer_choice = None

    while customer_choice not in valid_choices:
        if customer_choice != None:
            print("\nInvalid option.")
            customer_choice = input("\nMake your selection using valid option number: ")
        else:
            customer_choice = input("\nMake your selection using the option number: ")
            
    if customer_choice in ['4','5'] and rental.selected_customer == None:
        print("You must select a customer before updating it or deleting it.")
        print("Let's select a customer!")
        customer_choice = "3"
    
    return customer_choice
    
def respond_customer_choice(choice, rental, main_menu_choice):
    rental.print_selected_customer()
    # main_menu_choice = 'a'
    if choice=='1':
        print_stars()
        print("All customers:")
        for customer in rental.list_customers():
            print(customer)

    elif choice=='2':
        print("Great! Let's create a new customer.")
        name=input("What is the name of your customer? ") 
        postal_code=input("What is the postal_code of your customer? ")
        phone=input("What is the phone number of your customer? ") 
        response = rental.create_customer(name=name, postal_code=postal_code, phone=phone)

        print_stars()
        print("New customer:", response)
    elif choice=='3':
        select_by = input("Would you like to select by? Enter name or id: ")
        if select_by=="name":
            name = input("Which customer name would you like to select? ")
            rental.get_customer(name=name)
        elif select_by=="id":
            id = input("Which customer id would you like to select? ")
            if id.isnumeric():
                id = int(id)
                rental.get_customer(id=id)
        else:
            print("Could not select. Please enter id or name.") 

        if rental.selected_customer:
            print_stars()
            print("Selected customer: ", rental.selected_customer)

    elif choice=='4':
        print(f"Great! Let's update the customer: {rental.selected_customer}")
        name=input("What is the new name of your customer? ")
        postal_code=input("What is the new postal_code of your customer? ")
        phone=input("What is the new phone of your customer? ")
        response = rental.update_customer(name=name, postal_code=postal_code, phone=phone)

        print_stars()
        print("Updated customer:", response)
    elif choice=='5':
        rental.delete_customer()
        print_stars()
        print("Customer has been deleted.")
        print_stars()
        print("Current customers:")
        for customer in rental.list_customers():
            print(customer)

    elif choice=='6':
        delete_all = input("Are you sure you want to delete all customers? Y/N:  ").lower()
        if delete_all == "y":
            for customer in rental.list_customers():
                rental.get_customer(id=customer['id'])
                rental.delete_customer()

            print_stars()
            print("Deleted all customers.")

    else:
        main_menu_choice = get_main_menu_choice()

    print_stars()

    return main_menu_choice