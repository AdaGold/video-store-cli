import requests
from video_operations import VideoOperations
from customer_operations import CustomerOperations
from rental_operations import RentalOperations
from datetime import datetime


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_stars():
    print("\n**************************\n")

def list_options():
    
    options = {
        "1": "add a video", 
        "2": "edit a video",
        "3": "delete a video", 
        "4": "get information about all videos", 
        "5": "get information about one video", 
        "6": "add a customer",
        "7": "edit a customer",
        "8": "Delete a customer",
        "9": "get information about one customer",
        "10": "get information about all customers",
        "11": "check out a video to a customer",
        "12": "check in a video from a customer"
        }
    
    print_stars()
    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")
    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()
    
    return options
    
def main(play=True):
    print("WELCOME TO RETRO VIDEO STORE")
    
    #initialize video_operations
    video_operations = VideoOperations(URL)
    customer_operations = CustomerOperations(URL)
    rental_operations = RentalOperations(URL)
    
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, video_operations, customer_operations, rental_operations)

        video_operations.print_selected()
        #customer_operations.print_selected()
        #rental_operations.print_selected()

        if choice=='1':
            
            print_stars()
            print("Hi, let's add a video to the library")
            title=input("What is the title of your video? ")
            release_date=input("please provide the release date of your video (YYYY-MM-DD)")
            total_inventory=input("how many of these videos would you like to add to the total inventory?")
            response = video_operations.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print("New video:", response["id"])
            
        elif choice=='2':
            print(f"Great! Let's update the video: {video_operations.selected_video}")
            
            title=input("What is the new title of your video? ")
            release_date=input("What is the new release date of your video? ")
            total_inventory=input("What is the new total inventory of this video?")
            
            response = video_operations.edit_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("Updated video:", response["video"])

        elif choice=='3':
            video_operations.delete_video()
            print_stars()
            print("Video has been deleted.")

            print_stars()
            print(video_operations.get_all_video_information())
        
        elif choice=='4':
            print_stars()
            for video in video_operations.get_all_video_information():
                print(video)
            
        elif choice=='5':
            print("Here are the available videos:")
            all_videos = video_operations.get_all_video_information()
            print(f"all videos = {all_videos}")
            
            for vid in all_videos:
                print(f"Id:{vid['id']}, Title:{vid['title']}")
            
            video_id = input("Which video id would you like to select? ")
            if video_id.isnumeric():
                video_id = int(video_id)
                video_operations.selected_video = video_operations.get_one_video_information(video_id=video_id)
            else:
                print("Could not select. Please enter valid video id")
            
            if video_operations.selected_video:
                print_stars()
                print("Selected video: ", video_operations.selected_video["title"])
            
        
        elif choice =='6':
            print_stars()
            print("Hi, let's add a new customer to the register")
            name=input("What is the name of your customer? ")
            phone=input("please provide the phone number of your customer")
            postal_code=input("please provide the postal code of your customer")
            response = customer_operations.add_customer(name=name, phone=phone, postal_code=postal_code)
            print_stars()
            print("New customer:", response["customer"])
        
        elif choice == '7':
            print(f"Great! Let's update the customer: {customer_operations.selected_customer}")
            
            customer_id=input("What is the id of the customer you want to update?")
            name=input("What is the new name of your customer? ")
            phone=input("What is the new phone number of the customer? ")
            postal_code=input("What is the postal code of this customer?")
            
            response = customer_operations.edit_customer(name=name, phone=phone, postal_code=postal_code)

            print_stars()
            print("Updated customer:", response["customer"])
        
        elif choice == '8':
            customer_operations.delete_customer()
            print_stars()
            print("customer has been deleted.")

            print_stars()
            print(customer_operations.get_all_customer_information())
            
        elif choice == '9':
            select_by = input("Would you like to select by? Enter name or customer_id: ")
            if select_by=="name":
                name = input("Which customer would you like to select? ")
                customer_operations.get_one_customer_information(name=name)
                
            elif select_by=="customer_id":
                customer_id = input("Which customer id would you like to select? ")
                if customer_id.isnumeric():
                    customer_id = int(customer_id)
                    customer_operations.get_one_customer_information(customer_id=customer_id)
            else:
                print("Could not select. Please enter id or name.")
            
            if customer_operations.selected_customer:
                print_stars()
                print("Selected customer: ", customer_operations.selected_customer)
        
            
        elif choice == '10':
            print_stars()
            for customer in customer_operations.get_all_customer_information():
                print(customer)
        
        # elif choice == '11':
        # elif choice == '12':
        elif choice=='13':
            list_options()
        elif choice=='14':
            play=False
            print("\nThanks for using the video store CLI!")
        
        else:
            print("invalid choice", choice, "please select a valid choice")

        print_stars()
        
        
def make_choice(options, video_operations, customer_operations, rental_operations):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 12 to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['2', '3'] and video_operations.selected_video == None:
        print("You must select a video before updating it, deleting it, and getting a specific video")
        print("Let's select a video!")
        choice = "5"
        
    elif choice in ['7','8'] and customer_operations.selected_customer == None:
        print("You must select a customer before updating it, deleting it, and getting a specific customer")
        print("Let's select a customer!")
        choice = "9"
        
    return choice


if __name__ == "__main__":
    main()