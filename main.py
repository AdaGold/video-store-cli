from video_list import VideoList
from customer_list import CustomerList


def print_stars():
    print("\n**************************\n")


def list_options():

    options = {
        "1": "add a video",  # tested and working
        "2": "edit a video", # tested and working
        "3": "delete a video",
        "4": "get information about all videos",  # tested and working
        "5": "get information about one video",  # todo
        "6": "add a customer",  # todo
        "7": "edit a customer",  # todo
        "8": "delete a customer",  # todo
        "9": "get information about one customer",  # todo
        "10": "get information about all customers",  # todo
        "11": "check out a video to a customer",  # todo
        "12": "check in a video from a customer",  # todo
        "13": "list all options",  # todo
        "14": "Quit"  # todo

    }

    print_stars()
    print("Welcome to the Video List CLI")
    print("These are the actions you can perform")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options, video_list):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to wacth? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")

    return choice


def run_cli(play=True):

    # initialize task_list
    # task_list = TaskList(url="https://beccas-task-list-c15.herokuapp.com/")
    customer_list = CustomerList(
        url="https://retro-video-store-api.herokuapp.com/")
    video_list = VideoList(url="https://retro-video-store-api.herokuapp.com/")

    # print choices
    options = list_options()

    while play == True:

        # get input and validate
        choice = make_choice(options, video_list)

        video_list.print_selected()

        if choice == '1':
            print("Great! Let's add a new video.")
            title = input("What is the title of your video? ")
            release_date = input("What is the release_date of your video? ")
            total_inventory = input(
                "What is the total_inventory of your video? ")
            video_list.add_video(
                title=title, release_date=release_date, total_inventory=total_inventory)

        elif choice == '2':
            id = input("What is the id of your video? ")

            print(f"Great! Let's update the video with id {id}")
            title = input("What is the new title of your video? ")
            release_date = input("What is the new release_date of your video? ")
            total_inventory = input("What is the new total_inventory?")

            video_list.selected_video = {
                "id": id,
                "title": title,
                "release_date": release_date,
                "total_inventory": total_inventory
            }

            video_list.edit_video()

            print_stars()
            
            # todo: need to get the updated video
            print("Updated video:", video_list.selected_video) 
            

        elif choice == '3':
            video_list.delete_video()

            print_stars()
            print("video has been deleted.")

            print_stars()
            print(video_list.list_video())

        elif choice == '4':
            print_stars()
            print("Getting all videos:")
            print(video_list.list_video())

        elif choice == '5':
            select_by = input(
                "Would you like to select by title or id? Enter title or id: ")
            if select_by == "title":
                title = input("Which video title would you like to select? ")
                video_list.get_video(title=title)
            elif select_by == "id":
                id = input("Which video id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video_list.get_video(id=id)
            else:
                print("Could not select. Please enter title or id.")

            if video_list.selected_video:
                print_stars()
                print("Selected video: ", video_list.selected_video)

        elif choice == '6':
            total_inventory = video_list.mark_complete()

            print_stars()
            print("Completed task: ", total_inventory["video"])

        elif choice == '7':
            total_inventory = video_list.mark_incomplete()

            print_stars()
            print("Incomplete task: ", total_inventory["task"])

            list_options()
        elif choice == '14':
            play = False
            print("\nThanks for using the Video List CLI!")

        print_stars()


run_cli()
