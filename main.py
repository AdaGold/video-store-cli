import requests
from video_store import VideoStore

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_divider():
    print("\noOoOoOoOoOooOoOoOoOoOooOoOoOoOoOoOoOoOoO\n")

def main():
    print_divider()
    print("✨✨✨WELCOME TO RETRO VIDEO STORE✨✨✨")
    
def list_options():

    options = {
        "1": "Create a new video record", 
        "2": "Update a video record",
        "3": "Delete a video record", 
        "4": "Get information for all videos", 
        "5": "Select a video", 
        "6": "Create a new customer record",
        "7": "Update a customer record",
        "8": "Delete a customer record",
        "9": "Select a customer",
        "10": "Get information for all customers",
        "11": "Check out a video to a customer",
        "12": "Check in a video from a customer",
        "13": "List all options",
        "14": "Quit"
        }

    print_divider()
    print("These are the actions you can perform: ")
    print_divider()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_divider()

    return options

def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 and 14 to quit to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['2','3'] and video_store.selected_video == None:
        print("You must select a video before updating it or deleting it")
        print("Please select a video!")
        choice = "5"

    elif choice in ['7','8'] and video_store.selected_video == None:
        print("You must select a customer before updating them or deleting them")
        print("Please select a customer!")
        choice = "9"
    
    return choice

def run_cli(play=True):

    #initialize video_store
    video_store = VideoStore(url="https://retro-video-store-api.herokuapp.com")
    
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, video_store)

        video_store.print_selected()

##### VIDEO CHOICES #####
        if choice == '1':
            print("Creating a new video record: ")
            title = input("What is the title of your video? ")
            release_date = input("When was the release date of the video? ")
            total_inventory = input("How many videos with this title are in stock? ")
            response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_divider()
            print("New video record created:", response["video"])

        elif choice == '2':
            print(f"Updating video record: {video_store.selected_video}")
            title = input("What is the new title of video? ")
            release_date = input("What is the new release date of the video? ")
            response = video_store.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_divider()
            print("Updated video:", response["video"])

        elif choice == '3':
            video_store.delete_video()

            print_divider()
            print("Video record has been deleted.")

            print_divider()
            print(video_store.get_videos_list())

        elif choice == '4':
            print_divider()
            print("Video Records: ")
            for video in video_store.get_videos_list():
                print(video)

        elif choice == '5':
            select_by = input("Would you like to select by title or id: ")
            if select_by == "title":
                title = input("Which video title would you like to select? ")
                video_store.get_single_video(title=title)
            elif select_by == "id":
                id = input("Which video id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video_store.get_single_video(id=id)
            else:
                print("Selection not valid. Please enter an id or title.")
            
            if video_store.selected_video:
                print_divider()
                print("Selected video: ", video_store.selected_video)

##### CUSTOMER CHOICES #####
        elif choice == '6':
            print("Creating a new customer record: ")
            name = input("What is the customer's name? ")
            postal_code = input("What is the customer's postal code? ")
            phone = input("What is the customer's phone number? ")
            registered_at = input("When was the customer registered? ")
            response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone, registered_at=registered_at)

            print_divider()
            print("New customer record created:", response["customer"])

        elif choice == '7':
            print(f"Updating customer record: {video_store.selected_video}")
            name = input("What is the new customer's name? ")
            postal_code = input("What is the new customer's postal code? ")
            phone = input("What is the customer's new phone number? ")
            response = video_store.update_video(name=name, postal_code=postal_code, phone=phone)

            print_divider()
            print("Updated customer:", response["customer"])

        elif choice == '8':
            video_store.delete_customer()

            print_divider()
            print("Customer record has been deleted.")

            print_divider()
            print(video_store.get_customers_list())

        elif choice == '9':
            select_by = input("Would you like to select by name or id: ")
            if select_by == "name":
                title = input("What is the customer's name that you would like to select? ")
                video_store.get_single_customer(title=title)
            elif select_by == "id":
                id = input("What is the customer's id that you would like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video_store.get_single_customer(id=id)
            else:
                print("Selection not valid. Please enter a customer's name or id.")
            
            if video_store.selected_video:
                print_divider()
                print("Selected video: ", video_store.selected_video)

        elif choice == '10':
            print_divider()
            for customer in video_store.get_customers_list():
                print(customer)

##### RENTAL CHOICES #####
        elif choice == '11':
            print_divider()
            print("Checking out a video to a customer: ")

            video_id = input("Please enter the video's id: ")
            if video_id.isnumeric():
                video_id = int(video_id)
            video = video_store.check_out_video(video_id=video_id)
            print(video)
            
            customer_id = input("Please enter the customer's id: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            customer = video_store.check_out_video(customer_id=customer_id)
            print(customer)
            
            check_out_video = video_store.check_out_video(customer_id, video_id)
            print(check_out_video)
                
            print("Selected video has been successfully checked out: ", video_store.selected_video)

        elif choice == '12':
            print_divider()
            print("Checking in a video from a customer: ")

            customer_id = input("Please enter the customer's id: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            customer = video_store.check_out_video(customer_id=customer_id)
            print(customer)

            video_id = input("Please enter the video's id: ")
            if video_id.isnumeric():
                video_id = int(video_id)
            video = video_store.check_out_video(video_id=video_id)
            print(video)
            
            check_in_video = video_store.check_in_video(customer_id, video_id)
            print(check_in_video)  
                
            print("Selected video has been successfully checked in: ", video_store.selected_video)     

##### OTHER CHOICES #####        
        elif choice == '13':
            print_divider()
            list_options()
            print_divider()

        elif choice == '14':
            play=False
            print_divider()
            print("\nThanks for using Video Store CLI!")
            

if __name__ == "__main__":
    main()
    run_cli()