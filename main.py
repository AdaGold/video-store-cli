import requests
from video_store import VideoStore


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"
video_store = VideoStore()

def list_options():
    options = {
        "1" : "Add a Video", 
        "2" : "Edit a Video",
        "3" : "Delete a Video",
        "4" : "Browse all Videos",
        "5" : "Select one Video",
        "6" : "Add a new customer",
        "7" : "Update customer profile",
        "8" : "Remove customer",
        "9" : "View customer profile",
        "10" : "View all customers",
        "11" : "Check out a Video",
        "12" : "Return a Video", 
        "0" : "List all options"
    }
    for choice in options:
        print(f"Option {choice}: {options[choice]}")
    return options

def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print(f"Please select from the valid options, select 0 to view them again")
        choice = input("Make your selection: ")
    
    if choice in ["2", "3", "7", "8", "11", "12"] and video_store.selected_video == None:
        print("You must select an item before editing!")
        choice = "3"
    return choice


def main(store_open=True):
    print("WELCOME TO RETRO VIDEO STORE")
    print("Please select from the following options")
    options = list_options()
    while store_open:
        choice = make_choice(options, video_store)
    video_store.print_selected()



if __name__ == "__main__":
    main()