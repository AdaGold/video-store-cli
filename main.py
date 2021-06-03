from video_store import VideoStore

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO THE RETRO VIDEO STORE")
    pass


if __name__ == "__main__":
    main()


##############################
from video_store import VideoStore

def print_stars():
    print("\n**************************\n")

def list_options():

    # options = {
    #     "1": "List all videos", 
    #     "2": "Create a video",
    #     "3": "Select a video", 
    #     "4": "Update selected video", 
    #     "5": "Delete selected video", 
    #     "6": "List all customers",
    #     "7": "Create a customer",
    #     "8": "Select a customer",
    #     "9": "Update selected customer",
    #     "10": "Delete selected customers",
    #     "11": "Check out selected video to a customer",
    #     "12": "Check in selected video from a customer",
    #     "13": "List all options",
    #     "14": "Quit"
    #     }
    
    options = {
        "1": "add a video",
        "2": "edit a video",
        "3": "delete a video",
        "4": "get information about one video",
        "5": "get information about all videos",
        "6": "add a customer",
        "7": "edit a customer",
        "8": "delete a customer",
        "9": "get information about one customer",
        "10": "get information about all customers",
        "11": "check-out a video to a customer",
        "12": "check-in a video from a customer",
        "13": "List all options",
        "14": "Quit"
    }

    print_stars()
    print("These are the actions you can perform")
    print_stars()
    
    for number in options:
        # print(f"Option {number}. {options[number]}")
        print(f"Option {number}: {(options[number]).title()}")

    print_stars()
    return options


# def make_choice(options, video_store):
def make_choice(options):
    valid_choices = options.keys()
    # choice = None
    choice = input("\nPlease select option: ")

    while choice not in valid_choices:
        print("Please select 13 to see all options again")
        choice = input("Make your selection using the option number: ")

    # if choice in ['4','5','6','7'] and video_store.selected_task == None:
    #     print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
    #     print("Let's select a task!")
    #     choice = "3"
    
    return choice


def select_video(video_store):
    choice = input("Please enter video title: ")
    video_store.list_one_video(title=choice)
    return video_store.selected_video


def select_customer(video_store):
    choice = input("Please enter customer name: ")
    video_store.list_one_customer(name=choice)
    return video_store.selected_customer


def run_cli(play = True):

    #initialize video_store
    video_store = VideoStore(url=BACKUP_URL)
    
    # print choices
    options = list_options()

    while play == True:

        # get input and validate
        # choice = make_choice(options, video_store)
        choice = make_choice(options)

        # video_store.print_selected()

        # Choice 1: add a video
        if choice == '1':
            title = input("What is the title of the video? ")
            release_date = input("What is the release_date of the video? ")
            total_inventory = input("What is the total inventory of the video? ")
            response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)   

            print_stars()
            print("New video created:", title)

        # Choice 2: edit a video
        elif choice == '2':
            video = select_video(video_store)
            title = input("What is the new title of the video? ")
            release_date = input("What is the new release_date of the video? ")
            total_inventory = input("What is the new inventory of the video? ")
            response = video_store.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("Updated video:", response["title"])

        # Choice 3: delete a video
        elif choice == '3':
            video = select_video(video_store)
            video_store.delete_video()

            print_stars()
            print("Video has been deleted")

            print_stars()
            list_options()
        
        # Choice 4: list one video
        elif choice == "4":
            video_id = input("Enter video id: ")
            response = video_store.list_one_video(id=video_id)
            print_stars()
            print(response)

        # Choice 5: list all videos
        if choice == '5':
            print_stars()
            print("List all videos")
            for video in video_store.list_all_videos():
                print(video)
        
        # Choice 6: add a customer
        elif choice == '6':
            name = input("What is the name of the customer? ")
            postal_code = input("What is the postal code of the customer? ")
            phone = input("What is the phone number of the customer? ")
            response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone)   

            print_stars()
            print("New customer created:", name)

        # Choice 7: edit a customer
        elif choice == '7':
            customer = select_customer(video_store)
            name = input("What is the new name of the customer? ")
            postal_code = input("What is the new postal code of the customer? ")
            phone = input("What is the new phone number of the customer? ")
            response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone)   

            print_stars()
            # print("Updated customer:", response["name"])
            print("Updated customer:", name)

        # Choice 8: delete a customer
        elif choice == '8':
            customer = select_customer(video_store)
            video_store.delete_customer()

            print_stars()
            print("Customer has been deleted")

            print_stars()
            list_options()

        # Choice 9: list one customer
        elif choice == '9':
            customer_id = input("Enter customer id: ")
            response = video_store.list_one_customer(id=customer_id)
            print_stars()
            print(response)

        # Choice 10: list all customers
        elif choice == '10':
            print_stars()
            print("List all customers")
            for customer in video_store.list_all_customers():
                print(customer)
        
        # Choice 11: check out a video to a customer
        elif choice == '11':
            # customer_id = input("Enter customer id: ")
            # video_id = input("Enter video_id: ")
            # # print(f"The customer is {video_store.selected_customer}")
            # rental = video_store.check_out_video(customer_id = customer["id"], video_id = video["id"])
            # # rental = video_store.check_out_video()
            # # rental = video_store.check_out_video(customer_id=customer_id, video_id=video_id)
            # print(f"Video {rental[video_id]} has been checked_out to customer {rental[customer_id]}")

            customer = select_customer(video_store)
            video = select_video(video_store)
            print(f"The customer is {video_store.selected_customer}")
            rental = video_store.check_out_video(customer_id = customer["id"], video_id = video["id"])
            print(f"Video {rental['video_id']} has been checked_out to customer {rental['customer_id']}")

        # Choice 12: check in a video from a customer
        elif choice == '12':
            pass

        # Choice 13: list all options
        elif choice == '13':
            print_stars()
            list_options()

        # Choice 14: quit
        elif choice == '14':
            play = False
            print_stars()
            print("\nThanks for using the Video Store CLI!")

        print_stars()

run_cli()



