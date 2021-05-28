import requests
from video import Video
from rental import Rental
from customer import Customer

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def list_options():
    options = {
        "1": "Add a video",
        "2": "Edit a video",
        "3": "Delete a video",
        "4": "Get info about one video",
        "5": "Get info about all videos",
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Get info about one customer",
        "10": "Get info about all customers",
        "11": "Check out a video to a customer",
        "12": "Check in a video from customer",
        "13": "List all options",
        "14": "Quit"
    }

    print("What would you like to do?")
    print("**************************")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print("You must select a video before updating it, deleting it, checking it out, or checking it in.")
    return options

##########


def make_choice(options, class):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['2', '3', '4', '7', '8', '9', '11', '12'] and class.selected_one == None:
        print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
        print("Let's select a task!")
        choice = "3"

    return choice


def main():
    print("WELCOME TO RETRO VIDEO STORE")


if __name__ == "__main__":
    main()
