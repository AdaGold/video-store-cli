import requests
from video_store import VideoStore

# URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")

if __name__ == "__main__":
    main()

def select_video(video_store):
    choice = input("Would you like to select by? Enter title or id: ")
    if choice=="title":
        title = input("Which video title would you like to select? ")
        video_store.get_video(title=title)
    elif choice=="id":
        id = input("Which video id would you like to select? ")
        if id.isnumeric():
            id = int(id)
            video_store.get_video(id=id)
        else:
            print("Could not select. Please enter id or title.")
    return video_store.selected_video 

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
        "8": "delete a customer",
        "9": "get information about one customer",
        "10": "get information about all customers",
        "11": "check out a video to a customer",
        "12": "check in a video from a customer",
        "13": "List all options",
        "14" : "Quit"
        }

    print_stars()
    print("These are the actions you can perform at RETRO VIDEO STORE.")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options

def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Please make a selection.")
        choice = input("Make your selection using the option number: ")
    return choice

    # if choice in ['4','5','6','7'] and task_list.selected_task == None:
    #     print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
    #     print("Let's select a task!")
    #     choice = "3"

def run_cli(play=True):

    #initialize video store
    video_store = VideoStore(url=BACKUP_URL)

    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, video_store)

        # Option 1: add a video
        if choice=='1':
            print("Let's create a new video.")
            new_title = input("Title: ")
            new_release_date = input("Release Date: ")
            new_total_inventory = input("Total Inventory: ")
            response = video_store.add_video(title=new_title, release_date=new_release_date, total_inventory=new_total_inventory)

            print(f"New video #{response['id']} has been added.")

        # Option 2: edit a video 
        elif choice=='2':
            # video = select_video(video_store)
            select_video = input("Please select the video to edit by entering its id: ")
            if select_video.isnumeric():
                title=input("What is the new title of your video? ")
                release_date=input("What is the new release date of your video? ")
                total_inventory=input("What is the new total inventory of your video? ")
                response = video_store.update_video(select_video,title=title, release_date=release_date, total_inventory=total_inventory)      

                print_stars()
                print(f"Video #{response['id']} has been updated.") 
        
        # Option 3: delete a video 
        elif choice=="3":
            delete_id = input("Enter the video ID to delete: ")
            if delete_id.isnumeric():
                video_store.delete_video(id=delete_id)
                print(f"The video id #{delete_id} has been deleted.")
        
        # Option 4: get information about all videos
        elif choice=="4":
            for video in video_store.list_all_videos():
                print(video)
        
        # Option 5: get information about one video 
        elif choice=="5":
            video_id = input("Which video id would you like to select?: ")
            if video_id.isnumeric():
                video = video_store.get_video(id=video_id)
                print(video)


        # Option 11: check out a video to a customer
        elif choice == "11":
            print("Let's checkout a video!")
            video_id = input("Enter the video id: ")
            customer_id = input("Enter the customer id: ")

            if customer == None or video == None:
                print("No record found. Please enter valid information.")
            else:
                rental = video_store.checkout_video_to_customer(customer_id=customer_id, video_id=video_id)
                print(f"Video #{rental['video_id']} has been checked out to customer #{rental['customer_id']}.")

         # Option 12: check in a video from a customer
            print("Let's check in a video!")
            video_id = input("Enter the video id: ")
            customer_id = input("Enter the customer id: ")

            if customer == None or video == None:
                print("No record found. Please enter valid information.")
            else:
                return_rental = video_store.checkin_video_to_customer(customer_id=customer_id, video_id=video_id)
                print(f"Video #{return_rental['video_id']} has been returned from customer #{return_rental['customer_id']}.")

        elif choice=="13":
            list_options()

        elif choice=="14":
            play=False
            print("\nThanks for using the Video Store CLI!")

run_cli(True)