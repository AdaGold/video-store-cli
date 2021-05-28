import requests

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_stars():
    print("\n**************************\n")

def list_options():
    options = {
        "1": "I am an Employee", 
        "2": "I am a Customer",
        "3": "I don't want to be in this program anymore"
        }
    for num in options:
        print(f"Option {num}. {options[num]}")
    # print_stars()
    return options

def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        # print("What would you like to do? Select 9 to see all options again")
        choice = input("Make your selection using the option number: ")
    return choice

def list_employee_options():
    print("Thank you for being a valued member of our team!")
    print("What would you like to do?")
    options = {
        "1": "add a video", 
        "2": "edit a video",
        "3": "delete a video",
        "4": "get information about all videos",
        "5": "get information about one video",
        "6": "add a customer", 
        "7": "edit a customer",
        "8": "delete a customer",
        "9": "get information about one customer",
        "10": "get information about all customers",
        "11": "check out a video to a customer",
        "12": "check in a video from a customer",
        "13": "exit this program"
        }
    for num in options:
        print(f"Option {num}. {options[num]}")
    # print_stars()
    return options


def employee_options(play=True):
    employee_option = list_employee_options()
    while play == True:
        employee_choice = make_choice(employee_options, video_store)
        video_store.print_selected()

        if employee_choice == "2":
            for task in task_list.list_tasks():
                print("add later")


        if employee_choice == "13":
            play=False
            print("\nThanks for using the Video Store CLI!")



def customer_options():
    pass




def main(play=True):
    #I wrote URL instead of TaskList. is that right?
    video_store = URL(url="BACKUP_URL")
    print("WELCOME TO RETRO VIDEO STORE")
    print("Please tell us a bit about yourself")
    user_options = list_options()

    while play == True:
        choice = make_choice(user_options, video_store)
        video_store.print_selected()

        if choice == "1":
            employee_options()

        if choice == "2":
            customer_options()

        if choice == "3":
            play=False
            print("\nThanks for using the Video Store CLI!")


if __name__ == "__main__":
    main()