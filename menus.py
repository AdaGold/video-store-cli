from commands import *
from video_store import VideoStore
from main import video_store


# URL = "http://127.0.0.1:5000"
# BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

# video_store=VideoStore(url=URL)


def print_stars():
    print("\n*********************************\n")


#----MAIN MENU-----#   
def main_menu():
    main_menu_options = {

    "1.":"Manage Customer Records",
    "2.":"Manage Video Records",
    "3.":"Check-in Video",
    "4.":"Check-out Video",
    "5.": "All Done? Quit!"
    }
    print_stars()
    print("Welcome to the Main Menu!")
    print("Please pick which action you would like to perform")
    print_stars()

    for option in main_menu_options:
        print(f"{option} {main_menu_options[option]}")

    print_stars()

    return main_menu_options

def make_main_choice(main_menu_options):
    valid_choices = main_menu_options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do?")
        choice = input("Make your selection using the option numbers: ")
        return choice


#----CUSTOMER MENU----#
def customer_menu():
    customer_menu_options={
    "1.": "Get all Customers",
    "2.": "Look-up a Customer",
    "3.": "Add a Customer",
    "4.": "Update a Customer",
    "5.": "Delete a Customer",
    "6.": "Go back to Main Menu"}

    print_stars()
    print("Welcome to the Customer Menu!")
    print("Please pick which action you would like to perform")
    print_stars()
    

    for option in customer_menu_options:
        print(f"{option} {customer_menu_options[option]}")
    print_stars()

    return customer_menu_options

def make_customer_choice(customer_menu_options):
    valid_choices = customer_menu_options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 6 to go back to the main menu")
        choice = input("Make your selection using a valid option number: ")
    
    if choice =='1':
        video_store.list_customers()
    elif choice=='2':#getone
        id=input("Please input customer id: ")
        to_int(id)
        video_store.get_customer(id)
    elif choice=='3':#add
        print("Let's Create a Customer Account!")
        name = input("Please input customer name: ")
        postal_code=input("Please enter customer postal_code: ")
        phone = input("Please enter customer phone number: ")
        response = video_store.create_customer(name=name, postal_code=postal_code, phone = phone)
        print(response)
    elif choice=='4':#
        id= input("Please input customer id: ")
        to_int(id)
        title= input("Please input video title: ")
        release_date=input("Please enter video release date: ")
        total_inventory=input("Please enter total_inventory: ")
        response= video_store.update_video(id=id,title=title,
        release_date=release_date, total_inventory=total_inventory)
        print(response)
    elif choice=='5':#delete
        id=input("Please enter video id:")
        to_int(id)
        response = video_store.delete_customer(id=id)
        print(response)
    elif choice == '6':#main menu
        options= main_menu()
        choice = make_main_choice(options)
    return choice




#---VIDEO MENU---#
def video_menu():
    video_menu_options={
    "1.": "Get All Videos",
    "2.": "Look-up a Video",
    "3.": "Add a Video",
    "4.": "Update a Video",
    "5.": "Delete a Video",
    "6.": "Go back to Main Menu"}

    print_stars()
    print("Welcome to the Video Menu!")
    print("Please pick which action you would like to perform")
    print_stars()

    for option in video_menu_options:
        print(f"{option} {video_menu_options[option]}")
    print_stars()

    return video_menu_options

def make_video_choice(video_menu_options):

    valid_choices = video_menu_options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do?")
        choice = input("Make your selection using a valid option number: ")

        return choice

    if choice =='1':
        video_store.all_videos()
    elif choice=='2':#getone
        id=input("Please input video id: ")
        to_int(id)
        video_store.get_video(id)
    elif choice=='3':#add
        title= input("Please input video title: ")
        release_date=input("Please enter video release date: ")
        total_inventory=input("Please enter total_inventory: ")
        response=video_store.create_video(title=title, 
        release_date=release_date, total_inventory=total_inventory)
        print(response)
    elif choice=='4':#update
        id= input("Please input video id: ")
        to_int(id)
        title= input("Please input video title: ")
        release_date=input("Please enter video release date: ")
        total_inventory=input("Please enter total_inventory: ")
        response= video_store.update_video(id=id,title=title,
        release_date=release_date, total_inventory=total_inventory)
        print(response)
    elif choice=='5':#delete
        id=input("Please enter video id")
        to_int(id)
        response=video_store.delete_video(id=id)
        print(response)
    elif choice == '6':#main menu
        options= main_menu()
        choice = make_main_choice(options)
    return choice
    

