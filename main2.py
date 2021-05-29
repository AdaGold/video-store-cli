import requests
from video_store import VideoStore

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_stars():
    print("\n**************************\n")


def list_options():

    options = {
        "*": "List all options",
        "1": "Add a video", 
        "2": "Edit a video",
        "3": "Delete a video", 
        "4": "Get information about all videos", 
        "5": "Get information about one video", 
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Get information about all customers",
        "10": "Get information about one customers",
        "11": "Check out a video to a customer",
        "12": "Check in a video from a customer",
        "END" : "End operations and quit"
        }

    print_stars()
    print("WELCOME TO STELLA'S RETRO VIDEO STORE")
    print("Please select from the following menu.")
    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}: {options[choice_num]}")

    print_stars()
    return options


def select_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select * to see all options. Select End to quit.")
        choice = input("Make your selection using the option number: ")
    return choice



def run_cli(play=True):

    video_store = VideoStore(url=BACKUP_URL)
    options = list_options()

    while play==True:
        choice = select_choice(options, video_store)

        # 1: add a video
        if choice=="*":
            list_options()
        
        elif choice=='1':
            print("Adding a new video.")
            new_title = input("Title: ")
            new_release_date = input("Release Date: ")
            new_total_inventory = input("Total Inventory: ")
            response = video_store.add_video(title=new_title, release_date=new_release_date, total_inventory=new_total_inventory)

            print(f"New video #{response['id']} has been added.")

        # Option 2: edit a video 
        elif choice=='2':
            select_video = input("Please enter the id of the video to update: ")
            if select_video.isnumeric():
                title=input("What is the new title of your video? ")
                release_date=input("What is the new release date of your video? ")
                total_inventory=input("What is the new total inventory of your video? ")
                response = video_store.update_video(select_video,title=title, release_date=release_date, total_inventory=total_inventory)      

                print(f"Video #{response['id']} has been updated.") 

        # Option 3: delete a video 
        elif choice=="3":
            delete_id = input("Enter the video ID to delete: ")
            if delete_id.isnumeric():
                video_store.delete_video(id=delete_id)
                print(f"The video id #{delete_id} has been deleted.")

        # Option 4: get information about all videos
        elif choice=="4":
            for video in video_store.list_all_videos():
                print(video)

        # Option 5: get information about one video 
        elif choice=="5":
            video_id = input("Which video id would you like to select?: ")
            if video_id.isnumeric():
                video = video_store.get_video(id=video_id)
                print(video)

# ========CUSTOMER OPTIONS======== #

        # Option 6: add a customer
        if choice=='6':
            print("Let's add a new customer.")
            new_name = input("Name: ")
            new_postal_code = input("Postal Code: ")
            new_phone = input("Phone: ")
            response = video_store.add_customer(name=new_name, postal_code=new_postal_code, phone=new_phone)

            print(f"New customer #{response['id']} has been added.")

        # Option 7: edit a customer
        elif choice=='7':
            select_customer = input("Please select a customer to edit by entering the person's id: ")
            if select_customer.isnumeric():
                name=input("What is the new name of the customer? ")
                postal_code=input("What is the new postal code of the customer? ")
                phone=input("What is the new phone number of the customer? ")
                response = video_store.update_customer(select_customer, name=name,postal_code=postal_code, phone=phone)      

                print(f"Customer #{response['id']} has been updated.") 

        # Option 8: delete a customer 
        elif choice=="8":
            delete_id = input("Enter the customer ID to delete: ")
            if delete_id.isnumeric():
                video_store.delete_customer(id=delete_id)
                print(f"Customer id #{delete_id} has been deleted.")

        # Option 9: get information about all customers
        elif choice=="9":
            for customer in video_store.list_all_customers():
                print(customer)

        # Option 10: get information about one customer
        elif choice=="10":
            customer_id = input("Which customer id would you like to select?: ")
            if customer_id.isnumeric():
                customer = video_store.get_customer(id=customer_id)
                print(customer)

# ========RENTAL OPTIONS======== #

        # Option 11: check out a video to a customer
        elif choice == "11":
            print("Let's checkout a video!")
            video_id = input("Enter the video id: ")
            customer_id = input("Enter the customer id: ")

            if customer_id == None or video_id == None:
                print("No record found. Please enter valid information.")
            else:
                rental = video_store.checkout_video_to_customer(customer_id=customer_id, video_id=video_id)
                print(f"Video #{video_id} has been checked out to customer #{customer_id}.")

         # Option 12: check in a video from a customer
        elif choice == "12":
            print("Let's check in a video!")
            video_id = input("Enter the video id: ")
            customer_id = input("Enter the customer id: ")

            if customer_id == None or video_id == None:
                print("No record found. Please enter valid information.")
            else:
                return_rental = video_store.checkin_video_from_customer(customer_id=customer_id, video_id=video_id)
                print(f"Video #{video_id} has been returned from customer #{customer_id}.")

        elif choice=="END":
            play=False
            print("\nThanks for using the Video Store CLI!")

run_cli() 