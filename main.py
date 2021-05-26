import requests
from customer import Customer
from video import Video
from rental import Rental
from datetime import datetime, timedelta, date
from ascii import *

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def display(statement):
    print(statement)

def main():
    # print("WELCOME TO RETRO VIDEO STORE")
    display(TITLE)
    run_cli()

def print_stars():
    print("\n**************************\n")

def list_options():
    options = {
        "1": "To manage customers, type 1",
        "2": "To manage videos, type 2",
        "3": "To manage rentals, type 3",
        "4": "To quit, type 4"
    }

    print("Please choose from the following menu options:")
    display(LINE)

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    display(LINE)
    return options

def make_choices(options):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        display(LINE)
        print("What would you like to do? ")
        choice = input("Make your selections using the option number: ")

    # if choice in ['1', '2', '3', '4']:
    #     # print("You must select an option")
    #     choice = input("You must select an option:")

    return choice

def customer_options():
    options = {
        "1": "To list all Customers, type 1",
        "2": "To see information for one Customer, type 2",
        "3": "To add a new Customer, type 3",
        "4": "To edit a Customer, type 4",
        "5": "To delete a Customer, type 5",
        "6": "To return to the main menu, type 6"
    }
    print("Please choose from the following Customer menu options:")
    display(LINE)

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    display(LINE)
    return options

def handle_customer_choices(customer_choices, customers):
    # List all Customers
    if customer_choices == "1":
        display(LINE)   
        for customer in customers.list_customers():
            print(customer)

    # See information for one Customer
    elif customer_choices == "2":
        select_by = input("Would you like to select by name or id?: ")
        if select_by == "name":
            name = input("What is the name of your customer? ")
            customers.get_customer(name=name)
        elif select_by == "id":
            id = input("What is the id of your customer? ")
            if id.isnumeric():
                id = int(id)
                customers.get_customer(id=id)
        else:
            print("Could not select. Please enter name or id")
        
        if customers.selected_customer:
            display(LINE)
            print("Selected Customer: ", customers.selected_customer)

    # Add a new Customer      
    elif customer_choices == "3":
        print("Let's create a new customer")
        name = input("What is the name of your customer? ")
        postal_code = input("What is postal code of your customer? ")
        phone = input("What is the phone number of your customer? ")
        response = customers.create_customer(name=name,
                                            postal_code=postal_code, 
                                            phone=phone)
        # print("***** cli We're in choice !")
        display(LINE)
        print(f"New customer name: {name} \
                \nPostal Code: {postal_code}\
                \nPhone: {phone}")

    # Edit a Customer
    elif customer_choices == "4":
        # select_by = input("Would you like to select by name or id?: ")

        name = input("What is the name of your customer? ")
        customers.get_customer(name=name)
        # else:
        #     print("Could not select. Please enter name or id")
        
        if customers.selected_customer:
            display(LINE)

            print(f"Let's update the customer {customer.selected_customer}")
            new_name = input("What is the new name of your customer? ")
            postal_code = input("What is the new postal code of your customer? ")
            phone = input("What is the new phone number of your customer? ")
            response = customers.update_customer(name=new_name, 
                                                postal_code=postal_code, 
                                                phone=phone)
            display(LINE)
            print("Customer Updated: ", customers.selected_customer)
            print(f"Updated customer name: {name} \
                    \nPostal Code: {postal_code} \
                    \nPhone: {phone}")
        else:
            display(LINE)
            print("There is no customer by that name. Try again. ")

    # Delete a Customer
    elif customer_choices == "5":
        select_by = input("Would you like to select by name or id?: ")
        if select_by == "name":
            name = input("What is the name of your customer? ")
            customers.delete_customer(name=name)
        elif select_by == "id":
            id = input("What is the id of your customer? ")
            if id.isnumeric():
                id = int(id)
                customers.delete_customer(id=id)
        else:
            print("Could not select. Please enter name or id")

        display(LINE)
        print("Customer has been deleted.")

    # Return to Main menu
    elif customer_choices == "6":
        list_options()

def video_options():
    options = {
        "1": "To list all Videos, type 1",
        "2": "To see information for one Video, type 2",
        "3": "To add a new Video, type 3",
        "4": "To edit a Video, type 4",
        "5": "To delete a Video, type 5",
        "6": "To return to the main menu, type 6"
    }
    print("Please choose from the following Video menu options:")
    display(LINE)

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    display(LINE)
    return options

def handle_video_choices(video_choices, videos):
    # See all Videos
    if video_choices == "1":
        display(LINE)
        for video in videos.list_videos():
            print(video)

    # See information for one Video
    elif video_choices == "2":
        select_by = input("Would you like to select by title or id?: ")
        if select_by == "title":
            title = input("What is the title of your video? ")
            videos.get_video(title=title)
        elif select_by == "id":
            id = input("What is the id of your video? ")
            if id.isnumeric():
                id = int(id)
                videos.get_video(id=id)
        else:
            print("Could not select. Please enter title or id")
        
        if videos.selected_video:
            display(LINE)
            print("Selected Video: ", videos.selected_video)

    # Add a new Video     
    elif video_choices == "3":
        print("Let's create a new video")
        title = input("What is the title of your video? ")
        release_date = input("What is the release date of your video? ")
        total_inventory = input("What is the total inventory for your video ")
        available_inventory = total_inventory
        response = videos.create_video(title=title, 
                                    release_date=release_date, 
                                    total_inventory=total_inventory,
                                    available_inventory=available_inventory)
        # print("***** cli We're in choice !")
        display(LINE)
        print(f"New Video title: {title} \
                \nRelease Date: {release_date}\
                \nTotal Inventory: {total_inventory}\
                \nAvailable Inventory: {available_inventory}")

    # Edit a Customer
    elif video_choices == "4":

        title = input("What is the title of your video? ")
        videos.get_video(title=title)
        #new_release_date = input(f"Update the release date for video {selected_video['id']}:  ")
        #date_time_object= maya.parse(new_release_date).datetime()
        
        if videos.selected_video:
            display(LINE)

            print(f"Let's update the video {video.selected_video}")
            new_title = input("What is the new title of your video? ")
            release_date = input("What is the release date of your video? ")
            total_inventory = input("What is the total inventory? ")
            response = videos.update_video(title=new_title,
                                        release_date=release_date,
                                        total_inventory=total_inventory)
            display(LINE)
            print("Video Updated: ", videos.selected_video)
            print(f"Updated video title: {new_title} \
                    \nRelease Date: {release_date} \
                    \nTotal Inventory: {total_inventory}")
        else:
            display(LINE)
            print("There is no video by that title. Try again. ")

    # Delete a Customer
    elif video_choices == "5":
        select_by = input("Would you like to select by title or id?: ")
        if select_by == "title":
            title = input("What is the title of your video? ")
            videos.delete_video(title=title)
        elif select_by == "id":
            id = input("What is the id of your video? ")
            if id.isnumeric():
                id = int(id)
                videos.delete_video(id=id)
        else:
            print("Could not select. Please enter title or id")

        display(LINE)
        print("Video has been deleted.")

    # Return to Main menu
    elif video_choices == "6":
        list_options()

def rental_options():
    options = {
        "1": "To list all rentals, type 1",
        "2": "To rent a movie to a customer, type 2",
        "3": "To check in a rental, type 3",
        "4": "To return to the main menu, type 4"
    }
    print("Please choose from the following Rental menu options:")
    display(LINE)

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    display(LINE)
    return options

def handle_rental_choices(rental_choices, rentals):
    # See all Rentals
    if rental_choices == "1":
        display(LINE)
        for rental in rentals.list_rentals():
            print(rental)

    # Rent a movie to a customer
    elif rental_choices == "2":
        display(LINE)
        print("To rent a video to a customer please input the following information")
        customer_id = input("Customer ID? \n:: ")
        video_id = input("Video ID? \n:: ")
        
        # print("*** customer id", customer_id, "type ", type(int(customer_id)))
        # print("*** video id", video_id, "type ", type(video_id))
        response = rentals.create_rental(customer_id=int(customer_id), video_id=int(video_id))
        print("*** main response ", response)

        display(LINE)
        print(f"Successfully rented the video. due date is {datetime.today()+timedelta(days=7)}")

    # Check in a rental
    elif rental_choices == "3":
        display(LINE)
        print("To check in a video, please input the following information")
        customer_id = input("Customer ID? \n:: ")
        video_id = input("Video ID? \n:: ")
        
        response = rentals.update_video(customer_id=int(customer_id), video_id=int(video_id))
        print("Updated: ", response)

        display(LINE)
        print("Successfully checked in video")

    # Return to Main menu
    elif video_choices == "6":
        list_options()


def run_cli(play=True):

    customers = Customer(url="https://jen-retro-video-store.herokuapp.com")
    videos = Video(url="https://jen-retro-video-store.herokuapp.com")
    rentals = Rental(url="https://jen-retro-video-store.herokuapp.com")

    options = list_options()

    while play == True:
        choice = make_choices(options)

        if choice == "1":
            display(LINE)

            customer_choices = make_choices(customer_options())
            handle_customer_choices(customer_choices, customers)

        elif choice == "2":
            display(LINE)

            video_choices = make_choices(video_options())
            handle_video_choices(video_choices, videos)

        elif choice == "3":
            display(LINE)

            rental_choices = make_choices(rental_options())
            handle_rental_choices(rental_choices, rentals)

        elif choice == "4":
            play = False

            display(ENDING)



if __name__ == "__main__":
    main()