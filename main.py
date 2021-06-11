import requests
from customer import Customer
from video import Video

# URL = "http://localhost:5000"
URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


# def main():
#     print("WELCOME TO RETRO VIDEO STORE")
#     pass


def print_stars():
    print("\n**************************\n")


def list_options():


    options = {
        "1": "Create a customer", 
        "2": "Update a customer",
        "3": "Delete a customer",
        "4": "List all customers", 
        "5": "List details for one customer",
        "6": "Create a video", 
        "7": "Update a video",
        "8": "Delete a video",
        "9": "List all videos",
        "10": "List details for one video"
        }

    print_stars()

    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")

    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do?")
        choice = input("Make your selection using the option number: ")

    # if choice in ['4','5','6','7'] and task_list.selected_task == None:
    #     print("You must select a customer before updating it, deleting it, marking it complete, or marking it incomplete.")
    #     print("Let's select a customer!")
    #     choice = "3"
    
    return choice



def run_cli(play=True):

    #initialize 
    customer = Customer(url="https://localhost:5000/customers")
    video = Video(url="https://localhost:5000/videos")

    while play==True:

        # print choices
        options = list_options()
        choice = make_choice(options)

        # create a customer
        if choice == "1":
            print("Great! Let's create a new customer.")
            name = input("What is the customer's name? ")
            postal_code = input("What is the customer's postal code? ")
            phone_number = input("What is the customer's phone number? ")

            response = customer.create_customer(customer_name=name, postal_code=postal_code, phone_number=phone_number)
            print_stars()
            print("New task:", response["customer"])

        # update a customer
        elif choice == "2":
            print("Updating customer.")
            name = input("Enter the customer's updated name. ")
            postal_code = input("Enter the customer's updated postal code. ")
            phone_number = input("Enter the customer's updated phone number. ")

            response = customer.update_customer(customer_name=name, postal_code=postal_code, phone_number=phone_number)
            print_stars()

        # delete a customer
        elif choice == "3":
            response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
            self.selected_customer = None
            return response.json()

        # list all customers 
        elif choice == "4":
            print_stars()
            for customer in customer.all_customers():
                print(customer)

        # list details on one customer 
        elif choice == "5":
            print("Which customer's details would you like to view? ")
            customer_id = input("Enter the customer ID or name. ")
            if customer_id == "name":
                name = input("which customer name would you like to select? ")
                customer.get_specific_customer(name=name)
            elif customer_id == "id":
                id = input("Which customer ID would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    customer.get_specific_customer(id=id)
            else:
                print("Could not select. Please enter ID or title. ")
            
            if customer.selected_customer:
                print("Select:", customer.selected_customer)

            print_stars()


        # create a video
        if choice == "6":
            print("Great! Let's create a new video.")
            title = input("What is the video's title? ")
            release_date = input("What is the video's release date? ")
            total_inventory = input("What is the video's total inventory? ")

            response = video.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print("New video:", response["video"])

        # update a video
        elif choice == "7":
            print("Updating video. ")
            title = input("Enter the video's name. ")
            release_date = input("Enter the release date. ")
            total_inventory = input("Enter the total inventory. ")

            response = video.update_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()

        # delete a video
        elif choice == "8":
            response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
            self.selected_video = None
            return response.json()

        # list all videos 
        elif choice == "9":
            print_stars()
            for video in video.all_videos():
                print(video)

        # list details on one video 
        elif choice == "10":
            print("Which video's details would you like to view? ")
            video_id = input("Enter the video ID or title. ")
            if video_id == "title":
                name = input("which title name would you like to select? ")
                video.get_specific_video(title=title)
            elif video_id == "id":
                id = input("Which video ID would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video.get_specific_video(id=id)
            else:
                print("Could not select. Please enter ID or title. ")
            
            if video.selected_video:
                print("Select:", video.selected_video)

            print_stars()

run_cli()