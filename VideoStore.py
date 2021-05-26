import requests
import datetime as dt 
import maya




class VideoStore:
    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer

######### VIDEO STUFF ############ 
    def get_all_videos(self):
        response = requests.get(self.url+"/videos")
        print(response.json())
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
        date_time_object= maya.parse(new_release_date).datetime()
        new_total_inventory = input(f"Update the total inventory for video {selected_video['id']}:  ")
        query_params = {
            "title": new_title, 
            "release_date": str(date_time_object),
            "total_inventory": new_total_inventory
        }
        response = requests.put(self.url+f'/videos/{selected_video["id"]}', json=query_params)
        if response:
            print("Success!",  response)
        else: 
            print("Oops! Something went wrong. ")
        self.selected_video = response.json()
        return response.json()

    # had to employ a "cascade" to delete instances of video from rental table if they are 
    #cross referenced.  maybe come back with some logic to check for that first? 


    def delete_single_video(self, selected_video): 
        response = requests.delete(self.url+f"/videos/{selected_video['id']}")
        print(response)
        if response:
            print(f"The video {selected_video['id']} has been deleted. ")
        else: 
            return "Oops, something went wrong. "

######### CUSTOMER STUFF ############ 

    def get_all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()
            

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
        new_postal_code = input(f"Update the zip code for the customer {selected_customer['id']}:  ")
        new_phone = input(f"Update the phone number for the customer {selected_customer['id']}:   ")
        new_checkout_count = input(f"Update the number of videos checked out for customer {selected_customer['id']}:   ")

        query_params = {
            "name": new_name, 
            "postal_code": new_postal_code,
            "phone": new_phone, 
            "videos_checked_out_count": new_checkout_count
        }
        response = requests.put(self.url+f'/customers/{selected_customer["id"]}', json=query_params)
        if response:
            print("Success!",  response)
        else: 
            print("Oops! Something went wrong. ")
        self.selected_customer = response.json()
        return response.json()




    def delete_single_customer(self, id=None, name=None):
        pass 