#installed request in local machine 
import requests
from video_store import Videostore
from customer import Customer
from video_customer_relationship import Video_customer_relationship


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

# def main():
#     print("WELCOME TO RETRO VIDEO STORE")
#     pass


# if __name__ == "__main__":
#     main()

def list_options():
    options = {
        "1": "Create a video",
        "2": "Update selected video",
        "3": "Delete selected video",
        "4": "Select all videos",
        "5": "Select a video", 

        "6": "Create a customer",
        "7": "Update selected customer",
        "8": "Delete selected customer",
        "9": "Select all customers",
        "10": "Select a customer",

        "11": "Mark selected video check-in",
        "12": "Mark selected video check-out",

        "13": "List all options",
        "14": "Quit"
        }

#how can I start with options of selecting video and customer? 
    print("What would you like to do?")  
    print("**************************")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print("You must select a video or customer before updating it, deleting it, check-in, or check-out.")
    return options

def make_choice(options, video_store, customer):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['2','3','11','14'] and video_store.selected_video == None:
        print("You must select a video before updating it, deleting it, check-in, or check-out.")
        print("Let's select a video!")
        choice = "5"
    else:
        choice in ['7', '8'] and customer.selected_video == None
        print("You must select a customer before updating it or deleting it.")
        print("Let's select a customer")
        choice = "10"

    return choice

def print_stars():
    print("*******************************************************")

def run_cli_video_store():
    video_store = Videostore(url="https://retro-video-store-api.herokuapp.com/")

    options = list_options()

    play = True
    while play==True:

        # get input and validate
        choice = make_choice(options, video_store, customer)
        video_store.print_selected()


#All for videos 
        if choice == '1':
            print("Great! Let's create a new video.")
            title = input("What is the title of your video? ==> ")
            release_date = input("When is the release date of the video? ==> ")
            response = video_store.create_video(title=title, release_date=release_date)
            print("New video:", response["video"])
        
        elif choice == '2':
            print(f"Great! Let's update the video: {video_store.selected_video}")
            title = input("What is the new title of your video? ")
            release_date = input("When is the new release date of the video? ==> ")
            response = video_store.update_video(title=title, release_date=release_date)
            print("Updated video:", response["video"])

        elif choice=='3':
            video_store.delete_video()
            print("Video has been deleted.")
            print(video_store.list_videos())
        
        elif choice=='4':
            print("Videos:")
            print_stars()
            for video in video_store.list_videos():
                print(video)

        elif choice=='5':
            select_by = input("Would you like to select by? Enter video title or id: ")
            if select_by=="title":
                title = input("Which video title would you like to select? ")
                video_store.get_video(title=title)

            elif select_by=="id":
                id = input("Which video id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video_store.get_video(id=id)
            else:
                print("Could not select. Please enter id or title.")
            
            if video_store.selected_video:
                print("Selected video: ", video_store.selected_video)

#All for customer 
        elif choice == '6':
            print("Great! Let's create a new customer.")
            title = input("What is the title of the customer? ==> ")
            postal_code = input("What is customer's postal_code? ==> ")
            phone = input("What is customer's phone number? ==> ")

            response = customer.create_customer(title=title, postal_code=postal_code, phone=phone) #import not working for customer
            print("New customer:", response["customer"])
        
        elif choice == '2':
            print(f"Great! Let's update the customer: {customer.selected_customer}")
            title = input("What is the new title of your video? ")
            postal_code = input("What is customer's new postal_code? ==> ")
            phone = input("What is customer's new phone number? ==> ")

            response = customer.update_customer(title=title, postal_code=postal_code, phone=phone) #import not working for customer )
            print("Updated customer:", response["customer"])

        elif choice=='3':
            customer.delete_customer()
            print("Customer has been deleted.")
            print(customer.list_customers())
        
        elif choice=='4':
            print("Customer:")
            print_stars()
            for customer in customer.list_customers():
                print(customer)

        elif choice=='5':
            select_by = input("Would you like to select by? Enter customer title or postal_code or phone: ")
            if select_by=="title":
                title = input("Which customer title would you like to select? ")
                customer.get_customer(title=title)

            elif select_by=="postal_code":
                id = input("Which postal_code would you like to select? ")
                if id.isString():
                    postal_code = str(postal_code)
                    customer.get_customer(postal_code=postal_code)

            elif select_by=="phone":
                id = input("Which phone would you like to select? ")
                if id.isString():
                    phone = str(phone)
                    customer.get_customer(phone=phone)

            else:
                print("Could not select. Please enter title or postal_code or phone.")
            
            if customer.selected_customer:
                print("Selected customer: ", customer.selected_customer)

#make relationship between video and customer 
        elif choice=='11':
            response = video_store.check_in()
            print("Video check-in: ", response["video"])

        elif choice=='12':
            response = video_store.check_out()
            print("Video check-out: ", response["video"])

        # elif choice=='8':
        #     for task in task_list.list_tasks():
        #         task_list.get_task(id=task['id'])
        #         task_list.delete_task()
        #     print("Deleted all tasks.")

        elif choice=='13':
            list_options()

        elif choice=='14':
            play=False

        print_stars()

run_cli_video_store()