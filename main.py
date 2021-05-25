import requests
from video_list import VideoList
from customer_list import CustomerList
from rental_list import RentalList

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    pass


if __name__ == "__main__":
    main()


def print_stars():
    print("\n**************************\n")

def list_options():

    options = {
        "1": "List all videos", # done (4)
        "2": "Add a video", # done (1)
        "3": "Select a video", # need to look further into get_video (5) 
        "4": "Update selected video", # done (2)
        "5": "Delete selected task", # done (3)
        "6": "Mark selected task complete",
        "7": "Mark selected task incomplete",
        "8": "Delete all tasks",
        "9": "List all options",
        "10": "Quit"
        }

    print_stars()
    print("Welcome to Michelle's Retro Video Store CLI")
    print("Please select the action you would like to perform.")
    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options, video_list):
    valid_choices = options.keys()
    # choice = None

    # while choice not in valid_choices:
    # print("What would you like to do? Select 9 to see all options again")
    choice = input("Make your selection using the option number: ")

    # if choice in ['4','5','6','7'] and task_list.selected_task == None:
    #     print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
    #     print("Let's select a task!")
    #     choice = "3"
    
    return choice

def run_cli(play=True):

    #initialize video_list
    video_list = VideoList(url=URL)
    
    # print choices
    options = list_options()

    # while play==True:

        # get input and validate
    choice = make_choice(options, video_list)

    # video_list.print_selected()

    if choice =='1':
        print_stars()
        for video in video_list.list_videos():
            print(video)

    elif choice=='2':
        print("Let's add a new video to our inventory.")
        title=input("What is the title of the video? ")
        release_date=input("What was the video's release date? ")
        total_inventory=input("How many copies of this video are we adding to inventory? ")

        response = video_list.add_video(title=title, release_date=release_date, total_inventory=total_inventory)

        print_stars()
        print("New video:", response["title"], "has been added to inventory with id", response["id"])

    elif choice=='3':
        select_by = input("What would you like to search videos by?  Enter either title or id to begin: ")

        if select_by=="title":
            title = input("Please enter the video title you are looking for: ")
            video_list.get_video(title=title)
        elif select_by=="id":
            id = input("Please enter the video id you are looking for: ")
            # if id.isnumeric():
            id = int(id)
            video_list.get_video(id=id)
        else:
            print("Video not found.  Please enter a different id or title.")
        
        if video_list.selected_video:
            print_stars()
            print("Selected task: ", video_list.selected_video)

    elif choice=='4':
        select_by = input("What would you like to search videos by?  Enter either title or id to begin: ")

        if select_by=="title":
            title = input("Please enter the video title you are looking for: ")
            video_list.get_video(title=title)
        elif select_by=="id":
            id = input("Please enter the video id you are looking for: ")
            # if id.isnumeric():
            id = int(id)
            video_list.get_video(id=id)
        else:
            print("Video not found.  Please enter a different id or title.")

        print(f"Great! Let's update the task: {video_list.selected_video}")

        title=input("What is the new title of the selected video? ")
        release_date=input("What is the new release date of the selected video? ")
        total_inventory=input("What is the new inventory of the selected video? ")

        response = video_list.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

        print_stars()
        print("Updated video number:", response["id"], "to", response["title"]) 

    elif choice=='5':
        # id = input("Please enter the id of the video you would like to delete: ")
        # # video_to_delete = video_list.get_video(id=id)
        select_by = input("What would you like to search videos by?  Enter either title or id to begin: ")

        if select_by=="title":
            title = input("Please enter the video title you are looking for: ")
            video_list.get_video(title=title)
        elif select_by=="id":
            id = input("Please enter the video id you are looking for: ")
            # if id.isnumeric():
            id = int(id)
            video_list.get_video(id=id)
        else:
            print("Video not found.  Please enter a different id or title.")

        video_list.delete_video()

        print_stars()
        print("The video has been deleted from inventory.")

run_cli()