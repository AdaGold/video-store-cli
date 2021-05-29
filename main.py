import requests
from video import Video
from customer import Customer
from rental import Rental
#URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"


def print_brand():
    print()
    print("✨ ⏩ ⭐️ 🔥 🎞️  🤠 📼  RETRO VIDEO STORE 📼 ⏩ 🔥 🤠 ⭐️ 🎞️ ✨")
    print()
    print( ".................... 💗 Be Kind. 💗 ........................")
    print(" ..................🥺 Please Rewind. 🥺 ................... ")

def menu_options():
    options = {
        "1": "Add 1 Video to our Extensive Collection ", 
        "2": "Update 1 Video's Information",
        "3": "Delete a Video", 
        "4": "View all Video Info", 
        "5": "Info on 1 Video", 
        "6": "New Customer Sign Up",
        "7": "Update a Customer's Information",
        "8": "Delete 1 Customer ",
        "9": "View Info on 1 Customer",
        "10": "View all Customers",
        "11" : "Check in 1 Video",
        "12": "Check out 1 Video Return",
        "13" : "List all Options",
        "14": "Q U I T"
        }
    for one_option in options:
        print(f"Option #{one_option}. {options[one_option]} \n")
    
    return options
def make_choice(options, video, customer, rental):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print_brand()
        print()
        print("Please reference the list above for all the options you have \n")
        choice = input("What do you want to do?! Select a valid option: ")
        # check to make sure choice is a valid input by checking isnumeirc 

    if choice in ['2','3'] and video.selected_video == None:
        print("You must select a video before updating it, deleting it")
        print("Please select a Video!")
        # select info on one video
        choice = "5"
    
    if choice in ["7", "8"] and customer.selected_customer == None:
        print("You must select a customer before updating it, deleting it")
        print("Please select a Customer!")
        choice = "9"
    
    return choice        

def main(play=True):
    # initialize video_store
    video = Video(url = BACKUP_URL)
    customer = Customer(url= BACKUP_URL)
    rental = Rental(url=BACKUP_URL)
    print_brand()
    print()
    options = menu_options()

    while play == True:
        # get input and validate 
        choice = make_choice(options, video, customer, rental)
        video.print_selected()
        customer.print_selected()

        # "1": "Add 1 Video to our Extensive Collection " 
        if choice == '1':
            print("Let's get started on adding a new video to our growing collection !\n ")
            title=input("What is the title of the video? \n").title()
            release_date =input("When was the video realeased? \n")
            total_inventory =input("How many video copies do we own? \n")
            response = video.create_video(title=title, release_date =release_date, total_inventory=total_inventory)
            print()
            print("New Video Added to the Collection:", title.title())
            #print("New Video:", response["title"]) # I need to return the name of the video here 
        ## "2": "Update 1 Video's Information"    
        elif choice == '2':
            print(f"Let's update the video: {video.selected_video}")
            title=input("What is the new title of your video?\n")
            release_date=input("What is the new release date of your video? YYYY-MM-DD\n")
            total_inventory = int(input("What is the total inventory?\n"))
            response = video.edit_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print()
            print("Updated Video:", response)
        ## "3": "Delete a Video"    
        elif choice == '3':
            video.delete_video()
            print()
            print("Video has been deleted.")
            print()
            print(video.list_videos())
        ## "4": "View all Video Info"    
        elif choice == '4':
            for video in video.list_videos():
                print(video)
        ## "5": "Info on 1 Video"    
        elif choice == '5':
            select_by = input("Would you like to select by? Enter title or id: \n ")
            if select_by=="title":
                title = input("Which video title would you like to select? \n")
                video.get_video(title=title)
            elif select_by=="id":
                id = input("Which video id would you like to select? \n")
                if id.isnumeric():
                    id = int(id)
                    video.get_video(id=id)
            else:
                print("Could not locate. Please enter a valid id or title we have in our collection.")
            
            if video.selected_video:
                print()
                print("Selected Video: ", video.selected_video)
        # "6": "New Customer Sign Up"    
        elif choice == '6':
            print("Let's get started on adding a new customer!\n ")
            name=input("What is the name of the customer? \n").title()
            postal_code =input("What's the customer's postal code? \n")
            phone =input("What is the customer's phone number? \n")
            response = customer.create_new_customer(name=name, postal_code =postal_code, phone=phone)
            print()
            print("New Customer added to the Retro Video Store:", name.title())
        ## "7": "Update a Customer's Information"    
        elif choice == '7':
            print(f"Let's update the customer's information: {customer.selected_customer}")
            name=input("What updates do you want to make to the customer's name?\n")
            postal_code=input("What updates do you want to make to the customer's postal code?\n")
            phone = input("What updates do you want to make to the customer's phone?\n")
            response = customer.update_customer(name=name, postal_code=postal_code, phone=phone)
            print()
            print("Updated Customer:", response)
        ## "8": "Delete 1 Customer "    
        elif choice == '8':
            customer.delete_customer()
            print()
            print("The Customer has been deleted.")
            print()
            print(customer.list_customers())
        ## "9": "View  Info on 1 Customer"    
        elif choice == '9':
            select_by = input("Would you like to select by? Enter name or id: \n ")
            if select_by=="name":
                name = input("Which customer name would you like to locate? \n")
                customer.get_customer(name=name)
            elif select_by=="id":
                id = input("Which customer id would you like to locate? \n")
                if id.isnumeric():
                    id = int(id)
                    customer.get_customer(id=id)
            else:
                print("Could not locate. Please enter a valid customer id or name")
            
            if customer.selected_customer:
                print()
                print("Selected Customer: ", customer.selected_customer)
        ## "10": "View all Customers"    
        elif choice == '10':
            for customer in customer.list_customers():
                print(customer)
        # "11" : "Check in 1 Video"    
        elif choice == '11':
            print("Let's get started with the check-in process!\n ")
            video_id = input("What is the video id: ")
            if video_id.isnumeric():
                video_id = int(video_id)
                video.selected_video = video.get_video(id=video_id)
                print(video.selected_video) 
            customer_id = input("What is the customer's id checking ing the video: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                customer.selected_customer = customer.get_customer(id=customer_id)
                print(customer.selected_customer)
            
            checked_in_rental = rental.check_in(customer_id, video_id)
            print(checked_in_rental)
            print(" Success ! The video was checked in!")

        ## "12": "Check out 1 Video Return"   
        elif choice == '12':
            print("Let's get started with the check-out process!\n ")
            video_id = input("What is the video id: ")
            if video_id.isnumeric():
                video_id = int(video_id)
                video.selected_video = video.get_video(id=video_id)
                print(video.selected_video)

            customer_id = input("What is the customer's id: ")
            if customer_id.isnumeric():
                customer_id = int(customer_id)
                customer.selected_customer = customer.get_customer(id=customer_id)
                print(customer.selected_customer)
            
            checked_out_rental = rental.check_out(customer_id, video_id)
            print("Success! The video was checked out!")
            print(checked_out_rental)
            print()                            
        ## "13" : "List all Options"
        elif choice=='13':
            menu_options()
        # "14": "Q U I T"
        elif choice=='14':
            play=False
            print("\n 💸 💰 Thank you for logging off for the day! 💰 💸 \n 💆🏽‍♀️ 🍓 have a good rest of your day! 🍧 💅🏾")
        
            


main()

# you can just call main function to set up the cli, the only on she called 
# this tells the interpreter to run first in order for cli to show up bc you have other function involved 
# common pattern 
# you can remove this line and just call main 
# python interprets from the top down
#if __name__ == "__main__":
#    main()

# think of the logic on how to quit a program, i want to include it after each response, 
# on each line     
#select_by = input("First, How would you like to start the video look up process? Locating the title or id?: \n ")
#            if select_by == "title":
#                title = input("Which video title would you like to select? \n")
#                video.get_video(title=title)
#            elif select_by =="id":
#                if id.isnumeric():
#                    id = int(id)
#                    video.get_video(id=id)
#                else:
#                    print("Could not locate. Please enter a valid video id or name")
#            # now that I got the video I need to ask the user for the customer's id and add it to their rentals 
#            print("That's a great movie!")
#            select_by_customer = input("Who is the customer you would you like to rent this out to? Enter id or name: \n ")
#            if select_by_customer == "name":
#                name = input("Which customer name would you like to locate? \n")
#                customer.get_customer(name=name)
#            elif select_by =="id":
#                id = input("Which customer id would you like to locate? \n")
#                if id.isnumeric():
#                    id = int(id)
#                    customer.get_customer(id=id)
#                else:
#                    print("Could not locate. Please enter a valid video id or name")