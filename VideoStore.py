import requests
from print_functions import *
from datetime import datetime



URL = "http://localhost:5000"
BACKUP_URL = "https://bp-retro-video-store.herokuapp.com/"

############ INPUT VALIDATION HELPER FUNCTIONS ################# 

def is_valid_phone_number(phone):
    if len(phone) != 12: 
        return False
    for i in range(12):
        if i in [3, 7]:
            if phone[i] != "-":
                return False
        elif not phone[i].isalnum():
            return False
    return True

def is_valid_zip(postal_code):
    if len(postal_code) != 5:
        return False
    new_zip = postal_code.isnumeric()
    if not postal_code.isnumeric():
        return False
    return True

def how_many_days_late(due_date, today):
    pass



###############  CLASS #####################
class VideoStore:
    def __init__(self, url=BACKUP_URL, selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer




######### VIDEO STUFF ############ 
    def get_all_videos(self):
        sort_options = input("Would you like to sort by Title, ID, or Release Date?  ")

        if sort_options.lower() == "title":
            response = requests.get(self.url+"/videos?sort=title")
        elif sort_options.lower() == "release date":
            response = requests.get(self.url+"/videos?sort=release_date")
        elif sort_options.lower() == "id":
            response = requests.get(self.url+"/videos?sort=id")
        else:
            response = requests.get(self.url+"/videos")
        if response.status_code != 200:
            return "Oops! Something went wrong. "
        return response.json()
        

    def add_video_to_db(self):
        title = input("Please enter the title of the video:  ")
        release_date = input("Please enter the release date:  ")
        total_inventory = input("Please enter the number of videos for inventory:   ")
        
        query_params = { 
            "title": title, 
            "release_date": release_date,
            "total_inventory": total_inventory
                        }
        response = requests.post(self.url+"/videos", json=query_params)
        if response.status_code == 201:
            print(f"New Video added to database: {response.json()}")
        else:
            print("Oops! Something went wrong. ")

        return response.json()

    def get_single_video(self, id=None, title=None):
        for video in self.get_all_videos():
            if video["id"] == id:
                self.selected_video = video
            elif video["title"] == title:
                self.selected_video = video
        if not self.selected_video:
            print("Could not find that video.")
        return self.selected_video

    def edit_single_video(self, selected_video):
        new_title = input(f'Update the title for video {selected_video["id"]}:')
        new_release_date = input(f"Update the release date for video {selected_video['id']}:  ")
        new_total_inventory = input(f"Update the total inventory for video {selected_video['id']}:  ")
        query_params = {
            "title": new_title, 
            "release_date": new_release_date,
            "total_inventory": new_total_inventory
        }
        response = requests.put(self.url+f'/videos/{selected_video["id"]}', json=query_params)
        if response.status_code == 200:
            print("Success!",  response)
        else: 
            print("Oops! Something went wrong. ")
        self.selected_video = response.json()
        return response.json()


    def delete_single_video(self, selected_video): 
        response = requests.delete(self.url+f"/videos/{selected_video['id']}")
        print(response)
        if response.status_code == 200:
            print(f"The video {selected_video['id']} has been deleted. ")
        else: 
            return "Oops, something went wrong. "

######### CUSTOMER STUFF ############ 

    def get_all_customers(self):
        sorting_option = input("Would you like to sort customer by ID, Name, or Postal Code?:   ")
        if sorting_option.lower() == "name":
            response = requests.get(self.url+"/customers?sort=name")
        elif sorting_option.lower() == "postal code":
            response = requests.get(self.url+"/customers?sort=postal_code")
        elif sorting_option.lower() == "id":
            response = requests.get(self.url+"/customers?sort=id")
        else:
            response = requests.get(self.url+"/customers")
        return response.json()

    def add_customer_to_db(self): 
        name = input("Please enter the customers first and last name:   ")
        phone = ""
        while not is_valid_phone_number(phone):
            phone = input("Please enter the customers phone number with area code in the format XXX-XXX-XXXX:   ")
        postal_code = ""
        while not is_valid_zip(postal_code):
            postal_code = input("Please enter the customers zip code:   ")
        
        query_params = {
            "name": name, 
            "phone": phone, 
            "postal_code": postal_code
        }
        response = requests.post(self.url+"/customers", json=query_params)

        if response.status_code == 201:
            print(f"New Customer added to database: {response.json()}")
        else:
            print("Oops! Something went wrong. ")
            

    def get_single_customer(self, id=None, name=None):
        for customer in self.get_all_customers():
                if customer["id"] == id:
                    self.selected_customer = customer
                elif customer["name"]  == name:
                    self.selected_customer = customer
        if not self.selected_customer:
            print("We could not find that customer. ")
        return self.selected_customer
    
    def edit_single_customer(self, selected_customer):
        new_name = input(f'Update the name for customer {selected_customer["id"]}:  ')

        new_phone = ""
        while not is_valid_phone_number(new_phone):
            new_phone = input(f"Update the phone number for the customer {selected_customer['id']} XXX-XXX-XXXX:   ")

        new_postal_code = ""
        while not is_valid_zip(new_postal_code):
            new_postal_code = input(f"Update the zip code for the customer {selected_customer['id']}:  ")
        
        new_checkout_count = input(f"Update the number of videos checked out for customer {selected_customer['id']}:   ")

        query_params = {
            "name": new_name, 
            "postal_code": new_postal_code,
            "phone": new_phone, 
            "videos_checked_out_count": new_checkout_count
        }
        response = requests.put(self.url+f'/customers/{selected_customer["id"]}', json=query_params)
        if response.status_code == 200:
            print("Success!",  response)
        else: 
            print("Oops! Something went wrong. ")
        self.selected_customer = response.json()
        return response.json()


    def delete_single_customer(self, selected_customer):

        response = requests.delete(self.url+f"/videos/{selected_customer['id']}")
        if response.status_code == 200:
            print(f"The customer {selected_customer['id']} has been deleted. ")
        else:
            print("Oops! Something went wrong. ")


############## RENTAL HANDLING ############# 

    def check_out_movie(self):
        customer_id = input("Please enter the ID of the returning Customer:  ")
        video_id = input("Please enter the ID of the Customer's video:  ")

        query_params = { 
            "customer_id": int(customer_id), 
            "video_id": int(video_id)
                        }
        response = requests.post(self.url+"/rentals/check-out", json=query_params)
        if response.status_code == 404:
            print("\nUh Oh! The customer or video ID are incorrect. ")
            return response

        json_response = response.json()

        print("\n")
        print("Success!  The title has been checked out! ")
        print(f"Customer {json_response['customer_id']} has {json_response['videos_checked_out_count']} movie(s) checked out. ")
        print(f"The due date for Video {json_response['video_id']} is {json_response['due_date']}. ")
        print(f"There are {json_response['available_inventory']} copies of this title remaining. ")

    def check_in_movie(self):
        customer_id = input("Please enter the ID of the returning Customer:  ")
        video_id = input("Please enter the ID of the Customer's video:  ")       

        query_params = { 
            "customer_id": int(customer_id), 
            "video_id": int(video_id)
                        }
        response = requests.post(self.url+"/rentals/check-in", json=query_params)
        json_response = response.json()

        print("\n")
        print("Success! The title has been returned. ")
        print(f"Customer {json_response['customer_id']} has {json_response['videos_checked_out_count']} movie(s) checked out. ")
        print(f"There are {json_response['available_inventory']} copies of this title remaining. ")

    def get_rental_list_by_video(self, video_id):
        rental_list = requests.get(self.url+f"/videos/{video_id}/rentals")
        if not rental_list.json():
            print("\n Uh Oh! We couldn't find the video matching that ID. ")

        for rental in rental_list.json():
            customer_name = rental["name"]
            due_date = rental["due_date"]
            customer = self.get_single_customer(name=customer_name, id=None)
            print_customer_info(customer)
            print(f"Video due date is {due_date}")
            print("\n")
        

    def get_rental_list_by_customer(self, customer_id):
        rental_list = requests.get(self.url+f"/customers/{customer_id}/rentals")

        if not rental_list.json():
            print("\n Uh Oh!  We coulnd't find the customer matching that ID. ")

        for rental in rental_list.json():
            video_title = rental["title"]
            video_due_date = rental["due_date"]
            print_video_info(video_title)
            print(f"Video due date is {video_due_date}")
            print("\n")
    
    def is_overdue(self):
        rental_list = requests.get(self.url+"/rentals")
        overdue_list = []

        today = datetime.now()
        print(today)


        for rental in rental_list.json():
            due_date = datetime.strptime(rental["due_date"], "%a, %d %b %Y %H:%M:%S %Z")
            print(due_date)
            if due_date < today:
                overdue_list.append(rental)
        if not overdue_list:
            print("There are no overdue movies in the database. ")
        else:
            for overdue_movie in overdue_list:
                print_overdue_info(overdue_movie)
        
        



