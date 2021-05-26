from requests.api import options
from video_store import Employee


def print_stars():
    print("\n**************************\n")


def list_actions_on():

    actions_on = {
        "1": "Videos",
        "2": "Customers",
        "3": "Quit"
    }

    print_stars()
    print("Welcome to the Retro Video Store CLI")
    print("Make your choice. You can performe actions on:")
    print_stars()

    for choice_num in actions_on:
        print(f"Action {choice_num}. {actions_on[choice_num]}")

    return actions_on


def list_actions_video():

    actions_video = {
        "1": "Add a video",
        "2": "Edit a video",
        "3": "Delete a video",
        "4": "Get information about all videos",
        "5": "Get information about one video",
        "6": "Quit"
    }

    print_stars()
    print("What would you like to do? Make your choice.")
    print("These are the actions you can perform on Videos:")
    print_stars()

    for choice_num in actions_video:
        print(f"Action {choice_num}. {actions_video[choice_num]}")

    print_stars()

    return actions_video


def list_actions_customer():

    actions_customer = {
        "1": "Add a customer",
        "2": "Edit a customer",
        "3": "Delete a customer",
        "4": "Get information about all customers",
        "5": "Get information about one customer",
        "6": "Check-out a video to a customer",
        "7": "Check-in a video to a customer",
        "8": "Quit"
    }

    print_stars()
    print("What would you like to do? Make your choice.")
    print("These are the actions you can perform on Customers:")
    print_stars()

    for choice_num in actions_customer:
        print(f"Action {choice_num}. {actions_customer[choice_num]}")

    print_stars()

    return actions_customer


def make_choice():
    print_stars()
    choice = input("Make your selection using the option number >> ")
    return choice


def select_video(employee):
    video_id = input("Enter video ID >> ")
    if video_id.isnumeric():
        video_id = int(video_id)
        employee.get_one_video(id=video_id)
    else:
        print("Could not select a video. Please, enter ID.")
    # return selected_video


def run_video_store_cli(active=True):

    employee = Employee()

    group_options = list_actions_on()

    while active:
        choice = make_choice()
        if choice == "1":
            options = list_actions_video()
            choice = make_choice()

            if choice == '1':
                print("Add a video")
                title = input("Enter the video title >> ")
                release_date = input("Enter the video release date >> ")
                total_inventory = input("Enter the video total inventory >> ")
                response = employee.add_video(title=title,
                                              release_date=release_date,
                                              total_inventory=total_inventory)

                print("New video: ", response["title"])

            elif choice == '2':
                print("Edit a video")

            elif choice == '3':
                print("Delete a video")
                print("Select video to delete.")
                select_video(employee)
                response = employee.delete_video()
                print(f"Video with ID {response['id']} has been deleted.")

            elif choice == '4':
                print("Get information about all videos")
                for video in employee.list_all_videos():
                    print(f"""
                         ID: {video["id"]}
                         Title: {video["title"]}
                         Release date: {video["release_date"]}
                         Total inventory: {video["total_inventory"]}
                         Available inventory: {video["available_inventory"]}
                         """)

            elif choice == '5':
                print("Get information about one video")
                print("Select video.")
                select_video(employee)
                print(f"""
                         ID: {employee.selected_video["id"]}
                         Title: {employee.selected_video["title"]}
                         Release date: {employee.selected_video["release_date"]}
                         Total inventory: {employee.selected_video["total_inventory"]}
                         Available inventory: {employee.selected_video["available_inventory"]}
                         """)

            elif choice == '6':
                # Quit
                active = False
                print("\nYou just stopped using the Retro Video Store CLI!")

        elif choice == "2":
            options = list_actions_customer()
            choice = make_choice()

            if choice == '1':
                print("Add a customer")
            elif choice == '2':
                print("Edit a customer")
            elif choice == '3':
                print("Delete a customer")
            elif choice == '4':
                print("Get information about all customers")
            elif choice == '5':
                print("Get information about one customer")
            elif choice == '6':
                print("Check-out a video to a customer")
            elif choice == '7':
                print("Check-in a video to a customer")
            elif choice == '8':
                # Quit
                active = False
                print("\nYou just stopped using the Retro Video Store CLI!")
        else:
            active = False
            print("\nYou just stopped using the Retro Video Store CLI!")


if __name__ == "__main__":
    run_video_store_cli()
