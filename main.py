import requests

from video_store_API_stuff import Customer, Video, Rental


URL = "http://127.0.0.1:5000"

BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

# def main():
#     print("\n WELCOME TO RETRO VIDEO STORE")
#     pass

# if __name__ == "__main__":
#     main()

def print_frogges():

    print("\n🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 🐸 \n")


def list_options():
    """
    input: none
    output: presents a list of options the end-user can choose from 
    """

    options = {
        "1": "List all videos",
        "2": "Add a video", 
        "3": "Select a video",
        "4": "Edit selected video",
        "5": "Delete selected video", 
        "6": "List all customers",
        "7": "Add a customer",
        "8": "Select a customer",
        "9": "Update a customer",
        "10": "Delete a customer",
        "11": "Check out a video to a customer",
        "12": "Check in a video from a customer",
        "13": "List all options",
        "14": "Quit"
        }

    print_frogges()
    print("WELCOME TO RETRO VIDEO STORE\n")
    print("These are the actions you can perform:")
    print_frogges()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_frogges()

    return options


def make_choice(options, customer, video):
    """
    input: the list of options from list_options()
    output: 
    """
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("\nWhat would you like to do? Select 13 to see all options again, OR\n")
        choice = input("\nMake your selection using the option number: ")

    if choice in ['4','5'] and video.selected_video == None:
        print("\nYou must select a video before updating it or deleting it.")
        print("\nLet's select a video!")
        choice = "3"

    if choice in ['9', '10'] and customer.selected_customer == None:
        print("\nYou must select a customer record before updating it or deleting it.")
        print("\nLet's select a customer!")
        choice = "8"
    
    return choice
    

def run_cli(play=True):
    """
    input
    output
    """

    customers_list = Customer()
    videos_list = Video()
    rental_action = Rental()

    options = list_options()

    while play==True:

        choice = make_choice(options, customers_list, videos_list)

        customers_list.print_selected_customer()
        videos_list.print_selected_video()

        # "List all videos"
        if choice=='1':
            print_frogges()
            for video in videos_list.get_all_videos():
                print(video)


        # "Add a video"
        elif choice=='2':
            title = input("\nEnter video title:\n")
            release_date = input("Enter video release date:\n")
            total_inventory = input("Enter total starting inventory:\n")
            response = videos_list.add_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_frogges()
            print("\nSuccessfully added new video with ID:", response["id"])


        # "Select a video"
        elif choice=='3':
            select_by = input("\nWhat would you like to select by? Enter title or id: ")
            if select_by=="title":
                title = input("\nWhich video title would you like to select? ")
                videos_list.get_one_video(title=title)
            elif select_by=="id":
                id = input("\nWhich video id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    videos_list.get_one_video(id=id)
            else:
                print("\nCould not select. Please enter id or title.")
            
            if videos_list.selected_video:
                print_frogges()
                print("\nSelected video: ", videos_list.selected_video)


        # "Edit selected video"
        elif choice=='4':
            print(f"You've chosen to update the video: {videos_list.selected_video}")
            title=input("\nWhat is the new title of this video? ")
            release_date=input("\nWhat is the new release date for this video? ")
            total_inventory=input("\nWhat is the new total inventory for this video? ")
            response = videos_list.edit_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_frogges()
            print("\nSuccessfully updated video with ID:", response["id"])
            

        # "Delete selected video"
        elif choice=='5':
            videos_list.delete_video()

            print_frogges()
            print("Video has been deleted!")


        # "List all customers"
        elif choice=='6':
            print_frogges()
            for customer in customers_list.get_all_customers():
                print(customer)


        # "Add a customer"
        elif choice=='7':
            name = input("\nEnter customer name: ")
            postal_code = input("\nEnter customer's postal code: ")
            phone = input("\nEnter customer's phone number: ")
            response = customers_list.add_customer(name=name, postal_code=postal_code, phone=phone)

            print_frogges()
            print("\nSuccessfully added new customer with ID:", response["id"], response["registered_at"])


        # "Select a customer"
        elif choice=='8':
            select_by = input("\nWould you like to select by? Enter name or id: ")
            if select_by=="name":
                title = input("\nWhich customer name would you like to select? ")
                customers_list.get_one_customer(name=name)
            elif select_by=="id":
                id = input("\nWhich customer id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    customers_list.get_one_customer(id=id)
            else:
                print("\nCould not select. Please enter id or title.")
            
            if customers_list.selected_customer:
                print_frogges()
                print("\nSelected customer: ", customers_list.selected_customer)


        # "Update a customer"
        elif choice=='9':
            print(f"\nYou've chosen to update customer: {customers_list.selected_customer}")
            name=input("\nWhat is the new name of this customer? ")
            postal_code=input("\nWhat is the new postal code of this customer? ")
            phone=input("\nWhat is the new phone number of this customer? ")
            response = customers_list.update_customer(name=name, postal_code=postal_code, phone=phone)

            print_frogges()
            print("\nSuccessfully updated customer with ID:", response["id"])


        # "Delete a customer"
        elif choice=='10':
            customers_list.delete_customer()

            print_frogges()
            print("\nCustomer has been deleted!")


        # "Check out a video to a customer"
        elif choice=='11':
            customer_id=input("\nPlease enter ID of customer: ")
            video_id=input("\nPlease enter ID of video to be checked out: ")

            response = rental_action.check_out_video(customer_id, video_id)

            print_frogges()
            print(response)


        # "Check in a video from a customer"
        elif choice=='12':
            customer_id=input("\nPlease enter ID of customer: ")
            video_id=input("\nPlease enter ID of video to be checked in: ")

            response = rental_action.check_in_video(customer_id, video_id)

            print_frogges()
            print(response)


        # "List all options"
        elif choice=='13':
            list_options()


        # "Quit"
        elif choice=='14':
            play=False
            print("\n K BYE")

        print_frogges()

run_cli()
