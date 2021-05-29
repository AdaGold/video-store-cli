import requests
import datetime
from customers import Customers
from videos import Videos
from rentals import Rentals



# URL = "http://127.0.0.1:5000"
URL = "https://retro-video-store-api.herokuapp.com"


def print_stars():
    print("\n**************************\n")
    


def list_options():
    options = {
        "1": "Add a video", 
        "2": "Edit a video",
        "3": "Delete a video",
        "4": "List all videos",
        "5": "Get a video",
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "delete a customer",
        "9": "Get a customer",
        "10": "Get all customers",
        "11": "Check out a video",
        "12": "Check in a video",
        "00" : "Quit",   
    }
    
    print_stars()
    print("Welcome to the Retro Video Store!")
    print("These are your options:\n")
    
    
    for choice_num in options:
        print(f"{choice_num}, {options[choice_num]}")
    return options

def make_choice(options, videos):
    valid_choices = options.keys()
    choice = input("\nSelect option * ")
    
    while choice not in valid_choices:
        print("What would you like to do next? Select from the options above.")
        choice = input("Make your selection using the option number: ")
  
    return choice


def run_cli(play=True):
    
    videos = Videos(url=URL)
    customers = Customers(url=URL)
    rentals = Rentals(url=URL)
    
    options = list_options()

    while play==True:
        
        choice = make_choice(options, videos)

        if choice=='1':
            title=input("Please enter a title: ")
            release_date=input("Please enter a release date: ")
            total_inventory=input("How many copies do you have on hand? ")
            response = videos.add_video(title=title, release_date=release_date,
            total_inventory=total_inventory)

            print(f"New video '{title}' created")

        # update a video
        elif choice=='2':
            video_id = input("Please enter a ID: ")
            title=input("New title: ")
            release_date=input("New release date: ")
            total_inventory=input("How many copies? ")

            response = videos.update_video(video_id=video_id, title=title,
            release_date=release_date, total_inventory=total_inventory)


            print(f"Updated video id {video_id}")

        # delete a video
        elif choice=='3':
            video_id = input("Please enter an ID: ")
            videos.delete_video(video_id)
            print(f"Video {video_id} has been deleted")

        # list all videos
        elif choice=='4':
            for video in videos.list_videos():
                print(video)

        # get one video
        elif choice=='5':
            video_id = input("Please enter an ID: ")
            selected_video = videos.get_video(video_id=video_id)
            print(selected_video)

        # add a customer
        elif choice=='6':
            name=input("Please enter a name: ")
            postal_code=input("Please enter a postal code: ")
            phone=input("Please enter a phone number: ")
            response = customers.add_customer(name=name, postal_code=postal_code,
            phone=phone)
            print(f"Customer {name} created")

        # update a customer
        elif choice=='7':
            customer_id = input("Please enter an ID: ")
            name=input("Please enter a new name: ")
            postal_code=input("Please enter a new postal code: ")
            phone=input("Please enter a new phone: ")

            response = customers.update_customer(customer_id=customer_id,
            name=name, postal_code=postal_code, phone=phone)
            print(f"Updated customer id {customer_id}")

        # delete a customer
        elif choice=='8':
            customer_id = input("Please enter an ID: ")
            response = customers.delete_customer(customer_id)
            print(f"Customer number {customer_id} has been deleted")

        # get info about one customer
        
        elif choice=='9':
            customer_id = input("Please enter an ID: ")
            selected_customer = customers.get_one_customer(customer_id=customer_id)
            if selected_customer:
                print(selected_customer)

        # get info about all customers
        elif choice=='10':
            for customers in customers.all_customers():
                print(customers)

        # check out video 
        elif choice=='11':
            customer_id=input("Please enter a customer id: ")
            video_id=input("Please enter a video id: ")
            response = rentals.check_out(customer_id=customer_id,
            video_id=video_id)
            print("Video successfully checked out")
            print(f"Video id {video_id} checked out to {customer_id}")

        # check in video 
        elif choice=='12':
            customer_id=input("Please enter a customer id: ")
            video_id=input("Please enter a video id: ")
            response = rentals.check_in(customer_id=customer_id,
            video_id=video_id)
            print("Video successfully checked in")
            print(f"Video {video_id} checked in from {customer_id}")

        
        # end
        elif choice=='00':
            play=False
            print("\n Thank you for visiting our store. Come again soon.")

      

run_cli()