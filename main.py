import requests
from datetime import datetime
from rental_info import RentalInfo
from video_info import VideoInfo
from customer_info import CustomerInfo

URL = "http://127.0.0.1:5000"
# BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    if __name__ == "__main__":
        main()

def print_stars():
    print("\n*******************************************\n")

def list_options():
    
    options = {
        "1": "Add a video", 
        "2": "Edit a video",
        "3": "Delete a video", 
        "4": "Get information about videos", 
        "5": "Get information about video by ID", 
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Get information about customer by ID",
        "10": "Get information about all customers",
        "11": "Check out a video to a customer",
        "12": "Check in a video from a customer",
        "13": "List all options",
        "14" : "Quit"
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

    video_info = VideoInfo(URL)
    customer_info = CustomerInfo(URL)
    rental_info = RentalInfo(URL)
    options = list_options()

    while play==True:
        choice = make_choice(options, video_info, customer_info, rental_info)
        video_info.print_selected()
        customer_info.print_selected()

        if choice=='1':
            print_stars()
            print("Hello, let's add a video to the video store ")
            title=input("What is the title of your video? ")
            release_date=input("What is the release date of your video YYYY-MM-DD ")
            total_inventory=input("What is the total inventory? ")
            response = video_info.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print("New video:", response["id"])
            
        elif choice=='2':
            select_video = input(f"Please select the video you wish to edit: {video_info.get_all_video_information()} ")
            if select_video.isnumeric():
                print(f"Great! Let's update the video: {video_info.selected_video}")
                title=input("What is the new title of your video? ")
                release_date=input("What is the new release date (YYYY-MM-DD) of your video? ")
                total_inventory=input("What is the new inventory of this video? ")
            
                response = video_info.edit_video(video_id, title=title, release_date=release_date, total_inventory=total_inventory)
                print_stars()
                print("Updated video: ", response["title"])

        elif choice=='3':
            delete_video = input("Please input the video ID you wish to delete ")
            if delete_video.isnumeric():
                delete_video  = int(delete_video)
                video_info.delete_video(delete_video)
    
            print_stars()
            print("Video has successfully been deleted. ")
            print_stars()
        
        elif choice=='4':
            print_stars()
            for video in video_info.get_all_video_information():
                print(video)
            
        elif choice=='5':
            print("Here are the available videos: ")
            all_videos = video_info.get_all_video_information()
            # print(f"all videos = {all_videos}")
            
            for video in all_videos:
                print(f"Id: {video['id']}, Title: {video['title']}")
            
            video_id = input("Which video id would you like to select?: ")
            if video_id.isnumeric():
                video_id = int(video_id)
                video_info.selected_video = video_info.get_one_video_information(video_id=video_id)
            else:
                print("Please enter valid video id:")
            
            if video_info.selected_video:
                print_stars()
                print("Selected video information is : ", video_info.selected_video)
            
        elif choice =='6':
            print_stars()
            print("Adding a new customer to the register? ")
            name=input("What is their name?: ")
            phone=input("What is their phone number ex. 123-456-7890: ")
            postal_code=input("What is their postal code: ")
            response = customer_info.add_customer(name=name, phone=phone, postal_code=postal_code)
            print_stars()
            print("Success! New customer created with id :", response["id"])
        
        
        elif choice == '7':
            print(f"Great! Let's update the customer: {customer_info.selected_customer}")
            name=input("Enter the new name of the customer: ")
            phone=input("What is their new phone number ex. 123-456-7890: ")
            postal_code=input("What is their new postal code?: ")
            response = customer_info.edit_customer(customer_id, name=name, phone=phone, postal_code=postal_code)
            print_stars()
            print("Updated customer:", response["name"])
    
        
        elif choice == '8':
            customer_info.delete_customer(customer_id)
            print_stars()
            print("Success! customer has been deleted.")
            print_stars()
            
            
        elif choice == '9':
            print("Here are the customers: ")
            all_customers = customer_info.get_all_customer_information()
            
            for customer in all_customers:
                print(f"Id: {customer['id']}, name: {customer['name']}")
            
            customer_id = input("Select a customer?: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                customer_info.selected_customer = customer_info.get_one_customer_information(customer_id=customer_id)
            else:
                print("Error. Please enter valid customer id: ")
            
            if customer_info.selected_customer:
                print_stars()
                print("Selected customer: ", customer_info.selected_customer)
            
            
        elif choice == '10':
            print_stars()
            for customer in customer_info.get_all_customer_information():
                print(customer)
            
        
        elif choice == '11':
            print_stars()
            print("Let's checkout a video!: ")
            
            video_id = input("Enter the video id: ")
            if video_id.isnumeric():
                video_id = int(video_id)
                video_info.selected_video = video_info.get_one_video_information(video_id=video_id)
                print(video_info.selected_video)
                
            customer_id = input("Enter the customer id: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            customer_info.selected_customer = customer_info.get_one_customer_information(single_customer_id=customer_id)
            print(customer_info.selected_customer)
            
            checked_out_rental = rental_info.checkout_vid_to_customer(customer_id, video_id)
            print(checked_out_rental)
            print("video sucessfully checked out! Please return in 7 days to avoid any late fees. ")
            
        elif choice == '12':
            print_stars()
            print("you would like to return a video from a Customer: ")
            
            video_id = input("Enter the video id: ")
            if video_id.isnumeric():
                video_id = int(video_id)
                video_info.selected_video = video_info.get_one_video_information(video_id=video_id)
                print(video_info.selected_video)
            
            customer_id = input("Enter the customer id : ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            customer_info.selected_customer = customer_info.get_one_customer_information(single_customer_id=customer_id)
            print(customer_info.selected_customer)
            
            checked_in_rental = rental_info.checkin_vid_from_customer(customer_id, video_id)
            print(checked_in_rental)
            print("video sucessfully checked in to total inventory! ")
        
        elif choice=='13':
            list_options()
            
        elif choice=='14':
            play=False
            print("\nThank you, Bye!!")
        
        else:
            print("invalid choice", choice, "please select a valid choice ")

        print_stars()

        
        
def make_choice(options, video_info, customer_info, rental_info):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("Select 13 to see all options again: ")
        choice = input("Make your selection using the option numbers 1 - 14 : " )
        
    if choice in ['2', '3'] and video_info.selected_video == None:
        print("You must select a video before making edits: ")
        print("Please select a video!: ")
        choice = "5"
        
    elif choice in ['7','8'] and customer_info.selected_customer == None:
        print("You must select a customer before making edits: ")
        print("Please select a customer! : ")
        choice = "9"
        
    return choice

if __name__ == "__main__":
    main()



