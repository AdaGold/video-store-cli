import requests
from videos import VideoList
from customers import CustomerList

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    

def print_stars():
    print("\n**************************\n")

def list_options():

    options = {
        "1": "List all videos", 
        "2": "Create a new video",
        "3": "Select a single video", 
        "4": "Update a video", 
        "5": "Delete a video", 
        "6": "List all customers",
        "7": "Create a new customer",
        "8": "Select a single customer",

        # list all customers 
        # add customer 
        # select 1 customer 
        # edit customer
        # delete customer

        # check out a video to a customer
        # check in a video from a customer
        
        
        "9": "Select a customer", # list all options 
        "10": "Select all customers", # print("\nThanks for using the Video List CLI!")
        "11": "Check out a video to a customer",
        "12": "Select a customer",
        "13": "List all options",
        "14": "Quit"
        
        }

    print_stars()
    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")
    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options, video_list):
    valid_choices = options.keys()
    choice = None

    # while choice not in valid_choices:
    #     print("What would you like to do? Select 13 to see all options again")
    #     choice = input("Make your selection using the option number: ")

    # if choice in ['4','5','6','7'] and video_list.selected_video == None:
    #     print("You must select a video before updating it, deleting it, marking it complete, or marking it incomplete.")
    #     print("Let's select a video!")
    #     choice = "3"
    
    return choice

def run_cli(play=True):

    #initialize video_list, customer_list
    video_list = VideoList(url=BACKUP_URL)
    customer_list = CustomerList(url=BACKUP_URL)


    # print choices
    options = list_options()   

    while play==True:

        # get input and validate
        choice = make_choice(options, video_list)

        video_list.print_selected()

        if choice=='1':
            print_stars()
            for video in video_list.list_videos():
                print(video)
        elif choice=='2':
            print("Great! Let's create a new video.")
            title=input("What is the title of your video? ")
            description=input("What is the description of your video? ")
            total_inventory=input("How many videos are in the total inventory ")
            response = video_list.create_video(title=title, description=description, total_inventory=total_inventory)

            print_stars()
            print("New video:", response["video"])

        elif choice=='3':
            select_by = input("Would you like to select by? Enter title or id: ")
            if select_by=="title":
                title = input("Which video title would you like to select? ")
                video_list.get_video(title=title)
            elif select_by=="id":
                id = input("Which video id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video_list.get_video(id=id)
            else:
                print("Could not find video. Please enter id or title.")
            
            if video_list.selected_video:
                print_stars()
                print("Selected video: ", video_list.selected_video)

        elif choice=='4':
            print(f"Great! Let's update the video: {video_list.selected_video}")
            title=input("What is the new title of your video? ")
            description=input("What is the new description of your video? ")
            response = video_list.update_video(title=title, description=description)

            print_stars()
            print("Updated video:", response["video"])
        elif choice=='5':
            video_list.delete_video()

            print_stars()
            print("Video has been deleted.")

            print_stars()
            print(video_list.list_videos())

        elif choice=='6':
            print_stars()
            for customer in customer_list.list_customers():
                print(customer)


        elif choice=='7':
            print("Great! Let's create a new customer.")
            name=input("What is the name of your customer? ")
            postal_code=input("What is the postal code of your customer? ")
            phone=input("What is the customer's phone number?")
            response = customer_list.create_customer(name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("New customer:", response["customer"])

        elif choice=='8':
            select_by = input("Would you like to select by? Enter name or id: ")
            if select_by=="name":
                name = input("Which customer would you like to select? ")
                customer_list.get_customer(name=name)
            elif select_by=="id":
                id = input("Which customer id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    customer_list.get_customer(id=id)
            else:
                print("Could not find customer. Please enter id or title.")
            
            if video_list.selected_video:
                print_stars()
                print("Selected video: ", video_list.selected_video)



        elif choice=='9':
            list_options()
        elif choice=='10':
            play=False
            print("\nThanks for using the Video List CLI!")

        print_stars()


if __name__ == "__main__":
    main()