import requests
from datetime import datetime

from requests.models import Response

class RetroVideo:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer

    # Videos

    def create_video(self,title="Default Video",release_date="Default Release Date",total_inventory=None, available_inventory = None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
            "available_inventory": available_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, title=None, id=None):
        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    print(video)
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that name"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def update_video(self,title=None,release_date=None, total_inventory= None, available_inventory = None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]
        if not available_inventory:
            available_inventory= self.selected_video["available_inventory"]

        query_params = {
        "title": title,
        "total_inventory": total_inventory,
        "release_date": release_date,
        "available inventory": available_inventory
        
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()
    

    def print_selected(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")
    
    # Customers

    def create_customer(self,name="Default Name",phone="Default Phone",postal_code=None, registered_at = None, videos_checked_out=None ):
        query_params = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code,
            "registered_at": registered_at,
            "videos_checked_out": videos_checked_out
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, name=None, id=None):
        for customer in self.list_customers():
            if name:
                if customer["name"]==name:
                    id = customer["id"]
                    print(customer)
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find customer by that name"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def update_customer(self,name=None,phone=None, postal_code= None, registered_at = None, videos_checked_out = None):
        if not name:
            name = self.selected_customer["name"]
        if not phone:
            phone = self.selected_customer["phone"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not registered_at:
            registered_at = self.selected_customer["registered_at"]
        if not videos_checked_out:
            videos_checked_out = self.selected_customer["videos_checked_out"]
        query_params = {
        "name": name,
        "phone": phone,
        "postal_code": postal_code,
        "registered_at": registered_at,
        "videos_checked_out":videos_checked_out
        
        }
        response = requests.put(self.url+f"/customers/{self.selected_customer['id']}",json=query_params)
        print("response:", response)
        self.selected_customer = response.json()
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
    

    def print_selected(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected\n")
            
# Rentals
    def video_check_out(self,customer_id= None,video_id= None):
        query_params = {
        "customer_id": customer_id,
        "video_id": video_id
        }
        for video in self.list_videos():
            if video_id == video["id"]:
                self.selected_video = video
        print(customer_id, video_id)
        response = requests.post(self.url+"/rentals/check-out", json=query_params)
        print(self.url)
        print(response.__dict__)
        return response

    def video_check_in(self, customer_id= None, video_id=None):
        query_params = {
        "video_id": video_id,
        "customer_id": customer_id
        }
        
        for video in self.list_videos():
            if video_id == video["id"]:
                self.selected_video = video
        response = requests.post(self.url+"/rentals/check-in", json=query_params)
        if response != 200:
            print("Please enter a valid video id and customer id")
            
        return response
