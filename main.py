import datetime
from video_store import VideoStore

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def list_options():
    options = {
        "1": "add a video", 
        "2": "edit a video",
        "3": "delete a video",
        "4": "get information about all videos",
        "5": "get information about one video",
        "6": "add a customer",
        "7": "edit a customer",
        "8": "delete a customer",
        "9": "get information about one customer",
        "10": "get information about all customers",
        "11": "check out a video to a customer",
        "12": "check in a video from a customer",
        "00": "QUIT"
        }
    
    print("\nSelect one of the following options:")
    for option in options:
        print(f"Option {option}: {(options[option]).title()}")
    return options

def make_choice(options):
    valid_choices = options.keys()
    choice = input("\nSelect option > ")
    while choice not in valid_choices:
        choice = input("\nSelect option > ")
    return choice

def select_video(video_store):
    choice = input("Enter video title or id > ")
    if choice.isalpha():
        video_store.get_video(title=choice.lower())
    elif choice.isdigit():
        id = int(choice)
        video_store.get_video(id=id)
    return video_store.selected_video 

def select_customer(video_store):
    choice = input("Enter customer name or id > ")
    if choice.isalpha():
        video_store.get_customer(name=choice.lower())
    elif choice.isdigit():
        id = int(choice)
        video_store.get_customer(id=id)
    return video_store.selected_customer 

def get_video_data():
    title=input("Enter Title > ")
    release_date=input("Enter date (MM-DD-YYYY) the movie released > ")
    total_inventory=input("Enter #copies > ")
    return title, release_date, total_inventory

def is_video_data_valid(title, release_date, total_inventory):
    try:
        release_date = datetime.datetime.strptime(release_date, '%m-%d-%Y')
    except ValueError:
        print('Invalid date.')
        return False
    if title.isalpha() and total_inventory.isdigit():
        return True

def is_customer_data_valid(name, postal_code, phone):
    if name.isalpha() and \
        len(postal_code) == 5 and postal_code.isdigit() and \
        len(phone) == 10 and phone.isdigit():
        return True
    return False

def video_not_found():
    return "No video with that id or title has been found."

def get_customer_data():
    name=input("Enter name > ")
    postal_code=input("Enter postal code? > ")
    phone=input("Enter phone > ")
    return name, postal_code, phone

def customer_not_found():
    return "No customer with that id or name has been found."

def run_cli(play=True):
    video_store = VideoStore(url=BACKUP_URL)
    while play == True:
        options = list_options()
        choice = make_choice(options)

        # Option 1: add a video 
        if choice == "1":
            title, release_date, total_inventory = get_video_data()
            if not is_video_data_valid(title, release_date, total_inventory):
                print("Incorrect data.")
            else:
                video = video_store.add_video(title=title, release_date=release_date, total_inventory=total_inventory)            
                print(f"The video id #{video['id']} has been added.")
            
        # Option 2: edit a video 
        elif choice=="2":
            video = select_video(video_store)
            if video == None:
                video_not_found()
            else:
                title, release_date, total_inventory = get_video_data()
                video = video_store.update_video(title=title, release_date=release_date, total_inventory=total_inventory)            
                print(f"The video id #{video['id']} has been updated.") 
        
        # Option 3: delete a video 
        elif choice=="3":
            video = select_video(video_store)
            if video == None:
                video_not_found()
            else:
                video_store.delete_video()
                print(f"The video id #{video['id']} has been successfully deleted.")
        
        # Option 4: get information about all videos
        elif choice=="4":
            for video in video_store.list_videos():
                print(video)
        
        # Option 5: get information about one video 
        elif choice=="5":
            video = select_video(video_store)
            if video == None:
                video_not_found()
            else:
                for attr,info in video.items():
                    print(f"{attr}: {info}")

        # Option 6: add a customer 
        elif choice=="6":
            name, postal_code, phone = get_customer_data()
            if not is_customer_data_valid(name, postal_code, phone):
                print("Incorrect data.")
            else:
                customer = video_store.add_customer(name=name, postal_code=postal_code, phone=phone)
                print(f"Customer id #{customer['id']} has been successfully added.") # How to access customer id?
            
        # Option 7: edit a customer 
        elif choice=="7":
            # what if customer is not in the db?
            customer = select_customer(video_store)
            if customer == None:
                customer_not_found()
            else:
                name, postal_code, phone = get_customer_data()
                video_store.update_customer(name=name, postal_code=postal_code, phone=phone)
                print(f"Updates successfully have been made to customer {name}.")

        # Option 8: delete a customer 
        elif choice=="8":
            customer = select_customer(video_store)
            if customer == None:
                customer_not_found()
            else:
                video_store.delete_customer()
                print(f"Customer {customer} has been deleted.")

        # Option 9: get information about one customer 
        elif choice=="9":
            customer = select_customer(video_store)
            if customer == None:
                print(customer_not_found())
            else:
                for attr,info in customer.items():
                    print(f"{attr}: {info}")

        # Option 10: get information about all customers
        elif choice=="10":
            for customer in video_store.list_customers():
                print(customer)

        elif choice=="00":
            play=False
            print("Thank god it's over.")

run_cli(True)