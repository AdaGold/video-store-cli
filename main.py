# import requests
from video_list import VideoList
from customer_list import CustomerList
from rental_list import RentalList


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def main():
    print("WELCOME TO RETRO VIDEO STORE")
    pass

if __name__ == "__main__":
    main()


def print_stars():
    print("\n**************************\n")


def make_choice():

    options = {
        "1": "List all videos",
        "2": "Add a video", 
        "3": "Select a video",
        "4": "Update selected video", 
        "5": "Delete selected video", 
        "6": "List all customers",
        "7": "Add a customer",
        "8": "Select a customer",
        "9": "Update selected customer",
        "10": "Delete selected customer",
        "11": "Check-out video to customer",
        "12": "Check-in video to customer",
        }

    print_stars()
    print("Welcome to Michelle's Retro Video Store CLI")
    print("Please select the action you would like to perform.")
    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    choice = input("Make your selection using the option number: ")
    
    return choice


def select_video(video_list):
    select_by = input("What would you like to search videos by?  Enter either title or id to begin: ")

    if select_by=="title":
        title = input("Please enter the video title you are looking for: ")
        video = video_list.get_video(title=title)
    elif select_by=="id":
        id = int(input("Please enter the video id you are looking for: "))
        video = video_list.get_video(id=id)
    else:
        print("Please enter id or title to specify search.")

    return video


def select_customer(customer_list):
    select_by = input("What would you like to search customers by?  Enter either name or id to begin: ")

    if select_by=="name":
        name = input("Please enter the customer name you are looking for: ")
        customer = customer_list.get_customer(name=name)
    elif select_by=="id":
        id = int(input("Please enter the customer id you are looking for: "))
        customer = customer_list.get_customer(id=id)
    else:
        print("Please enter name or id to specify search query.")

    return customer


def run_cli():

    #initialize lists
    video_list = VideoList(url=URL)
    customer_list = CustomerList(url=URL)
    rental_list = RentalList(url=URL)

    # list choices and get input
    choice = make_choice()

# Customer Related Choices ---------------------------------------------------------------------------

    if choice =='1':
        print_stars()
        for video in video_list.list_videos():
            print(video)

    elif choice=='2':
        print("Let's add a new video to our inventory.")

        title=input("What is the title of the video? ")
        release_date=input("What was the video's release date? ")
        total_inventory=input("How many copies of this video are we adding to inventory? ")

        response = video_list.add_video(title=title, release_date=release_date, total_inventory=total_inventory)

        print_stars()
        print("New video:", response["title"], "has been added to inventory with id", response["id"])

    elif choice=='3':
        video = select_video(video_list)
        
        print_stars()
        print(f"Selected video: {video}") 

    elif choice=='4':
        video = select_video(video_list)

        if video:
            print(f"Great! Let's update the task: {video_list.selected_video}")

            title=input("What is the new title of the selected video? ")
            release_date=input("What is the new release date of the selected video? ")
            total_inventory=input("What is the new inventory of the selected video? ")

            response = video_list.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("Updated video number:", response["id"]) 

    elif choice=='5':
        video = select_video(video_list)
        
        if video:
            if video["available_inventory"] != video["total_inventory"]:
                print("Available inventory does not match total inventory.  There may be customer(s) who are currently renting copies of this video.")
                return

            video_list.delete_video()

            print_stars()
            print("The video has been deleted from inventory.")

# Customer Related Choices ---------------------------------------------------------------------------

    elif choice=='6':
        print_stars()
        for customer in customer_list.list_customers():
            print(customer)

    elif choice=='7': 
        print("Let's register a new customer to our client list.")

        name=input("What is the customer's name? ")
        postal_code=input("What is the customer's postal code? ")
        phone_num=input("What is the customer's phone number? ")

        response = customer_list.add_customer(name=name, postal_code=postal_code, phone_num=phone_num)

        print_stars()
        print("New customer", response["name"], "registered.")

    elif choice=='8':
        customer = select_customer(customer_list)

        print_stars()
        print(f"Selected customer: {customer}")
    
    elif choice=="9":
        customer = select_customer(customer_list)

        if customer:
            if customer_list.selected_customer:
                print(f"Great! Let's update the customer: {customer_list.selected_customer}")
                
                name=input("What is the new name of the selected customer? ")
                postal_code=input("What is the new postal code of the selected customer? ")
                phone_num=input("What is the new phone number of the selected customer? ")

        response = customer_list.update_customer(name=name, postal_code=postal_code, phone_num=phone_num)

        print_stars()
        print("Updated customer number:", response["id"]) 

    elif choice=='10':
        customer = select_customer(customer_list)

        if customer:
        # Note from chats w/Becca & Chris: prompt user to delete each associated rental first (CLI) or delete rentals (instances of CustomerVideoRental) associated with customer (API)
            if customer["videos_checked_out_count"] > 0:
                print("Customer has outstanding videos and cannot be deleted.")
                return

            customer_list.delete_customer()

            print_stars()
            print("The customer has been deleted from inventory.")

# Rental Related Choices ---------------------------------------------------------------------------

    elif choice=='11':
        print("Ready to check-out?")

        customer_id=int(input("What is the id of the customer? "))
        video_id=int(input("What is the id of the video? "))

        response = rental_list.check_out(customer_id=customer_id, video_id=video_id)

        print_stars()
        print("Video checked out.  Due on: ", response["due_date"])

    elif choice=='12':
        print("Checking in a video?")

        customer_id=int(input("What is the id of the customer? "))
        video_id=int(input("What is the id of the video? "))

        response = rental_list.check_in(customer_id=customer_id, video_id=video_id)

        print_stars()
        print("Video checked in.")

run_cli()