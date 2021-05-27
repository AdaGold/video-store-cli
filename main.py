import requests
from video import Video 
from customer import Customer

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def welcome_message(): 
    return("WELCOME TO RETRO VIDEO STORE")

def list_options():
    options = {
        "1": "Add a video", 
        "2": "Edit a video",
        "3": "Delete a video", 
        "4": "Get information on all videos", 
        "5": "Get information about one video", 
        "6": "Add a customer",
        "7": "Edit a customer",
        "8": "Delete a customer",
        "9": "Get information about one customer",
        "10": "Get information about all customers",
        "11": "Check out a video to a customer",
        "12": "Check in a video from a customer",
        "13": "List all options",
        "14": "Quit"
        }
    
    print("What would you like to do?")
    print("**************************")
    for choice_num in options: 
        print(f"Option {choice_num}. {options[choice_num]}")
    
    # do i need another prompt here like:
    # print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
    return options 

def make_choice(options, video, customer):
    valid_choices = options.keys()
    choice = None 

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")
    
    # if the choices need a video id, prompt user to select video with id 
    if choice in ["2", "3"] and video.selected_video == None: 
        print("You must select a video before updating it or deleting it.")
        print("Let's select a video!")
        choice = "5"
    
    # if the choices need a customer id, prompt user to select customer with id 
    if choice in ["7", "8"] and customer.selected_customer == None: 
        print("You must select a customer before updating them or deleting them.")
        print("Let's select a customer!")
        choice = "9"

    # if the choices need a customer id, prompt user to select customer with id 
    # dont know if i need this whole thing 
    # if choice in ["11", "12"] and video_list.selected_video == None and customer_list.selected_customer == None: 
    #     print("Let's select a customer!")
    #     choice = "9"
    #     print("Let's select a video")

    return choice

def print_stars():
    print("**************************")

def main():
    # print("WELCOME TO RETRO VIDEO STORE")
    print(welcome_message())
    # response = requests.get(BACKUP_URL + "/videos")
    # print(response.json())

    # initialize video.py & customer.py
    video = Video(url="https://retro-video-store-api.herokuapp.com")
    customer = Customer(url="https://retro-video-store-api.herokuapp.com")

    #print choices 
    options = list_options()

    play = True 
    while play == True: 

        # get input and validate 
        choice = make_choice(options, video, customer)

        video.print_selected()
        customer.print_selected()

        if choice =='1':
            print("Great! Let's add a new video.")
            title=input("What is the title of the video? ")
            release_date=input("When was the release_date of the video? ")
            total_inventory=input("What is the total inventory of the video? ")
            available_inventory=input("What is the available inventory of the video? ")
            response = video.add_video(title=title, release_date=release_date, total_inventory=total_inventory, available_inventory=available_inventory)
            video_info = video.get_video(title=title, id=response["id"])
            print("Video added:", video_info) 
        
        elif choice =='2': 
            print(f"Great! Let's update the video: {video.selected_video}")
            title=input("What is the new title of the video? ")
            release_date=input("What is the new release date of the video? ")
            total_inventory=input("What is the new total_inventory of the video? ")
            response = video.update_video(title=title, release_date=release_date, total_inventory=total_inventory)
            video_info = video.get_video(title=title, id=response["id"])
            print("Updated video:", video_info)
            print(video.selected_video)

        elif choice == '3':
            video.delete_video()
            print("Video has been deleted")
            print(video.list_videos())

        elif choice =='4': 
            print("Videos:")
            print_stars()
            for video in video.list_videos(): 
                print(video)

        elif choice == '5': 
            select_by = input("Would you like to select by? Enter title or id: ")
            if select_by == "title": 
                title = input("Which video title would you like to select? ")
                video.get_video(title=title)
            elif select_by == "id": 
                id = input("Which video id would you like to select? ")
                if id.isnumeric(): 
                    id = int(id)
                    video.get_video(id=id)
            else: 
                print("Could not select. Please enter id or title.")
            
            if video.selected_video: 
                print("Selected video: ", video.selected_video)

        elif choice == '6': 
            print("Great! Let's add a new customer.")
            name=input("What is the name of the customer? ")
            postal_code=input(f"What is {name}'s postal code? ")
            phone=input(f"What {name}'s phone number? ")
            response = customer.add_customer(name=name, postal_code=postal_code, phone=phone)
            customer_info = customer.get_customer_by_id(name=name, id=response["id"])
            print("Customer added:", customer_info) 

        elif choice == '7': 
            print(f"Great! Let's update the customer: {customer.selected_customer}")
            name=input("What is the new name of the customer? ")
            postal_code=input("What is the new postal code of the customer? ")
            phone=input("What is the new phone number of the customer? ")
            response = customer.update_customer(name=name, postal_code=postal_code, phone=phone)
            customer_info = customer.get_customer_by_id(name=name, id=response["id"])
            print("Updated customer:", customer_info)
            print(customer.selected_customer)

        elif choice == '8':
            customer.delete_customer()
            print("Customer has been deleted")
            print(customer.list_customers())

        elif choice == '9': 
            select_by = input("Would you like to select by? Enter name or id: ")
            if select_by == "name": 
                name = input("Which video name would you like to select? ")
                customer.get_customer_by_id(name=name)
            elif select_by == "id": 
                id = input("Which customer id would you like to select? ")
                if id.isnumeric(): 
                    id = int(id)
                    customer.get_customer_by_id(id=id)
            else: 
                print("Could not select. Please enter name or id.")
            
            if customer.selected_customer: 
                print("Selected customer: ", customer.selected_customer)

        elif choice == '10':
            print("Customers:")
            print_stars()
            for customer in customer.list_customers(): 
                print(customer)



if __name__ == "__main__":
    main()