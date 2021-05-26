import requests
from video_store import VideoStore
import datetime

def print_spaces():
    print("\n\n")

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def list_options():

    options = {
        "1": "List all customers",
        "2": "List all videos",
        "3": "Create a customer",
        "4": "Create a video",
        "5": "List one customer info",
        "6": "List one video info",
        "7": "Edit a customer",
        "8": "Edit a video",
        "9": "Delete a customer",
        "10": "Delete a video",
        "11": "Check out video to customer",
        "12": "Check in video",
        "13": "List all options",
        "14": "Quit"
        }
    print_spaces()
    print_spaces()
    print("*******  WELCOME DEAR EMPLOYEE TO YOUR FAVORITE VIDEOBUSTER CLI  *******")
    print_spaces()
    print(
"                         .-.   .-.,-.,---.  ,-.                                     \n"                         
"                          \ \ / / | || .-.\ | |                                     \n"                         
"                           \ V /  | || `-'/ | |                                     \n"                         
"                            ) /   | ||   (  | |                                     \n"                         
"                           (_)    | || |\ \ | |                                     \n"                         
"                                  `-'|_| \_\`-'                                     \n"                                                                                          
".-.   .-.,-. ,'|\"\   ,---.   .---.  ,---.   .-. .-.   .---.  _______ ,---.  ,---.  \n" 
" \ \ / / | | | |\ \  | .-'  / .-. ) | .-.\  | | | |  ( .-._)|__   __|| .-'  | .-.\  \n" 
"  \ V /  | | | | \ \ | `-.  | | |(_)| |-' \ | | | | (_) \     )| |   | `-.  | `-'/  \n" 
"   ) /   | | | |  \ \| .-'  | | | | | |--. \| | | | _  \ \   (_) |   | .-'  |   (   \n" 
"  (_)    | | /(|`-' /|  `--.\ `-' / | |`-' /| `-' |( `-'  )    | |   |  `--.| |\ \  \n"
"         `-'(__)`--' /( __.' )---'  /( `--' `---(_) `----'     `-'   /( __.'|_| \_\ \n" 
"                    (__)    (_)    (__)                             (__)            \n"
)
    print_spaces()
    print("These are the actions you can perform as an employee.\n")
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    return options


def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("\nWhat would you like to do? Select 11 to see all options again.\n")
        choice = input("Make your selection using the option number: ")
    
    return choice

def run_cli(play=True):

    #initialize video_store
    video_store = VideoStore(url="https://viri-video-store-app.herokuapp.com/")
    
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, video_store)

        if choice=='1':
            print("\n****\n")
            for customer in video_store.list_customers():
                print(f"Customer # {customer['id']} - Name: {customer['name']}.  Phone number: {customer['phone']}")
            print("\n****\n")

        elif choice=='2':
            print("\n****\n")
            for video in video_store.list_videos():
                print(f"Video id {video['id']} - Title: \"{video['title']}\". Available intenvory: {video['available_inventory']}")
                # print(video)
            print("\n****\n")

        elif choice=='3':
            print("\n****\n")
            print("Great! Let's create a new customer.")
            name=input("What is the name? ")
            postal_code=input("What is the postal code? ")
            phone=input("What is the phone? ") 
            response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone)
            print("New customer created with id: ", response["id"])

        elif choice=='4':
            print("\n****\n")
            print("Great! Let's create a new video.")
            title=input("What is the title? ")
            release_date=input("What is the release date? ")
            #1979-01-18
            total_inventory=input("What is the total inventory? ") 
            response = video_store.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print(response)
            print("New video created with id: ", response["id"])
        
        elif choice=='5':
            print("\n****\n")
            print("Great! Let's get your customer.")
            id_customer=input("What is the id you want? ")
            response = video_store.get_customer(id=id_customer)
            print(f"\nCustomer # {response['id']} - Name: {response['name']}.  Phone number: {response['phone']}")
        
        elif choice=='6':
            print("\n****\n")
            print("Great! Let's get your movie info.")
            id_video=input("What is the id you want? ")
            response = video_store.get_video(id=id_video)
            checkout_videos = response['total_inventory'] - response['available_inventory']
            print(f"\nVideo id {response['id']} - Title: \"{response['title']}\". Available intenvory: {response['available_inventory']}. Check-out inventory: {checkout_videos}")

        elif choice=='7':
            print("\n****\n")
            print(f"Great! Let's update your customer info\n")
            id_customer=input("What is the customer id you want to edit? ")
            name=input("What is the new name of your customer? ")
            postal_code=input("What is the new postal code of your customer? ")
            phone=input("What is the new phone number of your customer? ")
            response = video_store.update_customer(id_customer=id_customer, name=name, postal_code=postal_code, phone=phone)
            print(f"\nCustomer # {response['id']} with new name {response['name']} has been updated successfully!")
        
        elif choice=='8':
            print("\n****\n")
            print(f"Great! Let's update your video info\n")
            id_video=input("What is the video id you want to edit? ")
            title=input("What is the new title of your movie? ")
            release_date=input("What is the release date of this movie? ")
            total_inventory=input("What is the total inventory of this movie? ")
            response = video_store.update_video(id_video=id_video, title=title, release_date=release_date, total_inventory=total_inventory)
            print(f"\nVideo id {response['id']} with new title \"{response['title']}\" has been updated successfully!")
        
        elif choice=='9':
            print("\n****\n")
            print(f"Okay! Let's delete that customer")
            id_customer=input("What is the customer id you want to disappear? ")
            video_store.delete_customer(id_customer)
            print("Customer has been deleted.")
        
        elif choice=='10':
            print("\n****\n")
            print(f"Okay! Let's delete that video")
            id_video=input("What is the video id you want to disappear? ")
            video_store.delete_video(id_video)
            print("Video has been deleted.")
        
        elif choice=='11':
            print("\n****\n")
            print(f"Great! Let's check-out a video")
            customer_id=input("Please provide the customer id: ")
            video_title=input("Please provide the title of your movie: ")
            video = video_store.get_video(title=video_title)
            # print("Esto es lo que recibo como video_id: ", video_id)
            response = video_store.checkout_video(customer_id, video["id"])
            print("Check-out complete! This customer has ", response["videos_checked_out_count"],\
                " videos checked out so far. Your due date for this movie is: ",response["due_date"])



        # elif choice=='3':
        #     select_by = input("Would you like to select by? Enter title or id: ")
        #     if select_by=="title":
        #         title = input("Which task title would you like to select? ")
        #         task_list.get_task(title=title)
        #     elif select_by=="id":
        #         id = input("Which task id would you like to select? ")
        #         if id.isnumeric():
        #             id = int(id)
        #             task_list.get_task(id=id)
        #     else:
        #         print("Could not select. Please enter id or title.")
            
        #     if task_list.selected_task:
        #         print_stars()
        #         print("Selected task: ", task_list.selected_task)

        




        # elif choice=='6':
        #     response = task_list.mark_complete()

        #     print_stars()
        #     print("Completed task: ", response["task"])

        # elif choice=='7':
        #     response = task_list.mark_incomplete()

        #     print_stars()
        #     print("Incomplete task: ", response["task"])

        # elif choice=='8':
        #     for task in task_list.list_tasks():
        #         task_list.get_task(id=task['id'])
        #         task_list.delete_task()

        #     print_stars()
        #     print("Deleted all tasks.")

        elif choice=='13':
            print("\n****\n")
            list_options()

        elif choice=='14':
            play=False
            print_spaces()
            print("== Thank you so much for your service dear employee. We hope to see you soon! ==\n")
            print("Session ended.")


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