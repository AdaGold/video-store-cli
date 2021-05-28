import requests
from video import Video
from customer import Customer
from rental import Rental


URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://localhost:5000"

def list_options():
    options = {
        "1" : "Add a Video", 
        "2" : "Select a Video",
        "3" : "Browse all Videos",
        "4" : "Add a new customer",
        "5" : "Find a customer",
        "8" : "Remove customer",
        "9" : "Update customer profile",
        "10" : "View all customers",
        "11" : "Check out a Video",
        "12" : "Return a Video", 
        "0" : "List all options",
        "99" : "Close up for the day!"
    }
    
    for choice in options:
        print(f"Option {choice}: {options[choice]}")
    return options

def make_choice(all_options, video, customer, message = None, choice = None):
    valid_choices = all_options.keys()

    while choice not in valid_choices:
        message = print(f"Please select from the valid options, select 0 to view them again")
        choice = input("Make your selection: ")
    
    return choice

def main(store_open=True):

    video = Video(URL)
    customer = Customer(URL)
    rental = Rental(URL)
    options = list_options()

    while store_open:
        choice = make_choice(options, video, customer)
        
        if choice == '1':
            print("Let's add a video!")
            title = input("What's the name of the video?")
            release_date = input("What is the release date?")
            total_inventory = input("What is the total inventory?")
            response = video.add_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print("New Video:", response)
        
        elif choice == '2':
            select_by = input("Would you like to select by title, id, or release date?")
            if select_by == "title":
                title = input("Which title?")
                video.get_video(title=title)
            elif select_by == "id":
                id = input("Which ID?")
                video.get_video(id=int(id))
            elif select_by == "release date":
                release_date = input("When was it released?")
                video.get_video(release_date=release_date)
            else:
                print("Please enter title, id, or release date. ")
            
            video.print_selected()

            if video.selected_video:
                next_step = input("What would you like to do with the video? Select 1 to delete, or 2 to edit.")

                if next_step == '1':
                    print(f"Video {video.selected_video['title']} is being deleted.")
                    video.delete_video()
                
                elif next_step == '2':
                    print(f"Great! Let's edit {video.selected_video['title']}")
                    update = input("Would you like to edit the title, release date, or inventory?")
                    if update == 'title':
                        title = input("What's the new title?")
                    elif update == 'release_date':
                        release_date = input("What's the correct release date?")
                    elif update == 'inventory':
                        total_inventory = input("What's the new inventory total?")
                    response = video.update_video(title, release_date, total_inventory)

                    print("Updated video:", response["video"])
                


        elif choice == '4':
            print(video.list_videos())
        
        
        
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
                customer.get_customer(id=int(id))
            
            else:
                print("Please enter name, phone, or id")
        
            customer.print_selected()

        
        elif choice == '8':
            customer.delete_customer()
            print(f"Customer has been deleted. ")
        
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
            print(customer.list_customers())
        
        elif choice == '11':
            customer_id = input("Which customer id is renting?")
            video_id = input("Which video id are they renting?")

            response = rental.check_out(int(customer_id), int(video_id))
            print("Enjoy the movie!")
        
        elif choice == '12':
            customer_id = input("Which customer id is returning?")
            video_id = input("Which video id are they returning?")
            response = rental.check_in(int(customer_id), int(video_id))
            
            print("Thanks for bringing it back!")

        elif choice == '0':
            list_options()
        
        elif choice == "99":
            store_open = False
            print("Don't forget to lock up on your way out!")


if __name__ == "__main__":
    main()