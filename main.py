from video_store import VideoStore
from termcolor import colored
from pyfiglet import Figlet

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

video_store = VideoStore(url=URL)

def print_stars():
    print("\n**************************\n")

def home_logo():
    logo = Figlet(font="rounded")
    print(colored(logo.renderText("Retro Video"), "green"))


def menu_options():
    menu_options = {
        "1": "Video Check-Out",
        "2": "Video Check-In",
        "3": "Video Inventory",
        "4": "Customer Services"
    }

    print_stars()
    print("Welcome to Retro Video!\n")
    print("Choose from the following options: ")
    print_stars()

    for option in menu_options:
        print(f"Option {option}. {menu_options[option]}")
    
    return menu_options

def video_options():
    video_options = {
        "1": "View inventory",
        "2": "Search inventory",
        "3": "Add a new video",
        "4": "Update video details",
        "5": "Delete a video",
        "9": "Return to main menu"
    }

    print_stars()
    print("Video Menu")
    print_stars()

    for option in video_options:
        print(f"Option {option}. {video_options[option]}")
    
    return video_options

def customer_options():
    customer_options = {
        "1": "Look up customer",
        "2": "Add new customer",
        "3": "Update customer information",
        "4": "Delete customer",
        "5": "View all customers",
        "9": "Return to main menu"
    }
    print_stars()
    print("Customer Menu")
    print_stars()

    for option in customer_options:
        print(f"Option {option}. {customer_options[option]}")
    
    return customer_options

def option_choice(options):
    return_options = options()
    valid_choices = return_options.keys()
    choice = input("Enter an option number (or q to exit): ")
    if choice == "q" or choice == "Q":
            exit()

    while choice not in valid_choices:
        print("Invalid option.")
        print("To see the options again, enter 9.")
        choice = input("Enter a valid option number: ")

        if int(choice) == 9:
            menu_options()

    
    return choice

def video_tasks(choice):
    video_choice = int(choice)
    if video_choice == 1:
        # get all videos
        print_stars()
        print("Video Inventory\n")
        response = video_store.videos_index()
        print(response)
    # elif video_choice == 2:
    #     # search video by id or title
    elif video_choice == 3:
        # add a new video
        print_stars()
        print("Enter new video details: \n")
        title = input("Title: ")
        release_date = input("Release Date: ")
        total_inventory = input("Total Inventory: ")

        response = video_store.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
        
        print(response)

    # elif video_choice == 4:
    #     # update video details
    # elif video_choice == 5:
    #     # delete a video

# def customer_tasks(choice):
#     customer_choice = int(choice)
#     if customer_choice == 1:
#         # get customer details by id, name, or phone #
#     elif customer_choice == 2:
#         # add new customer
#     elif customer_choice == 3:
#         # update customer information
#     elif customer_choice == 4:
#         # delete customer
#     elif customer_choice == 5:
#         # view all customers

def check_out():

    print_stars()
    print("Video Check-out")
    print_stars()
    customer_id = input("Enter customer ID: ")
    video_id = input("Enter video ID: ")

    response = video_store.check_out(customer_id=customer_id, video_id=video_id)

    print(response)

def check_in():
    print_stars()
    print("Video Return")
    print_stars()
    customer_id = input("Enter customer ID: ")
    video_id = input("Enter video ID: ")

def run_cli(play=True):

    while play == True:
        choice = option_choice(menu_options)

        if int(choice) == 1:
            check_out()

        elif int(choice) == 2:
            check_in()

        elif int(choice) == 3:
            video_choice = option_choice(video_options)
            video_tasks(video_choice)

        elif int(choice) == 4:
            customer_choice = option_choice(customer_options)
            customer_tasks(video_choice)

def main():
    home_logo()
    run_cli()

    
if __name__ == "__main__":
    main()

