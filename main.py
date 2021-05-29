from video_list import VideoList
from customer_list import CustomerList
from rental_list import RentalList

def print_stars():
    print("\n**************************\n")


def list_options():

    options = {
        "1": "add a video",  # tested and working
        "2": "edit a video",  # tested and working
        "3": "delete a video",  # tested and working
        "4": "get information about all videos",  # tested and working
        "5": "get information about one video",  # tested and working
        "6": "add a customer",  # tested and working
        "7": "edit a customer",  # tested and working
        "8": "delete a customer",  # tested and working
        "9": "get information about one customer",  # tested and working
        "10": "get information about all customers",  # tested and working
        "11": "check out a video to a customer",  # tested and working
        "12": "check in a video from a customer",  # tested and working
        "13": "list all options",  # tested and working
        "14": "Quit"  # tested and working

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
    rental_list = RentalList(url="https://retro-video-store-api.herokuapp.com/")
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
            new_video = video_list.add_video(
                title=title, release_date=release_date, total_inventory=total_inventory)
            print(f"Your video has been created! id is {new_video['id']}")
        elif choice == '2':
            id = input("What is the id of your video? ")

            print(f"Great! Let's update the video with id {id}")
            title = input("What is the new title of your video? ")
            release_date = input(
                "What is the new release_date of your video? ")
            total_inventory = input("What is the new total_inventory?")

            video_list.selected_video = {
                "id": id,
                "title": title,
                "release_date": release_date,
                "total_inventory": total_inventory
            }

            video_list.edit_video()

            print_stars()
            5  # todo: need to get the updated video
            print("Updated video:", video_list.selected_video)

        elif choice == '3':
            id = input("What is the id of your video to delete? ")

            video_list.delete_video(id)

            print_stars()
            print("video has been deleted.")

            print_stars()
            print(video_list.list_video())

        elif choice == '4':
            print_stars()
            print("Getting all videos:")
            print(video_list.list_video())

        elif choice == '5':
            id = input("Which video id would you like to select? ")
            if id.isnumeric():
                id = int(id)
            video_list.selected_video = video_list.get_video(id=id)
            if video_list.selected_video:
                print_stars()
                print("Selected video: ", video_list.selected_video)
            else:
                print("can't find video")

        elif choice == '6':
            print("Great! Let's add a new customer.")
            name = input("What is the name of your customer? ")
            postal_code = input("What is the postal_code of your customer? ")
            phone = input(
                "What is the phone of your customer? ")
            new_customer = customer_list.add_customer(
                name=name, postal_code=postal_code, phone=phone)
            print(f"Your customer has been created! id is {new_customer['id']}")

        elif choice == '7':
            id = input("What is the id of your customer? ")

            print(f"Great! Let's update the customer with id {id}")
            name = input("What is the new name of your customer? ")
            postal_code = input(
                "What is the new postal_code of your customer? ")
            phone = input("What is the new phone?")

            customer_list.selected_customer = {
                "id": id,
                "name": name,
                "postal_code": postal_code,
                "phone": phone
            }

            customer_list.edit_customer()

            print_stars()
            print("Updated customer:", customer_list.selected_customer)

        elif choice == '8':
            id = input("What is the id of your customer to delete? ")

            customer_list.delete_customer(id)

            print_stars()
            print("customer has been deleted.")

            print_stars()
            print(customer_list.list_customer())
        elif choice == '9':
            id = input("Which customer id would you like to select? ")
            if id.isnumeric():
                id = int(id)
            customer_list.selected_customer = customer_list.get_customer(id=id)
            if customer_list.selected_customer:
                print_stars()
                print("Selected customer: ", customer_list.selected_customer)
            else:
                print("can't find customer")
        elif choice == '10':
            print_stars()
            print("Getting all customers:")
            print(customer_list.list_customer())
        elif choice == '11':
            customer_id = input("Which customer id would you like to select? ")
            video_id = input("Which video id would you like to select? ")
            print(rental_list.check_out(customer_id,video_id))
        elif choice == '12':
            customer_id = input("Which customer id would you like to select? ")
            video_id = input("Which video id would you like to select? ")
            print(rental_list.check_in(customer_id,video_id))
            
        elif choice == '13':
            list_options()
        elif choice == '14':
            play = False
            print("\nThanks for using the Video List CLI!")

        print_stars()


run_cli()
