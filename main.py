import requests
from video import Video 
from customer import Customer
from rental import Rental 


def welcome_message(): 
    return("WELCOME TO RETRO VIDEO STORE")

def print_line():
    print("--------------------------------------------------")

def list_options():
    print("\n---------------------- MENU ---------------------- ")

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

    for choice_num in options: 
        print(f"Option {choice_num}. {options[choice_num]}")

    return options 

def make_choice(options, video, customer):
    valid_choices = options.keys()
    choice = None 

    while choice not in valid_choices:
        print_line()
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option numbers 1-14: ")

    return choice

def select_video(video):
    print("Let's select a video by title or id:")
    select_by = input("Which do you want to use? Enter title or id: ")
    if select_by == "title": 
        title = input("Which video title would you like to select? ")
        video.get_video(title=title)
    elif select_by == "id": 
        id = input("Which video id would you like to select? ")
        if id.isnumeric(): 
            id = int(id)
            video.get_video(id=id)

    if video.selected_video: 
        print(f"Selected video: \n{video.selected_video}")
    else: 
        print("Video not found. Please enter a valid title or id.")
        return None

    return video.selected_video

def select_customer(customer):
    print("Let's select a customer by name or id:")
    select_by = input("Which do you want to use? Enter name or id: ")
    if select_by == "name": 
        name = input("Enter customer's name: ")
        customer.get_customer_by_id(name=name)
    elif select_by == "id": 
        id = input("Enter customer's id: ")
        if id.isnumeric(): 
            id = int(id)
            customer.get_customer_by_id(id=id)

    if customer.selected_customer: 
        print(f"Selected customer: \n{customer.selected_customer}")
    else: 
        print("Customer not found. Please enter a valid name or id.")
        return None

    return customer.selected_customer

def main(play=True):
    print(welcome_message())

    # initialize video.py & customer.py
    video = Video(url="https://retro-video-store-api.herokuapp.com")
    customer = Customer(url="https://retro-video-store-api.herokuapp.com")
    rental = Rental(url="https://retro-video-store-api.herokuapp.com")

    #print choices 
    options = list_options()

    play = True 
    while play == True: 

        # get input and validate 
        choice = make_choice(options, video, customer)

        if choice =='1':
            print('''
            [ ADD A VIDEO ]
            ''')
            print("\nGreat! Let's add a new video:")
            title=input("  > What is the title of the video? ")
            release_date=input("  > When was the release_date of the video? (YYYY/DD/MM) ")
            total_inventory=input("  > What is the total inventory of the video? ")
            available_inventory=input("  > What is the available inventory of the video? ")
            response = video.add_video(title=title, release_date=release_date, total_inventory=total_inventory, available_inventory=available_inventory)
            video_info = video.get_video(title=title, id=response["id"])
            video.selected_video = None
            print(f"Video successfully added: \n{video_info}")

        elif choice =='2': 
            print('''
            [ EDIT A VIDEO ]
            ''')
            if select_video(video) is None:
                continue
            print("\nGreat! Let's edit the video:")
            title=input("  > What is the new title of the video? ")
            release_date=input("  > What is the new release date of the video? (YYYY/DD/MM) ")
            total_inventory=input("  > What is the new total_inventory of the video? ")
            print("")
            response = video.edit_video(title=title, release_date=release_date, total_inventory=total_inventory)
            video_info = video.get_video(title=title, id=response["id"])
            print(f"Video successfully updated: \n{video_info}")
            # this lines clears out the selected video after being done with the put request
            video.selected_video = None


        elif choice == '3':
            print('''
            [ DELETE A VIDEO ]
            ''')
            if select_video(video) is None:
                continue
            print("\nYou will NEVER see this video again!!!")
            response = video.delete_video()
            print("Video successfully deleted.")

        elif choice =='4': 
            print('''
            [ GET INFORMATION ON ALL VIDEOS ]
            ''')
            for each_video in video.list_videos(): 
                print(each_video)

        elif choice == '5': 
            print('''
            [ GET INFORMATION ON ONE VIDEO ]
            ''')
            select_video(video)

# ---------------------customers---------------------- #

        elif choice == '6': 
            print('''
            [ ADD A CUSTOMER ]
            ''')
            print("\nGreat! Let's add a new customer:")
            name=input("  > What is the name of the customer? ")
            postal_code=input(f"  > What is {name}'s postal code? ")
            phone=input(f"  > What {name}'s phone number? ")
            print("")
            response = customer.add_customer(name=name, postal_code=postal_code, phone=phone)
            customer_info = customer.get_customer_by_id(name=name, id=response["id"])
            customer.selected_customer = None
            print(f"Customer was successfully added: \n{customer_info}")

        elif choice == '7': 
            print('''
            [ EDIT A CUSTOMER ]
            ''')
            if select_customer(customer) is None: 
                continue
            print(f"\nGreat! Let's update the customer:")
            name=input("  > What is the new name of the customer? ")
            postal_code=input("  > What is the new postal code of the customer? ")
            phone=input("  > What is the new phone number of the customer? ")
            print("")
            response = customer.update_customer(name=name, postal_code=postal_code, phone=phone)
            customer_info = customer.get_customer_by_id(name=name, id=response["id"])
            print(f"Customer {name} was successfully updated: \n{customer_info}")
            customer.selected_customer = None

        elif choice == '8':
            print('''
            [ DELETE A CUSTOMER ]
            ''')
            cancelled_customer = select_customer(customer)
            if cancelled_customer is None: 
                # break
                continue
            print(f"\n{cancelled_customer['name']} found out about Netflix, huh?")
            customer.delete_customer()
            print("Customer successfully deleted. I may lose my job at this rate.")

        elif choice == '9': 
            print('''
            [ GET INFORMATION ON ONE CUSTOMER ]
            ''')
            select_customer(customer)

        elif choice == '10':
            print('''
            [ GET INFORMATION ON ALL CUSTOMERS ]
            ''')
            for each_customer in customer.list_customers(): 
                print(each_customer)

# ---------------------rentals---------------------- #

        elif choice == '11': 
            print('''
            [ CHECK OUT A VIDEO TO A CUSTOMER ]
            ''')
            video_id = input("  > Enter the video id: ")
            # check if it is a valid id 
            if video_id.isnumeric():
                video_id = int(video_id)
                video.get_video(id=video_id)
            
            if video.selected_video:
                print(f"Selected video: \n{video.selected_video}")
            else: 
                print("Video not found. Please enter a valid id.")
                continue

            video.selected_video = None
            customer_id = input("  > Enter the customer id: ")
            # check if valid id 
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                customer.get_customer_by_id(id=customer_id)

            if customer.selected_customer:
                print(f"Selected customer: \n{customer.selected_customer}")
            else: 
                print("Customer not found. Please enter a valid id.")
                continue
            customer.selected_customer = None

            print("")
            checked_out = rental.check_out_video(customer_id=customer_id, video_id=video_id)
            customer_info = customer.get_customer_by_id(id=customer_id)
            video_info = video.get_video(id=video_id)
            print(f"Rental info: \n{checked_out}")
            print(f"{video_info['title']} successfully checked out to {customer_info['name']}!")

            
        elif choice == '12':
            print('''
            [ CHECK IN A VIDEO FROM A CUSTOMER ]
            ''')
            video_id = input("  > Enter the video id: ")
            # check if it is a valid id 
            if video_id.isnumeric():
                video_id = int(video_id)
                video.get_video(id=video_id)
            
            if video.selected_video:
                print(f"Selected video: \n{video.selected_video}")
            else: 
                print("Video not found. Please enter a valid id.")
                continue

            video.selected_video = None
            customer_id = input("  > Enter the customer id: ")
            # check if valid id 
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                customer.get_customer_by_id(id=customer_id)

            if customer.selected_customer:
                print(f"Selected customer: \n{customer.selected_customer}")
            else: 
                print("Customer not found. Please enter a valid id.")
                continue
            customer.selected_customer = None

            print("")
            checked_in = rental.check_in_video(customer_id=customer_id, video_id=video_id)
            customer_info = customer.get_customer_by_id(id=customer_id)
            video_info = video.get_video(id=video_id)
            print(f"Rental info: \n{checked_in}")
            print(f"{video_info['title']} successfully checked in {customer_info['name']}!")

# ---------------------etc---------------------- #

        elif choice == '13': 
            list_options()

        elif choice == '14':
            print('''
            [ EXIT ]
            ''')
            consent = input("\nDo you want to exit? select y/n: ")
            if consent == 'y': 
                play=False
                print("Thank you for using the video store CLI. Good bye!")

            if consent == 'n': 
                continue


if __name__ == "__main__":
    main()