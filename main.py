import requests
import json

from requests.api import delete
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
        print("Make a choice from the options above. ")
        choice = input("Choose an option: ")
    return choice

def list_options():

    options = {
        "1": "List all Videos", 
        "2": "Single Video Info",
        "3": "Edit Video", 
        "4": "Create Video", 
        "5": "Delete video", 
        "6": "View all CustDUMBers",
        "7": "View one CustDUMBer",
        "8": "Update one CustDUMBer",
        "9": "Remove Customer",
        "10": "Check Out Video",
        "11": "Check In Video",
        "12": "Quit"
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
            elif choice == '4':
                new_title = input("New Title: ")
                new_release_date = input("Release Date: ")
                new_total_inventory = input("Total Inventory: ")
                video_store.create_video(title=new_title, release_date=new_release_date, total_inventory=new_total_inventory)
            elif choice == '5':
                delete_id = input("Video ID: ")
                video_store.delete_video(id=delete_id)
            elif choice=='6':
                for bastard in video_store.all_customers_are_bastards():
                    print(bastard)
                print("Scroll Up To See CustDUMBers")
            elif choice == '7':
                input_id = input("What's the ID number of this person? ")
                chosen_one = video_store.get_custo(id=input_id)
                print("Selected Customer:")
                print(chosen_one)
            elif choice == '8':
                input_id = input("What's the ID of this person'? ")
                new_name = input("The Name: ")
                new_postal_code = input("The Postal Code: ")
                new_phone = input("Phone Number: ")
                video_store.update_custo(id=input_id, name=new_name, postal_code=new_postal_code, phone=new_phone)
            elif choice == '9':
                delete_id = input("Customer ID: ")
                video_store.delete_custo(id=delete_id)
            elif choice == '10':
                print("Check Out")
                custo_id = input("Customer ID: ")
                video_id = input("Video ID: ")
                video_store.check_out(custo_id=custo_id, video_id=video_id)
            elif choice == '11':
                print("Check In")
                custo_id = input("Customer ID: ")
                video_id = input("Video ID: ")
                video_store.check_in(custo_id=custo_id, video_id=video_id)
            elif choice=='12':
                play=False
                print("\nThanks for using the Video Store CLI")




def run_cli(play=True):
    video_store = VideoStore()
    show_users()
    user_choice = input("Make your selection using the option number: ")
    if user_choice == "1":
        print('\n')
        print ("Okay! Lets Get Started!! ;) :) ;) UwU")
        print('\n')
        admin_panel(play, video_store)
    else:
        print ("What do you think you're doing! Get off our computer")
        play = False

if __name__ == "__main__":
    main()
    run_cli()

