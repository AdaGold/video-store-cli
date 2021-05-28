import requests
from datetime import datetime
import json

class VideoStore:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None):
        self.url = url
        self.selected_video = selected_video
    
##### VIDEO #####

    def create_video(self, title="Default Title", release_date="Default Date", total_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def update_video(self, title=None, release_date="Default Date", total_inventory=0):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]

        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory}

        response = requests.put(self.url+f"/videos/{self.selected_video['id']}", 
                                json=query_params)
        print("response:", response)
        self.selected_video = response.json()["video"]
        return response.json()    

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()

    def videos_list(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_single_video(self, title=None, id=None):
        for video in self.videos_list():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that title: {title} or {id}"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def print_selected(self):
            if self.selected_video:
                print(f"Video with id {self.selected_video['id']} is currently selected\n")

##### CUSTOMER #####

    def create_customer(self, name="first last", postal_code=00000, phone="000-000-0000", registered_at=None):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone,
            "registered_at": registered_at
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def update_customer(self, name=None, postal_code=None, phone=None):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()["customer"]
        return response.json()


    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()
    
    def get_customers_list(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_single_customer(self, name=None, id=None):  
        for customer in self.get_customers_list():
            if name:
                if customer["name"]==name:
                    id = customer["customer_id"]
                    self.selected_customer = customer 
            elif id == customer["customer_id"]:
                self.selected_customer = customer 

        if self.selected_customer == None:
            return f"Could not find customer with name:{name} or id: {id}"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def print_selected_customer(self):
        if self.selected_customer:
            print(f"Customer with id {self.selected_customer['id']} is currently selected\n")    