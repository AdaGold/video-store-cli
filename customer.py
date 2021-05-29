# Helper function
def print_stars():
    print("\n******************************************************************************\n")

# Select main menu option
def get_main_menu_choice():
    print_stars()
    print("Welcome to the Video Store CLI")
    print("\n*********** Main Menu ************\n")
    options = {
        "A": "Manage customer records", 
        "B": "Manage video records",
        "C": "Manage rental records", 
        "D": "Quit"
        }
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    print("\n**********************************\n")
    main_menu_choice = input("Make your selection using the option letter: ").lower()
    print_stars()

    return main_menu_choice

# Helper function for customer option 3: Select a customer
def select_a_customer(cvr):
    select_by = input("Would you like to select by name or id? ")
    while select_by != "name" and select_by != "id" :
        select_by = input("Could not select. Please select an option by entering name or id: ")

    if select_by=="name":
        name = input("Which customer name would you like to select? ")
        cvr.get_customer(name=name)
        if not cvr.selected_customer:
            return "Invalid name, could not select."
    elif select_by=="id":
        id = input("Which customer id would you like to select? ")
        if id.isnumeric():
            id = int(id)
            cvr.get_customer(id=id)
        if not cvr.selected_customer:
            return "Invalid id, could not select." 
    
    return cvr.selected_customer

# Select customer option
def get_customer_choice():
    options = {
        "1": "List all customers", 
        "2": "Create a customer",
        "3": "Select a customer", 
        "4": "Update a customer", 
        "5": "Delete a customer", 
        "6": "Delete all customers",
        "7": "Back to main menu"
        }
    
    print("These are the actions you can perform: \n")
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
    
    return customer_choice

# Response to selected customer option
def respond_customer_choice(choice, cvr, main_menu_choice):
    if choice=='1':
        print_stars()
        print("All customers:")
        for customer in cvr.list_customers():
            print(customer)
        print_stars()

    elif choice=='2':
        print("Great! Let's create a new customer.")
        name=input("What is the name of your customer? ") 
        postal_code=input("What is the 5 digits postal code of your customer? ")
        phone=input("What is the phone number of your customer? Enter XXX-XXX-XXX: ") 
        response = cvr.create_customer(name=name, postal_code=postal_code, phone=phone)

        print_stars()
        print("New customer:", response)
        print_stars()

    elif choice=='3':
        response = select_a_customer(cvr)
        if isinstance(response, dict):
            print_stars()
            print("Selected customer: ", cvr.selected_customer)
        else:
            print(response)
        print_stars()

    elif choice=='4':
        selected_customer = select_a_customer(cvr)
        if isinstance(selected_customer, dict):
            print(f"Great! Let's update the customer: {cvr.selected_customer}")
            name=input("What is the new name of your customer? ")
            postal_code=input("What is the new 5 digits postal code of your customer? ")
            phone=input("What is the new phone of your customer? Enter XXX-XXX-XXX: ")
            response = cvr.update_customer(name=name, postal_code=postal_code, phone=phone)
            
            print_stars()
            print("Updated customer:", response)
        else:
            print(selected_customer)
        print_stars()

    elif choice=='5':
        selected_customer = select_a_customer(cvr)
        if isinstance(selected_customer, dict):
            delete_single = input("Are you sure you want to delete this customer? Y/N:  ").lower()
            if delete_single == "y":
                cvr.delete_customer()
                
                print_stars()
                print("Customer has been deleted.")
                
                print_stars()
                print("Current customers:")
                for customer in cvr.list_customers():
                    print(customer)
        else:
            print(selected_customer)
        print_stars()

    elif choice=='6':
        delete_all = input("Are you sure you want to delete all customers? Y/N:  ").lower()
        if delete_all == "y":
            for customer in cvr.list_customers():
                cvr.get_customer(id=customer['id'])
                cvr.delete_customer()

            print_stars()
            print("Deleted all customers.")
        print_stars()

    else:
        main_menu_choice = get_main_menu_choice()

    return main_menu_choice