import requests
from VideoStore import VideoStore

URL = "http://localhost:5000"
BACKUP_URL = "https://bp-retro-video-store.herokuapp.com/"


def print_linebreaks():
    print("\n#############################\n")

def main_menu_options(): 
    
    print("1: Video Information")
    print("2: Customer Information")
    print("3: Rental Information")
                


def video_menu_options():
    
    print("1:  List All Videos")
    print("2:  Select A Video To Edit")
    print("3:  Select A Video To Delete")


    
def customer_menu_options():
    customer_menu = {
                "1": "List All Customers",
                "2": "Select A Customer",
                "3": "Edit Selected Customer", 
                "4": "Delete Selected Customer"

    }
    return customer_menu

def rental_menu_options():
    rental_menu = {
                "1": "Check Out A Video", 
                "2": "Check In A Video"
    }
    
def print_video_info(video):
    print("\n")
    print(f"Title: {video['title']}")
    print(f"ID: {video['id']}")
    print(f"Release Date: {video['release_date']}")
    print(f"Total Inventory: {video['total_inventory']}")
    print(f"Available Inventory: {video['available_inventory']}")
    print("\n")



def main():

    print("WELCOME TO RETRO VIDEO STORE")
    print_linebreaks()
    print("PLEASE CHOOSE FROM THE FOLLOWING MENU: ")
    main_menu_options()
    user_input = input("::")
    if user_input == "1":
        video_store = VideoStore()
        print("PLEASE CHOOSE FROM THE FOLLOWING MENU: ")
        video_menu_options()
        video_user_input = input("::")
        if video_user_input == "1":
            all_videos = video_store.get_all_videos()
            for video in all_videos:
                print_video_info(video)

        elif video_user_input == "2":
            user_input = input("Please enter the ID of the video you would like to select:  ")
            selected_video = video_store.get_single_video(id=int(user_input))
            print_video_info(selected_video)
            video_store.edit_single_video(selected_video)

        
        elif video_user_input == "3":
            pass








if __name__ == "__main__":
    main()