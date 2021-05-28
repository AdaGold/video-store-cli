from video import VideoOps
import requests
from customer import CustomerOps
from video import VideoOps
from datetime import datetime

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def logo():
    print("J's Retro Store")
#Create a cool retro ASCII

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    print("LETS GET YOU A MOVIE OR TWO!")
    
def list_options():

    options = {
        "1": "List all options", 
        "2": "Add Customer",
        "3": "Update Customer",
        "4": "Delete Customer",
        "5": "List all Customer",
        "6": "Select a Customer",
        "7": "List all Videos",
        "8": "Add Video",
        "9": "Update Video",
        "10": "Delete Video",
        "11": "Select a video",
        "12": "Quit"
        }

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    return options


def make_choice(options, customer, video):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 1 for all available options!")
        choice = input("Make your selection using the option number: ")

    if choice in ['3','4'] and customer.selected_customer == None:
        print("You must select a customer before updating or deleting them.")
        print("Let's select a Customer!")
        choice = "5"

    if choice in ['9','10'] and video.selected_video == None:
        print("You must select a video before updating or deleting it.")
        print("Let's select a video!")
        choice = "7"
    
    return choice

def run_cli(play=True):

    #initialize customer
    customer = CustomerOps("https://retro-video-store-api.herokuapp.com", None)
    video = VideoOps ("https://retro-video-store-api.herokuapp.com", None)
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, customer, video)

        # customer.print_selected()
        if choice =="1":
            list_options()

        elif choice=='2':
            print("Great! Let's add a customer.")
            name=input("First and last name? ")
            phone=input("What is your phone number? ")
            postal_code =input("Enter your 5 digit zip code!")
            response = customer.add_customer(name=name, phone=phone, postal_code=postal_code)
            print("New customer:", response["customer"])

        elif choice=='3':
            print(f"Great! Let's update the customer info: {customer.selected_customer}")
            name=input("First and last name? ")
            phone=input("What is your phone number? ")
            postal_code =input("Enter your 5 digit zip code!")
            response = customer.update_customer(name=name, phone=phone, postal_code=postal_code)
            print("Updated customer:", response["customer"])

        elif choice=='4':
            customer.delete_customer()
            print("Customer has been deleted.")

            print(customer.list_customers())

        elif choice=='5':
            print("List of all customers!")
            for cust in customer.list_all_customers():
                print(cust)

        elif choice=='6':
            id = input("Select the customer id!")
            if id.isnumeric():
                id = int(id)
                customer.get_customer(id=id)
          
            if customer.selected_customer:
                print("Selected customer: ", customer.selected_customer)

        elif choice=='7':
            print("List of all video!")
            for vid in video.list_all_videos():
                print(vid)

        elif choice=='8': 
            print("Great! Let's add a video.")
            title=input("Movie Name?")
            release_date=input("What is the release date? ")
            total_inventory =input("What is the total inventory?")
            response = video.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print("New Video:", response["video"])

        elif choice=='9':
            print("Great! Let's update a video.")
            title=input("Movie Name?")
            release_date=input("What is the release date? ")
            total_inventory =input("What is the total inventory?")
            response = video.update_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print("Updated Video:", response["video"])

        elif choice=='10':
            video.delete_video()
            print("Video has been deleted.")

            print(video.list_all_videos())

        
        elif choice=='11':
            id = input("Select a video id!")
            if id.isnumeric():
                id = int(id)
                video.get_video(id=id)
          
            if video.selected_video:
                print("Selected video: ", video.selected_video)    
        
        elif choice=='12':
            play=False
            print("\nThanks for using Video CLI!")

run_cli()