from customer_list import CustomerList
from video_list import VideoList
from requests.api import post
from requests.models import Response
import requests


# URL = "https://retro-video-store-sjv.herokuapp.com"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_decoration():
    print("~~~~~~~~~~~~~~~~~~~~~~~~")

def get_actions():
    actions = {
        "1": "List all customers", 
        "2": "List all videos",

        "3": "Get a Customer", 
        "4": "Create a Customer", 
        "5": "Update a Customer", 
        "6": "Delete a Customer", 

        "7": "Get a Video", 
        "8": "Create a Video", 
        "9": "Update out a video",
        "10": "Delete a Video",

        "11": "Check out a video",
        "12":"Check in a video",

        "13": "List videos a customer checked out",
        "14": "List customers who checked out a specific video",
        "15": "Quit",
        "16" : "Show all actions"
        }
    print("\nWELCOME TO RETRO VIDEO STORE")
    print_decoration()

    for option in actions:
        print(f"Option {option}: {actions[option]}")
    return actions

def select_action(actions, customer_list):
    possible_actions = actions.keys()
    choice = None

    while choice not in possible_actions:
        print("What would you like to do? Select 16 to see all actions again")
        choice = input("Which action would you like to perform? ")

    # if choice in ['5','6','9','10','11','12'] and customer_list.selected_customer == None:
    #     print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
    #     choice = input("Which action would you like to perform? ")
    return choice


def main():
    customer_list = CustomerList('https://retro-video-store-api.herokuapp.com')
    video_list = VideoList('https://retro-video-store-api.herokuapp.com')
    
    actions = get_actions()
    choice = select_action(actions, customer_list)

    if choice == "1":
    # get all customers
        print("I'll grab all those customers!")
        for customer in customer_list.list_all_customers():
            print(customer)
        
    elif choice == "2":
    #  get all videos
        print("I'll grab all those videos!")
        for video in video_list.list_all_videos():
            print(video)

    elif choice == "3":
    # Get a Customer
        print("Okay, I'm ready to get a customer.")
        # attribute = input("Should we get them by id or name? ")
        # if attribute == 'id':
        id = input('What is their id? ')
            # check if digit. 
        if id.isnumeric():
            id = int(id)
            selected_customer = customer_list.get_customer(id=id)
            print(f"The customer you selected is: {selected_customer}")
            
    elif choice == "4":
    # Create a customer
        print("Okay, I'm ready to create a customer.")
        name=input('What is their name? ')
        postal_code=input('What is their postal code? ')
        phone=input('What is their phone number? ')
        response = customer_list.create_customer(name=name, postal_code=postal_code,phone=phone)

        print(f"You created a new customer with the id of: {response['id']}")
        
    elif choice == "5":
    # Update a customer
        print("Lets update that customer's info!")
        # get id
        id = input('What is their id? ')
        id = int(id)
        # select customer
        selected_customer = customer_list.get_customer(id=id)
        print(f"The customer you selected is: {selected_customer}")
        # get attributes
        name=input("What is the new name for your customer?")
        postal_code=input("What is the new postal code for your customer?")
        phone=input("What is the new phone number for your customer?")
        # create response
        response = customer_list.update_customer(name=name,postal_code=postal_code,phone=phone)
        # print output
        print_decoration()
        print(f"You updated that customer!")
        print(response)
        print_decoration()

    elif choice == "6":
    # Delete a customer
        print("Lets put that customer in the garbage!")
        id = input('What is their id? ')
        id = int(id)
        selected_customer = customer_list.get_customer(id=id)
        print(f"The customer you selected is: {selected_customer}")
        # select customer
        response = customer_list.delete_customer(id=id)
        print(response)
        print("You deleted that customer!")
            
    elif choice == "7":
        # get a video
        print("Okay, I'm ready to get a video.")
        id = input('What is the id of the video? ')
            # check if digit. 
        if id.isnumeric():
            id = int(id)
            selected_video = video_list.get_video(id=id)
            print(f"The video you selected is: {selected_video}")
    elif choice == "8":
        # create a video
        print("Okay, I'm ready to create a video.")
        title=input('What is the title? ')
        release_date=input('What is the release date? ')
        total_inventory=int(input('What is the total inventory? '))
        response = video_list.create_video(title=title, release_date=release_date,total_inventory=total_inventory)
        print(f"You created a new video with the id of: {response['id']}")
    
    elif choice == "9":
        # update a video
        print("Lets update that video's info!")
        # get id
        id = input('What is the id? ')
        id = int(id)
        # select video
        selected_video = video_list.get_video(id=id)
        print(f"The video you selected is: {selected_video}")
        title=input('What is the new title? ')
        release_date=input('What is the new release date? ')
        total_inventory=int(input('What is new the total inventory? '))
        response = video_list.update_video(title=title, release_date=release_date,total_inventory=total_inventory)
        # print output
        print_decoration()
        print(f"You updated that video!")
        print(response)
        print_decoration()

    elif choice == "10":
        # delete video
        print("Okay, lets delete a video!")
        id = input('What is the id of the video? ')
            # check if digit. 
        if id.isnumeric():
            id = int(id)
            selected_video = video_list.get_video(id=id)
            print(f"The video you selected is: {selected_video}")

        response = video_list.delete_video(id=id)
        print("You deleted that video!")

    elif choice == "11":
        # checkout a video
        print("Okay, lets check out a video!")

        # get customer
        customer_id = input('What is the id of the customer? ')
        selected_customer = customer_list.get_customer(id=customer_id)
        print(f"The customer you selected is: {selected_customer}")

        # get video
        video_id = input('What is the id of the video? ')
        selected_video = video_list.get_video(id=video_id)
        print(f"The video you selected is: {selected_video}")
        # create new instance of rental
        # query_params = {
        #     "video_id": 13,
        #     "customer_id": 99,
        # }
        query_params = {
            "video_id": video_id,
            "customer_id": customer_id,
        }
        response = requests.post(BACKUP_URL+"/rentals/check-out", json=query_params )

        print(response.json())

    elif choice == "12":
        print("Okay, lets check in a video!")

        # get customer
        customer_id = input('What is the id of the customer? ')
        selected_customer = customer_list.get_customer(id=customer_id)
        print(f"The customer you selected is: {selected_customer}")

        # get video
        video_id = input('What is the id of the video? ')
        selected_video = video_list.get_video(id=video_id)
        print(f"The video you selected is: {selected_video}")
        # checkin a video
        query_params = {
            "video_id": video_id,
            "customer_id": customer_id,
        }
        response = requests.post(BACKUP_URL+"/rentals/check-in", json=query_params )
        print(response.json())


if __name__ == "__main__":
    main()