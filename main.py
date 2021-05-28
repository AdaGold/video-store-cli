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
        "2": "Edit a video",
        "3": "Delete a video",
        "4": "Get information on all videos",
        "5": "Get information on one video",
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Get information on one customer",
        "10": "Get information on all customers",
        "11": "Check out a video to a customer",
        "12": "Check in a video from a customer",
        "13": "List all options",
        "14": "Quit"
    }
    print_stars()
    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    
    print_stars()

    return options

def make_choice(options, customer, video, rental):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 9 to see all options again")
        choice = input("Make your selection using the option number: ")
    
    # if choice in ['4','5','6','7'] and 

def main(play=True):
    video = Video(URL)
    customer = Customer(URL)
    rental = Rental(URL)
    options = list_options()

    # while play == True:
    #     choice

if __name__ == "__main__":
    main()