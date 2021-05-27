import requests
from video_store import VideoStore
from datetime import datetime, timedelta

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

# def main():
#     print("WELCOME TO RETRO VIDEO STORE")
#     pass

#     from video_store import VideoStore

def print_stars():
    print("\n**************************\n")

def list_options():

    options = {
        "1": "Add a video", 
        "2": "Edit a video",
        "3": "Delete a video", 
        "4": "See all videos", 
        "5": "Select a video", 
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Select a customer",
        "10": "See all customers",
        "11": "Check out a video",
        "*": "List all options",
        "q": "Quit"
        }

    print_stars()
    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")
    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select * to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['2','3','5'] and video_store.selected_video == None:
        print("You must select a video before updating it or deleting it")
        print("Let's select a video!")
        choice = "5"
    
    if choice in ['7','8','9','11'] and video_store.selected_customer == None:
        print("You must select a customer before updating, deleting, or checkingo out a video")
        print("Let's select a customer!")
        choice = "9"
    
    return choice

def run_cli(play=True):
    print("WELCOME TO RETRO VIDEO STORE")

    #initialize task_list
    video_store = VideoStore(url="https://retro-video-store-api.herokuapp.com")
    
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, video_store)

        # video_store.print_selected()

        if choice=='4': 
            print_stars()
            for video in video_store.list_videos():
                print(video)

        elif choice=='6':
            print("Great! Let's add a new customer.")
            name=input("What is the customer's name? ")
            postal_code=input("What is the customer's postal code? ")
            phone=input("What is the customer's new phone number?")
            registered_at=datetime.now()
        
            response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("New customer:", response)

        elif choice=='5': 
            select_by = input("Would you like to select by? Enter title or id: ")
            if select_by=="title":
                title = input("Which task title would you like to select? ")
                video_store.get_video(title=title)
            elif select_by=="id":
                id = input("Which video id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video_store.get_video(id=id)
            else:
                print("Could not select. Please enter id or title.")
            
            if video_store.selected_video:
                print_stars()
                print("Selected video: ", video_store.selected_video)

        elif choice=='2':
            print(f"Great! Let's update the video: {video_store.selected_video}")
            title=input("What is the new title of your video? ")
            release_date=input("What is the new release date of your video? ")
            total_inventory=input("What is the new total inventory of your video?")
            response = video_store.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("Updated video:", response)

        elif choice=='3':
            video_store.delete_video()

            print_stars()
            print("Video has been deleted.")

            print_stars()
            print(video_store.list_videos())

        elif choice=='1':
            print("Great! Let's add a new video.")
            title=input("What is the title of your video? ")
            release_date=input("What is the release date of your video? ")
            total_inventory=input("What is the total inventory?")
            response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("New video:", response) #only returns id number


        elif choice=='7': #edit a customer
            print(f"Great! Let's update the customer: {video_store.selected_customer}")
            name=input("What is the new name of your customer? ")
            postal_code=input("What is the new postal code of your customer? ")
            phone=input("What is the new phone number of your customer?")
            #do they want to update registered_at date? 
            #do they want to update videos checked out?
            response = video_store.update_customer(name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("Updated customer:", response)

        elif choice=='8':
            video_store.delete_customer()

            print_stars()
            print("Customer has been deleted.")

            print_stars()
            print(video_store.list_customers())

        elif choice=='9':
            select_by = input("Would you like to select by? Enter name or id: ")
            if select_by=="name":
                name = input("Which customer name would you like to select? ")
                video_store.get_customer(name=name)
            elif select_by=="id":
                id = input("Which customer id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video_store.get_customer(id=id)
            else:
                print("Could not select. Please enter id or name.")
            
            if video_store.selected_customer:
                print_stars()
                print("Selected customer: ", video_store.selected_customer)

        elif choice=='10':
            print_stars()
            for customer in video_store.list_customers():
                print(customer)
        
        elif choice =='11':
            print("Great! Let's check out a video!")
            verify=input(f"Is this you? Enter y/n {video_store.selected_customer}")
            if verify == 'y' or 'Y':
                select_by=input("Please select a video! Would you like you select by title or id?")
                if select_by=="name":
                    title=input("What is the title of the video you'd like to check out?  ")
                    video_store.get_video(title=title)
                elif select_by=="id":
                    id=input("What is the video id you'd like to check out?  ")
                    if id.isnumeric():
                        id=int(id)
                        video_store.get_video(id=id)
                else:
                    print("Could not select. Please enter id or title.")
                
                if video_store.selected_video:
                    customer_id=video_store.selected_customer["id"]
                    video_id=video_store.selected_video["id"]
                    video_store.check_out(customer_id, video_id)
                    print_stars()
                    print("You have successfully checked out ", video_store.selected_video)
            
        
        elif choice =='*':
            list_options()

        elif choice == 'q' or 'Q':
            play=False
            print("\nThanks for using the Video Store CLI!")

            print_stars() 

run_cli()