import requests
from customer import Customer
from rental import Rental
from video import Video

URL = "https://retro-video-store-api.herokuapp.com"
def print_stars():
    print("\n**************************\n")

def list_options():
    options = {
        "1": "Add a video",
        "2": "Select a video",
        "3": "Browse video catalog",
        "4": "Add a *new* customer",
        "5": "Get information on one customer",
        "6": "Get information on all customers",
        "7": "Check out a video",
        "8": "Check in a video",
        "9": "List all options",
        "0": "Quit"
    }

    print_stars()
    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    
    print_stars()

    return options
# 
def make_choice(options, customer, video, rental):
    valid_choices = options.keys()

    while choice not in valid_choices:
        print("What would you like to do? Select 9 to see all options again")
        choice = input("Make your selection using the option number: ")
    
    return choice

def main(play=True):
    # initialize instances
    video = Video(URL)
    customer = Customer(URL)
    rental = Rental(URL)
    options = list_options()
    
    while play:
        choice = make_choice(options, video, customer)

    # Option 1: Add a video
    if choice == 1:
        print("Preparing to add video...")
        title = input("What is the name of the video?")
        release_date = input("What is the video's release date?")
        total_inventory = input("What is the total inventory for this video?")
        response = video.add_video(title=title, release_date=release_date, total_inventory=total_inventory)

        print("New video:", response["video"])

if __name__ == "__main__":
    main()