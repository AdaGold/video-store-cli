import requests
from requests.api import options
from video_store_videos import Video
from video_store_customers import Customer
from video_store_rentals import Rental

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_stars():
    print("\n**************************\n")

def list_options():

    options = {
        "1": "Add a video", 
        "2": "Edit a video",
        "3": "Delete a video", 
        "4": "list all videos", 
        "5": "list a specific video",
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "list one customer",
        "10": "list all customers", 
        "11": "Check out a video to a customer",
        "12": "Check in a video from a customer", 
        "0": "Quit",
        "*": "Select a video",
        "$": "Select a customer",
        }

    print_stars()
    print("WELCOME TO RETRO VIDEO STORE! ")
    print("How can I help you? ")
    print_stars()

    for num_option in options: 
        print(f"Option {num_option}.{options[num_option]}")
    
    print_stars()
    return options

def make_choice(options, video, customer): 
    valid_choices = options.keys() 
    choice = None 

    while choice not in valid_choices: 
        choice = input("Make your selection using the option number: ")
    
    if choice in ['2','3','5'] and video.selected_video == None:
        print("You must select a video before viewing or update its information")
        print("Let's select a video!")
        choice = '*'
    elif choice in ['7','8','9','11','12'] and customer.selected_customer == None:
        print("You must select a customer before viewing or update their information")
        print("Let's select a customer!")
        choice = '$'

    return choice

def run_cli(play=True):
    
    #initialize video
    video = Video()
    customer = Customer()
    rental = Rental()

    #print choices 
    options = list_options() 

    while play == True: 
        choice = make_choice(options, video, customer)
        if choice in ['2','3','5']: 
            video.print_selected()
        elif choice in ['7','8','9','11','12']:
            customer.print_selected()

        if choice =='1':
            print("Great! Let's create a new video.")
            title = input("What is the title of your video? ")
            release_date = input("When was your video released? ")
            total_inventory = int(input("How many copies to add? "))
            response = video.create_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("New video:", response["id"])

        elif choice == '2': 
            print(f"Great! Let's update the video: {video.selected_video}")
            title=input("What is the revised title of your video? ")
            release_date=input("What is the revised release date of your video? ")
            total_inventory=input("What is the revised total inventory of your video? ")
            response = video.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("Updated video:", response)
        elif choice == '*':
            id = input("Which video id would you like to select? ")
            if id.isnumeric(): 
                id = int(id)
                video.get_video(id=id)
            else: 
                print("Could not select. Please enter id.")
            
            if video.selected_video: 
                print_stars() 
                print("Selected video: ", video.selected_video)
            else: 
                print("Could not find video by that id")
        
        elif choice == '3': 
            video.delete_video() 

            print_stars()
            print("Video has been deleted.")

            print_stars()
            print(video.list_videos())

        elif choice == '4': 
            print_stars()
            for video in video.list_videos():
                print(video)
        
        elif choice == '5': 
            # print_stars()
            # print("Please see below video details.")
            video.get_video()

        elif choice =='6':
            print("Great! Thank you for joining the store.")
            name = input("What is your name? ")
            postal_code = input("What is your postal code? ")
            phone = input("What is your phone number? ")
            response = customer.create_customer(name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("New customer:", response["id"])

        elif choice == '7': 
            print(f"Great! Let's update the customer: {customer.selected_customer}")
            name=input("What is the other name you want to go by? ")
            postal_code=input("What is the revised postal code ")
            phone=input("What is the revised phone number? ")
            response = customer.update_customer(name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("Updated customer:", response)

        elif choice == '$':
            id = input("Which customer id would you like to select? ")
            if id.isnumeric(): 
                id = int(id)
                customer.get_customer(id=id)
            else: 
                print("Could not select. Please enter id.")
            
            if customer.selected_customer: 
                print_stars() 
                print("Selected customer: ", customer.selected_customer)
            else: 
                print("Could not find customer by that id")
        
        elif choice == '8': 
            customer.delete_customer() 

            print_stars()
            print("Customer has been deleted.")

            print_stars()
            print(customer.list_customers())

        elif choice == '9': 
            # print_stars()
            # print("Please see below video details.")
            customer.get_customer()

        elif choice == '10': 
            print_stars()
            for customer in customer.list_customers():
                print(customer)
        
        elif choice =='11':
            print("Great! Let's check out a video for you!")
            customer_id = input("Would you like to check out a video or check out for someone else? ")
            if customer_id == "a video": 
                customer_id = customer.selected_customer['id']
            else: 
                customer_id = input("What is that customer's id? ")
            video_id = input("What is the video id of the video that you want to rent? ")
            response = rental.check_out_rental(customer_id=customer_id, video_id=video_id)

            print_stars()
            print("Checked out rental:", response)
        
        elif choice =='12':
            print("Great! Let's check in the video for you!")
            customer_id = input("Would you like to check in a video or check in for someone else? ")
            if customer_id == "a video":
                customer_id = customer.selected_customer['id']
            else: 
                customer_id = input("What is that customer's id? ")
            video_id = input("What is the video id of the video that you want to return? ")
            response = rental.check_in_rental(customer_id=customer_id, video_id=video_id)

            print_stars()
            print("Checked in rental:", response)
        
        elif choice=='0':
            play=False
            print("\nThanks for using the Video store CLI!")


if __name__ == "__main__":
    run_cli()