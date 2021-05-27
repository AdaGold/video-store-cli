import requests
from video_requests import VideoRequests

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    pass


if __name__ == "__main__":
    main()

def list_user_options():
    options = {
        1: "List all options",
        2: "Quit",
        #video requests
        3: "List all videos",
        4: "Select a video",
        5: "List total video inventory for store",
        6: "List total inventory for a specific video",
        7: "Add a Video",
        8: "Edit a Video",
        9: "Delete a video",
        #customer requests options
        10: "List all customers",
        11: "Select a customer",
        12: "Add a customer account",
        13: "Edit customer information",
        14: "Delete customer account",
        15: "Get information about a specific customer",
        16: "Get information about all customer accounts",
        #rental requests
        17: "Check out a video to a customer",
        18: "Check in a video to a customer",
    }

    main()
    print("These are the actions you can perform")

    for option_num in options:
        print(f"Option {option_num}. {options[option_num]}")

        return options  

def user_selects_option(options, video_requests):
    valid_selection = options.keys()
    user_selection = None

    while user_selection not in valid_selection:
        print("Please select an option, enter option 1 to see all options again")
        
        user_selection = input("Please enter the option number of the action you would like to take: ")
    
    if user_selection in [3, 4] and video_requests.videos == None:
        print("You must first select a video by entering option 3, before you can edit or delete it.")
        print("Please select a task: ")
        user_selection = "3"
    
    return user_selection


def cli_go(play=True):

    #initialize video_requests
    video_requests = VideoRequests(url="http://video-retro.herokuapp.com/")

    #print options
    options = list_user_options()

    while play == True:

        #get input and valifate
        selection = user_selects_option(options, video_requests)
        video_requests.print_video()

        #Actions for options

        if selection == '1': #list all options
            list_user_options()

        elif selection == '2': #quit
            play==False
            print("Back to the dull life of streaming!")
        
        elif selection == '3': #"List all videos"
            for video in video_requests.list_all_videos():
                print(video)
        
        elif selection == '4': #"Select a video"
            selection_method = input("You can select a video by title or id.\n If you would like to select by title, type 'title'. If you would like to select by id, type, 'id': ")
            if selection_method == "title":
                title = input("Please enter the title of the video you would like to select: ")
                video_requests.get_specific_video(title=title)
            elif selection_method == "id":
                id = input("Please enter the id of the video you would like to select: ")
                if id.isnumeric():
                    id = int(id)
                    video_requests.get_specific_video(id=id)
            else:
                print("Selection error, please enter 'id' or 'title' to make your selection.")

        elif selection == '5': #"List total video inventory for store"
            pass

        elif selection == '6': #"List total inventory for a specific video"
            pass

        elif selection == '7': #"Add a video"

            print("Yay a new video to add to the inventory!")
            title = input("Enter the title of the video: ")
            release_date = input("Enter the release date in yyyy-mm-dd format: ")
            total_inventory = input("Enter the total inventory for this video: ")
            response = video_requests.create_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print("New video:", response["video"])

        


