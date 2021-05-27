import requests
import json
from video_store import VideoStore

def main():
    print("WELCOME TO RETRO VIDEO STORE")

def show_users():
    # this can be expanded on to make exployees sign in, or give customer choices.
    users = {
        "1": "Employee", 
        "2": "Customer"
        }

    print("*****************************")
    print("Who Are You?")
    
    for choice_num in users:
        print(f"Option {choice_num}. {users[choice_num]}")
    "*****************************"
    return users

def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 9 to see all options again")
        choice = input("Make your selection using the option number: ")
    return choice

def list_options():

    options = {
        "1": "List all Videos", 
        "2": "Single Video Info",
        "3": "Edit Video", 
        "4": "", 
        "5": "Delete selected task", 
        "6": "Mark selected task complete",
        "7": "Mark selected task incomplete",
        "8": "Delete all tasks",
        "9": "List all options",
        "10": "Quit"
        }

    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")

    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    return options

def admin_panel(play, video_store):
        while play == True:
            options = list_options()
            choice = make_choice(options, video_store)
            if choice=='1':
                for video in video_store.get_all_videos():
                    print(video)
                print("Scroll Up To See Videos")
            elif choice == '2':
                input_id = input("What number of video do you want? ")
                chosen_one = video_store.get_video(id=input_id)
                print("Selected Video:")
                print(chosen_one)
            elif choice == '3':
                input_id = input("What number of video do you want? ")
                new_title = input("New Title: ")
                new_release_date = input("Release Date: ")
                new_total_inventory = input("Total Inventory: ")
                video_store.update_video(id=input_id, title=new_title, release_date=new_release_date, total_inventory=new_total_inventory)
            elif choice=='10':
                play=False
                print("\nThanks for using the Video Store CLI")




def run_cli(play=True):
    video_store = VideoStore()
    show_users()
    user_choice = input("Make your selection using the option number: ")
    if user_choice == "1":
        print ("Okay! Lets Get Started!! ;) :) ;) UwU")
        admin_panel(play, video_store)
    else:
        print ("What do you think you're doing! Get off our computer")
        play = False

if __name__ == "__main__":
    main()
    run_cli()


"""
Employee --> 1
--> add a video
Customer --> "Go away! You shouldn't be in our system." 
request = {
    "key": URL,
    "q": "Great Wall of China",
    "format": "json"
}

response = requests.get(path, params=query_params)
"""