import requests

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def print_stars():
    print("\n**************************\n")

def list_options():
    print("Thank you for being a valued member of our team!")
    print("What would you like to do?")
    options = {
        "1": "add a video", 
        "2": "edit a video",
        "3": "delete a video",
        "4": "get information about all videos",
        "5": "get information about one video",
        "6": "add a customer", 
        "7": "edit a customer",
        "8": "delete a customer",
        "9": "get information about one customer",
        "10": "get information about all customers",
        "11": "check out a video to a customer",
        "12": "check in a video from a customer",
        "13": "exit this program"
        }
    for num in options:
        print(f"Option {num}. {options[num]}")
    print_stars()
    return options

def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None
    while choice not in valid_choices:
        # print("What would you like to do? Select 9 to see all options again")
        choice = input("Make your selection using the option number: ")
    return choice






def main(play=True):
    #I wrote URL instead of TaskList. is that right?
    # video_store_customers = URL_customer(url="BACKUP_URL")
    video_store = TaskList(url="BACKUP_URL")
    print("WELCOME TO RETRO VIDEO STORE")

    user_options = list_options()

    while play == True:
        choice = make_choice(user_options, video_store)
        video_store.print_selected()

        if choice == "1":
            print(f"Let's add a new video")
            title = input("What is the name of the movie? ")
            release_date = input("When was the movie released? ")
            available_inventory = input("How many copies of this video do we have? ")
            response = video_store.create_video(title=title, release_date=release_date, available_inventory=available_inventory )

            print_stars()
            print("New movie:", response["title"])

        if choice == "2":
            print(f"Let's EDIT a video: {video_store.selected_video}")
            title=input("What is the updated title of the movie? ")
            release_date=input("What is the updated release date of the movie? ")
            available_inventory=input("What is the updated number of videos we have? ")
            response = video_store.save(title=title, release_date=release_date, available_inventory=available_inventory )

            print_stars()
            print("Updated movie:", response["title"]["release_date"]["available_inventory"])

        if choice == "3":
            print(f"Let's DELETE a video: {video_store.selected_video}")
            video_store.delete()

            print_stars()
            print("Video has been deleted.")

        if choice == "4":
            print(f"Let's get information about all videos. ")
            print_stars()
            videos = [video.to_json() for video in video_store.get_all_videos()]
            print(videos)


        if choice == "5":
            print(f"Let's get information about: {video_store.selected_video} ")
            print_stars()
            id = input("What is the id of the movie you would like information about? ")
            if id.isnumeric():
                id = int(id)
                video = video_store.get_video_by_id(id=id)
                if video_store.selected_video:
                    print_stars()
                    print(video.to_json())
            else:
                print("Please enter a numerical id. ")

        if choice == "6":
            print(f"Let's add a new customer")
            name = input("What is the name of the customer? ")
            postal_code = input("What is their postal code? ")
            phone = input("What is their phone number? ")
            response = video_store.create_customer(name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("New customer:", response["name"])

        if choice == "7":
            print(f"Let's EDIT a customer's info: {video_store.selected_customer}")
            name = input("What is the updated name of the customer? ")
            postal_code = input("What is their updated postal code? ")
            phone = input("What is their updated phone number? ")
            response = video_store.save(name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("Updated customer:", response["name"]["postal_code"]["phone"])

        if choice == "8":
            print(f"Let's DELETE a customer: {video_store.selected_customer}")
            video_store.delete()

            print_stars()
            print("Customer has been deleted.")

        if choice == "9":
            print(f"Let's get information about all customers. ")
            print_stars()
            customers = [customer.to_json() for customer in video_store.get_all_customers()]
            print(customers)


        if choice == "10":
            print(f"Let's get information about: {video_store.selected_customer} ")
            print_stars()
            id = input("What is the id of the customer you would like information about? ")
            if id.isnumeric():
                id = int(id)
                customer = video_store.get_customer_by_id(id=id)
                if video_store.selected_customer:
                    print_stars()
                    print(customer.to_json())
            else:
                print("Please enter a numerical id. ")

        if choice == "11":
            print(f"Let's check out a video to a customer. ")
            print_stars()
            customer_id = input("What is the id of the customer who would like to check out a video? ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                customer = video_store.get_customer_by_id(id=customer_id)
            
            if not customer_id.isnumeric() or not video_store.selected_customer:
                print("Please enter a valid numerical id. ")

            video_id = input("What is the id of the video being checked out? ")
            if video_id.isnumeric():
                video_id = int(video_id)
                video = video_store.get_video_by_id(id=video_id)
            
            if not video_id.isnumeric() or not video_store.selected_video:
                print("Please enter a valid numerical id. ")            

            result = video_store.customer.check_out(video_id=video.id, customer_id=customer.id)
    
            print(f"You checkout has been successful: {result}")

        if choice == "12":
            print(f"Let's check inm a video from a customer. ")
            print_stars()
            customer_id = input("What is the id of the customer who would like to return their video? ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                customer = video_store.get_customer_by_id(id=customer_id)
            
            if not customer_id.isnumeric() or not video_store.selected_customer:
                print("Please enter a valid numerical id. ")

            video_id = input("What is the id of the video being checked in? ")
            if video_id.isnumeric():
                video_id = int(video_id)
                video = video_store.get_video_by_id(id=video_id)
            
            if not video_id.isnumeric() or not video_store.selected_video:
                print("Please enter a valid numerical id. ")            

            result = video_store.customer.check_out(video_id=video.id, customer_id=customer.id)
            #delete rental?
            print(f"You checkout has been successful: {result}")

        if choice == "13":
            play=False
            print("\nThanks for using the Video Store CLI!")

if __name__ == "__main__":
    main()

