import requests
from retro_video_store import Video_Store

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_hashtags():
    print("\n######################################################################\n")

def list_options():

    options = {
        "1": "See all customers",
        "2": "Get information about a customer",
        "3": "Create a new customer profile",
        "4": "Edit a customer profile", 
        "5": "Delete a customer", 
        "6": "See all videos",
        "7": "See all the information about a video",
        "8": "Create a new video to add to the store",
        "9": "Edit a video's information",
        "10": "Delete a video",
        "11": "Check-out a video",
        "12": "Check-in a video",
        "13": "List all options",
        "14": "Quit"
        }

    print_hashtags()
    print("Welcome to the Retro Video Store!!!")
    print("Here are your options......")
    print_hashtags()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_hashtags()

    return options


def make_choice(options, retro_video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")
    
    return choice

def run_cli(play=True):

    #initialize retro_video_store
    retro_video_store = Video_Store(url="http://127.0.0.1:5000")
    
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, retro_video_store)

        retro_video_store.print_selected()

        if choice=='1':
            print_hashtags()
            print("Here are all of the customers we have in our database.")
            for customer in retro_video_store.list_of_customers():
                print(customer)

        elif choice=='2':
            id=input("What is the id of the customer you want information about? ")
            if id.isnumeric():
                id=int(id)
                print("Here is this customers information:", retro_video_store.get_customer(id=id))
            else:
                print("Please enter the number id.")

        elif choice=="3":
            name=input("What is the name of this new customer? ")
            postal_code=input("What is their postal code? ")
            phone=input("What's their phone number that they'll answer the most? ")
            response = retro_video_store.create_customer(name=name, postal_code=postal_code, phone=phone)
            print("New Customer id:", response["id"])

        elif choice=='4':
            print(f"Time to update someone's information!: {retro_video_store.selected_customer}")
            name=input("What is their new name? ")
            postal_code=input("What is their new postal code? ")
            phone=input("What is their new phone number (if they changed it)? ")
            response = retro_video_store.update_customer(id, name=name, postal_code=postal_code, phone=phone)

            print_hashtags()
            print("Updated customer name:", response["name"])

        elif choice=='5':
            customer_to_delete = input("What is the id of the customer you wish to delete? ")
            if customer_to_delete.isnumeric():
                customer_to_delete = int(customer_to_delete)
                retro_video_store.delete_customer(customer_to_delete)

            print_hashtags()
            print("That customer has been deleted.")

            print_hashtags()
            print("Here are the remaining customers......")
            print(retro_video_store.list_of_customers())

        if choice=='6':
            print_hashtags()
            print("Here are all of the videos we have in the store.")
            for video in retro_video_store.list_of_videos():
                print(video)

        elif choice=='7':
            id=input("What is the id of the video you want information about? ")
            if id.isnumeric():
                id=int(id)
                response = retro_video_store.get_video(id=id)
                print_hashtags()
                print("Here is the video's information:", response)
            else:
                print("Please enter the number id.")

        elif choice=="8":
            title=input("What is the name of this new video? ")
            release_date=input("When was it released? ")
            total_inventory=input("How much do we have to add to the store? ")
            response = retro_video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_hashtags()
            print("New Video information:", response["id"])

        elif choice=='9':
            print(f"Time to update a video's information!: {retro_video_store.selected_video}")
            title=input("What is it's new name? ")
            release_date=input("What is their new release date? ")
            total_inventory=input("How many copies of this do we have? ")
            response = retro_video_store.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_hashtags()
            print("Updated video info:", response["title"])

        elif choice=='10':
            video_to_delete = input("What is the id of the video you wish to delete? ")
            if video_to_delete.isnumeric():
                video_to_delete = int(video_to_delete)
                retro_video_store.delete_video(video_to_delete)

            print_hashtags()
            print("That video has been deleted.")

            print_hashtags()
            print("Here are the remaining videos in store......")
            print(retro_video_store.list_of_videos())

        elif choice=='11':
            print("Be prepared to enter the id of the video and customer for check-out.")
            video_id = input("What is the video id? ")
            if video_id.isnumeric():
                video_id = int(video_id)
                retro_video_store.get_video(id=video_id)
            
            customer_id = input("What is the customer is? ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                retro_video_store.get_customer(id=customer_id)

            response = retro_video_store.check_out_video(customer_id, video_id)
            print_hashtags()
            print("Video Check-out information: ", response)

        elif choice=='12':
            print("Be prepared to enter the id of the video and customer for check-in.")
            video_id = input("What is the video id? ")
            if video_id.isnumeric():
                video_id = int(video_id)
                retro_video_store.get_video(id=video_id)
            
            customer_id = input("What is the customer is? ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                retro_video_store.get_customer(id=customer_id)

            response = retro_video_store.check_in_video(customer_id, video_id)
            print_hashtags()
            print("Video Check-in information: ", response)

        elif choice=='13':
            list_options()

        elif choice=='14':
            play=False
            print("\nThanks for visiting the Retro Video Store! Come again :)")

        print_hashtags()

run_cli()