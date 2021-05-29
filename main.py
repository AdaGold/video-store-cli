import pprint
from video_store import VideoStore


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

video_store = VideoStore(url=BACKUP_URL)


def run_cli():

    print("WELCOME TO RETRO VIDEO STORE!\n"
          "These are the actions you can perform:")

    while True:
        options = list_options()
        choice = input('Which activity would you like to do? (select the option number): ')
        print() # Linebreak
        if choice not in options.keys():
            print('Invalid option.')
            continue
        if choice == '20':
            break
        if choice in ['4', '5', '6'] and video_store.selected_video == None:
            print("You must select a video before using it in any way")
            print("Let's select a video!")
            choice = "3"
        if choice in ['12', '13'] and video_store.selected_customer == None:
            print("You must selected a customer before using it in any way")
            print("Let's select a customer")
            choice = "9"


        action = options[choice]
        action()


def list_options():

    options = {
        "1": list_videos,
        "2": create_video,
        "3": select_video,
        "4": update_video,
        "5": delete_video,
        "6": checkout_video,
        "7": checkin_video,
        "8": list_customers,
        "9": get_customer_info,
        "10": list_customers_rentals,
        "11": create_customer,
        "12": update_customer,
        "13": delete_customer,
        "20": "Quit"
    }


    print() # Linebreak
    for key, action in options.items():
        action_desc = action if type(action) is str else action.__doc__
        print(f'Option {key}. {action_desc}')
    print()  # Linebreak

    return options


def list_videos():
    """List all videos"""

    print(*video_store.list_videos(), sep='\n')


def create_video():
    """Create a video"""

    print("Great! Let's create a new video.")
    title = input("What is the title of your video? ")
    total_inventory = input("How many copies of this movie are we adding? ")
    release_date = input("What was the movie's release date? ")
    response = video_store.create_video(title=title, total_inventory=total_inventory, release_date=release_date)
    print("New video id:", response["id"])


def select_video():
    """Select a video"""

    select_by = input("In order to select a video, write out title or id:  ")
    if select_by == "title":
        title = input("Which title would you like to select? ")
        video_store.get_video(title=title)
    elif select_by == "id":
        id = input("Which video id would you like to select? ")
        if id.isnumeric():
            id = int(id)
            video_store.get_video(id=id)
    else:
        print("Could not select. Please enter id or title.")
    if video_store.selected_video != None:
        print("Selected video: ", video_store.selected_video)


def update_video():
    """Update selected video"""

    print(f"Great! Let's update the video: {video_store.selected_video}")
    title = input("What is the new title of your video? ")
    release_date = input("What is the release date of your video? ")
    total_inventory = input("What is the new total inventory?")
    response = video_store.update_video(title=title, release_date=release_date, total_inventory=total_inventory)
    print("Updated video:", response)


def delete_video():
    """Delete a selected video"""

    id = input("Enter video id for deletion: ")
    if id.isnumeric():
        id = int(id)
        video_store.delete_video(id=id)
    print(f"Video id {id} has been deleted.")
    pprint.pprint(video_store.list_videos())


def checkout_video():
    """Check out a video"""

    print(f"Great! Let's grab some customer information for rental video: {video_store.selected_video}")
    customer_id = input("What is your id?")
    video_id = input("What is the video_id you want to check out?")
    due_date = input("when is the video due?")
    video_store.check_out_video(customer_id=customer_id, video_id=video_id, due_date=due_date)
    print(f"Customer {customer_id} checked out {video_id}, {due_date}")


def checkin_video():
    """Check in in a video"""

    customer_id = input("what is the customer's id that checked out the video?: ")
    current = video_store.get_customer_rentals(customer_id)
    print(f"Above are the videos customer with ID# {customer_id} has currently checked out.\n"
          f"To check in a video lets collect some info: ")
    video_id = input("What is the id of the video you want to check in?: ")
    video_store.check_in_video(customer_id=customer_id, video_id=video_id)
    print(f"Customer {customer_id} has returned {video_id}")


def list_customers():
    """Get list of customers"""

    print(*video_store.list_customers(), sep='\n')


def get_customer_info():
    """Get info on one customer by ID"""

    id = input("Type out customer's ID ")
    if id.isnumeric():
        id = int(id)
        video_store.get_customer(id)
    else:
        print("Could not find customer with that ID")
    if video_store.selected_customer != None:
        print("Selected customer:", video_store.selected_customer)


def list_customers_rentals():
    """Get customer's rental list"""

    id = input("Type out customer's ID ")
    if id.isnumeric():
        id = int(id)
        video_store.get_customer_rentals(id)

def create_customer():
    """Create a new customer"""
    print("Great! Let's create a new customer!")
    name = input("What is the name of our new customer? ")
    postal_code = input("What is their postal code? ")
    phone = input("What is their phone number? ")
    response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone)
    print("New customer id:", response["id"])

def update_customer():
    """Update customer information"""
    print(f"Great! Let's edit the customer info: {video_store.selected_customer}")
    name = input("What is the new name of this customer? ")
    postal_code = input("What is the new postal code? ")
    phone = input("What is the new phone number? ")
    response = video_store.update_customer(name=name, postal_code=postal_code, phone=phone)
    print("Updated customer info:", response)  

def delete_customer():
    """Delete a customer"""
    id = input("Enter customer id for deletion: ")
    if id.isnumeric():
        id = int(id)
        video_store.delete_customer(id)
    print(f"Customer id {id} has been deleted.")
    pprint.pprint(video_store.list_customers())

if __name__ == "__main__":
    run_cli()
