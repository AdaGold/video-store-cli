import requests
from customer import Customer
from rental import Rental
from video import Video

URL = "https://retro-video-store-api.herokuapp.com"
def print_stars():
    print("\n**************************\n")

def list_options():
    options = {
        "1": "Add a video",
        "2": "Select a video",
        "3": "Browse video catalog",
        "4": "Add a *new* customer",
        "5": "Get information on one customer",
        "6": "Get information on all customers",
        "7": "Check out a video",
        "8": "Check in a video",
        "9": "List all options",
        "0": "Quit"
    }

    print_stars()
    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    
    print_stars()

    return options

# 
def make_choice(options, customer, video, rental):
    valid_choices = options.keys()

    while choice not in valid_choices:
        print("What would you like to do? Select 9 to see all options again")
        choice = input("Make your selection using the option number: ")
    
    return choice

def main(play=True):
    # initialize instances
    video = Video(URL)
    customer = Customer(URL)
    rental = Rental(URL)
    options = list_options()
    
    while play:
        choice = make_choice(options, video, customer)

    # Option 1: Add a video
    if choice == '1':
        print("Preparing to add video...")
        title = input("What is the name of the video?")
        release_date = input("What is the video's release date?")
        total_inventory = input("What is the total inventory for this video?")
        response = video.add_video(title=title, release_date=release_date, total_inventory=total_inventory)

        print("New video:", response["video"])
    
    # Option 2: Select a video
    elif choice == '2':
        select = input("How would you like to select your video: by title, id, or release date?")
        if select == "title":
            title = input("Which title are you looking for?")
            video.get_video(title=title)
        elif select == "id":
            id = input("Please provide the ID")
            video.get_video(id=int(id))
        elif select == "release date":
            release_date = input("Please provide the release date")
            video.get_video(release_date=release_date)
        else:
            print("Please enter one of the following options: 'title', 'id', or 'release date'")
        
        video.print_selected()

        # next step for selected video
        if video.selected_video:
            next_step = input("What would you like to do with this video? Enter 1 to edit or 2 to delete")

            # Edit the selected video
            if next_step == '1':
                print(f"Preparing to edit {video.selected_video['title']}...")
                edit_option = input("What would you like to edit: title, release date, or total inventory?")
                if edit_option == "title":
                    title = input("Please provide the desired title")
                elif edit_option == "release date":
                    release_date = input("Please provide the desired release date?")
                elif edit_option == "total inventory":
                    total_inventory = input("Please provide the desired total inventory amount")
                response = video.update_video(title, release_date, total_inventory)

                print("Video updated:", response["video"])

            # Delete the selected video
            elif next_step == '2':
                print(f"{video.selected_video['title']} will be deleted")
                video.delete_video()
        

    # Option 3: Browse video catalog
    elif choice == '3':
        print(video.list_videos())
    
    # Option 4: Add a *new* customer
    elif choice == '4':
        print("Preparing to add a new customer...")
        name = input("Please provide the customer's name ")
        phone = input("Please provide the customer's phone number ")
        postal_code = input("Please provide the customer's postal code ")

        response = customer.add_customer(name=name, phone=phone, postal_code=postal_code)
        print("Customer added:", response["name"])
    
    # Option 5: Get information on one customer
    elif choice == '5':
        select = input("How would you like to select your video: by name, phone, or id?")
        if select == "name":
            name = input("Please provide the customer's name ")
            customer.get_customer(name=name)
        
        elif select == "phone":
            phone = input("Please provide the customer's phone number ")
            customer.get_customer(phone=phone)
        
        elif select == 'id':
            id = input("Please provide the customer ID ")
            customer.get_customer(id=int(id))
        
        else:
            print("Please enter one of the following options: 'name', 'phone', or 'id'")
        
        customer.print_selected()

        # next step for selected customer
        if customer.selected_customer:
            next_step = input("What would you like to do with this customer? Enter 1 to edit or 2 to delete")

            # Edit the selected customer
            if next_step == '1':
                print(f"Preparing to edit {customer.selected_customer['name']}...")
                edit_option = input("What would you like to edit: name, phone, or postal number?")
                if edit_option == 'name':
                    name = input("Please provide the customer's name ")
                if edit_option == 'phone':
                    phone = input("Please provide the customer's phone number ")
                if edit_option == 'postal code':
                    postal_code = input("Please provide the customer's postal code ")
                
                response = customer.update_customer(name, phone, postal_code)

            # Delete the selected customer
            elif next_step == '2':
                print(f"{customer.selected_customer['name']} will be deleted")
                customer.delete_customer()

    # Option 6: Get information on all customers
    elif choice == '6':
        print(customer.list_customers())
    
    # Option 7: Check out a video
    elif choice == '7':
        customer_id = input("Please provide the ID of the customer who will be renting a video ")
        video_id = input("Please provide the ID of the video they would like to rent ")
        response = rental.check_out(int(customer_id), int(video_id))
        print(response)

        if response.status_code != 200:
            print("The data provided was not sufficient, and the transaction is being cancelled")
        else:
            print("Thank you very much for your business! Enjoy your video!")
            



if __name__ == "__main__":
    main()