# < ------------------------------- ADA PROVIDED --------------------------- >

import requests

# URL = "http://127.0.0.1:5000"
# BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

# def main():
#     print("WELCOME TO RETRO VIDEO STORE")
#     pass




# < ------------------------------- ADA PROVIDED --------------------------- >

from blockbuster import Blockbuster

def main():
    print("WELCOME TO RETRO VIDEO STORE")

    run_cli()


def print_stars():
    print("\n**************************\n")

# < ------------------------------- MAIN OPTIONS --------------------------- >
def list_options():
    options = {
        "1": "Manage Customers",
        "2": "Manage Videos",
        "3": "Manage Rentals",
        "4": "Quit"
    }

    print_stars()
    print("Welcome to the Blockbuster CLI")
    print("Please select an option from the list")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    
    print_stars()
    
    return options

    # < ------------------------------- FUNC TO PRINT OPTIONS --------------------------- >

def make_choice(options):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do?")
        choice = input("Enter the option you want to move forward with: ")

    return choice

# < ------------------------------- CUSTOMER OPTIONS --------------------------- >

def customers_options():
    options = {
        "1": "List ALL customers",
        "2": "View customer details",
        "3": "Add a customer",
        "4": "Edit a customer",
        "5": "Delete a customer",
        "6": "Return to main screen"
    }

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    
    print_stars()
    
    return options

def manage_customer_options(customers_options):
    blockbuster = Blockbuster()
    # List ALL customers
    if customers_options == "1":
        print_stars()
        for customer in blockbuster.all_customers():
            print(f"ID: {customer['id']}")
            print(f"Name: {customer['name']}")
            print(f"Phone: {customer['phone']}")
            print(f"Postal Code: {customer['postal_code']}")
            print(f"Registered: {customer['registered_at']}")
            print(f"Videos Checked Out: {customer['videos_checked_out_count']}")
        print_stars()
    
    # View customer details
    elif customers_options == "2":
        print("Which customer's information would you like to view?")
        customer_id = input("Enter a customer id: ")
        response = blockbuster.single_customer(customer_id)
        print_stars()
        print(f"ID: {response['id']}")
        print(f"Name: {response['name']}")
        print(f"Phone: {response['phone']}")
        print(f"Postal Code: {response['postal_code']}")
        print(f"Registered: {response['registered_at']}")
        print(f"Videos Checked Out: {response['videos_checked_out_count']}")
        print_stars()

    # Add a customer
    elif customers_options == "3":
        print("Adding a new customer?")
        name = input("What is the customer's name? ")
        postal_code = input("Enter the customer's 5 digit postal code: ")
        phone = input("Enter the customer's 10 digit phone number: ")
        response = blockbuster.add_customer(name=name, postal_code=postal_code, phone=phone)
        print_stars()
        print("A new customer has been added to Blockbuster: ")
        print(response)
        print_stars()

    # Edit a customer
    elif customers_options == "4":
        print("Updating a customer?")
        customer_id = input("Enter the customer's id: ")
        name = input("Enter the customer's name: ")
        postal_code = input("Enter the new postal code: ")
        phone = input("Enter the new phone number: ")
        response = blockbuster.edit_customer(customer_id=customer_id, name=name, postal_code=postal_code, phone=phone)
        print_stars()
        print("Customer has been updated: ")
        print(response)
        print_stars()

    # Delete a customer
    elif customers_options == "5":
        print("Deleting a customer?")
        customer_id = input("Enter the customer's id: ")
        blockbuster.delete_customer(customer_id)
        print_stars()
        print("The customer has been deleted")
        print_stars()
    
    elif customers_options == "6":
        list_options()
        print_stars()


# < ------------------------------- VIDEO OPTIONS --------------------------- >

def videos_options():
    options = {
        "1": "List ALL videos", 
        "2": "View video details",
        "3": "Add a video",
        "4": "Edit a video",
        "5": "Delete a video",
        "6": "Return to main screen"
    }

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    
    print_stars()

    # valid_choices = options.keys()
    # choice = None

    # while choice not in valid_choices:
    #     print("What would you like to do?")
    #     choice = input("Enter the option you want to move forward with: ")

    return options

def manage_video_options(video_options):
    blockbuster = Blockbuster()
    # List ALL videos
    if video_options == "1":
        print_stars()
        for video in blockbuster.all_videos():
            print(video)
        print_stars()
    
    # View video details
    elif video_options == "2":
        print("Which video's details would you like to view?")
        video_id = input("Enter the video id: ")
        response = blockbuster.single_video(video_id)
        print_stars()
        print(f"ID: {response['id']}")
        print(f"Title: {response['title']}")
        print(f"Release date: {response['release_date']}")
        print(f"Total inventory: {response['total_inventory']}")
        # print(f"Available: {response['available_inventory']}")
        print_stars()
    
    # Add a video
    elif video_options == "3":
        print("Adding a new video?")
        title = input("Enter the video's title: ")
        release_date= input("Enter the video's release date, (MM/DD/YYYY): ")
        total_inventory = input("Enter the video's total inventory: ")
        # available_inventory = total_inventory
        response = blockbuster.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
        print_stars()
        print("A new video has been added to Blockbuster: ")
        print(response)
        print_stars()
    
    # Edit a video
    elif video_options == "4":
        print("Updating a video?")
        video_id = input("Enter the video id: ")
        title = input("Enter the video's updated title: ")
        release_date= input("Enter the video's updated release date, (MM/DD/YYYY): ")
        total_inventory = input("Enter the video's updated total inventory: ")
        # available_inventory = total_inventory
        response = blockbuster.edit_video(video_id=video_id, title=title, release_date=release_date, total_inventory=total_inventory)
        print_stars()
        print("Video has been updated: ")
        print(response)
        print_stars()
    
    # Delete a video
    elif video_options == "5":
        print("Deleting a video?")
        video_id = input("Enter the video's id: ")
        blockbuster.delete_video(video_id)
        print_stars()
        print("The video has been deleted")
        print_stars()
    
    elif video_options == "6":
        list_options()
        print_stars()


# < ------------------------------- RENTAL OPTIONS --------------------------- >

def rental_options():
    options = {
        "1": "Check-in rental",
        "2": "Check-out rental",
        "3": "Return to main screen"
    }

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    
    print_stars()
    
    return options

def manage_rental_options(rental_options):
    blockbuster = Blockbuster()
    # Check-in rental
    if rental_options == "1":
        print("Checking in a rental?")
        print("We need the customer id and the video id")
        customer_id = input("Enter the customer id: ")
        video_id = input("Enter the video id: ")
        response = blockbuster.check_in(customer_id=customer_id, video_id=video_id)
        print_stars()
        print("The video was checked in!")
        print(response)
        print_stars()
    
    # Check-out rental
    elif rental_options == "2":
        print("What video are we checking out?")
        video_id = input("Enter the video id: ")
        customer_id = input("Enter the customer id checking out the video: ")
        response = blockbuster.check_out(customer_id=customer_id, video_id=video_id)
        print_stars()
        print("The video was checked out!")
        print(response)
        print_stars()
    
    elif rental_options == "3":
        list_options()
        print_stars()

# < ------------------------------- RUN CLI FUNCTION --------------------------- >

def run_cli(play=True):

    # initialize blockbuster
    blockbuster = Blockbuster("https://mn-retro-video-store.herokuapp.com/") 


    while play == True:

        # get input & validate
        options = list_options()
        choice = make_choice(options)
        
        if choice == '1': 
            customer = make_choice(customers_options())
            manage_customer_options(customer)

        elif choice == '2':
            video = make_choice(videos_options())
            manage_video_options(video)   

        elif choice == '3':
            rental = make_choice(rental_options())
            manage_rental_options(rental)

        elif choice == '4':
            play = False
            print("Thank you for visiting Blockbuster!")


if __name__ == "__main__":
    main()