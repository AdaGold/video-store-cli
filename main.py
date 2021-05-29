import requests
from video_requests import VideoRequests
from customer_requests import CustomerRequests
from rental_requests import RentalRequests

URL = "http://127.0.0.1:5000"  #local host
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"
#MY_URL = "https://video-retro.herokuapp.com" #api route

video_requests = VideoRequests(url=BACKUP_URL)
customer_requests = CustomerRequests(url=BACKUP_URL)
rental_requests = RentalRequests(url=BACKUP_URL)

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    cli_go()

def welcome_screen():
    pass

def list_user_options():
    options = {
        1: "List all options",
        2: "Quit",
        #video requests
        3: "List all videos",
        4: "Select a video",
        5: "List total video inventory for store", #still need to figure thids out too
        6: "List total inventory for a specific video",
        7: "Add a Video",
        8: "Edit a Video",
        9: "Delete a video",
        10: "Delete all videos",
        #customer requests options
        11: "List all customers",
        12: "Select a customer", 
        13: "Get information about a specific customer", 
        14: "Get information about all customer accounts",
        15: "Add a customer account",
        16: "Edit customer information",
        17: "Delete customer account",
        18: "Delete all customer accounts",
        #rental requests
        19: "Check out a video to a customer",
        20: "Check in a video to a customer",
        21: "Check number of rentals a customer has", 
        22: "Print currently selected customer",
        23: "Print currently selected video"
    }

    print("These are the actions you can perform")

    for option_num in options:
        print(f"Option {option_num}. {options[option_num]}")

    return options  

def user_selection_option(options):
    valid_selection = options.keys()
    print(options.keys())
    user_selection = None

    while user_selection not in valid_selection:
        print("user_selection while loop begins")

        print("Please select an option, enter option 1 to see all options again\n.")
        
        user_selection = input("Please enter the option number of the action you would like to take: ")
        user_selection = int(user_selection)
        
    
    if user_selection in [8, 9] and video_requests.selected_video == None:
        print("You must first select a video by entering option 4, before you can edit or delete it.")
        print("Please select a video: ")
        user_selection = "4"
    
    if user_selection in [13, 16, 17, 18, 21] and customer_requests.selected_customer == None:
        print("You must first select a customer by entering option 12, before you can edit or delete a customer account.")
        print("Please select a customer: ")
        user_selection = "12"
    

    return user_selection


def cli_go(play=True):

    options = list_user_options()

    while play == True:

        user_selection = user_selection_option(options)
        video_requests.print_video()

        if user_selection == 1: #list all options
            list_user_options()

        elif user_selection == 2: #quit
            play=False
            print("Back to the dull life of streaming!")
        
        elif user_selection == 3: #"List all videos"
            for video in video_requests.list_all_videos():
                #format
                print(video)
        
        elif user_selection == 4: #"Select a video"
            selection_method = input("You can select a video by title or id.\n If you would like to select by title, type 'title'. If you would like to select by id, type, 'id': ")
            
            if selection_method == "title":
                title = input("Please enter the title of the video you would like to select: ")
                video_requests.get_specific_video(title=title)
            elif selection_method == "id":
                id = input("Please enter the id of the video you would like to select: ")
                if id.isnumeric():
                    id = int(id)
                    video_selection_response = video_requests.get_specific_video(id=id)
                    print(video_selection_response)
            else:
                print("Selection error, please enter 'id' or 'title' to make your selection.")
            
            if video_requests.selected_video:
                print("Currently selected video: ", video_requests.selected_video)

        elif user_selection == 5: #"List total video inventory for store"
            #selected_video.rental
            pass

        elif user_selection == 6: #"List total inventory for a specific video"
            #print(selected_video.total_inventory)
            pass

        elif user_selection == 7: #"Add a video"

            print("Yay a new video to add to the inventory!")
            title = input("Enter the title of the video: ")
            release_date = input("Enter the release date in yyyy-mm-dd format: ")
            total_inventory = input("Enter the total inventory for this video: ")
            response = video_requests.create_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print("New video:", response)
        
        elif user_selection == 8: #"Edit a Video"
            print("To update the video: ", video_requests.selected_video)
            title = input("Enter the new title of the video: ")
            release_date = input("Enter the new release date in yyyy-mm-dd format: ")
            total_inventory = input("Enter the new value (integer) for total inventory: ")  
            response = video_requests.update_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print("Updated video:", response) 
        
        elif user_selection == 9:
            print("You have selected to delete a video. Are you sure that you want to delete this video from the inventory list?") #"Delete a video"    
            confirm_delete = input("If yes enter 'Y', if no enter 'N': ")
            if confirm_delete == 'Y':
                video_requests.delete_video()
                print(f"The video has been deleted.")
                print(video_requests.list_all_videos())


        elif user_selection == 10: #Delete all videos 
            print("Deleted inventory can not be retrieved. Are you sure you want to delete all of the videos in the store inventory?")
            confirm_delete = input("Enter Y if you want to delete all videos, N to cancel the request: ")
            
            if confirm_delete == 'Y':
                for video in video_requests.list_all_videos():
                    video_requests.get_specific_video(id=video['id'])
                    video_requests.delete_video(id)
            
                print("All videos have been deleted.")
                print(video_requests.list_all_videos())
            

        #customer requests options 
        elif user_selection == 11: #List all customers
            
            for customer in customer_requests.list_all_customers():
                print(customer)


        elif user_selection == 12: #"Select a customer"
            selection_method = input("You can select a customer by name or by id. If you would like to select a customer by name, enter 'name'. If you would like to select a customer by id, enter 'id': ")
            
            if selection_method == "name":
                
                name = input("Please enter the name of the customer you would like to select: ")
                customer_requests.get_specific_customer(name=name)
            elif selection_method == "id":
                id = input("Please enter the id of the customer you would like to select: ")
                if id.isnumeric():
                    id = int(id)
                    customer_selection_response = customer_requests.get_specific_customer(id=id)
            else:
                print("Selection error, please type the keyword 'id' or the keyword 'name' to make your selection.")

            if customer_requests.selected_customer:
                print("The customer you selected is: ", customer_requests.selected_customer)
            
        elif user_selection == 13: #"Get information about a specific customer"

            customer_info = customer_selection_response

            i=1
            for k, v in customer_info.items():
                print (f"{k}: {v}")

        elif user_selection == 14: #"Get information about all customer accounts"
            pass

        elif user_selection == 15: #"Add a customer account"
            print("You selected to add a new customer. Please enter the following information:")
            name = input("Enter the customer's name: ")
            postal_code = input("Enter the customer's postal code: ")
            phone = input("Enter the customer's phone number: ")

            response = customer_requests.create_customer(name=name, postal_code=postal_code, phone=phone)
            print(response)
            print(f"The new customer created successfully. The new customer's id is: {response['id']}")

        elif user_selection == 16: #"Edit customer information"
            print("you have selected to edit a customers information. Please enter information for the fields that you would like to edit: ")
            name = input("Enter the customer's name: ")
            postal_code = input("Enter the customer's postal code: ")
            phone = input("Enter the customer's phone number: ")

            response = customer_requests.update_customer(name=name, postal_code=postal_code, phone=phone)
            #Id like to present the info in a better way here.
            #maybe a class method that turns this into plain text?
            print(f"Customer successfully updated:{response}")
        
        elif user_selection == 17: #"Delete customer account"
            print("You have selected to delete a customer account, Are you sure you want to delete the customer account?")
            print("Once a customer has been deleted, the information can no longer be retrieved.")
            
            confirm_delete = input("Enter 'Y' if you would like to delete the selected customer account \nand 'N' if you would like to return to the options list: ")
            
            if confirm_delete == "Y":
                customer_requests.delete_customer()
                print(f"The customer has been deleted.")
        
        elif user_selection == 18: #"Delete all customer accounts"
            print("You have selected to delete a customer account, Are you sure you want to delete the customer account?")
            print("Once a customer has been deleted, the information can no longer be retrieved.")

            confirm_delete = input("Enter 'Y' if you would like to delete the selected customer account \nand 'N' if you would like to return to the options list: ")
            
            if confirm_delete == "Y":

                for customer in customer_requests.list_all_customers():
                    customer_requests.get_specific_customer(id = customer['id'])
                    customer_requests.delete_customer(id)
                    print(f"All customers have been deleted.")

        elif user_selection == 19: #"Check out a video to a customer"
            print("You have selected to check out a video to a customer.")
            customer_id = input("Please enter the id of the customer you would like to check the video out to: ")
            video_id = input("Please enter the id of the video that you would like to check out: ")

            if customer_id.isnumeric():
                customer_id = int(customer_id)
            
            if video_id.isnumeric():
                video_id = int(video_id)

            response = rental_requests.create_rental(customer_id=customer_id, video_id=video_id)
            print(response)
            print(f"The new rental created successfully for customer with id:{customer_id} and video with id:{video_id}. The due date for the rental is {response['due_date']}.")
            

        elif user_selection == 20: #"Check in a video to a customer"
            print("You have selected to check in a video for a customer.")
            customer_id = input("Please enter the id of the customer: ")
            video_id = input("Please enter the id of the video that you would like to check in: ")
            
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            
            if video_id.isnumeric():
                video_id = int(video_id)
            
            response = rental_requests.check_in_video(customer_id=customer_id, video_id=video_id)
            print(response)

        elif user_selection == 21: #See how many rentals a customer has 
            customer_info = customer_selection_response

            customer_id = customer_info.get('id')
            customer_name = customer_info.get('name')
            rentals = customer_info.get('videos_checked_out_count')

            print(f"{customer_name} has {rentals} video(s) currently checked out.")

        elif user_selection == 22: #"Print currently selected customer"
            print(f"Currently selected customer: {customer_selection_response}")
        
        elif user_selection == 23: #"Print currently selected video"
            print(f"Currently video: {video_selection_response}")

        
if __name__ == "__main__":
    main()


