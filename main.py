import requests
from video import Video
from customer import Customer
from rental import Rental

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    pass


if __name__ == "__main__":
    main()


def print_stars():
    print("\n**************************\n")

def list_options():

    options = {
        "1": "add a video", #done
        "2": "edit a video", #done
        "3": "delete a video", #done
        "4": "get information about all videos", #done
        "5": "get information about one video", #select a video #done
        "6": "add a customer", #done
        "7": "edit a customer", #done
        "8": "Delete a customer", #done
        "9": "get information about one customer", #select a customer # done
        "10": "get information about all customers", # done
        "11": "check out a video to a customer",
        "12": "check in a video from a customer",
        "13": "List all options",#done
        "14": "Quit" #done
        }

    print_stars()
    print("Welcome to the Video Store CLI")
    print("These are the actions you can perform")
    print_stars()
    
    for choice_num in options:
        print(f"Option {choice_num}. {options[choice_num]}")

    print_stars()

    return options


def make_choice(options, video,customer,rental):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 13 to see all options again")
        choice = input("Make your selection using the option number 1-14: ")

    if choice in ['2','3'] and video.selected_video == None:
        print("You must get information about one video before updating it or deleting it.")
        print("Let's get information about one video")
        choice = "5"
    
    if choice in ['7','8'] and customer.selected_customer == None:
        print("You must get information about a customer before updating it or deleting it.")
        print("Let's get information about one customer")
        choice = "9"

    return choice

def run_cli(play=True):
    video=Video(url="https://retro-video-store-api.herokuapp.com/")
    customer=Customer(url="https://retro-video-store-api.herokuapp.com/")
    rental=Rental(url="https://retro-video-store-api.herokuapp.com/")
    # print choices
    options = list_options()

    while play==True:

        # get input and validate
        choice = make_choice(options, video,customer,rental)

        #options.print_selected()
        video.print_selected()
        customer.print_selected()
        #rental.print_selected()

        if choice=='4': #get information about all videos
            print_stars()
            for video in video.list_videos():
                print(f"Id: {video['id']},Title: {video['title']}")
                #print(video)
        elif choice=='1': #add a video
            print("Great! Let's add a video.")
            title=input("What is the title of your video? ")
            release_date=input("Enter release date ")
            total_inventory=input("Enter total inventory for this video ")
            response = video.create_video(title=title, release_date=release_date,total_inventory=total_inventory)
            video_info = video.get_video(title=title, id = response['id'])
            print_stars()
            print("New video:", video_info) 
            
        elif choice=='5': #select a video
            select_by = input("What would you like to select by? Enter 'title' or 'id': ")
            if select_by=="title":
                
                title = input("Which video title would you like to select? ")
               
                video.get_video(title=title)
                
            elif select_by=="id" or select_by == "ID" or select_by == "Id":
                id = input("Which video id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    video.get_video(id=id)
            else:
                print("Could not select. Please enter the words 'id' or 'title'.")
            # if selected_video:
            if video.selected_video:
                print_stars()
                print("Selected video: ", video.selected_video)
            else:
                print("\nInvalid id or title entry,\nplease check video list to make sure video is in inventory.\nSelect option 4 for inventory info\nOr select option 1 to add this video to inventory")
                
        
        elif choice=='2': #update a video
            print(f"Great! Let's update the video information: {video.selected_video}")
            title=input("What is the new title of your video? ")
            release_date=input("Enter Release Date:  ")
            total_inventory=input("Enter total inventory: ")
            response = video.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("Updated response:", response)
        
        elif choice=='3':#delete a video
            video.delete_video()

            print_stars()
            print("Video has been deleted.")

            print_stars()
            print(video.list_videos())
        
        elif choice=='10':
            print_stars()
            for customer in customer.list_customers():
                print(f"Id: {customer['id']}, Name: {customer['name']}")
                #print(customer)

        elif choice=='6':
            print("Great! Let's add a customer. ")
            name=input("What is the name of the customer? ")
            postal_code=input("Enter postal_code: ")
            phone=input("Enter phone: ")
            response = customer.create_customer(name=name, postal_code=postal_code, phone=phone)
            customer_info = customer.get_customer(name = name, id = response['id'])

            print_stars()
            print("New customer:", customer_info)

        elif choice=='9':
            select_by = input("Would you like to select by? Enter 'name' or 'id': ")
            if select_by=="name":
                name = input("Which customer name would you like to select? ")
                customer.get_customer(name=name)
            elif select_by=="id" or select_by == "ID" or select_by == "Id":
                id = input("Which customer id would you like to select? ")
                if id.isnumeric():
                    id = int(id)
                    customer.get_customer(id=id)
            else:
                print("Could not select. Please enter id or name.")
            
            if customer.selected_customer:
                print_stars()
                print("Selected customer: ", customer.selected_customer)

            else:
                print("\nInvalid id or name entry,\nplease check customer list to make sure customer exists.\nSelect option 10 for customer list info\nOr select option 6 to add this customer")

        elif choice=='7':
            print(f"Great! Let's update the customer information: {customer.selected_customer}")
            name=input("What is the new name of your customer? ")
            postal_code=input("Enter Postal Code:  ")
            phone=input("phone: ")
            response = customer.update_customer(name=name, postal_code=postal_code, phone=phone)

            print_stars()
            print("Updated resonse:", response)

        elif choice=='8':
            customer.delete_customer()

            print_stars()
            print("Customer has been deleted.")

            print_stars()
            print(customer.list_customers())

        elif choice == '11': #check out video to customer
            print_stars()
            print("Let's checkout a video! ")

            print("Here are all of the available videos: ")
            all_videos = video.list_videos()

            for choices in all_videos:
                print(f"Id: {choices['id']},Title: {choices['title']}")

            select_by = input("What would you like to select by? Enter either 'title' or 'id': ")
            
            if select_by == "title":
                title = input("which video title would you like to select? ")
                video.get_video(title=title)
            
            elif select_by == 'id':
                video_id = input("Which video ID would you like to select? ")
                if video_id.isnumeric():
                    video_id = int(video_id)
                    #video.selected_video = video.get_video(id=video_id)
                    video.get_video(id=video_id)

            else:
                print("please enter a valid video ID: ")
            
            if video.selected_video:
                print_stars()
                print("The chosen video information is: ", video.selected_video)
                print(video.selected_video)
            
            print("Here are all of the customers: ")

            all_customers = customer.list_customers()

            for person in all_customers:
                print(f"Id: {person['id']}, name: {person['name']}")

            select_by = input("What would you like to select by? Enter either 'name' or 'id': ")
            if select_by == "name":
                customer_name = input("Which customer name would you like to select? ")
                selected_customer=customer.get_customer(name=customer_name)
                print(video.selected_video)
                customer_id=selected_customer["id"]
                video_id=video.selected_video["id"]
                # video_id = selected_customer["video_id"]
            elif select_by == "id":
                customer_id = input("Which customer ID would you like to select? ")
                if customer_id.isnumeric():
                    customer_id = int(customer_id)
                    #customer.selected_customer = customer.get_customer(id=customer_id)
                    customer.get_customer(id=customer_id)
            
            else:
                print("Please enter valid customer ID: ")
            
            if customer.get_customer(id=customer_id):
                print_stars()
                #print("Selected customer: ", customer.get_customer(id=customer_id))
                response = rental.check_out(customer_id,video_id)
            print("Video successfully checked out! Rental info: ", response)

        elif choice == '12': #check in a video from customer
            print_stars()
            print("Let's return a video! ")

            print("Here are all of the available videos: ")
            all_videos = video.list_videos()

            for choices in all_videos:
                print(f'Id: {choices["id"]}, Title:{choices["title"]}')

            select_by = input("What would you like to select by? Enter either 'title' or 'id'. ")
            if select_by == "title":
                title = input("which video title would you like to select? ")
                video.get_video(title=title)
            
            elif select_by == "id":
                video_id = input("Which video ID would you like to select? ")
                if video_id.isnumeric():
                    video_id = int(video_id)
                    #video.selected_video = video.get_video(id=video_id)
                    video.get_video(id=video_id)
            else:
                print("Please enter a valid video ID: ")

            if video.selected_video:
                print_stars()
                print("Selected Video Information is: ", video.selected_video)
                #print(video.selected_video)

            print("Here are all of the customers: ")
            all_customers = customer.list_customers()

            for person in all_customers:
                print(f'id:{person["id"]},name: {person["name"]}')
                #print(f'ID: {customer['id']}, name: {customer['name']}')
            
            select_by = input("What would you like to select by? Enter either 'name' or 'id': ")
            if select_by == "name":
                customer_name = input("Which customer name would you like to select? ")
                selected_customer = customer.get_customer(name=customer_name)
                #print(selected_customer)
                customer_id=selected_customer['id']
                video_id=video.selected_video['id']
            elif select_by == "id":
                customer_id = input("Which customer ID would you like to select? ")
                if customer_id.isnumeric():
                    customer_id = int(customer_id)
                    #customer.selected_customer = customer.get_customer(id=customer_id)
                    customer.get_customer(id=customer_id)
            else:
                print("Please enter valid Customer ID: ")

            if customer.get_customer(id=customer_id):
                print_stars()
                #print("Selected customer: ", customer.selected_customer)
                response = rental.check_in(customer_id, video_id)
            print("Video sucessfully checked in! Rental Info: ", response)

        

        elif choice=='13':
            list_options()
        elif choice=='14':
            play=False
            print("\nThanks for using the Retro Video CLI!")

        print_stars()

run_cli()