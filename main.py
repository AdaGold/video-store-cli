from rentals import RentalList
from videos import VideoList
from customers import CustomerList

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    

def print_stars():
    print("\n**************************\n")

def list_options():

    options = {
        "1": "List all videos", 
        "2": "Create a new video",
        "3": "Select a single video", 
        "4": "Update a video", 
        "5": "Delete a video", 
        "6": "List all customers",
        "7": "Create a new customer",
        "8": "Select a single customer",
        "9": "Update a customer",
        "10": "Delete a customers",
        "11": "Check OUT a video to a customer",
        "12": "Check IN a video from a customer",   
        "13": "List all options",
        "14": "Quit"
        
        }

    print_stars()
    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")
    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options, video_list, customer_list, rental_list):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number: ")

    # if choice in ['4','5','6','7'] and video_list.selected_video == None:
    #     print("You must select a video before updating it, deleting it, marking it complete, or marking it incomplete.")
    #     print("Let's select a video!")
    #     choice = "3"
    
    return choice

def run_cli(play=True):

    #initialize video_list, customer_list
    video_list = VideoList(url=BACKUP_URL)
    customer_list = CustomerList(url=BACKUP_URL)
    rentals_list = RentalList(url=BACKUP_URL)


    # print choices
    options = list_options()   

    while play==True:

        # get input and validate
        choice = make_choice(options, video_list, customer_list, rentals_list)


        video_list.print_selected()
        customer_list.print_selected()

        #1 LIST ALL VIDEOS
        if choice=='1':
            print_stars()
            for video in video_list.list_videos():
                print(video)


        #2 CREATE A NEW VIDEO         
        elif choice=='2':
            print("Great! Let's create a new video.")
            title=input("What is the title of your video? ")
            release_date=input("What is the release date of your video? ")
            total_inventory=input("How many videos are in the total inventory? ")
            response = video_list.create_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("New video has been created:", response)


        #3 SELECT A VIDEO 
        elif choice=='3':
            select_by = input("Would you like to select by TITLE or ID?: ")
            if select_by=="title":
                title = input("What is the TITLE? ")
                video_list.get_video(title=title)
            elif select_by=="id":
                id = input("What is the ID? ")
                if id.isnumeric():
                    id = int(id)
                    video_list.get_video(id=id)
            
            else:
                print("Could not find video. Please enter id or title.")
            
            if video_list.selected_video:
                print_stars()
                print("Selected video: ", video_list.selected_video)
            


        #4 UPDATE A VIDEO 
        elif choice=='4':
            print(f"Great! Let's update the video: {video_list.selected_video}")
            title=input("What is the new title of your video? ")
            description=input("What is the new description of your video? ")
            response = video_list.update_video(title=title, description=description)

            print_stars()
            print("Video now updated:", response["video"])

        #5 DELETE A VIDEO
        elif choice=='5':
            video_list.delete_video()

            print_stars()
            print("Video has been deleted.")

            print_stars()
            print(video_list.list_videos())


        #6 LIST ALL CUSTOMERS
        elif choice=='6':
            print_stars()
            for customer in customer_list.list_customers():
                print(customer)

        #7 CREATE A NEW CUSTOMER
        elif choice=='7':
            print("Great! Let's create a new customer.")
            name=input("What is the name of your customer? ")
            postal_code=input("What is the postal code of your customer? ")
            phone=input("What is the customer's phone number?")
            response = customer_list.create_customer(name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("New customer:", response["customer"])

        #8 SELECT A SINGLE CUSTOMER
        elif choice=='8':
            select_by = input("Would you like to select by? Enter name or id: ")
            if select_by=="name":
                name = input("Which customer would you like to select? ")
                customer_list.get_customer(name=name)
            elif select_by=="id":
                id = input("Which customer id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    customer_list.get_customer(id=id)
            else:
                print("Could not find customer. Please enter id or title.")
            
            if customer_list.selected_customer:
                print_stars()
                print("Selected customer: ", customer_list.selected_customer)


        #9 UPDATE A CUSTOMER 
        elif choice=='9':
            print(f"Great! Let's update the customer: {customer_list.selected_customer}")
            name=input("What is the updated name of your customer? ")
            postal_code=input("What is the updated postal code of your customer? ")
            phone=("What is the updated phone numbner of your customer? ")
            response = customer_list.update_customer(name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("Customer now updated:", response["customer"])

        #10 DELETE A CUSTOMER
        elif choice=='10':
            customer_list.delete_customer()

            print_stars()
            print("Customer has been deleted.")

            print_stars()
            print(customer_list.list_customers())

        #11 CHECK OUT A VIDEO
        elif choice == '11':
            print("Great! Let's check out a video to a customer.")
            customer = customer_list.get_customer(customer_list)
            video_id = input("What is the video id? ")
            if video_id == None:
                return "Could not find video by that id"
            video_id = input("What is the video id? ")
            response = rentals_list.check_out_video(
                customer_id=customer_id, video_id=video_id)

        #12 CHECK IN A VIDEO
        elif choice == '12':
            print("Great! Let's check in a video from a customer.")
            customer_id = input("What is the customer id? ")
            video_id = input("What is the video id? ")
            response = rentals_list.check_in_video(
                customer_id=customer_id, video_id=video_id)

        elif choice == '13':
            choice = make_choice(options)

        elif choice == '14':
            play = False
            print("\nThank you for using the Retro Video Store CLI!")

        print_stars()


if __name__ == "__main__":
    main()
run_cli()