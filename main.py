import requests
from datetime import datetime
from rental_list import RentalList
from video_list import VideoList
from customer_list import CustomerList

URL = "http://127.0.0.1:5000"


def main():
    if __name__ == "__main__":
        main()

def print_squiggle():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def list_options():
    
    options = {
        "1": "Add a Video",
        "2": "Edit a Video",
        "3": "Delete a Video",
        "4": "Get all of the Videos Information",
        "5": "Get one of the Videos Information",
        "6": "Add a Customer",
        "7": "Edit a Customer",
        "8": "Delete a Customer",
        "9": "Get all of the Customers Information",
        "10": "Get one of the Customers Information",
        "11": "Check out a Video to a Customer",
        "12": "Check in a Video from a Customer",
        "13": "List all options",
        "14" : "Quit"
        }
    
    print_squiggle()
    print("Welcome to the Snazzy Video Store!")
    print("These are the actions you can perform")
    print_squiggle()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_squiggle()
    
    return options
    
def main(play=True):

    video_list = VideoList(URL)
    customer_list = CustomerList(URL)
    rental_list = RentalList(URL)
    options = list_options()

    while play==True:
        choice = make_choice(options, video_list, customer_list, rental_list)

        video_list.print_selected()
        customer_list.print_selected()

        if choice=='1':
            print_squiggle()
            print("Hi!! Let's add a video! ")
            title=input("What is the title of the video? ")
            release_date=input("What is the release date of the video? (YYYY-MM-DD) ")
            total_inventory=input("What is the total inventory for this video? ")
            response = video_list.create_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_squiggle()
            print("Great!! New video created with ID:", response["id"])
            
        elif choice=='2':
            print(f"Great! Let's update the video: {video_list.selected_video}")
            title=input("What is the new title of this video? ")
            release_date=input("What is the new release date of this video? (YYYY-MM-DD) ")
            total_inventory=input("What is the new inventory of this video? ")
            
            response = video_list.update_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print_squiggle()
            print("Updated video: ", response["title"])

        elif choice=='3':
            delete_video = input("Please input the video ID you would like to delete ")
            if delete_video.isnumeric():
                delete_video  = int(delete_video)
                video_list.delete_video(id=delete_video)
    
            print_squiggle()
            print("The video has successfully been deleted. ")
            print_squiggle()
        
        elif choice=='4':
            print_squiggle()
            for video in video_list.list_videos():
                print(video)
            
        elif choice=='5':
            print("Here are all of the available videos: ")
            all_videos = video_list.list_videos()
            
            for video in all_videos:
                print(f"Id: {video['id']}, Title: {video['title']}")
            
            select_by = input("What would you like to select by? Enter either a title or an id: ")
            if select_by == "title":
                title = input("Which video title would you like to select? ")
                video_list.get_video(title=title)
            elif select_by == "id":
                video_id = input("Which video ID would you like to select? ")
                if video_id.isnumeric():
                    video_id = int(video_id)
                    video_list.selected_video = video_list.get_video(id=video_id)
            else:
                print("Please enter a valid video ID:")
            
            if video_list.selected_video:
                print_squiggle()
                print("The choosen video information is: ", video_list.selected_video)
            
        elif choice =='6':
            print_squiggle()
            print("Hi!! Let's add a customer! ")
            name=input("What is the customers name? ")
            phone=input("What is their phone number? (xxx-xxx-xxxx) ")
            postal_code=input("What is their postal code? ")
            response = customer_list.create_customer(name=name, phone=phone, postal_code=postal_code)
            print_squiggle()
            print("Great! New customer created with ID:", response["id"])
        
        
        elif choice == '7':
            print(f"Great! Let's update the customer: {customer_list.selected_customer}")
            name=input("What is the new name of the customer? ")
            phone=input("What is their new phone number? (xxx-xxx-xxxx) ")
            postal_code=input("What is their new postal code? ")
            response = customer_list.update_customer(name=name, phone=phone, postal_code=postal_code)
            print_squiggle()
            print("Updated customer:", response["name"])
    
        
        elif choice == '8':
            customer_list.delete_customer(customer_id)
            print_squiggle()
            print("The customer has successfully been deleted. ")
            print_squiggle()
            
            
        elif choice == '9':
            print("Here are all of the customers: ")
            all_customers = customer_list.list_customers()
            
            for customer in all_customers:
                print(f"Id: {customer['id']}, name: {customer['name']}")
            
            select_by = input("What would you like to select by? Enter either a name or an id: ")
            if select_by == "name":
                name = input("Which customer name would you like to select? ")
                customer_list.get_customer(name=name)
            elif select_by == "id":
                customer_id = input("Which customer ID would you like to select? ")
                if customer_id.isnumeric():
                    customer_id = int(customer_id)
                    customer_list.selected_customer = customer_list.get_customer(id=customer_id)
            else:
                print("Please enter valid customer ID: ")
            
            if customer_list.selected_customer:
                print_squiggle()
                print("Selected customer: ", customer_list.selected_customer)
            
            
        elif choice == '10':
            print_squiggle()
            for customer in customer_list.list_customers():
                print(customer)
            
        
        elif choice == '11':
            print_squiggle()
            print("Let's checkout a video! ")
            
            print("Here are all of the available videos: ")
            all_videos = video_list.list_videos()
            
            for video in all_videos:
                print(f"Id: {video['id']}, Title: {video['title']}")
            
            select_by = input("What would you like to select by? Enter either a title or an id: ")
            if select_by == "title":
                title = input("Which video title would you like to select? ")
                video_list.get_video(title=title)
            elif select_by == "id":
                video_id = input("Which video ID would you like to select? ")
                if video_id.isnumeric():
                    video_id = int(video_id)
                    video_list.selected_video = video_list.get_video(id=video_id)
            else:
                print("Please enter a valid video ID:")
            
            if video_list.selected_video:
                print_squiggle()
                print("The choosen video information is: ", video_list.selected_video)
                print(video_list.selected_video)
            
            print("Here are all of the customers: ")
            all_customers = customer_list.list_customers()
            
            for customer in all_customers:
                print(f"Id: {customer['id']}, name: {customer['name']}")
            
            select_by = input("What would you like to select by? Enter either a name or an id: ")
            if select_by == "name":
                name = input("Which customer name would you like to select? ")
                customer_list.get_customer(name=name)
            elif select_by == "id":
                customer_id = input("Which customer ID would you like to select? ")
                if customer_id.isnumeric():
                    customer_id = int(customer_id)
                    customer_list.selected_customer = customer_list.get_customer(id=customer_id)
            else:
                print("Please enter valid customer ID: ")
            
            if customer_list.selected_customer:
                print_squiggle()
                print("Selected customer: ", customer_list.selected_customer)
            
            response = rental_list.create_rental(customer_id, video_id)
            print("Video sucessfully checked out! ")
            
        elif choice == '12':
            print_squiggle()
            print("Let's return a video! ")
            
            print("Here are all of the available videos: ")
            all_videos = video_list.list_videos()
            
            for video in all_videos:
                print(f"Id: {video['id']}, Title: {video['title']}")
            
            select_by = input("What would you like to select by? Enter either a title or an id: ")
            if select_by == "title":
                title = input("Which video title would you like to select? ")
                video_list.get_video(title=title)
            elif select_by == "id":
                video_id = input("Which video ID would you like to select? ")
                if video_id.isnumeric():
                    video_id = int(video_id)
                    video_list.selected_video = video_list.get_video(id=video_id)
            else:
                print("Please enter a valid video ID:")
            
            if video_list.selected_video:
                print_squiggle()
                print("The choosen video information is: ", video_list.selected_video)
                print(video_list.selected_video)
            
            print("Here are all of the customers: ")
            all_customers = customer_list.list_customers()
            
            for customer in all_customers:
                print(f"Id: {customer['id']}, name: {customer['name']}")
            
            select_by = input("What would you like to select by? Enter either a name or an id: ")
            if select_by == "name":
                name = input("Which customer name would you like to select? ")
                customer_list.get_customer(name=name)
            elif select_by == "id":
                customer_id = input("Which customer ID would you like to select? ")
                if customer_id.isnumeric():
                    customer_id = int(customer_id)
                    customer_list.selected_customer = customer_list.get_customer(id=customer_id)
            else:
                print("Please enter valid customer ID: ")
            
            if customer_list.selected_customer:
                print_squiggle()
                print("Selected customer: ", customer_list.selected_customer)
            
            response = rental_list.return_rental(customer_id, video_id)
            print("Video sucessfully checked in! ")
        
        elif choice=='13':
            list_options()
            
        elif choice=='14':
            play=False
            print("\nThank you, Bye!!")
        
        else:
            print("Invalid option", choice, "Please select a valid choice ")

        print_squiggle()
        
        
def make_choice(options, video_info, customer_info, rental_info):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all the options again! ")
        choice = input("Make your selection using the option numbers 1 - 14 : " )
        
    if choice in ['2', '3'] and video_info.selected_video == None:
        print("You must select a video before updating or deleting! ")
        print("Please select a video! ")
        choice = "5"
        
    elif choice in ['7','8'] and customer_info.selected_customer == None:
        print("You must select a customer before updating or deleting! ")
        print("Please select a customer! ")
        choice = "9"
        
    return choice

if __name__ == "__main__":
    main()