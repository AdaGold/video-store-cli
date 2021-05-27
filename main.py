from video_store import Customer

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def main():
    print("WELCOME TO RETRO VIDEO STORE")
    pass

# if __name__ == "__main__":
#     main()
def print_stars():
    print("**********************************")

MAIN_OPTIONS = {
    "1": "Manage Customers",
    "2": "Manage Videos",
    "3": "Manage Rentals",
    "4": "Quit",
}

CUSTOMER_OPTIONS = {
    "1": "List all customers",
    "2": "Add new customer",
    "3": "View customer details",
    "4": "Edit customer",
    "5": "Delete customer",
    "6": "Main menu",
    "7": "Quit"
}

VIDEO_OPTIONS = {
    "1": "List all vidoes",
    "2": "Add new video",
    "3": "View video details",
    "4": "Edit video",
    "5": "Delete video",
    "6": "Main menu",
    "7": "Quit"
}

RENTAL_OPTIONS = {
        "1": "Check-out video",
        "2": "Check-in video",
        "3": "Main menu",
        "4": "Quit"
    }

def choose_from_menu(options, menu_name):
    print(f"{menu_name} Menu:")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do?  ")
        choice = input("Make your selection:   ")
        return choice

def main_menu_to_other(play = True):
    
    while play==True:

        choice = choose_from_menu(MAIN_OPTIONS, "Main")

        if choice=="1":
            customer_route()
        # elif choice=="2":
        #     choice = choose_from_menu(VIDEO_OPTIONS, "Video")
        # elif choice =="3":
        #     options = rental_menu()
        #     choice = choose_from_rental_menu(options)
        # elif choice =="4":
        #     play = False
        #     print("BYE!")
        
        # return choice

def select_customer():
    customer = Customer()
    select_by = input("select by name or id?:  ")
    if select_by == "name":
        name = input("enter name:  ")
        customer.get_customer(name=name)
        if customer.selected_customer:
            selected_customer = customer.selected_customer
            print(selected_customer)
            return customer
            
    elif select_by == "id":
        id = input("enter id:  ")
        if id.isnumeric():
            id = int(id)
            customer.get_customer(id=id)
            if customer.selected_customer:
                selected_customer = customer.selected_customer
                temp = customer
                print(selected_customer)
                return customer
    else:
        print("could not select, please enter name or id")
        select_customer()

def customer_route(play=True):
    
    while play == True:

        choice = choose_from_menu(CUSTOMER_OPTIONS, "Customer")

        if choice=="1":
            customer = Customer()
            print(customer.list_customers())
        elif choice=="2":
            customer = Customer()
            print_stars()
            print("create a new customer:")
            print_stars()
            name=input("customer name: ")
            phone=input("customer phone: ")
            postal_code=input("customer postal code:  ")
            response = customer.create_customer(name=name, phone=phone, postal_code=postal_code)
            print_stars()
            print("New Customer Created:", response["id"])
            print_stars()
        elif choice=="3":
            select_customer()
        elif choice=="4":
            selected_customer = select_customer()
            name=input("edit customer name: ")
            phone=input("edit customer phone: ")
            postal_code=input("edit customer postal code:  ")
            response = selected_customer.update_customer(name=name, phone=phone, postal_code=postal_code)
            print_stars()
            print("Edited customer:", response["id"])
            print_stars()
        elif choice=="5":
            selected_customer = select_customer()
            response = selected_customer.delete_customer()
            print("Customer deleted", response["id"])
        elif choice=="6":
            choose_from_menu(MAIN_OPTIONS, "Main")
        else:
            play = False

main_menu_to_other() 