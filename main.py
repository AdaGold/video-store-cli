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
        "12": "check in a video from a customer",
        "13": "List all options again",
        "14" : "Quit"
        }
    
    print_stars()
    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")
    print_stars()
    
    for choice_num in options: 
        print(f"Option {choice_num}.{options[choice_num]}")

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
        choice = make_choice(options, video_operations, customer_operations) 

        if choice=='1':
            
            print_stars()
            print("Hi, let's add a video to the library")
            title=input("What is the title of your video? : ")
            release_date=input("please provide the release date of your video (YYYY-MM-DD) : ")
            total_inventory=input("how many of these videos would you like to add to the total inventory? : ")
            response = video_operations.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print("New video:", response["id"]) 
            
        elif choice=='2':
            
            print_stars()
            for video in video_operations.get_all_video_information():
                print(video)
            
            video_id = input(f"Great! Select the video id to update:")
            
            title=input("What is the new title of your video? ")
            release_date=input("What is the new release date (YYYY-MM-DD) of your video? ")
            total_inventory=input("What is the new total inventory of this video? ")
            
            response = video_operations.edit_video(video_id, title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print("Updated video : ", response["title"])

        elif choice=='3':
            all_videos = video_operations.get_all_video_information()
            for vid in all_videos:
                print(f"Id:{vid['id']}, Title:{vid['title']}")
                
            del_vid = input("Which video would you like to delete, please enter the id: ")
            if del_vid.isnumeric():
               del_vid  = int(del_vid)
               video_operations.delete_video(del_vid)
               
            print_stars()
            print("Video has been deleted. ")
            print_stars()
        
        elif choice=='4':
            print_stars()
            for video in video_operations.get_all_video_information():
                print(video)
            
        elif choice=='5':
            print("Here are the available videos: ")
            all_videos = video_operations.get_all_video_information()
            for vid in all_videos:
                print(f"Id:{vid['id']}, Title:{vid['title']}")
            
            video_id = input("Which video id would you like to get information on? : ")
            if video_id.isnumeric():
                video_id = int(video_id)
            else:
                print("Could not select. Please enter valid video id: ")
            
            if video_id:
                print_stars()
                print("Selected video information is : ", video_operations.get_one_video_information(video_id=video_id))
            
        elif choice =='6':
            print_stars()
            print("Hi, let's add a new customer to the register")
            name=input("What is the name of your customer? : ")
            phone=input("please provide the phone number (000-000-0000) of your customer : ")
            postal_code=input("please pro5vide the 5 digit postal code of your customer : ")
            response = customer_operations.add_customer(name=name, phone=phone, postal_code=postal_code)
            print_stars()
            print("New customer created with id :", response["id"])
        
        
        elif choice == '7':
            all_customers = customer_operations.get_all_customer_information()
            for customer in all_customers:
                print(f"Id:{customer['id']}, Name:{customer['name']}")
            customer_id = input("Which customer would you like to update, please enter the customer id: ")
            name=input("What is the new name of your customer? : ")
            phone=input("What is the new phone number of the customer? : ")
            postal_code=input("What is the postal code of this customer? : ")
            response = customer_operations.edit_customer(customer_id, name=name, phone=phone, postal_code=postal_code)
            print_stars()
            print("Updated customer:", response["name"])
    
        
        elif choice == '8':
            all_customers = customer_operations.get_all_customer_information()
            for customer in all_customers:
                print(f"Id:{customer['id']}, Name:{customer['name']}")
                
            customer_id = input("Which customer would you like to delete, please enter the customer id: ")
            customer_operations.delete_customer(customer_id)
            print_stars()
            print("customer has been deleted.")
            print_stars()
            
            
        elif choice == '9':
            print("Here are the customers:")
            all_customers = customer_operations.get_all_customer_information()
            
            for customer in all_customers:
                print(f"Id: {customer['id']}, name: {customer['name']}")
            customer_id = input("Which customer id would you like to select? : ")
            
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                customer_operations.selected_customer = customer_operations.get_one_customer_information(cust_id=customer_id)
            else:
                print("Could not select. Please enter valid customer id: ")
            
            if customer_operations.selected_customer:
                print_stars()
                print("Selected customer: ", customer_operations.selected_customer)
            
            
        elif choice == '10':
            print_stars()
            for customer in customer_operations.get_all_customer_information():
                print(customer) #need to do sorting in the API side
            
        
        elif choice == '11':
            print_stars()
            print("you would like to checkout a video to a Customer:")
            
            video_id = input("Enter the video id : ")
            if video_id.isnumeric():
                video_id = int(video_id)
            video = video_operations.get_one_video_information(video_id=video_id)
            print(video)
            
            customer_id = input("Enter the customer id : ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            customer = customer_operations.get_one_customer_information(cust_id=customer_id)
            print(customer)
            
            checked_out_rental = rental_operations.checkout_vid_to_customer(customer_id, video_id)
            print(checked_out_rental)
            print("video sucessfully checked out to the customer!")
            
        elif choice == '12':
            print_stars()
            print("you would like to return/check-in a video from a Customer:")
            
            video_id = input("Enter the video id : ")
            if video_id.isnumeric():
                video_id = int(video_id)
                video = video_operations.get_one_video_information(video_id=video_id)
                print(video)
            
            customer_id = input("Enter the customer id : ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            customer= customer_operations.get_one_customer_information(cust_id=customer_id)
            print(customer)
            
            checked_in_rental = rental_operations.checkin_vid_from_customer(customer_id, video_id)
            print(checked_in_rental)
            print("video sucessfully checked in to the library!")
        
        elif choice=='13':
            list_options()
            
        elif choice=='14':
            play=False
            print("\nYou are now exiting the video store CLI, Thank you!")
        
        else:
            print("invalid choice", choice, "please select a valid choice")

        print_stars()
        
        
def make_choice(options, video_operations, customer_operations):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all options again :")
        choice = input("Make your selection using the option numbers 1 - 14 : " )
    return choice 
    

if __name__ == "__main__":
    main()