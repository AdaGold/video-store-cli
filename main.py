import requests
from video import Video
from customer import Customer
from rental import Rental


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def list_options():
    options = {
        "1" : "Add a Video", 
        "2" : "Select a Video",
        "3" : "Delete a Video",
        "4" : "Browse all Videos",
        "5" : "Edit one Video",
        "6" : "Add a new customer",
        "7" : "Find a customer",
        "8" : "Remove customer",
        "9" : "Update customer profile",
        "10" : "View all customers",
        "11" : "Check out a Video",
        "12" : "Return a Video", 
        "0" : "List all options"
    }
    for choice in options:
        print(f"Option {choice}: {options[choice]}")
    return options

def make_choice(options, video, customer, rental):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print(f"Please select from the valid options, select 0 to view them again")
        choice = input("Make your selection: ")
    
    if choice in ["5", "3"] and video.selected_video == None:
        print("You must select a video before editing!")
        choice = "2"
    
    return choice


def main(store_open=True):

    video = Video(URL)
    customer = Customer(URL)
    rental = Rental(URL)
    options = list_options()

    while store_open:
        choice = make_choice(options, video, customer, rental)
        video.print_selected()
        customer.print_selected()

        if choice == '1':
            print("Let's add a video!")
            title = input("What's the name of the video?")
            release_date = input("What is the release date?")
            total_inventory = input("What is the total inventory?")
            response = video.add_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print("New Video:", response["video"])
        
        elif choice == '2':
            select_by = input("Would you like to select by title, id, or release date?")
            if select_by == "title":
                title = input("Which title?")
                video.get_video(title=title)
            elif select_by == "id":
                id = input("Which ID?")
                if id.isnumeric():
                    id = int(id)
                    video.get_video(id=id)
            elif select_by == "release date":
                release_date = input("When was it released?")
                video.get_video(release_date=release_date)
            else:
                print("Please enter title, id, or release date. ")
            
            if video.selected_video:
                print(f"Selected video is {video.title}")

        
        elif choice == '3':
            video.delete_video()

            print(video.list_videos())

        elif choice == '4':
            for video in video.list_videos():
                print(video)
        
        elif choice == '5':
            print(f"Great! Let's edit {video.selected_video}")
            update = input("Would you like to edit the title, release date, or inventory?")
            if update == 'title':
                title = input("What's the new title?")
            elif update == 'release_date':
                release_date = input("What's the correct release date?")
            elif update == 'inventory':
                total_inventory = input("What's the new inventory total?")
            response = video.update_video(title, release_date, total_inventory)

            print("Updated video:", response["video"])
        
        elif choice == '6':
            print("Let's add a new customer!")
            name = input("What's the name of the customer?")
            phone = input("What's the customer's phone number?")
            postal_code = input("What is the customer's postal code?")

            response = customer.add_customer(name=name, phone=phone, postal_code=postal_code)
            print("New customer:" , response["name"])
        
        elif choice == '7':
            select_by = input("Would you like to find the customer by name, phone, or id?")
            if select_by == 'name':
                name = input("What is the customer's name?")
                customer.get_customer(name=name)
            
            elif select_by == 'phone':
                phone = input("What is the customer's phone number?")
                customer.get_customer(phone=phone)
            
            elif select_by == 'id':
                id = input("What is the customer id?")
                customer.get_customer(id=id)

            else:
                print("Please enter name, phone, or id")
            
            if customer.select_customer:
                print(f"Selected customer: {customer.name}")
        
        elif choice == '8':
            customer.delete_customer()
            print(customer.list_customers())
        
        elif choice == '9':
            print("Great! Let's update the customer!")
            update = input("Would you like to update the name, phone, or postal number?")
            if update == 'name':
                name = input("What is the customer's updated name?")
            if update == 'phone':
                phone = input("What is the udpated phone number?")
            if update == 'postal code':
                postal_code = input("what is the updated postal code?")
            
            response = customer.update_customer(name, phone, postal_code)
        
        elif choice == '10':
            for customer in customer.list_customers():
                print(customer)


if __name__ == "__main__":
    main()