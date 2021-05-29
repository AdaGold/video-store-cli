import requests
from video_store_management import VideoStoreManagement

URL = "http://127.0.0.1:5000"
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

def logo():
    print("      *****************************")
    print("    *********************************")
    print("  *************************************")
    print(" ****************************************")
    print("****** WELCOME TO RETRO VIDEO STORE ******")
    print(" **************************************** ")
    print("  ************************************** ")
    print("    ********************************** ")
    print("      *****************************")
    print()
    print("           CHOOSE AN ACTION    ")
    print("                   |")
    print("                   |")
    print("                   |")
    print("                   V")

def list_options():
    """
        prints to the screen user options
    """
    options = {
        "1": "Create a new customer",
        "2": "Select a customer",
        "3": "Update customer information",
        "4": "Delete customer", 
        "5": "View all customers",
        "6": "Create a new video",#
        "7": "Select a video",
        "8": "Update a video ",#
        "9": "Delete a video",#
        "10": "View all videos",
        "11": "Check-out video",
        "12": "Check-in video",
        "13": "Quit"
        }
    for choice in options:
        print(f"{choice}.   {options[choice]}")
    return options

def user_choice(options):
    valid_choices = options.keys()
    choice = '0'
    while choice not in valid_choices:
        choice = input("CHOOSE A NUMBER--> ")
        if choice not in list_options():
            print("YOU MUST SELECT A VALID CHOICE")
    return choice
       

#runs entire program
def main(play=True):
    video_store_management = VideoStoreManagement(url=BACKUP_URL)
    while play==True:
        logo()
        options = list_options()#prints user options 
        choice = user_choice(options)#users choice from menu
        
        if choice == '1':#create customer
            print("SAWEEET.. LETS DO THIS..LETS GET THIS NEW CUSTOMER CREATED!")
            name=input("Customer first name --> ")
            postal_code=input(f"{name}'s postal code --> ")
            phone=input(f"{name}'s phone number --> ")
            video_store_management.create_customer(name,postal_code,phone)
            print(f"WHEWW..{name}'s profile was successfully created!")
        
        if choice == '2':#get customer
            id=input("ENTER THE CUSTOMERS ID --> ")
            search_by_id = video_store_management.get_customer(id=id)
            print(search_by_id)
        
        if choice == '3':#update customer
            id = input("ENTER CUSTOMERS ID YOU WANT TO UPDATE --> ")
            customer_to_update = video_store_management.get_customer(id=id)
            update = input("LETS GET THIS CUSTOMER UP TO DATE! FOR NAME UPDATE PRESS N,  PHONE UPDATE PRESS P, POSTAL CODE PRESS Z  ")
            if update == 'N':
                name = input("ENTER THE NEW NAME HERE --> ")
                customer_to_update["name"] = name
            elif update == 'P':
                phone = input("NEW PHONE NUMBER GOES HERE --> ")
                customer_to_update["phone"] = name
            elif update == 'Z':
                postal_code =input("NEW POSTAL CODE GOES HERE -->")
            query_params = {
                "id":customer_to_update["id"],
                "postal_code": customer_to_update["postal_code"],
                "phone": customer_to_update["phone"],
                "name": customer_to_update["name"]
                }
            response = requests.put(url=BACKUP_URL+f"/customers/{id}",json=query_params)
            print(response.json())
            return response.json()
            
        
        if choice =='4':#delete customer
            id = input("ENTER CUSTOMERS ID YOU WANT TO DELETE --> ")
            video_store_management.delete_customer(id=id)

        if choice == '5':#view customers
            for c in video_store_management.list_customers():
                print(c)
        
        if choice =='6':#create video
            title=input("YO... SO WHATS THIS NEW VIDS TITLE --> ")
            release_date=input(f" ENTER THE RELEASE DATE FOR {title} YYYY-MM-DD--> ")
            video_store_management.create_video(title=title,release_date=release_date)
            print(f"WHEWW..{title} was successfully created!")
        
        if choice =='7':#get video
            id=input("ENTER THE VIDEOS ID --> ")
            search_by_id = video_store_management.get_video(id=id)
            print(search_by_id)
        
        if choice =='8':#update video
            id = input("ENTER VIDEOS ID YOU WANT TO UPDATE --> ")  
            video_to_update = video_store_management.get_video(id=id)
            update_attribute = input('PRESS T TO UPDATE TITLE, D TO UPDATE RELEASE DATE --> ')
            if update_attribute == 'T':
                title = input('ENTER NEW VIDEO TITLE --> ')
                video_to_update['title'] = title
            elif update_attribute == 'D':
                release_date = input('ENTER NEW RELEASE DATE YYYY-MM-DD --> ')
                video_to_update["release_date"] == release_date
            query_params = {
                    "id" :video_to_update["id"],
                    "title" : video_to_update["title"],
                    "release_date" : video_to_update["release_date"],
                    "total_inventory": video_to_update['total_inventory']
            }
            response = requests.put(url=BACKUP_URL+f"/videos/{id}",json=query_params)
            print(response.json())
            return response.json()
        
        if choice =='9':#delete video
            id = input("ENTER VIDEO ID YOU WANT TO DELETE --> ")
            video_store_management.delete_video(id=id)
        
        if choice == '10':#view videos
             for v in video_store_management.list_videos():#function in customer
                print(v)
        
        if choice == '11':#check out video
            customer_id = input('ENTER THE ID OF THE CUSTOMER TO CHECK-OUT A VIDEO --> ')
            video_id = input('ENTER THE VIDEOS ID THAT IS GETTING CHECKED OUT --> ')
            video_store_management.check_out(customer_id=customer_id,video_id=video_id)
            print("ENJOY THE VIDEO!")
        
        if choice == '12':#check in video
            customer_id = input("ENTER THE ID OF THE CUSTOMER TO CHECK-IN A VIDEO --> ")
            video_id = input('ENTER THE VIDEOS ID TO CHECK_IN THE VIDEO --> ')
            video_store_management.check_in(customer_id=customer_id, video_id=video_id)
            print("CHECK-IN SUCCESSFUL")
        
        if choice =='13':#exit program
            print("")
            print("   <<<<<<<<<<>>>>>>>>>")
            print("<<<<<<<DUN DUN DUN>>>>>>>")
            print("<<<<<<<<<<<BYE>>>>>>>>>>>")
            print("   <<<<<<<<<<>>>>>>>>>")
            play = False
    return play
        
        
            
if __name__ == "__main__":
    main()
