import requests
from customers import Customers
from videos import Videos
from rentals import Rentals

URL = "https://whits-video-store.herokuapp.com/"

def print_stars():
    print("\n*******************************\n")

def list_options():
    options = {
        "1": "Get detailed information for all videos",
        "2": "Look up video",
        "3": "Look up videos by genre",
        "4": "Add a video to the inventory",
        "5": "Edit video information",
        "6": "Delete a video from the inventory",
        "7": "Get detailed information for all customers",
        "8": "Look up customer",
        "9": "Add a customer to the database",
        "10": "Edit customer information",
        "11": "Delete a customer from the database",
        "12": "Look up a customer's checked-out videos",
        "13": "Check out a video",
        "14": "Check in a video",
        "15": "List current rentals",
        "16": "List overdue rentals",
        "17": "Quit CLI",
        "o": "See all options"
    }


    print_stars()
    print("Welcome to the Video Store CLI!")
    print("These are your options:")
    print_stars()

    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Type 'o' to see all options.")
        choice = input("Make your selection using the option number: ")

    return choice


def run_cli(play=True):

    customers = Customers()
    videos = Videos()
    rentals = Rentals()
    options = list_options()

    while play == True:

        print_stars()

        choice = make_choice(options)

        if choice=="1":
            print_stars()
            for video in videos.list_videos():
                print(video)

        elif choice=="2":
            select_by = input("Would you like to select by title or id?: ")
            if select_by == "title":
                title = input("Please enter video title: ")
                response = videos.get_video(title=title)
            elif select_by == "id":
                id = input("Please enter video id: ")
                if id.isnumeric():
                    id = int(id)
                    response = videos.get_video(id=id)
                else:
                    print("Please enter a number!")
            else:
                print("You must type 'title' or 'id'!")

            if response:
                print(" ")
                print(response)

        elif choice=="3":
            genre = input("What genre are you interested in? ")
            response = videos.get_videos_by_genre(genre)
            print_stars()
            print(f"Videos in {genre} genre: ", response)

        elif choice=="4":
            print("I'll need some more information about the video you'd like to add.")
            title = input("What is the video's title? ")
            release_date = input("When was the video released? ")
            genre = input("What is this video's genre? ")
            total_inventory = input("How many copies would you like to add to the inventory? ")
            response = videos.add_video(title=title, release_date=release_date, genre=genre, total_inventory=total_inventory)
            print_stars()
            print("Video added: ", response)

        elif choice=="5":
            id = input("What is the id of the video you'd like to update? ")
            title = input("What is the title of the new video? ")
            release_date = input("When was this video released? ")
            genre = input("What is this video's genre? ")
            total_inventory = input("How many copies would you like to add to the inventory? ")
            response = videos.update_video(id=id, title=title, release_date=release_date, genre=genre, total_inventory=total_inventory)

            print_stars()
            print("Updated video: ", response)

        elif choice =="6":
            id = input("What is the id of the video you'd like to delete? ")
            response = videos.delete_video(id=id)
            print_stars()
            print("Deleted video: ", response)

        elif choice == "7":
            print_stars()
            for customer in customers.list_customers():
                print(customer)

        elif choice == "8":
            select_by = input("Would you like to select by id, name, or phone? ")
            if select_by == "name":
                name = input("Please enter full customer name: ")
                response = customers.get_customer(name=name)
            elif select_by == "id":
                id = input("Please enter customer id: ")
                if id.isnumeric():
                    id = int(id)
                    response = customers.get_customer(id=id)
                else:
                    print("Please enter a number!")
            elif select_by == "phone":
                phone = input("Please enter customer phone number in format 'xxx-xxx-xxxx': ")
                response = customers.get_customer(phone=phone)
            else:
                print("You must type 'id', 'name', or 'phone'!")

            if response:
                print(" ")
                print(response)

        elif choice == "9":
            print("I'll need some more information about the customer you'd like to add.")
            name = input("What is the customer's name? ")
            phone = input("What is the customer's phone number (in format xxx-xxx-xxxx)? ")
            postal_code = input("What is the customer's postal code? ")
            response = customers.add_customer(name=name, phone=phone, postal_code=postal_code)
            print_stars()
            print("Customer added: ", response)

        elif choice == "10":
            id = input("What is the id of the customer you'd like to update? ")
            name = input("What is the customer's name? ")
            postal_code = input("What is the customer's postal code? ")
            phone = input("What is the customer's phone number (format xxx-xxx-xxxx)? ")
            response = customers.update_customer(id=id, name=name, phone=phone, postal_code=postal_code)

            print_stars()
            print("Updated customer: ", response)

        elif choice == "11":
            id = input("What is the id of the customer you'd like to delete? ")
            response = customers.delete_customer(id=id)
            print_stars()
            print("Deleted customer: ", response)

        elif choice == "12":
            id = input("What is the customer's id? ")
            response = customers.get_customer_rentals(id)
            print(f"Rentals for customer {id}: ", response)

        elif choice == "13":
            video_id = input("What video are you checking out? Enter video id: ")
            customer_id = input("Who would you like to check-out the video to? Enter customer id: ")
            response = rentals.check_out(customer_id, video_id)
            print("Confirmation: ", response)

        elif choice == "14":
            video_id = input("What video are you returning? Enter video id: ")
            customer_id = input("Who is returning the video? Enter customer id: ")
            response = rentals.check_in(customer_id, video_id)
            print("Confirmation: ", response)
        
        elif choice == "15":
            for rental in rentals.get_all_rentals():
                print(rental)

        elif choice == "16":
            for rental in rentals.get_all_overdue():
                print(rental)

        elif choice == "17":
            play = False
            print("Thanks for using the Video Store CLI!")

        elif choice.lower() == "o":
            list_options()
    
def main():
    run_cli()






if __name__ == "__main__":
    main()






# def list_category_options():

#     category_options = {
#         "1": "Video Actions",
#         "2": "Customer Actions",
#         "3": "Rental Actions",
#         "4": "Quit CLI"
#     }

#     print("Welcome to the main menu.")
#     print("These are the types of actions you can perform.\n")

#     for choice_num in category_options:
#         print(f"Option {choice_num}. {category_options[choice_num]}")

#     print_stars()

#     return category_options


# def list_video_options():

#     video_options = {
#         "1": "Get detailed information for all videos",
#         "2": "Look up video by id",
#         "3": "Look up video by title",
#         "4": "Look up videos by genre",
#         "5": "Add a video to the inventory",
#         "6": "Edit video information",
#         "7": "Delete a video from the inventory",
#         "8": "Go back to main menu",
#         "9": "Quit CLI"
#     }

#     print("Welcome to the video actions menu.")
#     print("These are the actions you can perform.\n")
 

#     for choice_num in video_options:
#         print(f"Option {choice_num}. {video_options[choice_num]}")

#     print_stars()

#     return video_options


# def list_customer_options():
    
#     customer_options = {
#         "1": "Get detailed information for all customers",
#         "2": "Look up customer by id",
#         "3": "Look up customer by name",
#         "4": "Look up customer by postal code",
#         "5": "Add a customer to the database",
#         "6": "Edit customer information",
#         "7": "Delete a customer from the database",
#         "8": "Look up a customer's checked-out videos",
#         "9": "Return to main menu",
#         "10": "Quit CLI"
#     }

#     print_stars()
#     print("Welcome to the customer actions menu.")
#     print("These are the actions you can perform.")
#     print_stars()

#     for choice_num in customer_options:
#         print(f"Option {choice_num}. {customer_options[choice_num]}")
    
#     print_stars()

#     return customer_options


# def list_rental_options():

#     rental_options = {
#         "1": "Check out a video",
#         "2": "Check in a video",
#         "3": "List current rentals",
#         "4": "List overdue rentals",
#         "5": "Return to main menu",
#         "6": "Quit CLI"
#     }

#     print_stars()
#     print("Welcome to the rental actions menu.")
#     print("These are the actions you can perform.")
#     print_stars()

#     for choice_num in rental_options:
#         print(f"Option {choice_num}. {rental_options[choice_num]}")

#     print_stars()

#     return rental_options

# def make_category_choice(options):
#     valid_choices = options.keys()
#     choice = None

#     while choice not in valid_choices:
#         print("What type of action would you like to perform?")
#         choice = input("Make your selection using the option number: ")

#     return choice