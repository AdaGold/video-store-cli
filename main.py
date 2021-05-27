import datetime
from video_store import VideoStore

# BACKUP_URL = "https://retro-video-store-project.herokuapp.com"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com/"

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

def option_num(choice, options):
    return (f"You selected Option {choice}: {(options[choice]).title()}")

def select_video(video_store):
    choice = input("Enter video title or id > ")
    if choice.isdigit():
        id = int(choice)
        video_store.get_video(id=id)
    elif isinstance(choice, str):
        video_store.get_video(title=choice.lower())
    return video_store.selected_video 

def select_customer(video_store):
    choice = input("Enter customer name or id > ")
    if choice.isdigit():
        id = int(choice)
        video_store.get_customer(id=id)
    elif isinstance(choice, str):
        video_store.get_customer(name=choice.lower())
    return video_store.selected_customer 

def get_video_data():
    title=input("Enter Title > ")
    release_date=input("Enter date (YYYY-MM-DD) the movie released > ")
    total_inventory=input("Enter the number of copies > ")
    return title, release_date, total_inventory

def get_customer_data():
    name=input("Enter customer name > ")
    postal_code=input("Enter postal code > ")
    phone=input("Enter phone > ")
    return name, postal_code, phone

def is_video_data_valid(title, release_date, total_inventory):
    try:
        release_date = datetime.datetime.strptime(release_date, '%Y-%m-%d')
    except ValueError:
        return False
    if isinstance(title, str) and total_inventory.isdigit():
        return True

def is_customer_data_valid(name, postal_code, phone):
    if isinstance(name, str) and \
        len(postal_code) == 5 and postal_code.isdigit() and \
        len(phone) == 10 and phone.isdigit():
        return True
    return False

def not_found():
    return "No record has been found."

def not_valid_data():
    return "One or more values you entered are not valid."

def run_cli(play=True):
    video_store = VideoStore(url=BACKUP_URL)
    while play == True:
        options = list_options()
        choice = make_choice(options)

        # Option 1: add a video 
        if choice == "1":
            print(option_num(choice, options))
            title, release_date, total_inventory = get_video_data()
            if not is_video_data_valid(title, release_date, total_inventory):
                print(not_valid_data())
            else:
                video = video_store.add_video(title=title, release_date=release_date, total_inventory=total_inventory)            
                print(f"The video id #{video['id']} has been added.")
            
        # Option 2: edit a video 
        elif choice=="2":
            print(option_num(choice, options))
            video = select_video(video_store)
            if video == None:
                print(not_found())
            else:
                title, release_date, total_inventory = get_video_data()
                video = video_store.update_video(title=title, release_date=release_date, total_inventory=total_inventory)            
                print(f"The video id #{video['id']} has been updated.") 
        
        # Option 3: delete a video 
        elif choice=="3":
            print(option_num(choice, options))
            video = select_video(video_store)
            if video == None:
                print(not_found())
            else:
                video_store.delete_video()
                print(f"The video id #{video['id']} has been deleted.")
        
        # Option 4: get information about all videos
        elif choice=="4":
            print(option_num(choice, options))
            for video in video_store.list_videos():
                print(video)
        
        # Option 5: get information about one video 
        elif choice=="5":
            print(option_num(choice, options))
            video = select_video(video_store)
            if video == None:
                print(not_found())
            else:
                for attr,info in video.items():
                    print(f"{attr}: {info}")

        # Option 6: add a customer 
        elif choice=="6":
            print(option_num(choice, options))
            name, postal_code, phone = get_customer_data()
            if not is_customer_data_valid(name, postal_code, phone):
                print(not_valid_data())
            else:
                customer = video_store.add_customer(name=name, postal_code=postal_code, phone=phone)
                print(f"Customer id #{customer['id']} has been added.") 
            
        # Option 7: edit a customer 
        elif choice=="7":
            print(option_num(choice, options))
            customer = select_customer(video_store)
            if customer == None:
                print(not_found())
            else:
                name, postal_code, phone = get_customer_data()
                video_store.update_customer(name=name, postal_code=postal_code, phone=phone)
                print(f"Updates have been made to customer {name}.")

        # Option 8: delete a customer 
        elif choice=="8":
            print(option_num(choice, options))
            customer = select_customer(video_store)
            if customer == None:
                print(not_found())
            else:
                video_store.delete_customer()
                print(f"Customer {customer} has been deleted.")

        # Option 9: get information about one customer 
        elif choice=="9":
            print(option_num(choice, options))
            customer = select_customer(video_store)
            if customer == None:
                print(not_found())
            else:
                for attr,info in customer.items():
                    print(f"{attr}: {info}")

        # Option 10: get information about all customers
        elif choice=="10":
            print(option_num(choice, options))
            for customer in video_store.list_customers():
                print(customer)

        # Option 11: check out a video to a customer
        elif choice=='11':
            print(option_num(choice, options))
            customer = select_customer(video_store)
            video = select_video(video_store)
            if customer == None or video == None:
                print(not_found())
            else: 
                rental = video_store.check_out_video(customer_id=customer['id'],video_id=video['id'])
                print(f"Video #{rental['video_id']} has been checked out to customer #{rental['customer_id']}.")
        
        # Option 12: check in a video from a customer
        elif choice=='12':
            print(option_num(choice, options))
            customer = select_customer(video_store)
            video = select_video(video_store)
            if customer == None or video == None:
                print(not_found())
            else:
                rental = video_store.check_in_video(customer_id=customer['id'],video_id=video['id'])
                print(f"Video #{rental['video_id']} has been checked in to customer #{rental['customer_id']}.")

        elif choice=="00":
            play=False
            print("Oh thank God it's over.")

run_cli(True)