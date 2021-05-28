from os import name
import requests
from requests.api import options
from video_store import Employee

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def list_of_options():
    options = {
        "1": "To manage customers",
        "2": "To manage videos",
        "3": "To manage rental",
        "4": "To quit"
    }

    print("Please choose from the following menu options")
    for choice_num in options:
        print(f"{options[choice_num]}, type {choice_num}")
    return options

def make_a_choice(options):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        choice = input("::")
    return choice

def manage_customers():
    options = {
        "1": "To list all customers",
        "2": "To see information for one customer",
        "3": "To add a new customer",
        "4": "To edit a customer",
        "5": "To delete a customer",
        "6": "To return to the main menu",
    }

    print("Please choose from the following Customer menu options")
    for choice_num in options:
        print(f"{options[choice_num]}, type {choice_num}")
    return options

def make_a_choice_in_customer_menu_options(options, store_employee):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        choice = input("::")
    if choice in ['4','5'] and store_employee.selected_customer == None:
        print("You must select a customer before updating it or deleting it.")
        print("Let's select a customer!")
        choice = "2"
    return choice

def manage_videos():
    options = {
        "1": "To list all videos",
        "2": "To see information for one video",
        "3": "To add a new video",
        "4": "To edit a video",
        "5": "To delete a video",
        "6": "To return to the main menu",
    }

    print("Please choose from the following Video menu options")
    for choice_num in options:
        print(f"{options[choice_num]}, type {choice_num}")
    return options

def make_a_choice_in_video_menu_options(options, store_employee):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        choice = input("::")
    if choice in ['4','5'] and store_employee.selected_video == None:
        print("You must select a video before updating it or deleting it.")
        print("Let's select a video!")
        choice = "2"
    return choice

def manage_rentals():
    options = {
        "1": "To check out a video",
        "2": "To check in",
        "3": "To return to the main menu",
    }

    print("Please choose from the following Rental menu options")
    for choice_num in options:
        print(f"{options[choice_num]}, type {choice_num}")
    return options


def main():
    store_employee = Employee(url="https://retro-video-store-api.herokuapp.com")
    
    quit = False
    while not quit:
    # print art 
        print("WELCOME TO RETRO VIDEO STORE")
        options = list_of_options()
        choice = make_a_choice(options)
        if choice == "1":
            exit = False
            while not exit:
                customer_options = manage_customers()
                option_chosen= make_a_choice_in_customer_menu_options(customer_options, store_employee)
                if option_chosen == "1":
                    for customer in store_employee.get_all_customers():
                        print(customer)
                elif option_chosen == "2":
                    select_by = input("Would you like to select by name or id?  ")
                    if select_by == "name":
                        name = input("Which customer would you like to select?")
                        store_employee.get_a_customer(name=name)
                    elif select_by == "id":
                        id = input("Which customer id would you want to select?")
                        if id.isnumeric():
                            id = int(id)
                            store_employee.get_a_customer(id=id)
                    else:
                        print("Could not select. Please enter id or name.")
                    if store_employee.selected_customer:
                        print("selected customer: ", store_employee.selected_customer)   
                    if not store_employee.selected_customer:
                        print("Could not find a customer by that name or id")
                elif option_chosen == "3":
                    name =input("What is the name of your customer?")
                    postal_code =input("What is the customer's postal code?")
                    phone =input("What is the customer's phone number?")
                    response = store_employee.add_customer(name=name, postal_code=postal_code, phone=phone)
                    print("New customer", response)
                elif option_chosen == "4":
                    print(f"Great! Let's update the customer: {store_employee.selected_customer}")
                    name =input("What is the new name of your customer?")
                    print(name)
                    postal_code =input("What is the new customer's postal code?")
                    phone =input("What is the new customer's phone number?")
                    response = store_employee.update_customer(name=name, postal_code=postal_code, phone=phone)
                    print(response)
                elif option_chosen == "5":
                    store_employee.delete_customer()
                    print("The customer has been deleted")
                elif option_chosen == "6":
                    exit = True
        elif choice == "2":
            exit = False
            while not exit:
                video_options = manage_videos()
                option_chosen= make_a_choice_in_video_menu_options(video_options, store_employee)
                if option_chosen == "1":
                    for video in store_employee.get_all_videos():
                        print(video)
                elif option_chosen == "2":
                    select_by = input("Would you like to select by? Enter title or id: ")
                    if select_by == "title":
                        title = input("Which video would you like to select?")
                        store_employee.get_a_video(title=title)
                    elif select_by == "id":
                        id = input("Which video id would you want to select?")
                        if id.isnumeric():
                            id = int(id)
                            store_employee.get_a_video(id=id)
                    else:
                        print("Could not select. Please enter id or title")

                    if store_employee.selected_video:
                        print("selected video: ", store_employee.selected_video)
                    if not store_employee.selected_video:
                        print("Could not find a video by that title or id")    
                elif option_chosen == "3":
                    title =input("What is the title of your video?")
                    release_date =input("What is the video's release date?")
                    total_inventory =input("What is the video's total_inventory?")
                    response = store_employee.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
                    print("New video", response)
                elif option_chosen == "4":
                    print(f"Great! Let's update the video: {store_employee.selected_video}")
                    title =input("What is the new title of your video?")
                    release_date =input("What is the new video's release date?")
                    total_inventory =input("What is the new video's total_inventory?")
                    response = store_employee.update_video(title=title, release_date=release_date, total_inventory=total_inventory)
                    print(response)
                elif option_chosen == "5":
                    store_employee.delete_video()
                    print("The video has been deleted")
                elif option_chosen == "6":         
                    exit = True           
        elif choice == "3":
            exit = False
            while not exit:
                rental_options = manage_rentals()
                option_chosen= make_a_choice(rental_options)
                if option_chosen == "1":
                    customer_id = input("What is the customer id?")
                    video_id = input("What is the video id?")
                    response = store_employee.check_out(customer_id=customer_id, video_id=video_id)
                    print(response)
                elif option_chosen == "2":
                    customer_id = input("What is the customer id?")
                    video_id = input("What is the video id?")
                    response = store_employee.check_in(customer_id=customer_id, video_id=video_id)
                    print(response)
                elif option_chosen == "3":
                    exit = True
        elif choice == "4":
            print("Thanks for coming to our store!")   
            quit = True

if __name__ == "__main__":
    main()