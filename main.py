import requests
from video_store import VideoStore

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def main():
    videos = VideoStore()
    print("WELCOME TO RETRO VIDEO STORE")
    print("\n************************************\n")
    print("Please choose an option")
    print("Enter 1 to manage videos")
    print("Enter 2 to customers")
    print("Enter 3 to check-in/check-out")

    main_choice = input("Enter your choice: ")
    print("\n************************************\n")

    if main_choice == "1":
        print("What would you like to do in videos? ")
        print("Enter 1 to see all videos")
        print("Enter 2 to add video")
        print("Enter 3 to update a video")
        print("Enter 4 to delete a video")
        print("Enter 5 to get a video")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Here is a list of all videos")
            for video in videos.get_all_videos():
                print(video)

        elif choice == "2":
            print("You are about to add a new movie.")
            title = input("What is the title of the movie? ")
            release_date = input(f"When was {title} released? Please enter in yyyy-mm-dd. ")
            total_inventory = input(f"What is the total inventory of {title}? ")
            response = videos.add_video(title = title, release_date = release_date, total_inventory = total_inventory)

            print(f"{title} was created")

        elif choice == "3":
            video_id = input("Enter a video id: ")
            print(f"You are about to update a movie with video id: {video_id}")
            title = input("What is the new movie title? ")
            release_date = input(f"When was {title} released? Please enter in yyyy-mm-dd. ")
            total_inventory = input(f"What is the total inventory of {title}? ")
            response = videos.edit_video(video_id = video_id, title = title, release_date = release_date, total_inventory = total_inventory)

            print(f"{title} is now updated")

        elif choice == "4":
            try:
                print("You are about to delete a movie.")
                video_id = input("Enter a video id: ")
                videos.delete_video(video_id)
                print("This video has been deleted.")
            
            except:
                video_id not in videos.get_all_videos()
                print("Enter a valid video id.")
                video_id = input("Enter a video id: ")
                videos.delete_video(video_id)
                print("This video has been deleted.")
        
        elif choice == "5":
            print("What video would you like to view? ")
            video_id = input("Enter a video id: ")
            response = videos.get_video(video_id = video_id)
            print(response)

        else:
            print("Please enter a valid choice")

    elif main_choice == "2":
        print("What would you like to do in customers? ")
        print("Enter 1 to see all customers")
        print("Enter 2 to add customer")
        print("Enter 3 to update customer")
        print("Enter 4 to delete a customer")
        print("Enter 5 to retrieve customer")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Here is a list of all customers")
            for customer in videos.get_all_customers():
                print(customer)

        elif choice == "2":
            print("You are about to add a new customer.")
            name = input("What is the customer's name? ")
            postal_code = input("What is customer's postal code? ")
            phone = input("What is customer's phone number? ")
            response = videos.add_customer(name = name, postal_code = postal_code, phone_number = phone)

            print(f"{name} was created")

        elif choice == "3":
            customer_id = input("Enter customer's id: ")
            print(f"You are about to update a customer with id: {customer_id}")
            postal_code = input("What is customer's new postal code? ")
            phone = input("What is customer's new phone? ")
            response = videos.edit_customer(customer_id = customer_id, postal_code = postal_code, phone = phone)

            print(f"{customer_id} is now updated")

        elif choice == "4":
            try:
                print("You are about to delete customer.")
                customer_id = input("Enter customer's id: ")
                videos.delete_customer(customer_id)
                print("This customer has been deleted.")
            
            except:
                customer_id not in videos.get_all_customers()
                print("Enter a valid customer id.")
                customer_id = input("Enter a customer id: ")
                videos.delete_customer(customer_id)
                print("This customer has been deleted.")
        
        elif choice == "5":
            print("What customer would you like to view? ")
            customer_id = input("Enter a customer id: ")
            response = videos.get_customer(customer_id)
            print({
                "id" : response["id"],
                "name" : response["name"],
                "phone" : response["phone_number"],
                "postal_code" : response["postal_code"],
                "registered_at" : response["registered_at"],
                })

        else:
            print("Please enter a valid choice")

    elif main_choice == "3":
        print("Would you like to check-in? ")

    else: 
        print("Please enter a valid choice")


main()