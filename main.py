import requests
from video_store import VideoStore
import datetime

def print_spaces():
    print("\n\n")

def print_new_line():
    print(
       "\n █████ █████ █████ █████ █████ █████ █████ █████ █████ \n"
    )

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def list_models():
    models = {
        "1": "Customer Menu",
        "2": "Video Menu",
        "3": "Rentals Management",
        "4": "List all options",
        "5": "Quit"
    }

    print_spaces()
    print_spaces()
    print(" *********       WELCOME DEAR EMPLOYEE       *********")
    print_new_line()
    print(
    "       ██████╗ ███████╗████████╗██████╗  ██████╗     \n"
    "       ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗    \n"
    "       ██████╔╝█████╗     ██║   ██████╔╝██║   ██║    \n"
    "       ██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║    \n"
    "       ██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝    \n"
    "       ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝     \n\n"
                                              
    "       ██╗   ██╗██╗██████╗ ███████╗ ██████╗          \n"
    "       ██║   ██║██║██╔══██╗██╔════╝██╔═══██╗         \n"
    "       ██║   ██║██║██║  ██║█████╗  ██║   ██║         \n"
    "       ╚██╗ ██╔╝██║██║  ██║██╔══╝  ██║   ██║         \n"
    "        ╚████╔╝ ██║██████╔╝███████╗╚██████╔╝         \n"
    "          ╚═══╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝          \n"
                        
)
    print_new_line()
    print_spaces()
    print("This is the information you have access to as an awesome employee.\n")
    for choice_num in models:
        print(f"Option {choice_num}. {models[choice_num]}")

    return models


def list_video_options():
    options = {
        "1": "Create a video",
        "2": "List all videos",
        "3": "List one video info",
        "4": "Edit a video",
        "5": "Delete a video",
        "6": "List all options",
        "7": "Return to the main manu"
        }
    print_spaces()
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    return options


def list_customer_options():
    options = {
        "1": "Create a customer",
        "2": "List all customers",
        "3": "List one customer info",
        "4": "Edit a customer",
        "5": "Delete a customer",
        "6": "List all options",
        "7": "Return to the main manu"
        }
    print_spaces()
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    return options


def list_rental_options():
    options = {
        "1": "Check-out video",
        "2": "Check-in video",
        "3": "Get rentals by customer",
        "4": "Get video rental information",
        "8": "Return to the main manu"
        }
    print_spaces()
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    return options


def select_option(models, video_store):
    valid_options = models.keys()
    choice = None
    while choice not in valid_options:
        print("\nWhat info would you like to access? Select 4 to see all options again.\n")
        choice = input("Make your selection using the option number: ")
    
    return choice


def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("\nWhat would you like to do? Select 6 to see all options again.\n")
        choice = input("Make your selection using the option number: ")
    
    return choice


def run_cli(play=True):

    #initialize video_store
    video_store = VideoStore(url="https://viri-video-store-app.herokuapp.com/")
    # video_store = VideoStore(url=BACKUP_URL)
    
    #print models options
    models = list_models()

    while play==True:

        choice = select_option(models, video_store)

        if choice=='1':
            subplay=True
            print_new_line()
            print("*****   CUSTOMER MENU    *****")
            options = list_customer_options()
            
            while subplay==True:
                subchoice = make_choice(options, video_store)

                if subchoice=='1':
                    # print("\n****\n")
                    print_new_line()
                    print("Great! Let's create a new customer.")
                    name=input("What is the name? ")
                    postal_code=input("What is the postal code? ")
                    phone=input("What is the phone? ") 
                    response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone)
                    print("New customer created with id: ", response["id"])

                elif subchoice=='2':
                    # print("\n****\n")
                    print_new_line()
                    for customer in video_store.list_customers():
                        print(f"Customer # {customer['id']} - Name: {customer['name']}.  Phone number: {customer['phone']}")
                    print("\n****\n")
                
                elif subchoice=='3':
                    # print("\n****\n")
                    print_new_line()
                    print("Great! Let's get your customer.")
                    id_customer=input("What is the id you want? ")
                    response = video_store.get_customer(id=int(id_customer))
                    if response and "message" not in response.keys():
                        print("\n**** Customer Information:")
                        print(f"\nCustomer # {response['id']} - Name: {response['name']}.  Phone number: {response['phone']}")
                    else:
                        print(f"\nSorry, but customer {id_customer} doesn't exist.")

                elif subchoice=='4':
                    # print("\n****\n")
                    print_new_line()
                    print(f"Great! Let's update your customer info\n")
                    id_customer=input("What is the customer id you want to edit? ")
                    name=input("What is the new name of your customer? ")
                    postal_code=input("What is the new postal code of your customer? ")
                    phone=input("What is the new phone number of your customer? ")
                    response = video_store.update_customer(id_customer=id_customer, name=name, postal_code=postal_code, phone=phone)
                    print(f"\nCustomer # {response['id']} with new name {response['name']} has been updated successfully!")

                elif subchoice=='5':
                    # print("\n****\n")
                    print_new_line()
                    print(f"Okay! Let's delete that customer")
                    id_customer=input("What is the customer id you want to disappear? ")
                    response = video_store.get_customer(id=id_customer)
                    if response and "message" not in response.keys():
                        video_store.delete_customer(id_customer)
                        print("Customer has been deleted.")
                    else:
                        print("Oops! Looks like this customer has been already deleted because doesn't exist.")
                
                elif subchoice=='6':
                    # print("\n****\n")
                    print_new_line()
                    list_customer_options()

                elif subchoice=='7':
                    subplay=False
                    print_spaces()
                    print("== Thank you so much for visiting our CUSTOMER information. We hope to see you soon! ==\n")
                    print_spaces()
                    list_models()

        elif choice=='2':
            subplay=True
            print_new_line()
            print("*****   VIDEO MENU    *****")
            options = list_video_options()
            
            while subplay==True:
                subchoice = make_choice(options, video_store)

                if subchoice=='1':
                    print_new_line()
                    # print("\n****\n")
                    print("Great! Let's create a new video.")
                    title=input("What is the title? ")
                    release_date=input("What is the release date? ")
                    #Release date format example: 1979-01-18
                    total_inventory=input("What is the total inventory? ") 
                    response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
                    print("New video created with id: ", response["id"])

                elif subchoice=='2':
                    # print("\n****\n")
                    print_new_line()
                    for video in video_store.list_videos():
                        print(f"Video id {video['id']} - Title: \"{video['title']}\". ")
                        #print(f"Video id {video['id']} - Title: \"{video['title']}\". Available intenvory: {video['available_inventory']}")
                    print("\n****\n")
                
                elif subchoice=='3':
                    # print("\n****\n")
                    print_new_line()
                    print("Great! Let's get your movie info.")
                    id_video=input("What is the id you want? ")
                    response = video_store.get_video(id=id_video)
                    if response and "message" not in response.keys():
                        checkout_videos = response['total_inventory'] - response['available_inventory']
                        print("\n**** Video Information:")
                        print(f"\nVideo id {response['id']} - Title: \"{response['title']}\". Available intenvory: {response['available_inventory']}. Check-out inventory: {checkout_videos}")
                    else:
                        print(f"\nSorry, but video # {id_video} doesn't exist.")

                elif subchoice=='4':
                    # print("\n****\n")
                    print_new_line()
                    print(f"Great! Let's update your video info\n")
                    id_video=input("What is the video id you want to edit? ")
                    title=input("What is the new title of your movie? ")
                    release_date=input("What is the release date of this movie? ")
                    total_inventory=input("What is the total inventory of this movie? ")
                    response = video_store.update_video(id_video=id_video, title=title, release_date=release_date, total_inventory=total_inventory)
                    print(f"\nVideo id {response['id']} with new title \"{response['title']}\" has been updated successfully!")

                elif subchoice=='5':
                    # print("\n****\n")
                    print_new_line()
                    print(f"Okay! Let's delete that video")
                    id_video=input("What is the video id you want to disappear? ")
                    response = video_store.get_video(id=id_video)
                    if response and "message" not in response.keys():
                        video_store.delete_video(id_video)
                        print("Video has been deleted.")
                    else:
                        print("Oops! Looks like this video has been already deleted because doesn't exist.")

                elif subchoice=='6':
                    # print("\n****\n")
                    print_new_line()
                    list_video_options()

                elif subchoice=='7':
                    subplay=False
                    print_spaces()
                    print("== Thank you so much for visiting our CUSTOMER information. We hope to see you soon! ==\n")
                    print_spaces()
                    print_new_line()
                    list_models()


        elif choice=='3':
            subplay=True
            print_new_line()
            print("*****   RENTALS MENU    *****")
            options = list_rental_options()
            
            while subplay==True:
                subchoice = make_choice(options, video_store)

                if subchoice=='1':
                    print_new_line()
                    # print("\n****\n")
                    print(f"Great! Let's check-out a video")
                    customer_id=input("Please provide the customer id: ")
                    customer = video_store.get_customer(id=customer_id)
                    video_title=input("Please provide the title of your movie: ")
                    video = video_store.get_video(title=video_title)
                    if "message" not in video.keys() and "message" not in customer.keys():
                        response = video_store.checkout_video(customer_id, video['id'])
                        print("Check-out complete! This customer has ", response["videos_checked_out_count"],\
                            " videos checked out so far. Your due date for this movie is: ",response["due_date"])
                    else:
                        print("\nSorry. One or more of the ids provided are invalid.\n")

                
                elif subchoice=='2':
                    print_new_line()
                    # print("\n****\n")
                    print(f"Awesome! Let's check-in that video")
                    customer_id=input("Please provide the customer id: ")
                    customer = video_store.get_customer(id=customer_id)
                    video_title=input("Please provide the title of your movie: ")
                    video = video_store.get_video(title=video_title)
                    if "message" not in video.keys() and "message" not in customer.keys():
                        response = video_store.checkin_video(customer_id, video['id'])
                        #print("THIS IS MY RESPONSE:  ",response)
                        print("Check-in complete! This video has now an inventory of ", response['available_inventory'])
                    else:
                        print("\nSorry. One or more of the ids provided are invalid.\n")

                elif subchoice=='3':
                    print_new_line()
                    # print("\n****\n")
                    print(f"Awesome! Let's find how many rentals has a customer.")
                    customer_id=input("Please provide the customer id: ")
                    customer = video_store.get_rentals_by_customer(customer_id=customer_id)
                    print(f"\nThis customer has {len(customer)} movies checked-out.")
                    if customer:
                        print("These are the titles: ")
                        for rental in customer:
                            print(f"\n- Movie title: \"{rental['title']}\" - Due date: {rental['due_date']}.")
                    else:
                        print("No more information to display.")

                
                elif subchoice=='4':
                    print_new_line()
                    # print("\n****\n")
                    print(f"Awesome! Let's find out who checked-out a video.")
                    customer_id=input("Please provide the customer id: ")
                    customer = video_store.get_rentals_by_customer(customer_id=customer_id)
                    print(f"\nThis customer has {len(customer)} movies checked-out.")
                    if customer:
                        print("These are the titles: ")
                        for rental in customer:
                            print(f"\n- Movie title: \"{rental['title']}\" - Due date: {rental['due_date']}.")
                    else:
                        print("No more information to display.")
                
                elif subchoice=='8':
                    subplay=False
                    print_spaces()
                    print("== Thank you so much for visiting our CUSTOMER information. We hope to see you soon! ==\n")
                    print_spaces()
                    print_new_line()
                    list_models()

        elif choice=='4':
            print_new_line()
            # print("\n****\n")
            list_models()


run_cli()




"""
This was at the beginning:

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    response = requests.get(BACKUP_URL + "/videos")
    print(response.json())
    


if __name__ == "__main__":
    main()
"""