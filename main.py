import requests
from video_store import VideoStore

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

#consider adding a check for date feature to catch errors in date entry (not string)


def run_cli(play=True):

    video_store = VideoStore(url=URL)

    options = list_options()

    while play == True:

        choice = make_choice(options, video_store)

        # "1": "Add a Video" 
        if choice == '1':

            print("Ok! Let's record a new video.")
            title=input("What is the title of the movie? ")
            release_date=input("What date (MM-DD-YYYY) was the movie released? ")
            total_inventory=input("How many copies of this movie are being added to the store? ")

            response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print(f"New video ID: {response['id']}")

        # "2": "Edit a Video"
        elif choice=='2':
            
            video = select_video(video_store)
            if video == None:
                print("No video with that ID or title found.")
            else:
                # potential place to add more elements of choice for user
                # ask if they want to update each attribute of the movie
                title=input("What is the title of the movie? ")
                release_date=input("What date (MM-DD-YYYY) was the movie released? ")
                total_inventory=input("How many copies of this movie does the store own? ")
                #available_inventory is NOT currently updating
                response = video_store.update_video(
                                            title=title, 
                                            release_date=release_date, 
                                            total_inventory=total_inventory)
                print(f"Updates successfully made to video ID: {response['id']}")
                print(f">>>Title: {response['title']}")
                print(f">>>Release Date: {response['release_date']}")
                print(f">>>Total Inventory: {response['total_inventory']}")
                print(f">>>Available Inventory: {response['available_inventory']}")
        
        # "3": "Delete a Video"
        elif choice=='3':
            video = select_video(video_store)
            if video == None:
                print("No video with that ID or title found.")
            else:
                print(f"You selected this video to delete: {video}")
                print(f"Are you sure you want to delete?")
                certainty = input(f"Select Y or N: ")
                if certainty == "Y":
                    video_store.delete_video()
                    print(f"Video #{video['id']} successfully deleted.")
                # do something if they select N, don't want to delete
        
        # "4": "Get all Videos"
        elif choice=='4':
            for video in video_store.list_videos():
                print(video)
        
        # "5": "Get One Video"
        elif choice=='5':
            video = select_video(video_store)
            if video == None:
                print("No video with that ID or title found.")
            else:
                print(f"Information for video #{video['id']}:")
                print(f">>>Title: {video['title']}")
                print(f">>>Release Date: {video['release_date']}")
                print(f">>>Total Inventory: {video['total_inventory']}")
                print(f">>>Available Inventory: {video['available_inventory']}")

        #Option 6: Add a Customer
        elif choice=='6':

            print("Ok! Let's add a new customer.")
            name=input("What is the customer's name? ")
            postal_code=input("What is the customer's postal code? ")
            phone=input("What is the customer's phone number? ")

            response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone)
            print(f"New customer ID: {response['id']}")
        
        #Option 7: Edit a Customer
        elif choice=='7':

            customer = select_customer(video_store)
            if customer == None:
                print("No customer with that ID or name found.")
            else:
                # potential place to add more elements of choice for user
                # ask if they want to update each attribute of the customer
                name=input("What is the customer's name? ")
                postal_code=input("What is the customer's postal code? ")
                phone=input("What is the customer's phone number? ")
                #not a place to adjust registration OR videos checked out (managed in rentals)
                response = video_store.update_customer(
                                            name=name, 
                                            postal_code=postal_code, 
                                            phone=phone)
                print(f"Updates successfully made to customer ID: {response['id']}")
                print(f">>>Name: {response['name']}")
                print(f">>>Postal Code: {response['postal_code']}")
                print(f">>>Phone: {response['phone']}")
                print(f">>>Registered At: {response['registered_at']}")
                print(f">>>Videos Checked Out: {response['videos_checked_out_count']}")

        #Option 8: Delete a Customer
        elif choice=='8':

            customer = select_customer(video_store)
            if customer == None:
                print("No customer with that ID or name found.")
            else:
                print(f"You selected this video to delete: {customer}")
                print(f"Are you sure you want to delete?")
                certainty = input(f"Select Y or N: ")
                if certainty == "Y":
                    video_store.delete_customer()
                    print(f"Customer #{customer['id']} successfully deleted.")
                # do something if they select N, don't want to delete

        #Option 9: Get info for ONE Customer
        elif choice=='9':
            customer = select_customer(video_store)
            if customer == None:
                print("No customer with that ID or name found.")
            else:
                print(f"Information for customer #{customer['id']}:")
                print(f">>>Name: {customer['name']}")
                print(f">>>Postal Code: {customer['postal_code']}")
                print(f">>>Phone: {customer['phone']}")
                print(f">>>Registered At: {customer['registered_at']}")
                print(f">>>Videos Checked Out: {customer['videos_checked_out_count']}")

        #Option 10: Get info for ALL Customers
        elif choice=='10':
            for customer in video_store.list_customers():
                print(customer)

        #Option 11: Check OUT a Video
        elif choice=='11':
            # choose customer
            customer = select_customer(video_store)
            if customer == None:
                print("No customer with that ID or name found.")

            # choose video
            video = select_video(video_store)
            if video == None:
                print("No video with that ID or title found.")

            # check out video to customer
            rental = video_store.check_out_video_to_customer(
                customer_id=customer['id'],
                video_id=video['id']
            )
            # return success message
            if "error" in rental:
                print(rental['error'])
            else:
                print(f"Video #{rental['video_id']} checked out to Customer #{rental['customer_id']}")
                print(f"Video due back on {rental['due_date']}")
        
        #Option 12: Check IN a Video
        elif choice=='12':
            # choose customer
            customer = select_customer(video_store)
            if customer == None:
                print("No customer with that ID or name found.")

            # choose video
            video = select_video(video_store)
            if video == None:
                print("No video with that ID or title found.")

            # check in video to customer
            rental = video_store.check_in_video_to_customer(
                customer_id=customer['id'],
                video_id=video['id']
            )
            # return success message
            if "error" in rental:
                print(rental['error'])
            else:
                print(f"Video #{rental['video_id']} checked in to Customer #{rental['customer_id']}")


        elif choice=='13':
            play=False
            print("Bye!")
        
        # elif choice=='M':
        #     list_options()

    # print("WELCOME TO RETRO VIDEO STORE")
    # print("Select the information you want to interact with: ")
    # for choice_num in options:
    #     print(f"Option {choice_num}. {options[choice_num]}")
    
    # choice = input
    # response = requests.get(URL + "/videos")
    # print(response.json())


# if __name__ == "__main__":
#     main()


def list_options():

    options = {
        "1": "Add a Video", 
        "2": "Edit a Video",
        "3": "Delete a Video",
        "4": "Get all Videos",
        "5": "Get One Video",
        "6": "Add a Customer",
        "7": "Edit a Customer",
        "8": "Delete a Customer",
        "9": "Get Customer Info for One Customer",
        "10": "Get Customer Info for All Customers",
        "11": "Check OUT a Video",
        "12": "Check IN a Video",
        "13": "QUIT"
        }
    
    print("WELCOME TO RETRO VIDEO STORE")
    print("These are the actions you can perform: ")

    for choice_num in options:
        print(f"Option {choice_num}: {options[choice_num]}")
    
    return options


def make_choice(options, video_store):

    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do?")
        choice = input("Make your selection using the option number: ")

    # if choice in ['4','5','6','7'] and task_list.selected_task == None:
    #     print("You must select a task before updating it, deleting it, marking it complete, or marking it incomplete.")
    #     print("Let's select a task!")
    #     choice = "3"
    
    return choice

def select_video(video_store):
    print("Ok, let's select a video.")
    select_by = input("Would you like to select by title (1) or ID (2)? ")
    if select_by=="1":
        title = input("Enter the name of the movie: ")
        video_store.get_video(title=title)
    elif select_by=="2":
        id = input("Enter the movie ID number: ")
        if id.isnumeric():
            id = int(id)
            video_store.get_video(id=id)
    # need a way to catch dumb user who doesn't enter 1 or 2 
    return video_store.selected_video 

def select_customer(video_store):
    print("Ok, let's select a customer.")
    select_by = input("Would you like to select by name (1) or ID (2)? ")
    if select_by=="1":
        name = input("Enter the name of the customer: ")
        video_store.get_customer(name=name)
    elif select_by=="2":
        id = input("Enter the customer ID number: ")
        if id.isnumeric():
            id = int(id)
            video_store.get_customer(id=id)
    # need a way to catch dumb user who doesn't enter 1 or 2 
    return video_store.selected_customer 

def video_options():
    pass

def customer_options():
    pass

def rental_options():
    pass 

run_cli()