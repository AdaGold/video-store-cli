import requests
from video_store import VideoStore # import class + instance methods from other file

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def mark_intro():
    print("\n**************************\n")


def list_menu_options(): # DISPLAYS OPTIONS TO BLOCKBUSTER EMPLOYEE
    menu = {
        "1": "List all customers in Blockbuster's database", 
        "2": "Create a customer account in the Blockbuster database",
        "3": "Select a customer account from the database", 
        "4": "Update a customer's account information", 
        "5": "Delete a customer account from the database", 

        "6": "List all videos in Blockbuster's database", 
        "7": "Add a video to the Blockbuster database",
        "8": "Select a video from the database", 
        "9": "Update a video's due date", # any other attrs that can be updated for video? 
        "10": "Delete a video from the database",

        "11": "Check out a video to a customer", # checkout
        "12": "Check in a video from a customer", # check in

        "13": "List all menu options",
        "14": "Quit"
        }

    mark_intro()
    print("WELCOME TO BLOCKBUSTER'S DATABASE\n")
    print("Below is a list of actions you can take: \n")
    for option in menu: # for every key in the dict
        print(f"Option {option}. {menu[option]}")
    print()
    return menu

def select_action(menu, video_store):
    choices_offered = menu.keys() # "1", "2", etc.
    employee_choice = None # ini at falsey to start while loop

    while employee_choice not in choices_offered:
        print("What action are you looking to perform? ")
        employee_choice = input("Use your keypad to make a selection: ")
    if employee_choice in ["4", "5"] and video_store.selected_customer == None: # 11 and 12 too? add if statement for 'video must exist'?
        print("You have to select a customer account that exists before performing any work on it.")
        print("Choose a customer. ")
        employee_choice = 3
    return employee_choice # returns a string data type choice number

def run_cli(play=True):
    video_store = VideoStore(url="http://127.0.0.1:5000")
    choices = list_menu_options() # dict of all menu options

    while play == True:
        employee_choice = select_action(choices, video_store) # str
        if employee_choice in ["1","2","3","4","5"]: # 2 not working
            video_store.show_selected_customer()
        elif employee_choice in ["6","7","8","9","10"]:
            video_store.show_selected_video()
        
        if employee_choice == '1': # if they ask to see all customers
            mark_intro()
            mark_intro()
            for customer in video_store.list_customers():
                print(customer)
        elif employee_choice == '2':
            print("We'll create a new customer account, then. ")
            name = input("Enter the customer's name: ")
            phone = input("Enter the customer's phone number: ")
            postal_code = input("Enter the customer's postal code: ")
            for_display = video_store.create_customer(name=name, phone=phone, postal_code=postal_code)
            mark_intro()
            print("Customer account info: ", for_display["customer"]) # create_customer() called on 74 should return a jsonified dict whose var name is "customer"
        elif employee_choice == '3':
            choice_param = input("Want to select a customer by name, phone number or ID? ")
            if choice_param == "name":
                name = input("Enter the name of the customer whose account you want to work with: ")
                video_store.get_customer(name=name)
            elif choice_param == "phone number":
                phone = input("Enter the phone number of the customer account you want to work with: ")
                video_store.get_customer(phone=phone)
            # IF MAKING CLI MY WAY, DO I EVEN NEED TO ALLOW ID-LOOKUP? WHAT'S SIMPLEST?
            elif choice_param == "ID": # address case issue?
                cli_id = input("Which customer ID would you like to select? ")
                if cli_id.isnumeric(): # handle id coming in as str (from HTTP path?)
                    cli_id = int(cli_id)
                    video_store.get_customer(cli_id=customer_id) # WHAT SHOULD CUSTOMER_ID BE? TO BE RECOGNIZED?
            else:
                print("Could not select. Please enter the name or phone number of an existing customer. ")
            
            if video_store.selected_customer:
                mark_intro()
                print("Here is the customer you selected: ", video_store.selected_customer)
        elif employee_choice == '4': 
            print(f"Let's update the account information for {video_store.selected_customer}, then. ")
            name = input("Enter the new name for the customer account: ")
            phone = input("Enter the customer's new phone number: ")
            postal_code = input("Enter the customer's new postal code: ")
            for_update = video_store.update_customer(name=name, phone=phone, postal_code=postal_code)

            mark_intro()
            print("Here's the new account information: ", for_update["customer"]) # see choice 2 final lines for explanation
        elif employee_choice == '5':
            video_store.delete_customer()
            mark_intro()
            print("This customer account has been deleted. ")
            mark_intro()
            print(video_store.list_customers()) # confirm that customer's no longer there


        elif employee_choice == '6': # if they ask to see all videos
            mark_intro()
            mark_intro()
            for video in video_store.list_videos():
                print(video)
        elif employee_choice == '7':
            print("We'll add a new video to the database, then. ")
            title = input("Enter the video's title: ")
            release_date = input("Enter the video's release date: ") # account for formatting differences?
            total_inventory = input("Enter the number of copies that'll be added to the stock: ")
            available_inventory = total_inventory # collection of video copies just go to the store: none are checked out yet

            for_display = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory, available_inventory=available_inventory)
            mark_intro()
            print("Video addition details: ", for_display["video"]) # create_video() called on 120 should return a jsonified dict whose var name is "video"
        elif employee_choice == '8':
            choice_param = input("Want to select a video by title or ID? ")
            if choice_param == "title":
                name = input("Enter the title of the video you want to work with: ")
                video_store.get_video(title=title)
            # IF MAKING CLI MY WAY, DO I EVEN NEED TO ALLOW ID-LOOKUP? WHAT'S SIMPLEST?
            elif choice_param == "ID": # address case issue?
                cli_id = input("Which video ID would you like to select? ")
                if cli_id.isnumeric(): # handle id coming in as str (from HTTP path?)
                    cli_id = int(cli_id)
                    video_store.get_video(cli_id=video_id) # WHAT SHOULD VIDEO_ID BE? TO BE RECOGNIZED?
            else:
                print("Could not select. Please enter the title or ID of a video that's been added to the database. ")
            
            if video_store.selected_video:
                mark_intro()
                print("Here is the video you selected: ", video_store.selected_video)
        elif employee_choice == '9': 
            print(f"Let's update the due date for {video_store.selected_video}, then. ")
            due_date = input("Enter the new due date for the video using format YYYY-MM-DD: ") # define and control for format???????
            for_update = video_store.update_rental(due_date=due_date) # proper param??

            mark_intro()
            print("Here's the video's new due date: ", for_update["rental"]) # see choice 2 final lines for explanation; verify dict format: does that give the date itself?
        elif employee_choice == '10':
            video_store.delete_video()
            mark_intro()
            print("This video has been deleted from the database. ")
            mark_intro()
            print(video_store.list_videos()) # confirm that customer's no longer there
        elif employee_choice == '11':
            pass # CHECK-OUT PROCESS
        elif employee_choice == '12':
            pass # CHECK-IN PROCESS
        elif employee_choice == '13':
            list_menu_options()
        elif employee_choice == '14':
            play=False # set flag to False to stop the while loop
            print("\nThanks for using the Video Store CLI. Byeeeeee! ") # exit msg
        mark_intro() # make sure this is in while loop
        mark_intro() # "" 

run_cli()

# NEED THIS OR NO? change 'main' to '__run_cli__' and run_cli() ? 
#if __name__ == "__main__": # func holding menu options dict used to be called main()
#   main()