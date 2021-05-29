import requests
from video_store import VideoStore
from constants import *

def print_divider():
    print("^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
  
def print_line():
    print("----------------8<-------------[ VIP here ]------------------")
    
def list_options(options, WELCOME_MSG, info):
    print_divider()
    print(WELCOME_MSG)
    print_divider()
    
    print(info)
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")
    print_divider()
    return options

def make_choice(options, msg):
    valid_choice = options.keys()
    choice = None
    
    while choice not in valid_choice:
        print("What would you like to do?")
        choice = input(msg)
    return choice
  
def back_to_main_menu():
    main_menu_options = list_options(MAIN_MENU, WELCOME_BACK, MAIN_MENU_INFO)
    return make_choice(main_menu_options, MAIN_MSG)

  
def valid_id(id, video_store, category):
    if id.isnumeric():
        id = int(id)
        if category == "customer":
            customer = video_store.select_customer(id=id)
            if customer.get("details"):
                print("!Customer not found!")
                return False
            return customer
        elif category == "video":
            video = video_store.select_video(id=id)
            if video.get("details"):
                print("!Video not found!")
                return False
            return video
    else:
        print("Please provide a valid number!")
    
def main(play=True):
    print(LOGO)
    video_store = VideoStore("https://weishan-video-store.herokuapp.com/")
    main_menu_options = list_options(MAIN_MENU, WELCOME_MSG, MAIN_MENU_INFO)
    main_menu_choice = make_choice(main_menu_options, MAIN_MSG)
    
    while play==True:
        if main_menu_choice == "1":
            customer_options = list_options(CUSTOMER_MENU, "Customer Menu", CUSTOMER_INFO)
            customer_choice = make_choice(customer_options, CUSTOMER_MSG)
            if customer_choice == "1":
               for customer in video_store.list_customers():
                  print_line()
                  print("ID:" f"{customer['id']}\n"
                        "Name:" f"{customer['name']}\n"
                        "Phone:" f"{customer['phone']}\n"
                        "Postal Code:" f"{customer['postal_code']}\n"
                        "Current Rentals:" f"{customer['videos_checked_out_count']}\n")
            elif customer_choice == "2":  
                id = input("Please provide ID of the customer you want to check\n::")
                selected_customer = valid_id(id, video_store, "customer")
                if selected_customer: 
                    print(">>--->Customer information enclosed<---<<:\n"
                          "ID:" f"{selected_customer['id']}\n"
                          "Name:" f"{selected_customer['name']}\n"
                          "Phone:" f"{selected_customer['phone']}\n"
                          "Postal Code:" f"{selected_customer['postal_code']}\n"
                          "Current Rentals:" f"{selected_customer['videos_checked_out_count']}\n")
            elif customer_choice == "3":
                print("Hooray! We have a new customer.")
                name = input("What is the name of our customer?\n>>")
                postal_code = input("What is the zip code of our customer?\n>>")
                phone = input("What is the phone number of our customer?\n>>")
                response = video_store.add_customer(name=name, postal_code=postal_code, phone=phone)
                print_divider()
                print("New Customer: ", response["name"])
            elif customer_choice == "4":
                print("Be careful, you are about to modify customer info!")
                id = input("Please provide ID of the customer you want to edit\n::")
                selected_customer = valid_id(id, video_store, "customer")
                print("Selected Customer:", selected_customer["name"])
                name = input("What is the new name you want to update to? If no, just hit enter.\n>>")
                postal_code = input("What is the new postal code you want to update to? If no, just hit enter.\n>>")
                phone = input("What is the new phone number you want to update to? If no, just hit enter.\n>>")
                response = video_store.edit_customer(id=id, name=name, postal_code=postal_code, phone=phone)
                print_divider()
                print("Updated Customer: ",selected_customer["name"] )
            elif customer_choice == "5":
                print("Be careful, you are in the delete mode!")
                id = input("Please provide ID of the customer you want to delete\n::")
                customer_deleted = video_store.delete_customer(id=id)
                print_divider()
                print(f"Customer {customer_deleted['name']} has been deleted!")
            elif customer_choice == "6":
                main_menu_choice = back_to_main_menu()
        
        elif main_menu_choice == "2":
            video_options = list_options(VIDEO_MENU, "Video Menu", VIDEO_INFO)
            video_choice = make_choice(video_options, CUSTOMER_MSG)
            if video_choice == "1":
                for video in video_store.list_videos():
                    print_line()
                    print("ID:"  f"{video['id']}\n"
                          "Title:"  f"{video['title']}\n"
                          "Release Date:"  f"{video['release_date'][8:16]}\n"
                          "Total Inventory:"  f"{video['total_inventory']}\n"
                          "Available Inventory:"  f"{video['available_inventory']}\n")
            elif video_choice == "2":
                id = input("Please provide ID of the video you want to check\n::")
                selected_video = valid_id(id, video_store, "video")
                if selected_video: 
                    print(">>--->Video information enclosed<---<<:\n"
                          "ID:" f"{selected_video['id']}\n"
                          "Title:" f"{selected_video['title']}\n"
                          "Release Date:" f"{selected_video['release_date'][8:16]}\n"
                          "Total Inventory:" f"{selected_video['total_inventory']}\n"
                          "Available Inventory:" f"{selected_video['available_inventory']}\n")
            elif video_choice == "3":
                print("Yay, awesome video coming in!")
                title = input("What is the title of the new movie?\n>> ")
                release_date = input("What is the release date of the movie?\n>>")
                total_inventory = input("How many copies of this video do we have?\n>>")
                response = video_store.add_video(title=title, release_date=release_date, total_inventory=total_inventory)
                print_divider()
                print("New Video: ", response["title"])
            elif video_choice == "4":
                print("Be careful, you are about to modify video info!")
                id = input("Please provide ID of the video you want to edit\n::")
                selected_video = valid_id(id, video_store, "video")
                print("Selected Video:", selected_video["title"])
                title = input("What is the title you want to update to? If no, just hit enter.\n>>")
                release_date = input("What is the new release date you want to update to? If no, just hit enter.\n>>")
                total_inventory = input("What is the new inventory? If no, just hit enter.\n>>")
                response = video_store.edit_video(id, title, release_date, total_inventory)
                print_divider()
                print("Updated Video: ",selected_video["title"] )
            elif video_choice == "5":
                print("Be careful, you are in the delete mode!")
                id = input("Please provide ID of the video you want to delete\n::")
                video_deleted = video_store.delete_video(id=id)
                print_divider()
                print(f"Video {video_deleted['title']} has been deleted!")
            elif video_choice == "6":
                main_menu_choice = back_to_main_menu()
                
        elif main_menu_choice == "3":
            rental_options = list_options(RENTAL_MENU, "Rental Menu", RENTAL_INFO)
            rental_choice = make_choice(rental_options, RENTAL_MSG)
            if rental_choice == "1":
                print("Ready to checkout? We will need your id and the video id you want to checkout.")
                customer_id = input("What is your customer id?\n>>")
                video_id = input("What is the video id you want to check out?\n>>")
                customer = valid_id(customer_id, video_store, "customer")
                video = valid_id(video_id, video_store, "video")
                response = video_store.check_out(customer_id, video_id)
                if video and customer:
                    print(f"Video {video['title']} successfully checked out by {customer['name']}")
                else:
                    print("Cannot find matched record.")
            elif rental_choice == "2":
                print("Welcome back! Did you enjoy your video?")
                customer_id = input("What is your customer id?\n>>")
                video_id = input("What is the video id you want to check in?\n>>")
                customer = valid_id(customer_id, video_store, "customer")
                video = valid_id(video_id, video_store, "video")
                response = video_store.check_in(customer_id, video_id)
                if video and customer:
                    print(f"Video {video['title']} has been return by {customer['name']}")
                else:
                    print("Cannot find matched record.")
            elif rental_choice == "3":
                main_menu_choice = back_to_main_menu()
        elif main_menu_choice == "4":
            play = False
            print("=^_^=Thanks for visiting rainbow video store =^_^=")

if __name__ == "__main__":
    main()
    
    