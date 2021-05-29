import requests
from video_store import Video_store

#URL = "http://localhost:5000"
URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    pass


if __name__ == "__main__":
    main()

def print_stars():
    print("\n**************************\n")

def list_options():

    options = {
        "1": "List all videos in stock", 
        "2": "Create a new video record",
        "3": "Select a video", 
        "4": "Update selected video", 
        "5": "Delete selected video", 
        "6": "Delete all videos in stock",
        "7": "List all options",
        "8": "Quit",
        "9": "Rent out a video",
        "10": "Return a video"
        }

    print_stars()
    print("Welcome")
    print("These are the actions you can perform")
    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 7 to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['4','5'] and video_store.selected_video == None:
        print("You must select a video before updating it, deleting it, checking it out, or checking back in.")
        print("Let's select a video!")
        choice = "3"
    
    return choice

def run_cli(play=True):

    #initialize video
    video_store = Video_store(URL) ##put url here if you can't find it ya silly
    
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, video_store)

        #video_store.print_selected()

        if choice=='1':
            print_stars()
            for video in video_store.list_videos():
                print(video)

        elif choice=='2':
            print("Great! Let's create a new video.")
            title=input("What is the name of the video? ")
            release_date=input("When was this movie released?")
            total_inventory=input("How many copies of this video are we adding?")
            response = video_store.create_video(title=title, release_date=release_date, total_inventory= total_inventory)

            print_stars()
            print("New video:", response)

        elif choice=='3':
            select_by = input("Would you like to select by? Enter title or id: ")
            if select_by=="title":
                title = input("Which title would you like to select? ")
                video_store.get_video(title=title)
            elif select_by=="id":
                video_id = input("Which video id would you like to select? ")
                if video_id.isnumeric():
                    video_id = int(video_id)
                    video_store.get_video(video_id=video_id)
            else:
                print("Could not select. Please enter id or title.")
            
            if video_store.selected_video:
                print_stars()
                print("Selected video: ", video_store.selected_video)
        
        elif choice=='4':
            print(f"Great! Let's update the movie: {video_store.selected_video}")
            title=input("What is the title of your new video? ")
            release_date=input("When was it released?")
            total_inventory=input("How many copies do you have available to add to stock?")
            response = video_store.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("video:", response)
        elif choice=='5':
            video_store.delete_video()

            print_stars()
            print("Movie has been deleted.")

            print_stars()

        elif choice=='6':
            for video in video_store.list_videos():
                video_store.get_video(video_id=video['id'])
                video_store.delete_video()

            print_stars()
            print("Deleted all videos in stock. Out with the old.")

        elif choice=='7':
            list_options()

        elif choice=='8':
            play=False
            print("\nThanks!")

        elif choice =='9':
            customer_id = input("Which customer is renting today? (please provide customer id)")
            video_id = input("Which video would they like to rent? (please provide video id)" )
            response = video_store.check_out_video(int(customer_id), int(video_id))
            print(response) 
            print_stars()

        elif choice =='10':
            customer_id = input("Which customer is returning today? (please provide customer id)")
            video_id = input("Which video are they returning? (please provide video id)")
            response = video_store.check_in_video(int(customer_id), int(video_id))
            print(response) 
            print_stars()


        print_stars()


run_cli()

