import requests
from video_store import VideoStore 

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def mark_intro():
    print("\n**************************\n")

def list_menu_options(): 
    menu = {
        "1": "List all customers in Blockbuster's database", 
        "2": "Create a customer account in the Blockbuster database",
        "3": "Select a customer account from the database", 
        "4": "Update a customer's account information", 
        "5": "Delete a customer account from the database", 

        "6": "List all videos in Blockbuster's database", 
        "7": "Add a video to the Blockbuster database",
        "8": "Select a video from the database", 
        "9": "Update a video's due date",
        "10": "Delete a video from the database",

        "11": "Check out a video to a customer", 
        "12": "Check in a video from a customer",

        "13": "List all menu options",
        "14": "Quit"
        }

    mark_intro()
    print("WELCOME TO BLOCKBUSTER'S DATABASE\n")
    print("Below is a list of actions you can take: \n")
    for option in menu: 
        print(f"Option {option}. {menu[option]}")
    print()
    return menu

def select_action(menu, video_store):
    choices_offered = menu.keys() 
    employee_choice = None

    while employee_choice not in choices_offered:
        print("What action are you looking to perform? ")
        employee_choice = input("Use your keypad to make a selection: ")
    if employee_choice in ["4", "5"] and video_store.selected_customer == None: 
        print("You have to select a customer account that exists before performing any work on it.")
        print("Choose a customer by pressing 3. ")
        employee_choice = 3
    return employee_choice 

def run_cli(play=True):
    video_store = VideoStore(url="https://retro-video-store-api.herokuapp.com")
    choices = list_menu_options() 

    while play == True:
        employee_choice = select_action(choices, video_store) 
        if employee_choice in ["1","2","3","4","5"]: 
            video_store.show_selected_customer()
        elif employee_choice in ["6","7","8","9","10"]:
            video_store.show_selected_video()
        
        if employee_choice == '1':
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
            print('FOR DISPLAY: ', for_display) # {'id': 116}
            print("Customer created. Their account ID is: ", for_display["id"])
        elif employee_choice == '3':
            choice_param = input("Want to select a customer by name or ID? ")
            if choice_param == "name": 
                name = input("Enter the name of the customer whose account you want to work with: ")
                print("Customer account info you selected: ", video_store.get_customer(name=name))
            elif choice_param == "id":
                # print("LOOOOOK: ", type(video_store.selected_customer)) # <class 'NoneType'>
                cli_id = input("Which customer ID would you like to select? ")

                if (cli_id.isnumeric()) == False:
                    print("Use digits, please.")
                elif (cli_id.isnumeric()) == True:
                    cli_id = int(cli_id)
                    print("Customer account info you selected: ", video_store.get_customer(id=cli_id))
            else:
                print("Could not select. Please enter the name or ID of an existing customer. ")
        elif employee_choice == '4': 
            print(f"Then, let's update the account information inside this collection: {video_store.selected_customer}. ")
            name = input("Enter the new name for the customer account: ")
            phone = input("Enter the customer's new phone number: ")
            postal_code = input("Enter the customer's new postal code: ")
            for_update = video_store.update_customer(name=name, phone=phone, postal_code=postal_code)
            mark_intro()
            print("Here's the new account information: ", for_update) # Here's the new account information: {'id': 198, 'name': 'Maxine Waters', 
                                                                        # 'phone': '333-333-0000', 'postal_code': '20022',
                                                                        # 'registered_at': 'Sat, 29 May 2021 01:56:21 GMT', 'videos_checked_out_count': 0}
        elif employee_choice == '5':
            video_store.delete_customer()
            mark_intro()
            print("This customer account has been deleted. See below: ")
            mark_intro()
            for customer in video_store.list_customers():
                print(customer)
        elif employee_choice == '6':
            mark_intro()
            for video in video_store.list_videos():
                print(video)
        elif employee_choice == '7':
            print("We'll add a new video to the database, then. ")
            title = input("Enter the video's title: ")
            release_date = input("Enter the video's release date (format: YYYY-MM-DD): ")
            total_inventory = input("Enter the number of copies that'll be added to the stock: ")
            available_inventory = total_inventory

            for_display = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory,\
                                                    available_inventory=available_inventory)
            mark_intro()
            print("Video addition details: ", for_display) # {'id': 238}
        elif employee_choice == '8':
            choice_param = input("Want to select a video by title or ID? ")
            if choice_param == "title":
                title = input("Enter the title of the video you want to work with: ")
                print("Video info you selected: ", video_store.get_video(title=title))
            elif choice_param == "id": # address case issue later
                cli_id = input("Which video ID would you like to select? ")
                if (cli_id.isnumeric()) == False:
                    print("Use digits, please.")
                elif (cli_id.isnumeric()) == True:
                    cli_id = int(cli_id)
                    print("Video info you selected: ", video_store.get_video(id=cli_id)) # ... = {'id': 237, 'release_date': 'Sun, 12 May 2002 00:00:00 GMT', 
                                                                                        # 'title': 'The Matrix', 'total_inventory': 5}
            else:
                print("Could not select. Please enter the title or ID of an existing video. ")
        elif employee_choice == '9': # NOT WORKING 5/27/21, 8:27pm  
            print(f"Then, let's update the due date inside this collection: {video_store.selected_video}. ")
            due_date = input("Enter the new due date for the video using format YYYY-MM-DD: ") 
            for_update = video_store.update_rental(due_date=due_date) # ERROR THROWN HERE. linked to line 107 in video_store.py
            print("HEYOOOOO: ", for_update)
            mark_intro()
            print("Here's the video's new due date: ", for_update) # should be {"due_date": whatever the given date format is}
        elif employee_choice == '10':
            video_store.delete_video()
            mark_intro()
            print("This video has been deleted from the database. See below: ")
            mark_intro()
            for video in video_store.list_videos():
                print(video)
        elif employee_choice == '11': # CHECK-OUT PROCESS; call check_out func from video_store.py
            pass 
        elif employee_choice == '12': # CHECK-IN PROCESS; call check_out func from video_store.py
            pass
        elif employee_choice == '13':
            list_menu_options()
        elif employee_choice == '14':
            play=False
            print("\nThanks for using the Video Store CLI. Byeeeeee! ")
        mark_intro()


run_cli()

# change 'main' to '__run_cli__' and main() to run_cli() ? 
#if __name__ == "__main__": # func holding menu options dict used to be called main()
#   main()