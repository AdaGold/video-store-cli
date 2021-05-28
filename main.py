import requests
from retro_video import RetroVideo

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

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
        "9": "Get information about all customers",
        "10": "Get information about one customer",
        "11": "Check out a video to a customer",
        "12": "Check in a video from a customer"
    }

    print("WELCOME TO RETRO VIDEO STORE")
    print("What would you like to do?")

    for option_num in options:
        print(f"Option {option_num}. {options[option_num]}")
    
    return options

def make_choice(options, retro_video):
    valid_choices = options.keys()
    choice = None 

    while choice not in valid_choices:
        choice = input("Make your selection using the option number: ")

    return choice

def main(play=True):
    options = list_options()
    valid_choices = options.keys()
    choice =  input("Make your selection using the option number: ")
    retro_video = RetroVideo(url=BACKUP_URL)

    if choice not in valid_choices:
        print("Please choose a valid option!")

    elif choice == "1":
        print("Great! Let's create a new video.")
        title=input("What is the title of the video? ")
        release_date=input("What is the release date of your task? ")
        total_inventory= input("How many videos are being added?")
        response = retro_video.add_video(title=title, release_date=release_date, total_inventory=total_inventory )

            
        print("New video added")

    elif choice=='2':
        print("Great! Let's update the video")
        id = input("What is the id of the video you would like to edit?")
        if id.isnumeric():
                    id = int(id)
                    retro_video.get_video(id=id)
        else:
                print("Could not select. Please enter valid id. ")
        title=input("What is the new title of your task? ")
        release_date=input("What is the new release date of your task? ")
        total_inventory= input("What is the updated inventory?")
        response = retro_video.edit_video(title=title, release_date=release_date, total_inventory=total_inventory)

        print("Updated video")

    elif choice=='3':
        id = input("What is the id of the video you would like to delete?")
        if id.isnumeric():
                    id = int(id)
                    retro_video.get_video(id=id)
        else:
                print("Could not select. Please enter valid id. ")
        retro_video.delete_video()
        print("Video has been deleted")

    elif choice=='4':
        for video in retro_video.get_videos():
            print(video)

    elif choice=='5':
        id = input("What is the id of the video you would like to get more information?")
        if id.isnumeric():
                    id = int(id)
                    retro_video.get_video(id=id)
        else:
                print("Could not select. Please enter valid id. ")
        print(retro_video.selected_video)

    elif choice == "6":
        print("Great! Let's add a new customer")
        name=input("What is the name of the customer? ")
        postal_code=input("What is their postal code? ")
        phone= input("What is their phone number?")
        response = retro_video.add_customer(name=name, postal_code=postal_code, phone=phone)

            
        print("New customer added")

    elif choice=='7':
        print("Great! Let's update a customer")
        id = input("What is the id of the customer you would like to edit?")
        if id.isnumeric():
                    id = int(id)
                    retro_video.get_customer(id=id)
        else:
                print("Could not select. Please enter valid id. ")
        name=input("What is the new name of the customer? ")
        postal_code=input("What is their new postal code? ")
        phone= input("What is their new phone number?")
        response = retro_video.edit_customer(name=name, postal_code=postal_code, phone=phone)

    elif choice=='8':
        id = input("What is the id of the customer you would like to delete?")
        if id.isnumeric():
                    id = int(id)
                    retro_video.get_customer(id=id)
        else:
                print("Could not select. Please enter valid id. ")
        retro_video.delete_customer()
        print("Customer has been deleted")

    elif choice=='9':
        for customer in retro_video.get_customers():
            print(customer)

    elif choice=='10':
        id = input("What is the id of the customer you would like to get more information?")
        if id.isnumeric():
                    id = int(id)
                    retro_video.get_customer(id=id)
        else:
                print("Could not select. Please enter valid id. ")
        print(retro_video.selected_customer)

    elif choice == "11":
        print("Great! Let's check out a video to a customer")
        id=input("What is the id of the video?")
        customer_id=input("What is the id of the customer? ")
        if id.isnumeric():
                    id = int(id)
                    retro_video.get_video(id=id)
        response = retro_video.check_out_video(video_id=id, customer_id=customer_id)

        print("Video has been checked out")

    elif choice == "12":
        print("Great! Let's check in a video to a customer")
        id=input("What is the id of the video?")
        customer_id=input("What is the id of the customer? ")
        if id.isnumeric():
                    id = int(id)
                    retro_video.get_video(id=id)

        response = retro_video.check_in_video(video_id=id, customer_id=customer_id)
        print("Video has been checked in")

if __name__ == "__main__":
    main()