from video_store import VideoStore


def main():
    print("\nWELCOME TO THE RETRO VIDEO STORE")

if __name__ == "__main__":
    main()


##############################

def print_stars():
    print("\n**************************\n")

def list_options():
    
    options = {
        "1": "add a video",
        "2": "edit a video",
        "3": "delete a video",
        "4": "list one video",
        "5": "list all videos",
        "6": "add a customer",
        "7": "edit a customer",
        "8": "delete a customer",
        "9": "list one customer",
        "10": "list all customers",
        "11": "check-out a video to a customer",
        "12": "check-in a video from a customer",
        "13": "list all videos checked-out by customer",
        "14": "list all customers who checked-out a specific video",
        "15": "list all options",
        "16": "quit"
    }

    print_stars()
    print("These are the available options")
    print_stars()
    
    for number in options:
        print(f"Option {number}: {(options[number]).title()}")

    print_stars()
    return options


def make_choice(options):
    valid_choices = options.keys()
    choice = input("\nPlease select option: ")

    while choice not in valid_choices:
        print("Please select 15 to see all options again")
        choice = input("Make your selection using the option number: ")
    
    return choice


def select_video(video_store):
    choice = input("Please enter video title: ")
    video_store.list_one_video(title=choice)
    return video_store.selected_video


def select_customer(video_store):
    choice = input("Please enter customer name: ")
    video_store.list_one_customer(name=choice)
    return video_store.selected_customer


def run_cli(play = True):

    #initialize video_store
    video_store = VideoStore()
    
    # print choices
    options = list_options()

    while play == True:

        # get input and validate
        choice = make_choice(options)

        # Choice 1: add a video
        if choice == '1':
            title = input("What is the title of the video? ")
            release_date = input("What is the release_date of the video? ")
            total_inventory = input("What is the total inventory of the video? ")
            response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)   

            print_stars()
            print("New video created:", title)

        # Choice 2: edit a video
        elif choice == '2':
            video = select_video(video_store)

            if video == None:
                return "This video has not been found"

            title = input("What is the new title of the video? ")
            release_date = input("What is the new release_date of the video? ")
            total_inventory = input("What is the new inventory of the video? ")

            response = video_store.update_video(
                title=title, 
                release_date=release_date, 
                total_inventory=total_inventory
            )

            print_stars()
            print("Updated video:", response["title"])

        # Choice 3: delete a video
        elif choice == '3':
            video = select_video(video_store)

            if video == None:
                return "This video has not been found"

            video_store.delete_video()

            print_stars()
            print("Video has been deleted")
        
        # Choice 4: list one video
        elif choice == "4":
            video = input("Please enter video title or id: ")

            if video == None:
                return "This video has not been found"

            elif video.isalpha():
                response = video_store.list_one_video(title=video)
            elif video.isdigit():
                response = video_store.list_one_video(id=int(video))

            print_stars()
            print(response)

        # Choice 5: list all videos
        if choice == '5':
            print_stars()
            print("The video list is: ")

            for video in video_store.list_all_videos():
                print(video)
        
        # Choice 6: add a customer
        elif choice == '6':
            name = input("What is the name of the customer? ")
            postal_code = input("What is the postal code of the customer? ")
            phone = input("What is the phone number of the customer? ")
            response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone)   

            print_stars()
            print("New customer created:", name)

        # Choice 7: edit a customer
        elif choice == '7':
            customer = select_customer(video_store)

            if customer == None:
                return "This customer has not been found"

            name = input("What is the new name of the customer? ")
            postal_code = input("What is the new postal code of the customer? ")
            phone = input("What is the new phone number of the customer? ")
            response = video_store.create_customer(
                name=name, 
                postal_code=postal_code, 
                phone=phone
            )   

            print_stars()
            print("Updated customer:", name)

        # Choice 8: delete a customer
        elif choice == '8':
            customer = select_customer(video_store)

            if customer == None:
                return "This customer has not been found"

            video_store.delete_customer()

            print_stars()
            print("Customer has been deleted")

            print_stars()
            list_options()

        # Choice 9: list one customer
        elif choice == '9':
            customer = input("Please enter customer name or id: ")

            if customer == None:
                return "This customer has not been found"

            elif customer.isalpha():
                response = video_store.list_one_customer(name=customer)
            elif customer.isdigit():
                response = video_store.list_one_customer(id=int(customer))

            print_stars()
            print(response)

        # Choice 10: list all customers
        elif choice == '10':
            print_stars()
            print("The list of customers is: ")

            for customer in video_store.list_all_customers():
                print(customer)
        
        # Choice 11: check out a video to a customer
        elif choice == '11':
            customer = select_customer(video_store)
            video = select_video(video_store)

            if customer == None or video == None:
                return "Please verify customer and/or video information"

            rental = video_store.check_out_video(customer_id = customer["id"], video_id = video["id"])
            print(f"Video {rental['video_id']} has been checked_out to customer {rental['customer_id']}")

        # Choice 12: check in a video from a customer
        elif choice == '12':
            customer = select_customer(video_store)
            video = select_video(video_store)

            if customer == None or video == None:
                return "Please verify customer and/or video information"

            rental = video_store.check_in_video(customer_id = customer["id"], video_id = video["id"])
            print(f"Video {rental['video_id']} has been checked_in to customer {rental['customer_id']}")

        # Choice 13: list all videos checked out to a specific customer
        elif choice == '13':
            customer = select_customer(video_store)

            if customer == None:
                return "This customer has not been found"

            response = video_store.checked_out_videos_by_customer(customer["id"])

        # Choice 14: list all customers who checked-out a specific video
        elif choice == '14':
            video = select_video(video_store)

            if video == None:
                return "This video has not been found"

            response = video_store.customers_checked_out_this_video(video["id"])

        # Choice 15: list all options
        elif choice == '15':
            print_stars()
            list_options()

        # Choice 16: quit
        elif choice == '16':
            play = False
            print_stars()
            print("\nThanks for using the Video Store CLI!")

        print_stars()

run_cli()

