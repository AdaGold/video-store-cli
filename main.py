import requests
from video import Video
from rental import Rental
from customer import Customer
import pdb

BACKUP_URL = "http://127.0.0.1:5000"
URL = "https://retro-video-store-api.herokuapp.com"


def stars():
    print("***************************")


##########

def list_options():
    options = {
        "1": "Add a video",
        "2": "Edit a video",
        "3": "Delete a video",
        "4": "Select one video",
        "5": "Get info about all videos",
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Select one customer",
        "10": "Get info about all customers",
        "11": "Check out a video to a customer",
        "12": "Check in a video from customer",
        "13": "List all options",
        "14": "Quit"
    }
    stars()
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    stars()

    print("Note: you must select a video or customer before updating it, deleting it, checking it out, or checking it in.")
    return options


##########

def make_choice(options, video, customer):
    pdb.set_trace()
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all the options again...")
        choice = input("Make your selection using the option number: ")
    if choice in ['2', '3'] and video.selected_video == None:
        print("You must select a video before updating it, deleting it, checking it out, or checking it in.")
        print("Let's select a video!")
        choice = "4"
        return choice
    elif choice in ['7', '8'] and customer.selected_customer == None:
        print("You must select a customer before updating it or deleting it.")
        print("Let's select a customer!")
        choice = "9"
        return choice
    return choice


##########

def main():
    print("WELCOME TO THE VERY LAST BLOCKBUSTER VIDEO IN THE WHOLE WIDE WORLD")

    # initialize task_list
    video = Video(URL)
    customer = Customer(URL)
    rental = Rental(URL)

    # print choices
    options = list_options()

    play = True
    while play == True:

        # get input and validate
        choice = make_choice(options, video, customer)
        # video.print_selected()
        # customer.print_selected()
        stars()

        if choice == '5':
            print("Videos:")
            stars()
            for video in video.list_videos():
                print(video)
        elif choice == '10':
            print("Customers:")
            stars()
            for customer in customer.list_customers():
                print(customer)

        elif choice == '3':
            video.delete_video()
            print("Video has been deleted.")
            print(video.list_videos())
        elif choice == '8':
            customer.delete_customer()
            print("Customer has been deleted.")
            print(customer.list_customers())

        elif choice == '1':
            print("Great! Let's create a new video.")
            title = input("What is the title of your video? ")
            release_date = input("What is the release date of your video? ")
            total_inventory = input(
                "What is the total inventory of your video? ")
            response = video.create_video(
                title=title, release_date=release_date, total_inventory=total_inventory)
            print("New Video:", response["video"])
        elif choice == '6':
            print("Great! Let's create a new customer.")
            name = input("What is the name of your customer? ")
            postal_code = input("What is the postal code of your customer? ")
            phone = input(
                "What is the phone # of your customer? ")
            response = customer.create_customer(
                name=name, postal_code=postal_code, phone=phone)
            print("New Customer:", response["customer"])

        elif choice == '2':
            print(f"Great! Let's update the video: {video.selected_video}")
            title = input("What is the title of your video? ")
            release_date = input("What is the release date of your video? ")
            total_inventory = input(
                "What is the total inventory of your video? ")
            response = video.update_video(
                title=title, release_date=release_date, total_inventory=total_inventory)
            print("Updated video:", response["video"])
        elif choice == '7':
            print(
                f"Great! Let's update the customer: {customer.selected_customer}")
            name = input("What is the name of your customer? ")
            postal_code = input("What is the postal code of your customer? ")
            phone = input(
                "What is the phone # of your customer? ")
            response = customer.update_customer(
                name=name, postal_code=postal_code, phone=phone)
            print("Updated customer:", response["customer"])

        elif choice == '4':
            select_by = input(
                "What would you like to select your video by? Enter title or id: ")
            if select_by == "title":
                title = input("Which video title would you like to select? ")
                video.get_video(title=title)
            elif select_by == "id":
                # pdb.set_trace()
                id = input("Which video id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video.selected_video = video.get_video(id=id)
            else:
                print("Could not select. Please enter id or title.")
            if video.selected_video:
                print("Selected video: ", video.selected_video)
        elif choice == '9':
            select_by = input(
                "What would you like to select the customer by? Enter name or id: ")
            if select_by == "name":
                title = input("What's the customer's name? ")
                customer.get_customer(name=name)
            elif select_by == "id":
                id = input("Which customer id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    customer.get_customer(id=id)
            else:
                print("Could not select. Please enter id or name.")
            if customer.selected_customer:
                print("Selected customer: ", customer.selected_customer)

        elif choice == '11':
            print("Great! Let's check-out a new video.")
            customer_id = input("What is the ID of the customer today? ")
            video_id = input(
                "What is the ID of the video that will be checked out? ")
            response = rental.check_out(
                customer_id=customer_id, video_id=video_id)
            print("Enjoy your new video! Might I suggest just using Netflix next time so we can finally go out of business?")

        elif choice == '12':
            print("Great! Let's check-in your used video.")
            customer_id = input("What is the ID of the customer today? ")
            video_id = input(
                "What is the ID of the video that will be checked in? ")
            response = rental.check_in(
                customer_id=customer_id, video_id=video_id)
            print("Thank you now please leave...")

        elif choice == '13':
            list_options()
        elif choice == '14':
            play = False

        stars()


##########

if __name__ == "__main__":
    main()
