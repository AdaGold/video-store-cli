# import requests

# URL = "http://127.0.0.1:5000"
# BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

# def main():
#     print("WELCOME TO RETRO VIDEO STORE")
#     pass


# if __name__ == "__main__":
#     main()


from check_in_check_out_list import CheckInOut
from requests.api import options
from video_list import VideoList
from customer_list import CustomerList

# URL = "http://127.0.0.1:5000"

# BACKUP_URL = "https://halisas-retro-video-store-api.herokuapp.com"

def main(play=True):

    video_store = VideoList(url="http://localhost:5000/")
    customer_store = CustomerList(url="http://localhost:5000/")
    rental_store = CheckInOut(url="http://localhost:5000/")
    options=list_options()

    while play == True:
        choice = make_choice(options,video_store,customer_store)
        video_store.print_selected()  
        
        if choice == '1':
            print('Create a new video now:')
            title=input('Video title: ')
            release_date=input('Release_date: ')
            total_inventory=input('Total_inventory: ')
            response = video_store.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print('New video has been created: Video ID #',response["id"])

        elif choice == '2':
            print(f"Great! Let's update the video: {video_store.selected_video}")
            title=input("What is the new title of your video? ")
            release_date=input("What is the new release date of your video? ")
            total_inventory=input("What is the new total inventory of your video? ")
            response = video_store.edit_one_video(title=title, release_date=release_date,total_inventory=total_inventory)
            print("Updated video:", response)

        elif choice == '3':
            video_store.delete_a_video()
            print("Video has been deleted.")
            print(video_store.get_videos())

        elif choice == '4':
            for video in video_store.get_videos():
                print(video)

        elif choice == '5':
            select_by = input("Would you like to select by? Enter title or id: ")

            if select_by=="title":
                title = input("Which video title would you like to select? ")
                video_store.get_one_video(title=title)

            elif select_by=="id":
                video_id = input("Which video id would you like to select? ")

                if video_id.isnumeric():
                    video_id  = int(video_id)
                    video_store.get_one_video(id=video_id)
            else:
                print("Could not select. Please enter id or title.")
            
            if video_store.selected_video:
                print("Selected video: ", video_store.selected_video)

        elif choice == '6':
            print('Create a new customer now:')
            name=input('Customer name: ')
            phone=input('Customer phone: ')
            postal_code=input('Postal_code: ')
            response = customer_store.add_customer(name=name, phone=phone, postal_code=postal_code)
            print('New customer data has been created: Video ID #',response["id"])

        elif choice == '7':
            print(f"Great! Let's update the task: {customer_store.selected_customer}")
            name=input("What is the new name of customer? ")
            phone=input("What is the new phone number of customer? ")
            postal_code=input("What is the new postal code of customer? ")
            response = customer_store.edit_one_customer(name=name, phone=phone,postal_code=postal_code)
            print("Updated customer:", response)

        elif choice == '8':
            customer_store.delete_a_customer()
            print("customer has been deleted.")
            print(customer_store.get_customers())
        
        elif choice == '9':
            for customer in customer_store.get_customers():
                print(customer)

        elif choice == '10':
            select_by = input("Would you like to select by? Enter title or id: ")

            if select_by=="name":
                name = input("Which customer name would you like to select? ")
                customer_store.get_one_customer(name=name)

            elif select_by=="id":
                customer_id = input("Which customer id would you like to select? ")

                if customer_id.isnumeric():
                    customer_id = int(customer_id)
                    customer_store.get_one_customer(id=customer_id)

            else:
                print("Could not select. Please enter id or title.")
            
            if customer_store.selected_customer:
                print("Selected video: ", customer_store.selected_customer)

        elif choice == '11':
            print("would like to check out a video?")
            video_id = input("Enter the video id : ")

            if video_id.isnumeric():
                video_id = int(video_id)
                video_store.selected_video = video_store.get_one_video(id=video_id)
                print(video_store.selected_video)

            customer_id = input("Enter the customer id : ")

            if customer_id.isnumeric():
                customer_id = int(customer_id)

            customer_store.selected_customer = customer_store.get_one_customer(id=customer_id)
            print(customer_store.selected_customer)

            checked_out_rental = rental_store.checkout_video_to_customer(customer_id, video_id)
            print(checked_out_rental)
            print("video sucessfully checked out to the customer!")
            
        elif choice=='12':
            print("would like to check in a video?")
            video_id = input("Enter the video id : ")

            if video_id.isnumeric():
                video_id = int(video_id)
                video_store.selected_video = video_store.get_one_video(id=video_id)
                print(video_store.selected_video)

            customer_id = input("Enter the customer id : ")

            if customer_id.isnumeric():
                customer_id = int(customer_id)

            customer_store.selected_customer = customer_store.get_one_customer(id=customer_id)
            print(customer_store.selected_customer)

            checked_in_rental = rental_store.checkin_video_from_customer(customer_id, video_id)
            print(checked_in_rental)
            print("video sucessfully checked in to the store!")

        elif choice == '13':
            list_options()

        elif choice == '14':
            play = False
            print("\nThanks for using the Video List CLI!")

        
def list_options():

    options = {
        "1": "Add a video", 
        "2": "Edit a video",
        "3": "Delete a video", 
        "4": "Get information about all videos", 
        "5": "Get information about one video", 
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "get information about all customer",
        "10": "get information about one customer",
        "11": "check out a video to a customer",
        "12": "check in a video from a customer	",
        "13": "List all options",
        "14": "Quit"
        }

    print("Welcome to the Video List CLI")
    print("These are the actions you can perform")

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    return options

def make_choice(options, video_list,customer_list):
    valid_choice = options.keys()
    choice = None

    while choice not in valid_choice:
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")
    if choice in ['2','3'] and video_list.selected_video == None:
        print("You must select a task before updating it, deleting it.")
        print("Let's select a task!")
        choice = "5"
    elif choice in ['7','8'] and customer_list.selected_customer == None:
        print("You must select a task before updating it, deleting it.")
        print("Let's select a task!")
        choice = "10"
    
    return choice


if __name__ == "__main__":
    main()



