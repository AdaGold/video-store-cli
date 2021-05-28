from videostore import VideoStore



def print_stars():
    print("\n**************************\n")

def list_options():

    options = {
        "1": "List all videos", 
        "2": "Add video",
        "3": "Get a video", 
        "4": "Update a video", 
        "5": "Delete a video", 
        "6": "List all customers",
        "7": "Add a customer",
        "8": "Get a customer",
        "9": "Update a customer",
        "10": "Delete a customer",
        "11": "Checkout video",
        "12": "Checkin video",
        "13": "List all options",
        "14": "Quit"
        }

    print_stars()
    print("Welcome to the Retro Video Store CLI")
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
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")

    return choice

def print_video(video):
    print_stars()
    print(f"ID: {video['id']}")
    print(f"Title: {video['title']}")
    print(f"Release Date: {video['release_date']}")
    print(f"Available: {video['total_inventory']}")
    print_stars()

def print_customer(customer):
    print_stars()
    print(f"ID: {customer['id']}")
    print(f"Name: {customer['name']}")
    print(f"Phone: {customer['phone']}")
    print(f"Postal Code: {customer['postal_code']}")
    print(f"Registered At: {customer['registered_at']}")
    print(f"Rented Videos: {customer['videos_checked_out_count']}")
    print_stars()

def run_cli(play=True):

    #initialize retro video store
    video_store = VideoStore("https://retro-video-store-api.herokuapp.com")
    
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options)


        if choice == '1':
            print_stars()
            for video in video_store.get_videos_info():
                # print(video)
                print(f"ID: {video['id']} - Title: {video['title']}")

        elif choice == '2':
            print("Great! Let's add a new video.")
            title=input("What is the title of your video? ")
            release_date=input("What is the release date of your video? (MM/DD/YYYY): ")
            total_inventory=input("What is the total inventory? ")
            response = video_store.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_stars()
            print("New video: ") 
            print(response)
            print_stars()

        elif choice == '3':
            print("Fantastic! Let's choose a video!")
            video_id = input("Enter a video id: ")
            response = video_store.get_video_info(video_id)
            print_video(response)

        elif choice == '4':
            print("Great! Let's update the video!")
            video_id = input("Enter a video id: ")
            title=input("What is the new title of your video? ")
            release_date=input("What is the new release date of your video? (MM/DD/YYYY): ")
            total_inventory=input("What is the new total inventory? ")
            response = video_store.edit_video(video_id=video_id, title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("Updated video: ")
            print(response)
            print_stars()

        elif choice == '5':
            print("Which video would you like to delete?")
            video_id = input("Enter a video id: ")
            video_store.delete_video(video_id)
            print_stars()
            print("Video has been deleted.")
            print_stars()

        elif choice == '6':
            print_stars()
            for customer in video_store.get_customers_info():
                # print(customer)
                print(f"ID: {customer['id']} - {customer['name']} - Phone: {customer['phone']} - Rented Videos: {customer['videos_checked_out_count']}")
            print_stars()

        elif choice == '7':
            print("Wonderful! Let's add a new customer!")
            name=input("What is the name of the customer? ")
            postal_code=input("What is the postal code of the customer? ")
            phone=input("What is the phone number of the customer? ")
            response = video_store.add_customer(name=name, postal_code=postal_code, phone=phone)
            print_stars()
            print("New customer: ") 
            print(response)
            print_stars()

        elif choice == '8':
            print("Whohoo! Let's choose a customer!")
            customer_id = input("Enter a customer id: ")
            response = video_store.get_customer_info(customer_id)
            print_customer(response)

        elif choice == '9':
            print("Wonderous! Let's update the customer!")
            customer_id = input("Enter a customer id: ")
            name=input("What is the name of the customer? ")
            postal_code=input("What is the postal code of the customer? ")
            phone=input("What is the phone number of the customer? ")
            response = video_store.edit_customer(customer_id=customer_id, name=name, postal_code=postal_code, phone=phone)
            print_stars()
            print("Updated customer: ")
            print(response)
            print_stars()

        elif choice == '10':
            print("Which customer would you like to delete?")
            customer_id = input("Enter a customer id: ")
            video_store.delete_customer(customer_id)
            print_stars()
            print("The customer has been deleted.")
            print_stars()

        elif choice == '11':
            print("What video would you like to check out? ")
            customer_id = input("Enter the customer id: ")
            video_id = input("Enter the video id: ")
            response = video_store.check_out_video(customer_id=customer_id, video_id=video_id)
            print_stars()
            print("The video was checked out! ")
            print(response)
            print_stars()
        elif choice == '12':
            print("What video would you like to check in? ")
            customer_id = input("Enter the customer id: ")
            video_id = input("Enter the video id: ")
            response = video_store.check_in_video(customer_id=customer_id, video_id=video_id)
            print_stars()
            print("The video was checked in! ")
            print(response)
            print_stars()

        elif choice == '13':
            list_options()
        elif choice == '14':
            play=False
            print("\nThanks for using the Retro Video Store CLI!")

        print_stars()

run_cli()