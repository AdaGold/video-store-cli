from videos import Video
from customers import Customer
from rental import Rental

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def main():
    print("WELCOME TO RETRO VIDEO STORE")
    pass

# if __name__ == "__main__":
#     main()
def print_stars():
    print("**********************************")
# MENU DICTS

MAIN_OPTIONS = {
    "1": "Manage Customers",
    "2": "Manage Videos",
    "3": "Manage Rentals",
    "4": "Quit",
}

CUSTOMER_OPTIONS = {
    "1": "List all customers",
    "2": "Add new customer",
    "3": "View customer details",
    "4": "Edit customer",
    "5": "Delete customer",
    "6": "Main menu",
    "7": "Quit"
}

VIDEO_OPTIONS = {
    "1": "List all vidoes",
    "2": "Add new video",
    "3": "View video details",
    "4": "Edit video",
    "5": "Delete video",
    "6": "Main menu",
    "7": "Quit"
}

RENTAL_OPTIONS = {
        "1": "Check-out video",
        "2": "Check-in video",
        "3": "Main menu",
        "4": "Quit"
    }
### DISPLAY AND CHOOSE FROM MENUS
def choose_from_menu(options, menu_name):
    print(f"{menu_name} Menu:")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do?  ")
        choice = input("Make your selection:   ")
        return choice

def main_menu_to_other(play = True):
    
    while play==True:

        choice = choose_from_menu(MAIN_OPTIONS, "Main")

        if choice=="1":
            customer_route()
        elif choice=="2":
            video_route()
        elif choice =="3":
            rental_route()
        elif choice =="4":
            play = False
            print("BYE!")
        

### CUSTOMER ROUTES
def customer_route(play=True):
    while play == True:

        choice = choose_from_menu(CUSTOMER_OPTIONS, "Customer")

        if choice=="1":
            customer = Customer()
            print(customer.list_customers())
        elif choice=="2":
            customer = Customer()
            print_stars()
            print("create a new customer:")
            print_stars()
            name=input("customer name: ")
            phone=input("customer phone: ")
            postal_code=input("customer postal code:  ")
            response = customer.create_customer(name=name, phone=phone, postal_code=postal_code)
            print_stars()
            print("New Customer Created:", response["id"])
            print_stars()
        elif choice=="3":
            select_customer()
        elif choice=="4":
            selected_customer = select_customer()
            name=input("edit customer name: ")
            phone=input("edit customer phone: ")
            postal_code=input("edit customer postal code:  ")
            response = selected_customer.update_customer(name=name, phone=phone, postal_code=postal_code)
            print_stars()
            print("Edited customer:", response["id"])
            print_stars()
        elif choice=="5":
            selected_customer = select_customer()
            #could add another param here to ensure correct customer was selected before deleting
            response = selected_customer.delete_customer()
            print("Customer deleted", response["id"])
        elif choice=="6":
            choose_from_menu(MAIN_OPTIONS, "Main")
        else:
            play = False

def select_customer():
    customer = Customer()
    select_by = input("select by name or id?:  ")
    if select_by == "name":
        name = input("enter name:  ")
        customer.get_customer(name=name)
        if customer.selected_customer:
            selected_customer = customer.selected_customer
            print(selected_customer)
            return customer
            
    elif select_by == "id":
        id = input("enter id:  ")
        if id.isnumeric():
            id = int(id)
            customer.get_customer(id=id)
            if customer.selected_customer:
                selected_customer = customer.selected_customer
                print(selected_customer)
                return customer
    else:
        print("could not select, please enter name or id")
        select_customer()

###VIDEO ROUTES
def video_route(play=True):
    while play == True:

        choice = choose_from_menu(VIDEO_OPTIONS, "Video")

        if choice=="1":
            video = Video()
            print(video.list_videos())
        elif choice=="2":
            video = Video()
            print_stars()
            print("create a new video:")
            print_stars()
            title=input("video title: ")
            release_date=input("release date: ")
            total_inventory=input("total inventory:  ")
            response = video.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print("New Video Created:", response["id"])
            print_stars()
        elif choice=="3":
            select_video()
        elif choice=="4":
            selected_video = select_video()
            title=input("edit title: ")
            release_date=input("edit release_date: ")
            total_inventory=input("edit total_inventory:  ")
            response = selected_video.update_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print("Edited video:", response["id"])
            print_stars()
        elif choice=="5":
            selected_video = select_video()
            #could add another param here to ensure correct video was selected before deleting
            response = selected_video.delete_video()
            print("Video deleted", response["id"])
        elif choice=="6":
            choose_from_menu(MAIN_OPTIONS, "Main")
        else:
            play = False

def select_video():
    video = Video()
    select_by = input("select by title or id?:  ")
    if select_by == "title":
        title = input("enter title:  ")
        video.get_video(title=title)
        if video.selected_video:
            selected_video = video.selected_video
            print(selected_video)
            return video
            
    elif select_by == "id":
        id = input("enter id:  ")
        if id.isnumeric():
            id = int(id)
            video.get_video(id=id)
            if video.selected_video:
                selected_video = video.selected_video
                print(selected_video)
                return video
    else:
        print("could not select, please enter name or id")
        select_video()

##RENTAL ROUTES
def rental_route(play=True):
    while play == True:

        choice = choose_from_menu(RENTAL_OPTIONS, "Rental")

        if choice=="1":
            rental = Rental()
            print_stars()
            print("create a new rental:")
            print_stars()
            video_id = input("video id:  ")
            customer_id = input("customer id:  ")
            response = rental.check_out(video_id=video_id, customer_id=customer_id)
            print_stars()
            print("New Rental Created due:", response["due_date"])
            print_stars()
        elif choice=="2":
            rental = Rental()
            print_stars()
            print("check-in rental:")
            print_stars()
            video_id = input("video id:  ")
            customer_id = input("customer id:  ")
            response = rental.check_in(video_id=video_id, customer_id=customer_id)
            print_stars()
            print("Rental Returned")
            print_stars()
        elif choice=="3":
            choose_from_menu(MAIN_OPTIONS, "Main")
        else:
            play = False







main_menu_to_other() 