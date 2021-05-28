import requests
from models.video import Video
from models.customer import Customer
from models.rental import Rental

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
if __name__ == "__main__":
    main()

def print_stars():
    print("\n**************************\n")

def list_options():
    options = {
        "1": "List all videos", 
        "2": "Create a video",
        "3": "Select a video", 
        "4": "Update selected video", 
        "5": "Delete a video", 
        "6": "List all customers",
        "7": "Create a customer",
        "8": "Select a customer",
        "9": "Update a customer",
        "10": "Delete a customer",
        "11": "Check out a video to a customer",
        "12": "Check in a video to a customer",
        "13": "Exit"
        }
    print("What would you like to do?")
    print_stars()
    print("These are the actions you can perform")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    print("You must select a video or customer before altering it.")
    print_stars()

    return options

def make_choice(options, video, customer): 
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do?")
        choice = input("Make your selection using the option number: ")

    if choice in ['4','5'] and video.selected_video == None:
        print("You must select a video before altering or deleting it.")
        choice = "3"
    if choice in ['9','10'] and customer.selected_customer == None:
        print("You must select a customer before altering or deleting it.")
        choice = "8"
    
    return choice

def run_cli():
    video = Video(BACKUP_URL)
    customer = Customer(BACKUP_URL)
    rental = Rental(BACKUP_URL)
    print(f"this is the video: {video}")
    options = list_options()

    play = True
    while play==True:
        choice = make_choice(options, video, customer)
        
        if choice=='1':
            print_stars()
            print("Videos:")
            for vid in video.list_videos():
                print(vid)
        elif choice=='2':
            print("Great! Let's create a new video.")
            title=input("What is the title of your video? ")
            total_inventory=input("What is the total inventory of your video? ")
            video.create_video(title=title, total_inventory=total_inventory)
            print("New video:", title) 
        elif choice=='3':
            id = input("What is the id of the video you like to select? ")
            if id.isnumeric():
                id = int(id)
                video.selected_video = video.get_one_video(id=id) 
            if video.selected_video:
                print("Selected video: ", video.selected_video)
        elif choice=='4':
            print(f"Great! Let's update the video: {video.selected_video}")
            title=input("What is the new title of your video? ")
            total_inventory=input("What is the new total inventory of your video? ")
            release_date= input("What is the release date? (format YYYY-MM-DD) ")
            video.update_video(video_id=video.selected_video["id"], title=title, total_inventory=total_inventory, release_date=release_date)
            print(f"Updated video title: {title}. Updated total inventory: {total_inventory}.")
        elif choice=='5':
            video.delete_video()
            print("Video has been deleted.")
            print(f"These are the remaining videos: ")
            for vid in video.list_videos():
                print(vid)
        elif choice=='6':
            print_stars()
            print("Customers:")
            for person in customer.list_customers():
                print(person)
        elif choice=='7':
            print("Great! Let's create a new customer.")
            name=input("What is the name of your customer? ")
            postal_code =input("What is the customer's postal code? ")
            phone =input("What is the customer's phone number? ")
            customer.create_customer(name=name, postal_code=postal_code, phone=phone)
            print("New customer:", name) 
        elif choice=='8':
            id = input("What is the id of the customer you like to select? ")
            if id.isnumeric():
                id = int(id)
                customer.selected_customer = customer.get_one_customer(id)
            if customer.selected_customer:
                print("Selected customer: ", customer.selected_customer)
        elif choice=='9':
            print(f"Great! Let's update the customer: {customer.selected_customer}")
            name=input("What is the new name of your customer? ")
            postal_code =input("What is the customer's new postal code? ")
            phone =input("What is the customer's new phone number? ")
            customer.update_customer(customer_id=customer.selected_customer["id"], name=name, postal_code=postal_code, phone=phone)
            print(f"Updated customer: {name}.")
        elif choice =='10':
            customer.delete_customer()
            print("Customer has been deleted.")
            print(f"These are the remaining customers: ")
            for person in customer.list_customers():
                print(person)
        elif choice == '11':
            print(f"Great! Let's checkout a video to a customer.")
            video_id =input("Enter the video id: ")
            if video_id.isnumeric():
                video_id = int(video_id)
            video.selected_video = video.get_one_video(video_id)
            print(video.selected_video)

            customer_id=input("Enter customer id: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            
            customer.selected_customer = customer.get_one_customer(customer_id)
            print(customer.selected_customer)

            new_rental = rental.check_out(customer_id=customer_id, video_id=video_id)
            print(f"Rental info: {new_rental}")
            print(f"{video.selected_video['title']} checked out to {customer.selected_customer['name']}")
        elif choice == '12':
            print(f"Great! Let's check in the video.")
            video_id =input("Enter the video id: ")
            if video_id.isnumeric():
                video_id = int(video_id)
            video.selected_video = video.get_one_video(video_id)
            print(video.selected_video)

            customer_id=input("Enter customer id: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            
            customer.selected_customer = customer.get_one_customer(customer_id)
            print(customer.selected_customer)

            rental.check_in(customer_id=customer_id, video_id=video_id)
            print(f"{video.selected_video['title']} checked in from {customer.selected_customer['name']}")
        elif choice=='13':
            play=False


run_cli()







