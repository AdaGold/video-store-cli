from video import Video
import requests

URL = "http://127.0.0.1:5000" # is this the correct URL for my local API? How does it know to connect?
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_stars():
    print("\n**************************\n")

def main(): # what is this main function supposed to do?
    print_stars()
    print("WELCOME TO RETROWAVE VIDEO")
    print_stars()


if __name__ == "__main__":
    main()

def list_options():

    options = {
        "1": "Add a video",
        "2": "Update a video",
        "3": "Delete a video",
        "4": "Get info about all videos",
        "5": "Get info about one video",
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Get info about one customer",
        "10": "Get info about all customers",
        "11": "Check out video to customer",
        "12": "Check in video from customer",
        "13": "List all options",
        "14": "Quit"
    }

    for choice_num in options:
        print(f"{choice_num}, {options[choice_num]}")

    return options

def make_choice(options, video): # are we inputting the entire file as a parameter here?
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print_stars()
        print(f"What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")

    # if choice in ['2', '3', '5'] and video.selected_task == None:
    #     print("You must select a video before updating, deleting, or viewing it")
    #     choice = '5'

        return choice

def run_cli(play=True):

    # initialize video
    video = Video(url=URL)

    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, video)

        video.print_selected_video()

        # add a video
        if choice=='1':
            print(f"Let's add a video!")
            title=input("Please enter a title: ")
            release_date=input("Please enter a release date: ")
            total_inventory=input("How many copies are there total? ")
            available_inventory=input("How many copies are available? ")
            response = video.add_video(title=title, release_date=release_date,
            total_inventory=total_inventory, available_inventory=available_inventory)

            print("New video created") # add more print info here
        # update a video
        elif choice=='2':
            print(f"Let's update the video: {video.selected_video}")
            title=input("Please enter a new title: ")
            release_date=input("Please enter a new release date: ")
            total_inventory=input("How many copies are there total? ")
            available_inventory=input("How many copies are available? ")
            response = video.update_video(title=title, release_date=release_date,
            total_inventory=total_inventory, available_inventory=available_inventory)

            print_stars()
            print("Updated video") # add more print info here
        # delete a video
        elif choice=='3':
            video.delete_video()

            print_stars()
            print("Video has been deleted")
        # get info about all videos
        elif choice=='4':
            print_stars()
            for video in video.list_videos():
                print(video)
        # get info about one video
        elif choice=='5':
            select_by = input("Would you like to select by? Enter title or id: ")
            if select_by=="title":
                title = input("Which video title would you like to select? ")
                video.get_video(title=title)
            elif select_by=="id":
                video_id = input("Which video id would you like to select? ")
                if video_id.isnumeric():
                    video_id = int(video_id)
                    video.get_video(video_id=video_id)
            else:
                print("Could not select. Please enter id or title.")

            if video.selected_video:
                print_stars()
                print("Selected video: ", video.selected_video)
        # add a customer
        elif choice=='6':
            pass
        # update a customer
        elif choice=='7':
            pass
        # delete a customer
        elif choice=='8':
            pass
        # get info about one customer
        elif choice=='9':
            pass
        # get info about all customers
        elif choice=='10':
            pass
        # check out video to customer
        elif choice=='11':
            pass
        # check in video from customer
        elif choice=='12':
            pass
        # list all options
        elif choice=='13':
            list_options()
        # quit
        elif choice=='14':
            play=False
            print("\nThanks for using Retrowave Video's CLI!")

        print_stars()

run_cli()
