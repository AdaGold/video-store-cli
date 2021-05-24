import requests
from video_store import VideoStore

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def run_cli(play=True):

    video_store = VideoStore(url=URL)

    options = list_options()

    while play == True:

        choice = make_choice(options, video_store)

        if choice == '1':

            print("Ok! Let's record a new video.")
            title=input("What is the title of the movie? ")
            release_date=input("What date was the movie released? ")
            total_inventory=input("How many copies of this movie are being added to the store? ")

            response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print("New video:", response["title"])


    # options = {
    #     "1": "Add a Video", 
    #     "2": "Edit a Video",
    #     "3": "Delete a Video",
    #     "4": "Get all Videos",
    #     "5": "Get One Video",
    #     "6": "Add a Customer",
    #     "7": "Edit a Customer",
    #     "8": "Delete a Customer",
    #     "9": "Get Customer Info for One Customer",
    #     "10": "Get Customer Info for All Customers",
    #     "11": "Check OUT a Video",
    #     "12": "Check IN a Video"
    #     }


    # print("WELCOME TO RETRO VIDEO STORE")
    # print("Select the information you want to interact with: ")
    # for choice_num in options:
    #     print(f"Option {choice_num}. {options[choice_num]}")
    
    # choice = input
    # response = requests.get(URL + "/videos")
    # print(response.json())


# if __name__ == "__main__":
#     main()


def list_options():

    options = {
        "1": "Add a Video", 
        "2": "Edit a Video",
        "3": "Delete a Video",
        "4": "Get all Videos",
        "5": "Get One Video",
        "6": "Add a Customer",
        "7": "Edit a Customer",
        "8": "Delete a Customer",
        "9": "Get Customer Info for One Customer",
        "10": "Get Customer Info for All Customers",
        "11": "Check OUT a Video",
        "12": "Check IN a Video",
        "13": "QUIT"
        }
    
    print("WELCOME TO RETRO VIDEO STORE")
    print("These are the actions you can perform: ")

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    
    return options


def make_choice(options, video_store):

    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do?")
        choice = input("Make your selection using the option number: ")

    # if choice in ['4','5','6','7'] and task_list.selected_task == None:
    #     print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
    #     print("Let's select a task!")
    #     choice = "3"
    
    return choice


def video_options():
    pass

def customer_options():
    pass

def rental_options():
    pass 

run_cli()