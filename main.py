import requests
from video_store import VideoStore
from datetime import datetime, timedelta

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def print_stars():
    print("\n**************************\n")

def list_options_customer():

    options = {
        "1": "See all videos", 
        "2": "Select a video", 
        "3": "Edit your account info",
        "4": "Delete your account",
        "5": "See account details",
        "6": "Check out a video",
        "7": "Check in a video",
        "*": "List all options",
        "q": "Quit"
        }

    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options

def list_options_employee():

    options = {
        "1": "See all videos", 
        "2": "Select a video",
        "3": "Delete a video", 
        "4": "Add a video", 
        "5": "Edit a video", 
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Select a customer",
        "10": "See all customers",
        "11": "Check out a video",
        "12": "Check in a video",
        "*": "List all options",
        "q": "Quit"
        }

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
    
    for key, value in options.items():
        if key == choice:
            prompt = value

    if prompt in ['Check out a video', 'Check in a video', 'Edit a video', 'Delete a video']:
        if video_store.selected_video == None:
            print("Let's select a video!")
            choice = "2"

        else:
            print(video_store.selected_video)
            verify=input(f"Is this the video you wanted? Please select yes or no  ")

            if verify == "no":
                print("Ok, let's select a different video!")
                choice = "2"
    
    if prompt in ['Check out a video', 'Check in a video', 'Edit a customer','Delete a customer']:
        if video_store.selected_customer == None:
            print("You must select a customer first!  ")
            print("Let's select a customer!")
            choice = "9"

        else:
            print(video_store.selected_customer)
            verify=input("Is this the customer you wanted? Please select yes or no  ")

            if verify == "no":
                print("Ok, let's select a different customer!")
                choice = "9"

    return choice

def run_cli(play=True):
    print("WELCOME TO RETRO VIDEO STORE")

    video_store = VideoStore(url="https://retro-video-store-api.herokuapp.com")
    
    choice=input("Select 1 if you are a customer, or 2 if you are a video store employee.  ")

    if choice == "1":
        print("Welcome Video Store Customer!  ")
        select_by=input("Let's find your account. Would you like to select by name or id?  ")
        
        if select_by=="name":
            name = input("Which customer name would you like to select? ")
            video_store.get_customer(name=name)

        elif select_by=="id":
            id = input("Which customer id would you like to select? ")
            if id.isnumeric():
                id = int(id)
                video_store.get_customer(id=id)
        else:
            print("Could not select. Please enter id or name.  ")
        
        if not video_store.selected_customer:
            print("No customer found.  ")
        
        else:
            print_stars()
            print("Selected customer: ", video_store.selected_customer)
            print_stars()
            print(f"Welcome {video_store.selected_customer['name']}!")
            print("What would you like to do today?")

            options=list_options_customer()

            while play==True:
                choice = make_choice(options, video_store)

                if choice == '1':
                    print_stars()
                    for video in video_store.list_videos():
                        print(video)

                elif choice =='2':

                    select_by = input("Would you like to select by? Enter title or id: ")
                    if select_by=="title":
                        title = input("Which video title would you like to select? ")
                        video_store.get_video(title=title)
                    elif select_by=="id":
                        id = input("Which video id would you like to select? ")
                        if id.isnumeric():
                            id = int(id)
                            video_store.get_video(id=id)
                    print(video_store.selected_video)

                elif choice == '3':
                    print(f"Great! Let's update your account.")
                    name=input("What is your new name? ")
                    postal_code=input("What is your new postal code? ")
                    phone=input("What is your new phone number?")

                    response = video_store.update_customer(name=name, postal_code=postal_code, phone=phone)

                    print_stars()
                    print("Updated account information:", response)

                elif choice=='4':
                    video_store.delete_customer()

                    print_stars()
                    print("Customer has been deleted.")

                    print_stars()

                    play=False
                    print("\nThanks for using the Video Store CLI!")

                    print_stars()

                elif choice == '5':
                    print_stars()
                    print("Your account details: ", video_store.selected_customer)

                elif choice == '6':
                
                    if video_store.selected_video:
                        #print due date
                        customer_id=video_store.selected_customer["id"]
                        video_id=video_store.selected_video["id"]
                        video_store.check_out(customer_id, video_id)
                        print_stars()
                        print("Great! You have successfully checked out ", video_store.selected_video)
                        print_stars()
                
                elif choice == '7':
                
                    if video_store.selected_video:
                        #print due date
                        customer_id=video_store.selected_customer["id"]
                        video_id=video_store.selected_video["id"]
                        video_store.check_in(customer_id, video_id)
                        print_stars()
                        print("Great! You have successfully checked in ", video_store.selected_video)
                        print_stars()

                elif choice =='*':
                    list_options_customer()

                elif choice == 'q' or choice == 'Q':
                    play = False
                    print("\nThanks for using the Video Store CLI!")

                    print_stars() 


#------------------VIDEO STORE EMPLOYEE-------------------

    elif choice == "2":

        print("Welcome Video Store Employee!  ")
        print("What would you like to do?  ")

        options=list_options_employee()

        while play==True:

            choice = make_choice(options, video_store)

            if choice=='1': 
                print_stars()
                for video in video_store.list_videos():
                    print(video)
        

            elif choice=='2': 
                select_by = input("Would you like to select by? Enter title or id: ")
                if select_by=="title":
                    title = input("Which video title would you like to select? ")
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

            
            elif choice=='3':
                video_store.delete_video()

                print_stars()
                print("Video has been deleted.")

                print_stars()
                print(video_store.list_videos())

                #pick new video to delete or confirm currently selected video
            
            elif choice=='4':
                print("Great! Let's add a new video.")
                title=input("What is the title of your video? ")
                release_date=input("What is the release date of your video? ")
                total_inventory=input("What is the total inventory?  ")
                response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)

                print_stars()
                print("New video:", response) #only returns id number??

            elif choice=='5':

                # select_by=input("Please select a video! Would you like you select by title or id?  ")
                # if select_by=="title":
                #     title=input("What is the title of the video you'd like to edit?  ")
                #     video_store.get_video(title=title)
                # elif select_by=="id":
                #     id=input("What is the video id you'd like to update?  ")
                #     if id.isnumeric():
                #         id=int(id)
                #         video_store.get_video(id=id)
                # else:
                #         print("Could not select. Please enter id or title.  ")
                
                if video_store.selected_video:
                    print(f"Great! Let's update the video: {video_store.selected_video}  ")
                    title=input("What is the new title of your video? ")
                    release_date=input("What is the new release date of your video? ")
                    total_inventory=input("What is the new total inventory of your video?  ")
                    response = video_store.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

                    print_stars()
                    print("Updated video:", response)
            
            elif choice=='6':
                print("Great! Let's add a new customer.")
                name=input("What is the customer's name? ")
                postal_code=input("What is the customer's postal code? ")
                phone=input("What is the customer's new phone number?")
                registered_at=datetime.now()
            
                response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone)

                print_stars()
                print("New customer:", response)


            elif choice=='7': #edit a customer

                #confirm selected customer or select different one
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

                if video_store.selected_customer:
                    verify=input(f"Is this the correct customer? Enter yes or no {video_store.selected_customer}")
                    if verify == 'yes':
                        select_by=input("Please select a video! Would you like you select by title or id?")
                        if select_by=="title":
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
                else:
                    print("Let's first select a customer!")
                    choice = '9'
                
            
            elif choice =='*':
                list_options_employee()

            elif choice == 'q' or 'Q':
                play=False
                print("\nThanks for using the Video Store CLI!")

                print_stars() 
    else:
        print("Please select a valid option. Select 1 if you are a customer, or 2 if you are a video store employee.  ")
        #get it to start over


run_cli()