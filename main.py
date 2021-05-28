from models.video import Video
from models.customer import Customer
from models.rental import Rental
import requests
from utility import print_stars, to_integer, print_logo

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main(): # what is this main function supposed to do?
    print_stars()
    print_logo()
    print_stars()

if __name__ == "__main__":
    main()

def list_options():

    options = {
        "1": "Add video",
        "2": "Update video",
        "3": "Delete video",
        "4": "Get info about all videos",
        "5": "Get info about one video",
        "6": "Add customer",
        "7": "Edit customer",
        "8": "Delete customer",
        "9": "Get info about one customer",
        "10": "Get info about all customers",
        "11": "Check out video to customer",
        "12": "Check in video from customer",
        "13": "List all options",
        "14": "Exit"
    }

    for choice_num in options:
        print(f"{choice_num}, {options[choice_num]}")

    return options

def make_choice(options, video):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print_stars()
        print(f"What would you like to do?")
        choice = input("Input an option number: ")

        return choice

def run_cli(play=True):

    # initialize classes
    video = Video(url=URL)
    customer = Customer(url=URL)
    rental = Rental(url=URL)

    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, video)

        # add a video
        if choice=='1':
            title=input("Please enter a title: ")
            release_date=input("Please enter a release date: ")
            total_inventory=input("How many copies are there total? ")
            response = video.add_video(title=title, release_date=release_date,
            total_inventory=total_inventory)

            print(f"New video '{title}' created")

        # update a video
        elif choice=='2':
            video_id = input("Which video would you like to update?\n"
            "Please enter an ID: ")
            to_integer(video_id)

            title=input("Please enter a new title: ")
            release_date=input("Please enter a new release date: ")
            total_inventory=input("How many copies are there total? ")

            response = video.update_video(video_id=video_id, title=title,
            release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print(f"Updated video id {video_id}")

        # delete a video
        elif choice=='3':
            video_id = input("Which video would you like to delete?\n"
            "Please enter an ID: ")
            to_integer(video_id)

            video.delete_video(video_id)

            print(f"Video {video_id} has been deleted")

        # get info about all videos
        elif choice=='4':
            print_stars()
            for video in video.list_videos():
                print(video)

        # get info about one video
        elif choice=='5':
            video_id = input("Which video would you like to view?\n"
            "Please enter an ID: ")
            to_integer(video_id)

            selected_video = video.get_video(video_id=video_id)
            print(selected_video)

        # add a customer
        elif choice=='6':
            print(f"Let's add a customer!")
            name=input("Please enter a name: ")
            postal_code=input("Please enter a postal code: ")
            phone=input("Please enter a phone number: ")
            response = customer.add_customer(name=name, postal_code=postal_code,
            phone=phone)
            print(f"Customer {name} created")

        # update a customer
        elif choice=='7':
            customer_id = input("Which customer would you like to update?\n"
            "Please enter an ID: ")
            to_integer(customer_id)

            name=input("Please enter a new name: ")
            postal_code=input("Please enter a new postal code: ")
            phone=input("Please enter a new phone: ")

            response = customer.update_customer(customer_id=customer_id,
            name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print(f"Updated customer number {customer_id}")

        # delete a customer
        elif choice=='8':
            customer_id = input("Which customer would you like to delete?\n"
            "Please enter an ID: ")
            to_integer(customer_id)

            print_stars()
            response = customer.delete_customer(customer_id)
            print(response)
            #print(f"Customer number {customer_id} has been deleted")

        # get info about one customer
        elif choice=='9':
            customer_id = input("Which customer would you like to view?\n"
            "Please enter an ID: ")
            to_integer(customer_id)

            selected_customer = customer.get_customer(customer_id=customer_id)
            if selected_customer:
                print(selected_customer)

        # get info about all customers
        elif choice=='10':
            print_stars()
            for c in customer.list_customers():
                print(c)

        # check out video to customer
        elif choice=='11':
            customer_id=input("Please enter a customer id: ")
            video_id=input("Please enter a video id: ")
            to_integer(customer_id)
            to_integer(video_id)

            response = rental.check_out(customer_id=customer_id,
            video_id=video_id)
            print("Video successfully checked out")
            print(f"Video id {video_id} checked out to {customer_id}")

        # check in video from customer
        elif choice=='12':
            customer_id=input("Please enter a customer id: ")
            video_id=input("Please enter a video id: ")
            to_integer(customer_id)
            to_integer(video_id)

            response = rental.check_in(customer_id=customer_id,
            video_id=video_id)
            print("Video successfully checked in")
            print(f"Video {video_id} checked in from {customer_id}")

        # list all options
        elif choice=='13':
            list_options()

        # quit
        elif choice=='14':
            play=False
            print("\nThanks for using Retrowave Video's CLI!")

        print_stars()

run_cli()
