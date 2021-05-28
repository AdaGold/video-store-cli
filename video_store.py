import requests
from requests.models import Response

class Employee:
    def __init__(self, url = "https://retro-video-store-api.herokuapp.com", selected_customer = None,selected_video = None, selected_rental=None):
        self.url = url
        self.selected_customer = selected_customer
        self.selected_video = selected_video
        self.selected_rental = selected_rental

    def add_customer(self, name, postal_code, phone):
        query_params = {
            "name": name,
            "postal_code":postal_code,
            "phone":phone
        }
        response = requests.post(self.url+"/customers", json=query_params)
        return response.json()

    def get_all_customers(self):

        response = requests.get(self.url+"/customers")
        return response.json()

    def get_a_customer(self, name = None, id = None):

        for customer in self.get_all_customers():
            if name:
                if customer["name"] == name:
                    id = customer["id"]
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer
        if self.selected_customer == None:
            return "Could not find a customer by that name or id"
        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def update_customer(self, name = None, postal_code = None, phone = None):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postale code"]
        if not phone:
            phone = self.selected_customer["phone"]
        
        query_params = {
            "name": name,
            "postal_code":postal_code,
            "phone":phone
        }
        response = requests.put(self.url+f"/customers/{self.selected_customer['id']}", json=query_params)
    
        self.selected_customer = response.json()
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")   
        self.selected_customer = None
        return response.json()

    # video

    def add_video(self, title, release_date, total_inventory):
        query_params = {
            "title": title,
            "release_date":release_date,
            "total_inventory":total_inventory
        }
        response = requests.post(self.url+"/videos", json=query_params)
        return response.json()

    def get_all_videos(self):

        response = requests.get(self.url+"/videos")
        return response.json()

    def get_a_video(self, title = None, id = None):
        for video in self.get_all_videos():
            if title:
                if video["title"] == title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video
        if self.selected_video == None:
            return "Could not find a video by that title or id"
        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def update_video(self, title = None, release_date = None, total_inventory = None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]
        
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory":total_inventory
        }
        response = requests.put(self.url+f"/videos/{self.selected_video['id']}", json=query_params)
    
        self.selected_video = response.json()
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")   
        self.selected_video = None
        return response.json()

    def check_out(self, customer_id, video_id):

        query_params = {
            "customer_id": customer_id,
            "video_id":video_id
        }
        response = requests.post(self.url+"/rentals/check-out", json=query_params)
        self.selected_rental = response.json()
        return response.json()

    def check_in(self, customer_id, video_id):

        query_params = {
            "customer_id": customer_id,
            "video_id":video_id
        }
        response = requests.post(self.url+"/rentals/check-in", json=query_params)
        self.selected_rental = None
        return response.json()







