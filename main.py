import requests
from video_store import VideoStore

VIDEO_STORE = VideoStore()

#---------------------# INITIAL OPTIONS #---------------------#

def handle_options(display=False, choice=False):
    options = {
        "0": ["Display Options"],
        "1": ["List all customers", customer_list],
        "2": ["List all videos", video_list],
        "3": ["Add new customer to system", add_customer],
        "4": ["Add new video to system", add_video],
        "5": ["Select a specific customer", customer_selection],
        "6": ["Select a specific video", video_selection],
        "7": ["Check out a video", check_out_rental],
        "8": ["Check in a video", check_in_rental],
        "9": ["List overdue rentals", list_overdue_rentals],
        "10": ["Exit video store"]
        }
    if display:
        print("Here is a list of possible actions:")
        print("")
        for num in options:
            print(f"{num}. {options[num][0]}")
        return options
    if choice:
        options[choice][1]()

def customer_list():
    for customer in VIDEO_STORE.list_customers():
        display_customer(customer)

def video_list():
    for video in VIDEO_STORE.list_videos():
        display_video(video)

def add_customer():
    print("Please enter the following information about the new customer:")
    name = input("Name: ")
    postal_code = input("Postal Code: ")
    phone = input("Phone: ")
    response = VIDEO_STORE.create_customer(name, postal_code, phone)
    print_pattern
    print(f"New customer created: {response['name']}")

def add_video():
    print("Please enter the following information about the new video:")
    title = input("Title: ")
    release_date = input("Release Date: ")
    total_inventory = input("Total Inventory: ")
    response = VIDEO_STORE.create_video(title, release_date, total_inventory)
    print_pattern()
    print(f"New video created: {response['title']}")

def customer_selection():
    if select_customer():
        print_pattern()
        print("Here is your selected customer:")
        display_customer(VIDEO_STORE.current_customer)
        second_choice = make_choice(handle_more_options(display=True))
        if second_choice == "0":
            make_choice(handle_more_options(display=True))
        else:
            handle_more_options(customer=True, choice=second_choice)
    else:
        print_pattern()
        print("Sorry. Customer not found.")

def video_selection():
    if select_video():
        print_pattern()
        print("Here is your selected video:")
        display_video(VIDEO_STORE.current_video)
        second_choice = make_choice(handle_more_options(display=True))
        if second_choice == "0":
            make_choice(handle_more_options(display=True))
        else:
            handle_more_options(video=True, choice=second_choice)
    else:
        print_pattern()
        print("Sorry. Video not found.")
        print 

def check_out_rental():
    # Could do some cleanup here
    print("Which video would you like to check-out?")
    video = select_video()
    print("Which customer should this video be checked out to?")
    customer = select_customer()
    if customer == None or video == None:
        print_pattern()
        print("I'm sorry. The customer or video could not be found.")
    else:
        rental = VIDEO_STORE.checkout_video(customer["id"], video["id"])
        print_pattern()
        if "details" in rental:
            print(rental["details"])
        else:
            print("Video rented successfully!")
            print("")
            display_rental(rental, customer, video)

def check_in_rental():
    print("Which video would you like to check-in?")
    video = select_video()
    print("Which customer is returning this video?")
    customer = select_customer()
    if customer == None or video == None:
        print_pattern()
        print("I'm sorry. The customer or video could not be found.")
    else:
        rental = VIDEO_STORE.checkin_video(customer["id"], video["id"])
        display_rental(rental, customer, video)

#Optional Enhancement
def list_overdue_rentals():
    print("Here is a list of all overdue rentals:")
    overdue_rentals = VIDEO_STORE.get_overdue_rentals()
    for rental in overdue_rentals:
        display_rental(rental, rental, rental)


#---------------------# SECONDARY OPTIONS #---------------------#

def handle_more_options(display=False, customer=False, video=False, choice="5"):
    options = {
        "0":["Display Options"],
        "1": ["Update selection", update_customer, update_video],
        "2": ["Delete Selection", delete_customer, delete_video],
        "3": ["Display current rentals", current_customer_rentals, current_video_rentals],
        "4": ["Display rental history", customer_rental_history, video_rental_history]
        }
    if display:
        print("")
        print("Choose the action you wish to perform on your selection:")
        print("")
        for num in options:
            print(f"{num}. {options[num][0]}")
        return options
    elif customer:
        options[choice][1]()
    elif video:
        options[choice][2]()

def update_video():
    print("Let's update this video! (Enter 'None' for any info you do not want to update)")
    title = input("Enter new video title: ")
    if title.lower() == "none":
        title = None
    release_date = input("Enter new release date: ")
    if release_date.lower() == "none":
        release_date = None
    total_inventory = input("Enter new total inventory: ")
    if total_inventory.lower() == "none":
        total_inventory = None
    print_pattern()
    print("Video successfully modified:")
    display_video(VIDEO_STORE.update_video(title, release_date, total_inventory))

def update_customer():
    print("Let's update this customer! (Enter 'None' for any info you do not want to update)")
    name = input("Enter new customer name: ")
    if name.lower() == "none":
        name = None
    postal_code = input("Enter new postal code: ")
    if postal_code.lower() == "none":
        postal_code = None
    phone = input("Enter new phone #: ")
    if phone.lower() == "none":
        phone = None
    print_pattern()
    print("Customer successfully modified:")
    display_customer(VIDEO_STORE.update_customer(name, postal_code, phone))

def delete_video():
    ans = input("Are you sure you want to delete this video permenantly? (y/n) ")
    if ans == "y":
        print_pattern()
        print(VIDEO_STORE.delete_video()['details'])
    else:
        print("Okay. Let's wait on deleting that.")

def delete_customer():
    ans = input("Are you sure you want to delete this customer permenantly? (y/n) ")
    if ans == "y":
        print_pattern()
        print(VIDEO_STORE.delete_customer()["details"])
    else:
        print("Okay. Let's wait on deleting that.")

#Optional Enhancement
def current_customer_rentals():
    current_rentals = VIDEO_STORE.list_customer_rentals()
    print(f"Videos currently rented to {VIDEO_STORE.current_customer['name']}:")
    for rental in current_rentals:
        print("")
        print(rental["title"])
        print(f"Due Date: {rental['due_date']}")

#Optional Enhancement
def current_video_rentals():
    current_rentals = VIDEO_STORE.list_video_rentals()
    print(f"Customers currently renting '{VIDEO_STORE.current_video['title']}':")
    for rental in current_rentals:
        print("")
        print(rental["name"])
        print(f"Due Date: {rental['due_date']}")

#Optional Enhancement
def customer_rental_history():
    rental_history = VIDEO_STORE.get_customer_rental_history()
    print(f"Videos previously rented to {VIDEO_STORE.current_customer['name']}:")
    for rental in rental_history:
        print("")
        print(rental["title"])
        print(f"Due Date: {rental['due_date']}")
        print(f"Return Date: {rental['check_in_date']}")

#Optional Enhancement
def video_rental_history():
    rental_history = VIDEO_STORE.get_video_rental_history()
    print(f"Customers who previously rented '{VIDEO_STORE.current_video['title']}':")
    for rental in rental_history:
        print("")
        print(rental["name"])
        print(f"Due Date: {rental['due_date']}")
        print(f"Return Date: {rental['check_in_date']}")

#---------------------# HELPER FUNCTIONS #---------------------#

def print_pattern():
    print("")
    print("-----------------------------------------------")
    print("")

def make_choice(options):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        print_pattern()
        print("What action would you like to take?")
        print("(Select '0' to view current options again)")
        choice = input("Please make your selection: ") 
    print_pattern()
    return choice

def display_customer(customer):
    print("")
    print(customer['name'])
    print(f"Postal Code: {customer['postal_code']}")
    print(f"Phone #: {customer['phone']}")
    print(f"Date Registered: {customer['registered_at']}")
    print(f"Videos Out Count: {customer['videos_checked_out_count']}")
    print(f"ID: {customer['id']}")

def display_video(video):
    print("")
    print(video['title'])
    print(f"Release Date: {video['release_date']}")
    print(f"Total Inventory: {video['total_inventory']}")
    print(f"Available Inventory: {video['available_inventory']}")
    print(f"ID: {video['id']}")

def display_rental(rental, customer, video):
    print("")
    print(f"Video Title: {video['title']}")
    print(f"Customer Name: {customer['name']}")
    print(f"Due Date: {rental['due_date']}")
    print(f"Return Date: {rental['check_in_date']}")

def select_video():
    sort = input("Would you like to search by video id or video title?: ").lower()
    valid_sort = False
    while valid_sort == False:
        if sort == "id":
            id = input("Please enter video id: ")
            return VIDEO_STORE.get_video(id=id)
        elif sort == "title":
            title = input("Please enter video title: ")
            return VIDEO_STORE.get_video(title=title)
        else:
            sort = input("Please enter vaild sorting method (id or title): ")

def select_customer():
    sort = input("Would you like to search by customer id, name or phone #?: ")
    sort = sort.lower()
    valid_sort = False
    while valid_sort == False:
        if sort == "id":
            id = input("Please enter customer id: ")
            return VIDEO_STORE.get_customer(id=id,)
        elif sort == "name":
            name = input("Please enter customer name: ")
            return VIDEO_STORE.get_customer(name=name)
        elif sort == "phone":
            phone = input("Please enter customer phone: ")
            return VIDEO_STORE.get_customer(phone=phone)
        else:
            sort = input("Please enter vaild sorting method (id, name, or phone #): ")


#---------------------# RUN CLI #---------------------#
def main(play=True):
    print_pattern()
    print("WELCOME TO RETRO VIDEO STORE")
    print_pattern()
    option_list = handle_options(display=True)
    while play == True:
        choice = make_choice(option_list)
        if choice == "0":
            handle_options(display=True)
        elif choice == "10":
            play = False
            print("Thanks for using the Video Store Interface!")
        else:
            handle_options(choice=choice)

if __name__ == "__main__":
    main()