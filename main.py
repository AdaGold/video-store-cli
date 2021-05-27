import requests
from video_store import VideoStore

# URL = "http://127.0.0.1:5000"
# BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_pattern():
    print("////////////////////////////////////////////////")

def list_options():
    # Maybe just have every possible option in the first options list
    options = {
        "1": "List all videos",
        "2": "List all customers",
        "3": "Add new video to system",
        "4": "Add new customer to system",
        "5": "Select a specific video",
        "6": "Select a specific customer",
        "7": "Check out a video",
        "8": "Check in a video"
        }
    print("Here is a list of possible actions:")
    print("")
    for num in options:
        print(f"{num}. {options[num]}")
    print_pattern()
    return options

def list_more_options():
    options = {
        "1": "Update selection",
        "2": "Delete Selection",
        "3": "List current rentals"
        }
    print("What would you like to do with your selection?")
    print("")
    for num in options:
        print(f"{num}. {options[num]}")
    print_pattern()
    return options

def make_choice(options):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        choice = input("Please select which action you would like to take: ")
    return choice

def display_video(video):
    print("")
    print(video['title'])
    print(f"Release Date: {video['release_date']}")
    print(f"Total Inventory: {video['total_inventory']}")
    print(f"Available Inventory: {video['available_inventory']}")
    print(f"ID: {video['id']}")

def display_customer(customer):
    print("")
    print(customer['name'])
    print(f"Postal Code: {customer['postal_code']}")
    print(f"Phone #: {customer['phone']}")
    print(f"Date Registered: {customer['registered_at']}")
    print(f"Videos Out Count: {customer['videos_checked_out_count']}")
    print(f"ID: {customer['id']}")



def main():
    video_store = VideoStore()

    print("WELCOME TO RETRO VIDEO STORE")
    options = list_options()
    choice = make_choice(options)

    if choice == "1":
        print_pattern()
        for video in video_store.list_videos():
            display_video(video)
    
    elif choice == "2":
        print_pattern()
        for customer in video_store.list_customers():
            display_customer(customer)
    
    elif choice == "3":
        print("Please enter the following information about the new video:")
        title = input("Title: ")
        release_date = input("Release Date: ")
        total_inventory = input("Total Inventory: ")
        video_store.create_video(title, release_date, total_inventory)
        print("New video created!")
    
    elif choice == "4":
        print("Please enter the following information about the new customer:")
        name = input("Name: ")
        postal_code = input("Postal Code: ")
        phone = input("Phone: ")
        video_store.create_customer(name, postal_code, phone)
        print("New customer created!")
    
    elif choice =="5":
        sort = input("Would you like to search by video id or video title?: ")
        sort = sort.lower()
        valid_sort = False
        while valid_sort == False:
            if sort == "id":
                id = input("Please enter video id: ")
                video_store.get_video(id=id)
                valid_sort = True
            elif sort == "title":
                title = input("Please enter video title: ")
                video_store.get_video(title=title)
                valid_sort = True
            else:
                sort = input("Please enter vaild sorting method (id or title): ")
        if video_store.current_video:
            print_pattern()
            print("Here is your selected video:")
            display_video(video_store.current_video)
            second_choice = make_choice(list_more_options())
            if second_choice == "1":
                #What if they don't want to update everything? Maybe give choiced?
                print("Cool! Let's update this video:")
                title = input("Enter new video title: ")
                release_date = input("Enter new release date: ")
                total_inventory = input("Enter new total inventory: ")
                print("Video successfully created:")
                display_video(video_store.update_video(title, release_date, total_inventory))
            elif second_choice == "2":
                #Deletion doesn't really work. Must fix!
                ans = input("Are you sure you want to delete this video permenantly? (y/n)")
                if ans == "y":
                    video_store.delete_video()
                else:
                    print("Okay. Let's wait on deleting that.")
            else:
                pass
                #get rental from vid
        else:
            print("Sorry, video not found.")
    
    elif choice == "6":
        sort = input("Would you like to search by customer id, name or phone #?: ")
        sort = sort.lower()
        valid_sort = False
        while valid_sort == False:
            if sort == "id":
                id = input("Please enter customer id: ")
                video_store.get_customer(id=id,)
                valid_sort = True
            elif sort == "name":
                name = input("Please enter customer name: ")
                video_store.get_customer(name=name)
                valid_sort = True
            elif sort == "phone":
                phone = input("Please enter customer phone: ")
                video_store.get_customer(phone=phone)
                valid_sort = True
            else:
                sort = input("Please enter vaild sorting method (id, name, or phone #): ")
        if video_store.current_customer:
            display_customer(video_store.current_customer)
        else:
            print("Sorry, customer not found.")
    

if __name__ == "__main__":
    main()