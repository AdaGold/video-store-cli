from os import read, register_at_fork
from datetime import datetime
from retro_video import RetroVideo

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    # run_cli()
    pass

    def print_stars():
        print("\n**************************\n")

    def list_options():

        options = {
            "1": "Add a Video", 
            "2": "Edit a Video",
            "3": "Delete a Video", 
            "4": "Get information about all videos", 
            "5": "Get information about one video", 
            "6": "Add a customer",
            "7": "Edit a customer",
            "8": "Delete a customer",
            "9": "Get information about one customer", 
            "10": "Get information about all customers",
            "11": "Check out a video to a customer",
            "12": "Check in a video to a customer",
            "13": "Quit"
            }

        print_stars()
        print("Welcome to the Retro Video Store CLI")
        print("These are the actions you can perform")
        print_stars()

        
        for choice_num in options:
            print(f"Option {choice_num}. {options[choice_num]}")

        print_stars()

        return options

    def make_choice(options, retro_video):
        valid_choices = options.keys()
        choice = None

        while choice not in valid_choices:
                print("Please choose an option from the list above")
                choice = input("Please enter you selection here: ")
        if choice in ['2','3'] and retro_video.selected_video==None:
            print("To edit or delete you must select a video")
            choice = "5"

        elif choice in ['7','8'] and retro_video.selected_customer==None:
            print("To edit or delete you must select a customer")
            choice = "9"

        elif choice in valid_choices:
            return choice
            
            

    def run_cli(play=True):
        retro_video = RetroVideo(url="https://retro-video-store-api.herokuapp.com")

        options = list_options()

        while play==True:

            choice = make_choice(options, retro_video)


            retro_video.print_selected()
            
            # Create a video
            if choice=='1':
                print("Great! Let's add a new video.")
                title=input("What is the title of your video? ")
                release_date=input("What is the release date of your video? ")
                total_inventory=input("What is the total inventory of your video? ")
                available_inventory = input("what is the available inventory of your video?")
                response = retro_video.create_video(title=title, total_inventory=total_inventory, release_date = release_date, available_inventory = available_inventory)

                print_stars()
                print("New video:", response)
            # Edit a video
            elif choice=='2':
                print(f"Okay! We will be editing {retro_video.selected_video}")
                title=input("What is the new title of your video? ")
                release_date=input("What is the new release date of your video? ")
                total_inventory=input("What is the new total inventory of your video? ")
                available_inventory = input("What is the new available inventory of your video? ")
                response = retro_video.update_video(title=title, release_date = release_date, total_inventory=total_inventory, available_inventory = available_inventory)

                print_stars()
                print("Updated Video:", response)
            # Delete selected video
            elif choice=='3':
                retro_video.delete_video()

                print_stars()
                print("Video has been deleted.")

                print_stars()
                print(retro_video.list_videos())
            # Get information about all videos
            elif choice=='4':
                print_stars()
                for video in retro_video.list_videos():
                    print(video)
            # Get information about one video
            elif choice=='5':
                title = input("Please enter the video title you would like to select: ")
                retro_video.get_video(title=title)
                if title == None:
                    print("Could not select. Please enter a video title.")
                
                if retro_video.selected_video:
                    print_stars()
                    print("Selected video: ", retro_video.selected_video)
    # ================================== Customer ========================================================================
            
            # Create a customer
            if choice=='6':
                print("Great! Let's add a new customer.")
                name=input("What is the name of your customer? ")
                phone=input("What is the phone number of your customer? ")
                postal_code=input("What is the postal_code of your customer? ")
                registered_at = input("what is the time your customer was registered at?")
                videos_checked_out = input("How many videos are check out for your customer?")
                response = retro_video.create_customer(name=name, phone=phone, postal_code = postal_code, registered_at=registered_at, videos_checked_out = videos_checked_out)

                print_stars()
                print("New customer:", response)
            # Edit a customer
            elif choice=='7':
                print(f"Okay! We will be editing {retro_video.selected_customer}")
                name=input("What is the new name of your customer? ")
                phone=input("What is the new phone number of your customer? ")
                postal_code=input("What is the new postal_code of your customer? ")
                registered_at= input("When was your customer registered at? ")
                videos_checked_out = input("How many videos are check out for your customer?")
                response = retro_video.update_customer(name=name, phone=phone, postal_code = postal_code, registered_at=registered_at, videos_checked_out= videos_checked_out)

                print_stars()
                print("Updated Customer:", response)
            # Delete selected customer
            elif choice=='8':
                retro_video.delete_customer()

                print_stars()
                print("Customer has been deleted.")

                print_stars()
                print(retro_video.list_customers())
            # Get information about all customers
            elif choice=='9':
                name = input("Please enter the customer name you would like to select: ")
                retro_video.get_customer(name=name)
                if name == None:
                    print("Could not select. Please enter a customer name.")
                
                if retro_video.selected_customer:
                    print_stars()
                    print("Selected customer: ", retro_video.selected_customer)
            # Get information about one customer
            elif choice=='10':
                print_stars()
                for customer in retro_video.list_customers():
                    print(customer)
# ============================================ Rentals =====================================
            # Check out a video to a customer
            elif choice == "11":
                print("Please enter the customer id and video id for the movie you would like to check out.")
                customer_id = input("Customer id: ")
                video_id = input("Video id: ")
                print(customer_id, video_id)
                response = retro_video.video_check_out(customer_id, video_id)
                print(response)
                print("Check out was successful")

            # Check in a video to a customer
            elif choice == "12":
                print("Please enter the customer id and video id for the movie you would like to check in.")
                customer_id = input("Customer id: ")
                video_id = input("Video id: ")
                response = retro_video.video_check_in(customer_id=customer_id, video_id=video_id)
                if response == 200:
                    print("Check in was successful")


    # ============================================ Quit =====================================
            # Quit
            elif choice == "13":
                play=False
                print("\nThanks for using the Retro Video Store CLI!")

            print_stars()

    run_cli()

if __name__ == "__main__":
    main()
