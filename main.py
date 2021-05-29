import requests
from video_requests import VideoRequests
from customer_requests import CustomerRequests
from rental_requests import RentalRequests
import json

URL = "http://127.0.0.1:5000"  #local host
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"
#MY_URL = "https://video-retro.herokuapp.com" #api route

video_requests = VideoRequests(url=BACKUP_URL)
customer_requests = CustomerRequests(url=BACKUP_URL)
rental_requests = RentalRequests(url=BACKUP_URL)

def main():
    print("WELCOME TO RETRO VIDEO STORE")
    cli_go()

def list_user_options():
    options = {
        1: "List all options",
        2: "Quit",
        #video requests
        3: "List all videos",
        4: "Select a video",
        5: "List total video inventory for store", 
        6: "List total inventory for a specific video",
        7: "Add a Video",
        8: "Edit a Video",
        9: "Delete a video",
        10: "Delete all videos",
        #customer requests options
        11: "List all customers",
        12: "Select a customer", 
        13: "Get information about a specific customer", 
        14: "Add a customer account",
        15: "Edit customer information",
        16: "Delete customer account",
        17: "Delete all customer accounts",
        #rental requests
        18: "Check out a video to a customer",
        19: "Check in a video to a customer",
        20: "Check number of rentals a customer has", 
        21: "Print currently selected customer",
        22: "Print currently selected video"
    }

    print("These are the actions you can perform")

    for option_num in options:
        print(f"{option_num}. {options[option_num]}")

    return options  

def user_selection_option(options):
    valid_selection = options.keys()
    user_selection = None

    while user_selection not in valid_selection:

        print("\nPlease select an option, enter option 1 to see all options again.\n")
        
        user_selection = input("Please enter the option number of the action you would like to take: ")
        user_selection = int(user_selection)
        
    
    if user_selection in [6, 8, 9, 22] and video_requests.selected_video == None:
        print("\nYou must first select a video by entering option 4, before you can edit or delete it.")
        print("Please select a video by selecting option #4.")
        user_selection = "4"
    
    if user_selection in [13, 15, 16, 17, 20, 21] and customer_requests.selected_customer == None:
        print("\nYou must first select a customer by entering option 12, before you can edit or delete a customer account.")
        print("Please select a customer by selecting option #12. ")
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
            print("Retro video store is sad to ya go, come back soon!!!!")
        
        elif user_selection == 3: #List all videos

            videos = video_requests.list_all_videos()

            for video_dict in videos:
                print(json.dumps(video_dict, indent=4))
        
        elif user_selection == 4: #Select a video
            selection_method = input("\nYou can select a video by title or id.\n\nIf you would like to select by title, type 'title'. If you would like to select by id, type, 'id': \n")
            
            if selection_method == "title":
                title = input("\nPlease enter the title of the video you would like to select: ")
                video_requests.get_specific_video(title=title)

            elif selection_method == "id":
                id = input("\nPlease enter the id of the video you would like to select: ")
                if id.isnumeric():
                    id = int(id)
                    video_selection_response = video_requests.get_specific_video(id=id)
            else:
                print("\nSelection error, please enter 'id' or 'title' to make your selection.")
            
            if video_requests.selected_video:
                
                video = video_requests.selected_video
                video_id = video.get('id')
                video_title = video.get('title')
                video_release_date = video.get('release_date')
                video_total_inventory = video.get('total_inventory')
                
                print(f"\nThe currently selected video is:\n\n ID: {video_id}\n Title: {video_title}\n Release Date: {video_release_date}\n Total Inventory: {video_total_inventory}\n")


        elif user_selection == 5: #List total video inventory for store

            video_inventory_totals = []
            
            for video in video_requests.list_all_videos():
                video_inventory_totals.append(video.get('total_inventory'))

            total_store_inventory_num = sum(video_inventory_totals)
            
            print(f"\nThe total store inventory is: {total_store_inventory_num}")


        elif user_selection == 6: #List total inventory for a specific video

            video_info = video_selection_response

            video_id = video_info.get('id')
            video_title = video_info.get('title')
            total_inventory = video_info.get('total_inventory')

            print(f"\nThe total available inventory for video: {video_title} is {total_inventory}.")

        elif user_selection == 7: #Add a video

            print("\nYay a new video to add to the inventory!")
            title = input("\nEnter the title of the video: ")
            release_date = input("\nEnter the release date in yyyy-mm-dd format: ")
            total_inventory = input("\nEnter the total inventory for this video: ")
            response = video_requests.create_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print("\nNew video:", response)
        
        elif user_selection == 8: #Edit a Video
            
            selected_video = video_requests.selected_video
            print("\nTo update the video: ", selected_video.get('title'))
            title = input("\nEnter the new title of the video: ")
            release_date = input("\nEnter the new release date in yyyy-mm-dd format: ")
            total_inventory = input("\nEnter the new value (integer) for total inventory: ")  
            response = video_requests.update_video(title=title, release_date=release_date, total_inventory=total_inventory)
            print("\nVideo successfully updated.")
            print("\nVideo details: ")
            
            for k, v in response.items():
                print(f"{k}: {v}")
        
        elif user_selection == 9: #Delete a video
            
            print("\nYou have selected to delete a video. Are you sure that you want to delete this video from the inventory list?") #"Delete a video"    
            confirm_delete = input("\nIf yes enter 'Y', if no enter 'N': ")
            
            if confirm_delete == 'Y':
                video_requests.delete_video()
                print(f"\nThe video has been deleted.")
    

        elif user_selection == 10: #Delete all videos 
            print("\nDeleted inventory can not be retrieved. Are you sure you want to delete all of the videos in the store inventory?")
            confirm_delete = input("\nEnter Y if you want to delete all videos, N to cancel the request: ")
            
            if confirm_delete == 'Y':
                for video in video_requests.list_all_videos():
                    video_requests.get_specific_video(id=video['id'])
                    video_requests.delete_video(id)
            
                print("\nAll videos have been deleted.")
            
        elif user_selection == 11: #List all customers

            customers = customer_requests.list_all_customers()

            for customer_dict in customers:
                print(json.dumps(customer_dict, indent=4))
            

        elif user_selection == 12: #Select a customer

            selection_method = input("\nYou can select a customer by name or by id. If you would like to select a customer by name, enter 'name'. If you would like to select a customer by id, enter 'id': ")
            
            if selection_method == "name":
                
                name = input("\nPlease enter the name of the customer you would like to select: ")
                customer_selection_response_name = customer_requests.get_specific_customer(name=name)

            elif selection_method == "id":
                id = input("\nPlease enter the id of the customer you would like to select: ")
                if id.isnumeric():
                    id = int(id)
                    customer_selection_response = customer_requests.get_specific_customer(id=id)
            else:
                print("\nSelection error, please type the keyword 'id' or the keyword 'name' to make your selection.")

            customer = customer_requests.selected_customer
            id = customer.get('id')
            name = customer.get('name')
            postal_code = customer.get('postal_code')
            phone = customer.get('phone')

            if customer_requests.selected_customer:
                print(f"\nThe currently selected customer is:\n\n ID: {id}\n Title: {name}\n Release Date: {postal_code}\n Phone: {phone}\n")
        
        elif user_selection == 13: #Get information about a specific customer

            customer_info = customer_selection_response

            i=1
            for k, v in customer_info.items():
                print (f"{k}: {v}")

        elif user_selection == 14: #Add a customer account

            print("\nYou selected to add a new customer. Please enter the following information:")
            name = input("\nEnter the customer's name: ")
            postal_code = input("\nEnter the customer's postal code: ")
            phone = input("\nEnter the customer's phone number: ")

            response = customer_requests.create_customer(name=name, postal_code=postal_code, phone=phone)
            print(f"\nThe new customer created successfully. \n\n New customer details: \n ID: {response['id']}\n {name}\n {postal_code}\n {phone}\n")

        elif user_selection == 15: #Edit customer information

            print("\nYou have selected to edit a customers information. Please enter information for the fields that you would like to edit: ")
            name = input("\nEnter the customer's name: ")
            postal_code = input("\nEnter the customer's postal code: ")
            phone = input("\nEnter the customer's phone number: ")

            response = customer_requests.update_customer(name=name, postal_code=postal_code, phone=phone)
            print(f"\nCustomer successfully updated: {response}")
        
        elif user_selection == 16: #Delete customer account

            print("\nYou have selected to delete a customer account, Are you sure you want to delete the customer account?")
            print("\nOnce a customer has been deleted, the information can no longer be retrieved.")
            
            confirm_delete = input("\nEnter 'Y' if you would like to delete the selected customer account. \n Enter 'N' if you would like to return to the options list: ")
            
            if confirm_delete == "Y":
                customer_requests.delete_customer()
                print(f"\nThe customer has been deleted.")
        
        elif user_selection == 17: #Delete all customer accounts

            print("\nYou have selected to delete a customer account, Are you sure you want to delete the customer account?")
            print("\nOnce a customer has been deleted, the information can no longer be retrieved.")

            confirm_delete = input("\nEnter 'Y' if you would like to delete the selected customer account \nand 'N' if you would like to return to the options list: ")
            
            if confirm_delete == "Y":

                for customer in customer_requests.list_all_customers():
                    customer_requests.get_specific_customer(id = customer['id'])
                    customer_requests.delete_customer(id)
                    print(f"\nAll customers have been deleted.")

        elif user_selection == 18: #Check out a video to a customer

            print("\nYou have selected to check out a video to a customer.")
            customer_id = input("\nPlease enter the id of the customer you would like to check the video out to: ")
            video_id = input("\nPlease enter the id of the video that you would like to check out: ")

            if customer_id.isnumeric():
                customer_id = int(customer_id)
            
            if video_id.isnumeric():
                video_id = int(video_id)

            response = rental_requests.create_rental(customer_id=customer_id, video_id=video_id)

            print(f"\nThe new rental created successfully for customer with ID: {customer_id} and video with ID: {video_id}. The due date for the rental is {response['due_date']}.")
            

        elif user_selection == 19: #Check in a video to a customer

            print("\nYou have selected to check in a video for a customer.")
            customer_id = input("\nPlease enter the id of the customer: ")
            video_id = input("\nPlease enter the id of the video that you would like to check in: ")
            
            if customer_id.isnumeric():
                customer_id = int(customer_id)
            
            if video_id.isnumeric():
                video_id = int(video_id)
            
            response = rental_requests.check_in_video(customer_id=customer_id, video_id=video_id)

        elif user_selection == 20: #See how many rentals a customer has 
            
            customer_info = customer_selection_response

            customer_id = customer_info.get('id')
            customer_name = customer_info.get('name')
            rentals = customer_info.get('videos_checked_out_count')

            print(f"\n{customer_name} has {rentals} video(s) currently checked out.")

        elif user_selection == 21: #Print currently selected customer

            if customer_requests.selected_customer:

                customer = customer_requests.selected_customer
                id = customer.get('id')
                name = customer.get('name')
                postal_code = customer.get('postal_code')
                phone = customer.get('phone')

                print(f"\nThe currently selected customer is:\n\n ID: {id}\n Title: {name}\n Release Date: {postal_code}\n Phone: {phone}\n")
                
        
        elif user_selection == 22: #Print currently selected video

            if video_requests.selected_video:
                
                video = video_requests.selected_video
                video_id = video.get('id')
                video_title = video.get('title')
                video_release_date = video.get('release_date')
                video_total_inventory = video.get('total_inventory')

                print(f"\nThe currently selected video is:\n\n ID: {video_id}\n Title: {video_title}\n Release Date: {video_release_date}\n Total Inventory: {video_total_inventory}\n")

        
if __name__ == "__main__":
    main()


