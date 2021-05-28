from datetime import datetime
from customer import print_stars, get_main_menu_choice

# Helper function
def is_int(value):
    try:
        return int(value)
    except ValueError:
        return None

def is_datetime(value):
    try:
        return datetime.strptime(value, "%m/%d/%Y")
    except ValueError:
        return None

# Helper function for video option 3: Select a video
def select_a_video(cvr):
    select_by = input("Would you like to select by title or id? ").lower()
    while select_by != "title" and select_by != "id" :
        select_by = input("Could not select. Please select an option by entering title or id: ").lower()

    if select_by=="title":
        title = input("Which video title would you like to select? ")
        cvr.get_video(title=title)
        if not cvr.selected_video:
            return "Invalid title, could not select." 
    elif select_by=="id":
        id = input("Which video id would you like to select? ")
        if id.isnumeric():
            id = int(id)
            cvr.get_video(id=id)
        if not cvr.selected_video:
            return "Invalid id, could not select." 
    
    return cvr.selected_video

# Select video option
def get_video_choice():
    options = {
        "1": "List all videos", 
        "2": "Create a video",
        "3": "Select a video", 
        "4": "Update a video", 
        "5": "Delete a video", 
        "6": "Delete all videos",
        "7": "Back to main menu"
        }
    
    print("These are the actions you can perform: \n")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    valid_choices = options.keys()
    video_choice = None

    while video_choice not in valid_choices:
        if video_choice != None:
            print("\nInvalid option.")
            video_choice = input("\nMake your selection using valid option number: ")
        else:
            video_choice = input("\nMake your selection using the option number: ")
    
    return video_choice

# Response to selected video option
def respond_video_choice(choice, cvr, main_menu_choice):
    if choice=='1':
        print_stars()
        print("All videos:")
        for video in cvr.list_videos():
            print(video)
    elif choice=='2':
        print("Great! Let's create a new video.")
        title=input("What is the title of your video? ") 
        if not title:
            title = "Default Title"

        release_date=input("What is the release date of your video? Enter mm/dd/yyyy: ")
        if not release_date:
            release_date = None
        else:    
            while not is_datetime(release_date):
                release_date=input("Invalid input, please enter release date of your video in mm/dd/yyyy format: ")

        total_inventory=input("What is the total inventory of your video? ") 
        if not total_inventory:
            total_inventory = 0
        else:
            while not is_int(total_inventory):
                total_inventory=input("Invalid input, please enter a number for the total inventory of your video: ")

        response = cvr.create_video(title=title, release_date=release_date, total_inventory=total_inventory)

        print_stars()
        print("New video:", response)

    elif choice=='3':
        response = select_a_video(cvr)
        if isinstance(response, dict):
            print_stars()
            print("Selected video: ", response)
        else:
            print(response)

    elif choice=='4':
        selected_video = select_a_video(cvr)
        if isinstance(selected_video, dict):
            print(f"Great! Let's update the video: {cvr.selected_video}")
            title=input("What is the new title of your video? ")
            if not title:
                title = selected_video["title"]

            release_date=input("What is the new release_date of your video? Enter mm/dd/yyyy: ")
            if not release_date:
                release_date = selected_video["release_date"]
            else:
                while not is_datetime(release_date):
                    release_date=input("Invalid input, please enter release date of your video in mm/dd/yyyy format: ")

            total_inventory=input("What is the new total_inventory of your video? ")
            if not total_inventory:
                total_inventory = selected_video["total_inventory"]
            else:    
                while not is_int(total_inventory):
                    total_inventory=input("Invalid input, please enter a number for the total inventory of your video: ")

            response = cvr.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("Updated video:", response)
        else:
            print(selected_video)

    elif choice=='5':
        selected_video = select_a_video(cvr)
        if isinstance(selected_video, dict):
            delete_single = input("Are you sure you want to delete this video? Y/N:  ").lower()
            if delete_single == "y":
                cvr.delete_video()
                print_stars()
                print("Video has been deleted.")
                print_stars()
                print("Current videos:")
                for video in cvr.list_videos():
                    print(video)
        else:
            print(selected_video)

    elif choice=='6':
        delete_all = input("Are you sure you want to delete all videos? Y/N:  ").lower()
        if delete_all == "y":
            for video in cvr.list_videos():
                cvr.get_video(id=video['id'])
                cvr.delete_video()

            print_stars()
            print("Deleted all videos.")

    else:
        main_menu_choice = get_main_menu_choice()

    print_stars()

    return main_menu_choice