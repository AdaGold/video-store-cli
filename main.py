import requests
from video import Video
from rental import Rental
from customer import Customer

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def stars():
    print("**************************")

##########


def list_options():
    options = {
        "1": "Add a video",
        "2": "Edit a video",
        "3": "Delete a video",
        "4": "Select one video",
        "5": "Get info about all videos",
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Select one customer",
        "10": "Get info about all customers",
        "11": "Check out a video to a customer",
        "12": "Check in a video from customer",
        "13": "List all options",
        "14": "Quit"
    }

    print("What would you like to do?")
    stars()
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    # print("You must select a video before updating it, deleting it, checking it out, or checking it in.")
    return options


##########

def make_choice(options, video, customer):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")

    # if choice in ['2', '3', '7', '8', '11', '12'] and class.selected_one == None:
    #     print("You must select an item before updating it, deleting it, checking it out, or checking it in.")
    #     print("Let's select an item!")
    #     choice = "4"

    return choice


##########

def main():
    print("WELCOME TO RETRO VIDEO STORE")

    # initialize task_list
    video = Video(URL)
    customer = Customer(URL)
    rental = Rental(URL)

    # print choices
    options = list_options()

    play = True
    while play == True:

        # get input and validate
        choice = make_choice(options, video, customer)

        video.print_selected()
        customer.print_selected()

        stars()

        if choice == '5':
            print("Videos:")
            stars()
            for video in video.list_videos():
                print(video)
        elif choice == '10':
            print("Customers:")
            stars()
            for customer in customer.list_customers():
                print(customer)
        elif choice == '1':
            print("Great! Let's create a new video.")
            title = input("What is the title of your task? ")
            description = input("What is the description of your task? ")
            response = task_list.create_task(
                title=title, description=description)
            print("New task:", response["task"])


if __name__ == "__main__":
    main()
