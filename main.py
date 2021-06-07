import requests
from videos_list import VideoList
from customer_list import CustomerList
from rentals_list import RentalList

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def main():
    print("WELCOME TO RETRO VIDEO STORE")
    response = requests.get(BACKUP_URL)


def print_stars():
    print("\n**************************\n")


def valid_entry_customer(customer_list, select_by):
    if select_by == "name":
        name = input("Which customer name would you like to select? ")
        return customer_list.get_customer(name=name)
    elif select_by == "id":
        id = input("Which customer id would you like to select? ")
        if id.isnumeric():
            id = int(id)
            return customer_list.get_customer(id=id)
    else:
        print("Could not select. Please enter id or title.")


def valid_entry(video_list, select_by):
    if select_by == "title":
        title = input("Which video title would you like to select? ")
        return video_list.get_video(title=title)
    elif select_by == "id":
        id = input("Which video id would you like to select? ")
        if id.isnumeric():
            id = int(id)
            return video_list.get_video(id=id)
    else:
        print("Could not select. Please enter id or title.")


def select_video(video_list):
    select_by = input("Would you like to select by? Enter title or id: ")
    result = valid_entry(video_list, select_by)
    if result:
        if result == "Could not find customer by that name or id":
            select_video(video_list)
        else:
            video_list.selected_video = result
            print_stars()
            print("Selected video: ", video_list.selected_video)
    else:
        select_video(video_list)


def select_customer(customer_list):
    select_by = input("Would you like to select by? Enter name or id: ")
    result = valid_entry_customer(customer_list, select_by)
    if result:
        if result == "Could not find customer by that id or title.":
            select_customer(customer_list)
        else:
            customer_list.selected_customer = result
            print_stars()
            print("Selected customer: ", customer_list.selected_customer)
    else:
        select_customer(customer_list)


def list_options():

    options = {
        "1": "List all videos",
        "2": "Create a video",
        "3": "Update selected video",
        "4": "Delete selected video",
        "5": "Select a video",
        "6": "List all customers",
        "7": "Create a customer",
        "8": "Update selected customer",
        "9": "Delete selected customer",
        "10": "Select a customer",
        "11": "Check out a video to a customer",
        "12": "Check in a video from a customer",
        "13": "List all options",
        "14": "Quit"
    }

    print_stars()
    print("Welcome to the Retro Video Store CLI")
    print("These are the actions you can perform")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options, video_list, customer_list, rentals_list):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 14 to see all options again")
        choice = input("Make your selection using the option number: ")
    return choice


def run_cli(play=True):

    # initialize video_list, customer_list, and rental_list
    video_list = VideoList(url=BACKUP_URL)
    customer_list = CustomerList(url=BACKUP_URL)
    rentals_list = RentalList(url=BACKUP_URL)
    # print choices
    options = list_options()

    while play == True:

        # get input and validate
        choice = make_choice(options, video_list, customer_list, rentals_list)

        video_list.print_selected()
        customer_list.print_selected()
        # rentals_list.print_selected()
        if choice == '1':
            print_stars()
            print("Here is all the videos we have")
            for video in video_list.list_videos():
                print(video)
        elif choice == '2':
            print("Great! Let's create a new video.")
            title = input("What is the title of your video? ")
            release_date = input("What is the release date of your video? ")
            total_inventory = input(
                "What is the total inventory of your video? ")
            response = video_list.create_video(
                title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("New video has been created:", response)

        elif choice == '3':
            if not video_list.selected_video:
                print("You must select a video you want to update")
                print("Let's select a video!")
                select_video(video_list)
            update=input(f"Currely selected video is {video_list.selected_video}, is this the video you want to update?y/n ")
            if update == "n":
                select_video(video_list)
            print(f"Great! Let's update the video: {video_list.selected_video}")
            title = input("What is the new title of your video? ")
            release_date = input(
                "What is the new release_date of your video? ")
            total_inventory = input(
                "What is the new total_inventory of your video? ")
            response = video_list.update_video(
                title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("Video has been updated:", response)
        elif choice == '4':
            select_video(video_list)
            if not video_list.selected_video:
                print("You must select a video you want to delete")
                select_video(video_list)
            print(video_list.delete_video().text)

            print_stars()
            print("Video has been deleted.")

            print_stars()

        elif choice == '5':
            select_video(video_list)
        elif choice == '6':
            print_stars()
            for customer in customer_list.list_customers():
                print(customer)
        elif choice == '7':
            print("Great! Let's create a new customer.")
            name = input("What is the name of the customer? ")
            postal_code = input("What is the postal code of the cutomer? ")
            phone = input("What is the phone number of the customer? ")
            response = customer_list.create_customer(
                name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("A New Customer has been Created:", response)

        elif choice == '8':
            if not customer_list.selected_customer:
                print("You must select customer you want to update")
                print("Let's select a customer!")
                select_customer(customer_list)
            update=input(f"Currely selected customer is {customer_list.selected_customer}, is this the customer you want to delete?y/n ")
            if update == "n":
                select_customer(customer_list)
            print( f"Great! Let's update customer selected: {customer_list.selected_customer}")
            name = input("What is the new name of the customer? ")
            postal_code = input("What is the new postal code of the customer? ")
            phone = input("What is the new phone number of the customer? ")
            response = customer_list.update_customer(
                name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("Customer has been updated:", response)
        elif choice == '9':
            customer_list.delete_customer()
            if not customer_list.selected_customer:
                print("You must select customer to delete")
                select_customer(customer_list)
            update=input(f"Currely selected customer is {customer_list.selected_customer}, is this the customer you want to delete?y/n ")
            if update == "n":
                select_customer(customer_list)
            # if customer_list.selected_customer == None:
            #     return "Could not find customer by that name or id"
            # select_customer(customer_list)

            customer_list.delete_customer()

            print_stars()
            print("Customer has been deleted.")

            print_stars()

        elif choice == '10':
            select_customer(customer_list)

            print_stars()

        elif choice == '11':
            print("Great! Let's check out a video to a customer.")
            customer = get_customer(customer_list)
            video = get_video(video_list)
            response = rentals_list.check_out_video(
                customer_id=customer["id"], video_id=video["id"])

        elif choice == '12':
            print("Great! Let's check in a video from a customer.")
            customer = get_customer(customer_list)
            video = get_video(video_list)
            response = rentals_list.check_in_video(
                customer_id=customer["id"], video_id=video["id"])
            print("Video has been check-in")

        elif choice == '13':
            list_options()
        elif choice == '14':
            play = False
            print("\nThank you for using the Retro Video Store CLI!")

        print_stars()


def get_customer(customer_list):
    customer_id_input = input("What is the customer id? ")
    customer = customer_list.get_customer(id=customer_id_input)
    if customer == "Could not find customer by that name or id":
        print("Could not find customer by that id")
        return get_customer(customer_list)
    return customer

def get_video(video_list):
    video_id_input = input("What is the video id? ")
    video = video_list.get_video(id=video_id_input)
    if video == "Could not find video by that name or id":
        print("Could not find video by that id")
        return get_video(video_list)
    return video
        


if __name__ == "__main__":
    main()

run_cli()
