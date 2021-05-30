import requests
URL = "https://retro-video-store-api.herokuapp.com"

def main():
    pass

if __name__ == "__main__":
    main()

from requests.models import to_native_string
from retro_video import RetroVideo

def print_retro_video():
    print("\n⭐⭐⭐ Retro 📼 Video ⭐⭐⭐\n")    

def print_stars():
    print("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐\n")

def list_options():
    options = {
        "1": "add a video",
        "2": "edit a video",
        "3": "delete a video",
        "4": "get information about all videos",
        "5": "get information about one video",
        ######################################
        "6": "add a customer",
        "7": "edit a customer",
        "8": "delete a customer",
        "9": "get information about one customer",
        "10": "get information about all customers",
        ######################################
        "11": "check out a video to a customer",
        "12": "check in a video from a customer",
        "13": "Quit"
    }

    print_retro_video()
    print("Welcome to Retro Video CLI")
    print("These are the actions you can perform")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    print_stars()

    return options

def make_choice(options, retro_video):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        print("What would you like to do?")
        choice = input("Make your selection using the option number: ")
    return choice 

def run_cli(play=True):
    #initialize retro_video
    retro_video = RetroVideo(url="https://retro-video-store-api.herokuapp.com/")

    options = list_options()

    while play==True:
        choice = make_choice(options, retro_video)

                #######################################
                ########### VIDEO OPTIONS #############
                #######################################
### CHOICE 1 ###
        if choice=="1": # add a video
            print("Great! Let's add a new video.")
            title=input("What is the title of the video? ")
            release_date=input("What is the release date of the video? ")
            total_inventory=input("What is the total inventory of the video?")
            response = retro_video.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print(f"The New Video \'{title}\' with {response} was successfully added.")
### CHOICE 2 ###
        elif choice=="2": # edit a video
            retro_video.select_video()

            print(f"Great! Let's edit the video: {retro_video.selected_video}")
            title=input("What is the new title of the video?")
            release_date=input("What is the new release date of the video?")
            total_inventory=input("What is the new total inventory of the video?")
            response = retro_video.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("Updated video:", response)
### CHOICE 3 ###
        elif choice=="3": # delete a video
            retro_video.delete_video()
            print_stars()
            print("\n❌ 📼 Video has been deleted. 📼 ❌\n")
# ### CHOICE 4 ###
        elif choice=="4": # "get information about all videos"
            print("\n⭐ 📼 ⭐ 📼 ⭐ All Videos ⭐ 📼 ⭐ 📼 ⭐\n")
            for video in retro_video.list_videos():
                print("📼 📼 📼 📼 📼 📼 📼 📼 📼 📼 📼")
                print(f"Video ID: {video['id']}")
                print(f"Release Date: {video['release_date']}")
                print(f"Title: {video['title']}")
                print(f"Total Inventory: {video['total_inventory']}")
                print("📼 📼 📼 📼 📼 📼 📼 📼 📼 📼 📼")                
                print("⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐ ⭐")
            print_stars()
### CHOICE 5 ###
        elif choice=="5": # "get information about one video",
            print("\n📼 🔎 Let's Get the Video Information! 🔍 📼\n")
            retro_video.select_video()

                #######################################
                ########## CUSTOMER OPTIONS ###########
                #######################################
### CHOICE 6 ###
        elif choice=="6": # "add a customer"
            print("Great! Let's add a new customer.")
            name=input("What is the name of the customer? ")
            phone=input("What is the phone number for the customer?")
            postal_code=input("What is the postal code for the customer?")
            response = retro_video.create_customer(name=name, phone=phone, postal_code=postal_code) # registered_at=None,videos_checked_out_count=None
            print_stars()
            print("New customer:", response)
### CHOICE 7 ###
        elif choice=="7": # "edit a customer"
            retro_video.select_customer()

            print(f"Great! Let's edit this customers information: {retro_video.selected_customer}")
            name=input("What is the new name of the customer?")
            phone=input("What is the new phone number for the customer?")
            postal_code=input("What is the new postal code for the customer?")
            response = retro_video.update_customer(name=name, phone=phone, postal_code=postal_code) #,registered_at=None,videos_checked_out_count=None 

            print_stars()
            print("Updated customer:", response) # ["customer"]
### CHOICE 8 ###
        elif choice=="8": # "delete a customer"
            #retro_video.select_customer()
            retro_video.delete_customer()
            print("\n❌ 📼 Customer has been deleted. 📼 ❌\n")
### CHOICE 9 ###
        elif choice=="9": # "get information about one customer"
            print("\n📼 🔎 Let's Get a Customer's Information! 🔍 📼\n")
            retro_video.select_customer()

### CHOICE 10 ###
        elif choice=="10": # "get information about all customers",
            print_stars()
            for customer in retro_video.list_customers():
                print(customer)

            print("\n⭐ 🧑🏿‍🤝‍🧑🏾🧑🏼‍🤝‍🧑🏻 ⭐ All Customers ⭐ 🧑🏿‍🤝‍🧑🏾🧑🏼‍🤝‍🧑🏻 ⭐\n")
            for customer in retro_video.list_customers():
                print("🍿 🍿 🍿 🍿 🍿 🍿 🍿 🍿 🍿 🍿 🍿")
                print(f"Customer ID: {customer['id']}")
                print(f"Customer Name: {customer['name']}")
                print(f"Phone: {customer['phone']}")
                print(f"Registration Date: {customer['registered_at']}")
                print(f"Number of Videos Checked Out: {customer['videos_checked_out_count']}")
                print("🍿 🍿 🍿 🍿 🍿 🍿 🍿 🍿 🍿 🍿 🍿")                
                print("\n \n")
            print_stars()

                #######################################
                ########### RENTAL OPTIONS ############
                #######################################
### CHOICE 11 ###
        elif choice=="11": # "check out a video to a customer",
            print("Great! Let's check out a video.")
            print("First, Select a customer.")
            print("Then, Select a video that the customer wants to check out.")
            
            retro_video.check_out()

            print_stars()

# ### CHOICE 12 ###
        elif choice=="12": # "check in a video from a customer"
            print("Great! Let's check out a video.")
            print("First, Select the customer.")
            print("Then, Select the video that the customer wants to return.")
            
            retro_video.check_in()

            print_stars()

                #######################################
                ############# QUIT OPTION #############
                #######################################
# ### CHOICE 13 ###
        elif choice=='13': # "13": "Quit"
            play=False
            print("\nThanks for using the Video Store CLI!\n")

    print_retro_video()

run_cli()