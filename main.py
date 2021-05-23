from requests.api import options
from video_store import Employee


def print_stars():
    print("\n**************************\n")


def list_actions_on():

    actions_on = {
        "1": "Video",
        "2": "Customer"
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
    choice = input("Make your selection using the option number: ")
    return choice


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
            elif choice == '2':
                print("Edit a video")
            elif choice == '3':
                print("Delete a video")
            elif choice == '4':
                print("Get information about all videos")
            elif choice == '5':
                print("Get information about one video")
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

        # employee.add_video(title="test cli",
        #                    release_date="1981-01-01",
        #                    total_inventory=100)


run_video_store_cli()
