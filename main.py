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


def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select * to see all options. Select END to quit.")
        choice = input("Make your selection using the option number: ")
    return choice



def run_cli(play=True):

    video_store = VideoStore(url=BACKUP_URL)
    options = list_options()

    while play==True:
        choice = make_choice(options, video_store)

        if choice=="*":
            list_options()
        
        #Option 1: add a video
        elif choice=='1':
            print("Adding a new video. Please enter the following information.")
            new_title = input("Title: ")
            new_release_date = input("Release Date: ")
            new_total_inventory = input("Total Inventory: ")
            response = video_store.add_video(title=new_title, release_date=new_release_date, total_inventory=new_total_inventory)
            print("New video created, id# ", response["id"])

        #Option 2: edit a video 
        elif choice=='2':
            select_video = input("Enter the id of the video to update: ")
            if select_video.isnumeric():
                title=input("Enter the updated title of your video: ")
                release_date=input("Enter the updated release date of your video: ")
                total_inventory=input("Enter the updated total inventory of your video: ")
                response = video_store.edit_video(select_video,title=title, release_date=release_date, total_inventory=total_inventory)      
                print(f"Video #{response['id']} has been updated.") 

        #Option 3: delete a video 
        elif choice=="3":
            delete_id = input("Enter the video ID to delete: ")
            if delete_id.isnumeric():
                video_store.delete_video(id=delete_id)
                print(f"The video id #{delete_id} has been deleted.")

        #Option 4: get information of all videos
        elif choice=="4":
            for video in video_store.list_all_videos():
                print(video)

        #Option 5: get information of one video 
        elif choice=="5":
            video_id = input("Select the video ID: ")
            if video_id.isnumeric():
                video = video_store.get_video(id=video_id)
                print(video)

        #Option 6: add a customer
        elif choice=='6':
            print("Adding a new customer. Please enter the following information.")
            name = input("Customer Name: ")
            postal_code = input("Postal Code: ")
            phone = input("Phone: ")
            response = video_store.add_customer(name=name, postal_code=postal_code, phone=phone)
            print("New customer created, id# ", response["id"])

        #Option 7: edit a customer
        elif choice=='7':
            select_customer = input("Enter the id of the video to update: ")
            if select_customer.isnumeric():
                name=input("Enter the updated name of the customer: ")
                postal_code=input("Enter the updated postal code of the customer: ")
                phone=input("Enter the updated phone number of the customer: ")
                response = video_store.update_customer(select_customer, name=name,postal_code=postal_code, phone=phone)      
                print(f"Customer #{response['id']} has been updated.") 

        #Option 8: delete a customer 
        elif choice=="8":
            delete_id = input("Enter the customer ID to delete: ")
            if delete_id.isnumeric():
                video_store.delete_customer(id=delete_id)
                print(f"Customer #{delete_id} has been deleted.")

        #Option 9: get information of all customers
        elif choice=="9":
            for customer in video_store.list_all_customers():
                print(customer)

        #Option 10: get information of one customer
        elif choice=="10":
            customer_id = input("Enter the customer ID to view information: ")
            if customer_id.isnumeric():
                customer = video_store.get_customer(id=customer_id)
                print(customer)

        # Option 11: check out a video
        elif choice == "11":
            print("Checking out a video.")
            video_id = input("Enter the video id: ")
            customer_id = input("Enter the customer id: ")

            if customer_id == None or video_id == None:
                print("No record found. Please enter valid information.")
            else:
                rental = video_store.checkout_video(customer_id=customer_id, video_id=video_id)
                print(f"Check-out completed! Video #{video_id} has been checked out to customer #{customer_id}.")

         # Option 12: check in a video
        elif choice == "12":
            print("Checking in a video")
            video_id = input("Enter the video id: ")
            customer_id = input("Enter the customer id: ")

            if video_id == None or customer_id == None:
                print("No record found. Please enter valid information.")
            else:
                check_in = video_store.checkin_video(customer_id=customer_id, video_id=video_id)
                print(f"Check-in completed! Video #{video_id} has been returned from customer #{customer_id}.")

        elif choice=="END":
            play=False
            print("\nThanks for using the Video Store CLI!")

run_cli() 