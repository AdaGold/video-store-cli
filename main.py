import requests
from my_retro_store_operations import CustomerOperations, RentalOperations
from my_retro_store_operations import VideoOperations
import time,sys
from datetime import date, datetime

def print_stars():
    print("\n**********\n")

#progress bar loading animation
def progress_bar(count, total, status=''):
    bar_len = 10
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

def call_bar():
    total = 10
    i = 0
    while i < total:
        i += 1
        progress_bar(i, total, status='Please wait. Loading options for you')
        time.sleep(0.3)
    progress_bar(i, total, status='Loading is complete. Thanks for waiting')

def list_options():
    options = {
        #Video
        "1": "Create a video",
        "2": "Update a video",
        "3": "Delete a video",
        "4": "List all videos",
        "5": "Get one video", 
        #Customer
        "6": "Create a customer",
        "7": "Update a customer",
        "8": "Delete a customer",
        "9": "Select one customer", 
        "10": "List all customers",
        #Rental
        "11": "Check out a video to a customer",
        "12": "Check in a video from a customer",
        #Operations
        "*": "List all options",
        "#": "Quit"
    }
    print_stars()
    print("WELCOME TO RETRO VIDEO STORE")
    print("These are the actions you can perform")
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    print_stars()
    return options

def make_choice(options, customer_operations, video_operations, rental_operations):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        choice = input("Please make your selection using the one of the listed option number: ")

    return choice

def valid_release_date(date_string):
    format = "%m-%d-%Y"

    try:
        datetime.strptime(date_string, format)
        return True 
    except ValueError:
        print("Invalid entry. Please enter date as MM-DD-YYYY")
        return False

url="https://aida-retro-video-store-api.herokuapp.com"

def main(play=True):
    
    print_stars()
    print("... \N{smiling face with smiling eyes} ... WELCOME TO AIDA'S RETRO VIDEO STORE ... \N{hugging face}")
    call_bar()

    customer_operations = CustomerOperations(url)
    video_operations = VideoOperations(url)
    rental_operations = RentalOperations(url)
    options = list_options()

    while play==True:

        choice = make_choice(options, customer_operations, video_operations, rental_operations)

        if choice=='1':
            print("Hashing it out! Let's create a new video!")
            title=input("What is the name of the video: ")
            release_date=input("Please enter a release date: ")
            if valid_release_date(release_date):
                release_date = release_date
            else:
                release_date=input("Please enter a date as (MM-DD-YYYY): ")
                if valid_release_date(release_date):
                    release_date = release_date
                else:
                    print("Oops, your entry is still invalid. Date will be stored as a default current date. You can update it later with option 2")
                    release_date = str(datetime.now())
            total_inventory=input("How many copies are there in total? ")
            call_bar()
            response = video_operations.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print(f"Here is the ID of new video record: {response['id']} ")

        elif choice=='2':
            list_videos = video_operations.get_all_videos()
            for video in list_videos:
                print(f"Video Id: {video['id']}, Video Title: {video['title']}")
            video_id = input("Which video would you like to update? Please enter ID: ")
            if video_id.isnumeric():
                video_id = int(video_id)
                print(f"Great, let's update the video with ID: {video_id}")
                title=input("What is the new title of the movie?  ")
                release_date=input("Please enter a new release date: ")
                if valid_release_date(release_date):
                    release_date = release_date
                else:
                    release_date=input("Please enter a valid new date: ")
                    if valid_release_date(release_date):
                        release_date = release_date
                    else:
                        print("Oops, your entry is still invalid. Date will be stored as a default current date. You can update it later with option 2")
                        release_date = str(datetime.now())
                total_inventory=input("How many copies are there total? ")
                response = video_operations.update_video(video_id, title=title, release_date=release_date,total_inventory=total_inventory)
                print_stars()
                print(f"Successfully updated the video with ID: {response['id']} - title: {response['title']} - release date: {response['release_date']} - inventory: {response['total_inventory']}")
            else:
                print("Id type is integer. Please enter valid id.")

        elif choice=='3':
            list_videos = video_operations.get_all_videos()
            for video in list_videos:
                print(f"Id:{video['id']}, Title:{video['title']}")
            video_id = input("Which video would you like to delete? Please enter ID: ")
            if video_id.isnumeric():
                video_id = int(video_id)
                video_operations.delete_video(video_id)
                print_stars()
                print(f"Success! Video with ID {video_id} has been deleted")
            else:
                print("Id type is integer. Please enter valid id.")

        elif choice=='4':
            print_stars()
            for video in video_operations.get_all_videos():
                print(video)
        elif choice=='5':
            print("Here are the videos:")
            list_videos = video_operations.get_all_videos()
            for video in list_videos:
                print(f"Id: {video['id']}, name: {video['title']}")
            video_id = input("Which video id would you like to select? ")
            if video_id.isnumeric():
                video_id = int(video_id)
                video_operations.selected_video = video_operations.get_one_video(video_id=video_id)
                if video_operations.selected_video:
                    print(f"Selected video: {video_operations.selected_video}")
            else:
                print("Id type is integer. Please enter valid id.")
        
        elif choice=='6':
            print("Splendid! New customer more money! ")
            name=input("What is the name of the customer ")
            postal_code=input("What is the postal code? ")
            phone=input("Please write down a phone number to contact ")
            call_bar()
            response = customer_operations.create_customer(name=name, postal_code=postal_code,phone=phone)
            print_stars()
            print(f"Here is the ID of new customer: {response['id']}")
        elif choice=='7':
            list_customer = customer_operations.get_all_customers()
            for customer in list_customer:
                print(f"Customer Id: {customer['id']}, name: {customer['name']}")
            customer_id = input("Which customer would you like to update? Please enter ID: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                print(f"Great! Let's update the customer with ID: {customer_id}")
                name=input("What is the new name of your customer? ")
                postal_code=input("What is the new postal code of your customer? ")
                phone=input("Please write down a new phone number : ")
                response = customer_operations.update_customer(customer_id, name=name, postal_code=postal_code,phone=phone)
                print_stars()
                print(f"Successfully updated the customer with ID: {response['id']} - name: {response['name']} - postal code: {response['postal_code']} - phone: {response['phone']}")
            else:
                print("Id type is integer. Please enter valid id.")

        elif choice=='8':
            list_customer = customer_operations.get_all_customers()
            for customer in list_customer:
                print(f"Customer Id: {customer['id']}, name: {customer['name']}")
            customer_id = input("Which customer you would like to delete? Please enter ID: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                customer_operations.delete_customer(customer_id)
                print_stars()
                print(f"Customer with ID {customer_id} has been deleted")
            else:
                print("Id type is integer. Please enter valid id.")

        elif choice=='9':
            print("Here are the customers:")
            list_customers = customer_operations.get_all_customers()
            for customer in list_customers:
                print(f"Customer Id: {customer['id']}, name: {customer['name']}")

            customer_id = input("Which customer id would you like to select? ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                customer_operations.selected_customer = customer_operations.get_one_customer(customer_id=customer_id)
                if customer_operations.selected_customer:
                    print(f"Selected customer: {customer_operations.selected_customer}")
            else:
                print("Id type is integer. Please enter valid id.")

        elif choice=='10':
            print_stars()
            for customer in customer_operations.get_all_customers():
                print(customer)
        elif choice=='11':
            customer_id=input("Starting a rental procedure. Please enter a customer id: ")
            video_id=input("Please enter a video id: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            else:
                print("Id type is integer. Please enter valid id.")
            if video_id.isnumeric():
                video_id = int(video_id)
            else:
                print("Id type is integer. Please enter valid id.")
            call_bar()
            response = rental_operations.check_out(customer_id=customer_id, video_id=video_id)
            print(f"*** Calling the shots! Selected video id {video_id} has been checked out! ")
        elif choice=='12':
            customer_id=input("Starting a return procedure. Please enter a customer id: ")
            video_id=input("Please enter a video id: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            else:
                print("Id type is integer. Please enter valid id.")
            if video_id.isnumeric():
                video_id = int(video_id)
            else:
                print("Id type is integer. Please enter valid id.")
            call_bar()
            response = rental_operations.check_in(customer_id=customer_id, video_id=video_id)
            print("Here is the updated return report:", response)
            print(f"*** Thank you customer id {customer_id}! Selected video id {video_id} has been checked in! ***")
        elif choice =='*':
            list_options()
        elif choice=='#':
            play=False
            print("... \N{smiling face with smiling eyes} ... Thanks for using the Retro Video store created by Aida ... \N{winking face}")

        print_stars()

if __name__ == "__main__":
    main()
