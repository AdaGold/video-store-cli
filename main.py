import requests
from requests.api import get
from customer import Customer
from video import Video
from rental import Rental 


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def print_stars():
    print("\n**************************\n")


def list_options():

    options = {
        "1": "Add a video", 
        "2": "Edit a video",
        "3": "Delete a video",
        "4": "Get information about all videos", 
        "5": "Get information about one video",
        "6": "Add a customer", 
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Get information about all customers",
        "10": "Get information about one customer",
        "11": "Check out a video to a customer",
        "12": "Check in a video from a customer"
        }

    print_stars()

    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")

    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options):
    
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do?")
        choice = input("Please enter a number from the list of options: ")
        
        while choice not in valid_choices:
            choice = input("Invalid input. Please choose a number from the list of options. ")
    
    return choice

# def restart():

#     print_stars()
#     if_done = input("Would you like to complete any other tasks? Please input yes or no: ")
#     print_stars()

#     while if_done != "yes" and if_done != "no":
#         print_stars()
#         if_done = input("Invalid input. Please enter yes or no: ")


#     if if_done == "yes":
#         print_stars()
#         run_cli()

#     else:
#         play=False  


def run_cli(play=True):

    #initialize 
    customer = Customer(BACKUP_URL)
    video = Video(BACKUP_URL)
    rental = Rental(BACKUP_URL)

    # print options 
    # options = list_options()

    while play==True:

        # print options 
        options = list_options()

        choice = make_choice(options)

        # add a video
        if choice == "1":
            print("Great! Let's create a new video.")
            title = input("Please enter the video's title: ")
            release_date = input("Please enter the video's release date: ")
            total_inventory = input("Please enter the video's total inventory: ")

            response = video.create_video(title, release_date, total_inventory)
            print_stars()
            print("New video created successfully.")
            print_stars()

            # restart()

        # edit a video
        elif choice == "2":
            video_id = input("Please enter video ID of video needing to be updated: ")
            get_video = video.get_specific_video(video_id)
            # get_videos = video.all_videos()

            # while video_id not in get_videos:
            #     print_stars()
            #     print("Invalid input. Please see list of videos:")
            #     print(get_videos)
            #     print_stars()
            #     video_id = input("Please enter a valid title or ID number: ")
            #     print_stars()

            # else:
            print(get_video)
            print("Let's update this video.")
            title = input("Enter the video's updated name: ")
            release_date = input("Enter the video's updated release date: ")
            total_inventory = input("Enter the video's updated total inventory: ")

            response = video.update_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print("Video updated successfully")
            print_stars()

            # restart()

        # delete a video
        elif choice == "3":
            video_id = input("Please enter the ID of the video you would like to delete: ")
            get_video = video.get_specific_video(video_id)
            response = video.delete_video(video_id)

            print(get_video)

            print_stars()
            print(f"Video {get_video['title']} successfully deleted.")
            print_stars()

            # restart()

        # get information about all videos 
        elif choice == "4":
            print_stars()
            for video in video.all_videos():
                print(video)

            # restart()

        # get information about one video 
        elif choice == "5":
            video_id = input("Enter the ID of the video information you would like to retrieve: ")
            get_video = video.get_specific_video(video_id)

            print(get_video)
            print_stars()

            # restart()

        # add a customer
        if choice == "6":
            print("Great! Let's create a new customer.")
            name = input("Please enter customer's name: ")
            postal_code = input("Please enter customer's postal code: ")
            phone_number = input("Please enter customer's phone number: ")

            response = customer.create_customer(name, postal_code, phone_number)
            print_stars()
            print("New customer created successfully.")
            print_stars()

            # restart()

        # edit a customer
        elif choice == "7":
            customer_id = input("Please enter the customer ID needing to be updated: ")
            get_customer = customer.get_specific_customer(customer_id)
            # get_customers = customer.all_customers()

            # if not customer_id:
            #     print(get_customer)
            #     restart()

            # else:

            print("Let's update this customer.")
            name = input("Enter the customer's updated name: ")
            postal_code = input("Enter the customer's updated postal code: ")
            phone_number = input("Enter the customer's updated phone number: ")

            response = customer.update_customer(customer_id=customer_id, customer_name=name, postal_code=postal_code, phone_number=phone_number)
            print_stars()
            print("Customer updated successfully")
            print_stars()

            # restart()

        # delete a customer
        elif choice == "8":
            customer_id = input("Please enter ID of the customer you would like to delete: ")
            get_customer = customer.get_specific_customer(customer_id)
            response = customer.delete_customer(customer_id)

            print(get_customer)

            print_stars()
            print(f"Customer {get_customer['name']} successfully deleted.")
            print_stars()

            # restart()

        # get information about all customers 
        elif choice == "9":

            print_stars()

            for customer in customer.all_customers():
                print(customer)
            
            # restart()

        # get information about one customer
        if choice == "10":
            customer_id = input("Enter the ID of the customer information you would like to retrieve: ")
            get_customer = customer.get_specific_customer(customer_id)
            print_stars()

            print(get_customer)
            print_stars

            # restart()

        # check out a video to a customer
        elif choice == "11":
            video_id = input("Enter video ID: ")
            customer_id = input("Enter customer_id: ")

            response = rental.check_out(video_id, customer_id)

            video = video.get_specific_video(video_id)
            customer = customer.get_specific_customer(customer_id)

            print(f"Video {video_id} was checked out to {customer['name']}.")

            # restart()

        # check in a video from a customer
        elif choice == "12":
            video_id = input("Enter video ID: ")
            customer_id = input("Enter customer ID: ")

            response = rental.check_in(video_id, customer_id)
            print(f"Video {video_id} was checked in from {customer['name']}.")

            # restart()

run_cli()