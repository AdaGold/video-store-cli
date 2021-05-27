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

def list_options():

    options = {
        "1": "Add Video", 
        "2": "Edit Video",
        "3": "Delete Video"
        }

    print("*****************************")
    print("What Do You Want to Do?")
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    "*****************************"
    return options


def make_choice(options):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 9 to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['4','5','6','7'] and task_list.selected_task == None:
        print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
        print("Let's select a task!")
        choice = "3"
    
    return choice

def list_options():

    options = {
        "1": "List all Videos", 
        "2": "Create a task",
        "3": "Select a task", 
        "4": "Update selected task", 
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

def admin_panel(play):
        while play == True:
            options = list_options()
            store = make_choice(options)
            return store

def run_cli(play=True):
    video_store = VideoStore()
    show_users()
    user_choice = input("Make your selection using the option number: ")

    if user_choice == "1":
        print ("Okay! Lets Get Started!! ;) :) ;) UwU")
        admin_panel(play)
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