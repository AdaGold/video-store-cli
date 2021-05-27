import requests
from datetime import datetime, timedelta
class VideoStore:
    def __init__(self, url="http://127.0.0.1:5000", selected_rental = None, selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer
        self.selected_rental = selected_rental
    
    #Video Store Employee: add a video
    def create_video(self,title="Default Video",release_date=None,total_inventory=None): 
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

#get info about all customers
    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

#get info about one video
    def get_video(self, title=None, id=None):
        
        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find task by that name or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

#get info about one customer
    def get_customer(self, name=None, id=None):
        
        for customer in self.list_customers():
            if name:
                if customer["name"]==name:
                    id = customer["id"]
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find task by that name or id"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    #add a customer
    def create_customer(self,name=None,postal_code=None, phone=None, registered_at = None, videos_checked_out_count=0): 
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone,
            "registered_at": registered_at,
            "videos_checked_out_count": videos_checked_out_count
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    #Edit a video
    def update_video(self,title=None,release_date=None, total_inventory=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]

        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()["video"]
        return response.json()
    
    #Edit a customer
    def update_customer(self, name=None,postal_code=None, phone=None, registered_at = None, videos_checked_out_count=0):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]
        if not registered_at:
            regustered_at = datetime.now() #is this what I want??
        if not videos_checked_out_count:
            videos_checked_out_count = self.selected_customer["videos_checked_out_count"]

        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone,
        "registered_at": registered_at,
        "videos_checked_out_count": videos_checked_out_count
        }

        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()
        return response.json()

    #delete a video
    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()

    # #get all rentals
    # def list_rentals(self):
    #     response=requests.get(self.url+"/rentals")
    #     return response.json()

    # #get rental details
    # def get_rental(self, rental_id=None):
    #     for rental in self.list_rentals():
    #         if rental_id:
    #             if rental[]
    
    #delete a customer
    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
    
    def check_out(self, customer_id=None, video_id=None): 
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id,
        }
        response = requests.post(self.url+"/rentals/check-out",json=query_params)
 
        return response.json()

    # def check_out(self, customer_id=None, video_id=None):
    #     response = requests.post(self.url+f"/rentals/{self.selected_customer['id']}/mark_complete")
    #     self.selected_task = response.json()["task"]
    #     return response.json()

    # def mark_incomplete(self):
    #     response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_incomplete")
    #     self.selected_task = response.json()["task"]
    #     return response.json()

    # def print_selected_video(self):
    #     if self.selected_video:
    #         print(f"Video with id {self.selected_video['id']} is currently selected\n")
    

    # def print_selected_customer(self):
    #     if self.selected_customer:
    #         print(f"Customer with id {self.selected_customer['id']} is currently selected\n")


        
