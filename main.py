from videostoreAPI import CustomerAPI, VideoAPI, RentalAPI
import time
from tqdm import tqdm
import cfonts
from cfonts import colors
import colorama 
from colorama import Fore, Style

colorama.init(autoreset=True)
colors = ['red', 'blue']

############################################################################################

def display_options():
    options = {
        "1": "Register new movie", 
        "2": "Update movie info",
        "3": "Delete movie from database",
        "4": "View all movies", 
        "5": "View movie info",
        "6": "Register new user",
        "7": "Update user info",
        "8": "Delete user from database", 
        "9": "View user account",
        "10": "View all users",
        "11": "Check-out movie", 
        "12": "Check-in movie", 
        "13": "View all options",
        "14": "Exit"
        }  

    for option in options:
        menu_options = cfonts.render(f"{Style.BRIGHT}{Fore.YELLOW}{option}. {options[option]}", font='console', space=False)
        print(menu_options)
    return options

def make_choice(options):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        print(f"\n{Style.BRIGHT}{Fore.GREEN}S{Fore.YELLOW}E{Fore.MAGENTA}L{Fore.BLUE}E{Fore.CYAN}C{Fore.WHITE}T {Fore.RED}O{Fore.CYAN}N{Fore.BLUE}E.")
        choice = input(f"{Fore.YELLOW}Enter 13 to view all options: {Fore.WHITE}")
        while choice not in options.keys():
            choice = input(f"{Fore.RED}400-Bad Request. Please input a valid option: {Fore.WHITE}")
    return choice

def main(play=True):
    greeting = cfonts.render("Retro Video Store", font='block',colors=colors)
    print(greeting) 
    menu = cfonts.render(f"{Fore.GREEN}M{Fore.YELLOW}E{Fore.MAGENTA}N{Fore.BLUE}U {Fore.CYAN}O{Fore.WHITE}P{Fore.YELLOW}T{Fore.RED}I{Fore.BLUE}O{Fore.GREEN}N{Fore.MAGENTA}S{Fore.CYAN}: \n", font='console', space=False)
    print(menu)
    options = display_options()
    while play==True:
        choice = make_choice(options)
        if choice in ["1","2","3","4","5"]:
            video_endpoints(choice)
        elif choice in ["6","7","8","9","10"]:
            customer_endpoints(choice)
        elif choice in ["11","12"]:
            rental_endpoints(choice)
        elif choice == '13':
            display_options()
        elif choice == '14':
            greeting2 = cfonts.render("\nSee You Space Cowboy!", font='tiny', colors=colors)
            print(greeting2)
            play=False

############################################################################################

def customer_endpoints(choice):
    if choice=='6':
        print(f"{Style.BRIGHT}\nRegistering new user? Enter the info below:")
        name=input("Name: ")
        postal_code=input("Postal code: ")
        phone=input("Phone number: ")
        response = CustomerAPI.register_user(name=name, postal_code=postal_code, phone=phone)
        print("New user has been registered: User ID #", response["id"])

    elif choice=='7':
        print(f"{Style.BRIGHT}\nEnter USER ID to update account.")
        user_id=input('User ID:')
        while user_id.isalpha() or not user_id:
            user_id = input(f"{Fore.RED}Could not select. Please enter a numerical ID:")
        customer = CustomerAPI.get_user(user_id)
        if not customer:
                print(f"{Fore.RED}User with this ID does not exist.")
        print(f"You selected {customer['name']} with USER ID #{customer['id']}")
        print(f"{Style.BRIGHT}Enter new info below.")
        name=input("Name: ")
        postal_code=input("Postal code: ")
        phone=input("Phone number: ")
        response = CustomerAPI.update_user_account(user_id=user_id,
                                                    name=name, 
                                                    postal_code=postal_code, 
                                                    phone=phone)
        print(f"{Style.BRIGHT}\nUpdated user account:",
                f"\nName:",response["name"],
                f"\nID:",response['id'],
                f"\nPostal Code:",response['postal_code'],
                f"\nPhone #:",response['phone'],
                f"{Fore.GREEN}\nUser successfully updated.")                          

    elif choice=='8':
        print(f"{Style.BRIGHT}\nEnter USER ID to delete user.")
        user_id=input('User ID:')
        while user_id.isalpha() or not user_id:
            user_id = input(f"{Fore.RED}Could not select. Please enter a numerical ID:")
        if user_id.isnumeric():
            user_id = int(user_id)
            customer = CustomerAPI.delete_customer(user_id)
            if not customer:
                print(f"{Fore.RED}User with this ID does not exist.")
            print(f"{Fore.GREEN}User successfully deleted.")                           

    elif choice=='9':
        print(f"{Style.BRIGHT}\nEnter USER ID to view user account.")
        user_id=input('User ID:')
        while user_id.isalpha() or not user_id:
            user_id = input(f"{Fore.RED}Could not select. Please enter a numerical ID:")
        if user_id.isnumeric():
            user_id = int(user_id)
            customer = CustomerAPI.get_user(user_id)
            if not customer:
                print(f"{Fore.RED}User with this ID does not exist.")
            print(f'\nName: {customer["name"]} | ID: {customer["id"]} | Postal Code: {customer["postal_code"]} | Phone #:{customer["phone"]}')
    
    elif choice=='10':
        all_users = [user for user in CustomerAPI.list_users()]
        for i in tqdm(all_users, colour='green'):
            time.sleep(.01)
        for user in all_users:
            index =all_users.index(user)
            print(f'\n{index+1}. Name: {user["name"]} | ID: {user["id"]} | Postal Code: {user["postal_code"]} | Phone #:{user["phone"]}')

############################################################################################

def video_endpoints(choice):
    if choice == '1':
        print(f"{Style.BRIGHT}\nRegistering new video? Enter the info below:")
        title=input("Movie title: ")
        release_date=input("Release_date (MM/DD/YYYY): ")
        total_inventory=input("Total_inventory: ")
        response = VideoAPI.register_video(title=title,
                                        release_date=release_date,
                                        total_inventory=total_inventory)
        print(f"{Fore.GREEN}New video has been registered: Video ID #", response["id"])
    
    elif choice=='2':
        print(f"{Style.BRIGHT}\nEnter VIDEO ID to update info.")
        video_id=input('Video ID:')
        while video_id.isalpha() or not video_id:
            video_id = input(f"{Fore.RED}Could not select. Please enter a numerical ID:")
        video = VideoAPI.get_video(video_id)
        print(f"You selected {video['title']} with VIDEO ID #{video['id']}")
        print(f"{Style.BRIGHT}Enter new info below.")
        title=input("Title: ")
        release_date=input("Release date (MM/DD/YYYY): ")
        total_inventory=input("Total Inventory: ")
        response = VideoAPI.update_video_info(video_id=video_id,
                                            title=title, 
                                            release_date=release_date, 
                                            total_inventory=total_inventory)
        print(f"{Style.BRIGHT}\nUpdated video:",
                f"\nTitle:",response["title"],
                f"\nID:",response['id'],
                f"\nRelease Date:",response['release_date'],
                f"\nTotal Inventory:",response['total_inventory'],
                f"{Fore.GREEN}\nVideo successfully updated.")                          
    
    elif choice=='3':
        print(f"{Style.BRIGHT}\nEnter VIDEO ID to delete video.")
        video_id=input('Video ID:')
        while video_id.isalpha() or not video_id:
            video_id = input(f"{Fore.RED}Could not select. Please enter a numerical ID:")
        if video_id.isnumeric():
            video_id = int(video_id)
            video = VideoAPI.delete_video(video_id)
            if not video:
                print(f"{Fore.RED}Video with this ID does not exist.")
            print(f"{Fore.GREEN}Video successfully deleted.")   

    elif choice == '4':
        all_videos = [video for video in VideoAPI.list_videos()]
        for i in tqdm(all_videos, colour='green'):
            time.sleep(.01)
        for video in all_videos:
            index =all_videos.index(video)
            print(f'\n{index+1}. Title: {video["title"]} | ID: {video["id"]} | Release Date: {video["release_date"]} | Total Inventory #:{video["total_inventory"]}')
    
    elif choice=='5':
        print(f"{Style.BRIGHT}\nEnter VIDEO ID to view video info.")
        video_id=input('Video ID:')
        while video_id.isalpha() or not video_id:
            video_id = input(f"{Fore.RED}Could not select. Please enter a numerical ID:")
        if video_id.isnumeric():
            video_id = int(video_id)
            video = VideoAPI.get_video(video_id)
            if not video:
                print(f"{Fore.RED}Video with this ID does not exist.")
            print(f'\nTitle: {video["title"]} | ID: {video["id"]} | Release Date: {video["release_date"]} | Total Inventory #:{video["total_inventory"]}')


############################################################################################

def rental_endpoints(choice):
    if choice=='11':
        print(f"{Style.BRIGHT}\nChecking out? Whatcha got?")
        user_id=input('User ID: ')
        video_id=input('Video ID: ')
        while video_id.isalpha() or user_id.isalpha() or not video_id or not user_id:
            print(f"{Fore.RED}User ID or Video ID is not valid. Please enter a valid number.")
            user_id=input('User ID: ')
            video_id=input('Video ID: ')
        if user_id.isnumeric():
            user_id = int(user_id)
        if video_id.isnumeric():
            video_id = int(video_id)
        RentalAPI.checkout(user_id=user_id, video_id=video_id)
        print(f"{Fore.GREEN}Video #{video_id} checked out to User ID# {user_id}.")

    elif choice=='12':
        print(f"{Style.BRIGHT}\nChecking in? Whatcha got?")
        user_id=input('User ID: ')
        video_id=input('Video ID: ')
        while video_id.isalpha() or user_id.isalpha() or not video_id or not user_id:
            print(f"{Fore.RED}User ID or Video ID is not valid. Please enter a valid number.")
            user_id=input('User ID: ')
            video_id=input('Video ID: ')
        if user_id.isnumeric():
            user_id = int(user_id)
        video_id=input('Video ID: ')
        if video_id.isnumeric():
            video_id = int(video_id)
        RentalAPI.checkin(user_id=user_id, video_id=video_id)
        print(f"{Fore.GREEN}Video #{video_id} successfully checked in.")

if __name__ == "__main__":
    main()







