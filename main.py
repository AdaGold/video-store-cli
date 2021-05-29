import requests
from video_store import Videostore

URL = "http://127.0.0.1:5000"
VIDEO_STORE_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("################################################")
    print("******** WELCOME TO RETRO VIDEO STORE **********")
    print("################################################")


if __name__ == "__main__":
    main()

def list_options():
    options = {
        "1": "Create a video",
        "2": "Update selected video",
        "3": "Delete selected video",
        "4": "List all videos",
        "5": "Select a video", 

        "6": "Create a customer",
        "7": "Update selected customer",
        "8": "Delete selected customer",
        "9": "List all customers",
        "10": "Select a customer",

        "11": "Check out a video to a customer",
        "12": "Check out a video to a customer",

        "13": "List all options",
        "14": "Quit"
        }


    # Start with options of selecting video and customer
    print("\nWhat would you like to do?")  
    print("**************************\n")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print("\nYou must select a video or customer before updating it, deleting it, check-in, or check-out.\n")
    return options
    

def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")

    # if choice in ['2','3','11','12'] and video_store.selected_video == None:
    #     print("You must select a video before updating it, deleting it, check-in, or check-out.")
    #     print("Let's select a video!")
    #     choice = "5"
    
    # if  choice in ['7', '8'] and video_store.selected_customer == None:
    #     print("You must select a customer before updating it or deleting it.")
    #     print("Let's select a customer")
    #     choice = "10"

    return choice

def print_stars():
    print("*******************************************************\n")

def run_cli_video_store():
    video_store = Videostore(url=VIDEO_STORE_URL)

    options = list_options()

    play = True
    while play==True:

        # get input and validate
        choice = make_choice(options, video_store)

        # video_store.print_selected_video()
        # video_store.print_selected_customer()


# ==========All For Video Options========== 

        # Option 1: create a video
        if choice == '1':
            print("Great! Let's create a new video.")
            title = input("Title of the video: ")
            release_date = input("The release date of the video: ")
            total_inventory = input("The total Inventory: ")
            response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print(f"New video: {title} has been added.") 
        
        # Option 2: update a video
        elif choice == '2':
            print("Great! Let's update the video")
            title = input("New title of the video: ")
            release_date = input("New release date of the video: ")
            total_inventory =input("New total inventory: ")
            response = video_store.update_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print(f"Updated video: {title} has been updated.") 
        
        # Option 3: Delete a video 
        elif choice=='3':
            delete_video_id = input("Enter video id to delete: ")
            if delete_video_id.isnumeric():
                video_store.delete_video(delete_video_id)
                print(f"Video id {delete_video_id} has been deleted.")
                

        # Option 4: Get information of all videos
        elif choice=='4':
            print("Videos: ")
            print_stars()
            for video in video_store.list_videos():
                print(video)

        # Option 5: Get information of one video 
        elif choice=='5':
            select_by = input("Select by video ID: ")
            if select_by.isnumeric():
                video = video_store.get_video(id=video_id)
                print(video)


# ==========All For Customers Options========== 

        # Option 6: Create a new customer 
        elif choice == '6':
            print("Great! Let's create a new customer.")
            name = input("Name of the customer: ")
            postal_code = input("Customer's postal_code: ")
            phone = input("Customer's phone number: ")

            response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone) 
            print("New customer: #{response['id']} has been added.") 
        
        # Option 7: Edit a customer 
        elif choice == '7':
            print("Great! Let's update the customer.")
            name = input("New name of the customer: ")
            postal_code = input("Customer's new postal_code: ")
            phone = input("Customer's new phone number: ")

            response = video_store.update_customer(name=name, postal_code=postal_code, phone=phone) 
            print("Updated customer: #{response['id']} has been updated.") 

        # Option 8: Delete a customer 
        elif choice =='8':
            delete_customer_id = input("Enter the customer id to delete: ")
            if delete_customer_id.isnumeric():
                video_store.delete_customer(id=delete_customer_id)
            print("Customer id #{delete_customer_d} has been deleted.")
            
        
        # Option 9: Get information of all customers 
        elif choice =='9':
            print("Customer: ")
            print_stars()
            for customer in video_store.list_customer():
                print(customer)

        # Option 10: Get information of one customer 
        elif choice =='10':
            select_by = input("Select by customer ID: ")
            if select_by.isnumeric():
                customer = video_store.get_customer(id=customer_id)
                print(customer)


# ==========Video and Customer: Checkin/Check-out========== 

        # Option 11: Check out a video to a customer 
        elif choice=='11':
            print("You are checking out a video!")
            video_id = input("Video id: ")
            customer_id = input("Customer id: ")

            if customer_id == None or video_id == None:
                print("No record found.")
            else: 
                checkout = video_store.check_out(customer_id=customer_id, video_id=video_id)
            print("You checked out #{video_id} to customer #{customer_id}")
    
        # Option 12: Check in video from a customer 
        elif choice=='12':
            print("You are checking in a video!")
            video_id = input("Video id: ")
            customer_id = input("Customer id: ")

            if customer_id == None or video_id == None:
                print("No record found.")
            else: 
                checkin = video_store.check_in(customer_id=customer_id, video_id=video_id)
            print("You checked in video #{video_id} from a customer #{customer_id}.")

        # Option 13: List all options 
        elif choice=='13':
            list_options()

        # Option 14: End of the program 
        elif choice=='14':
            play=False
            print("This is the end of the program.")
            print_stars()

run_cli_video_store()