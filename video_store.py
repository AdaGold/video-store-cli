import requests
import datetime

class VideoStore:
    def __init__(self, url="http://localhost:5000", current_customer=None, current_video=None, current_rental=None):
        self.url = url
        self.current_customer = current_customer
        self.current_video = current_video


    #---------------------# CUSTOMER METHODS #---------------------#

    def create_customer(self, name="Default Name", postal_code="00000", phone="000-000-0000"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, id=None, name=None, phone=None):
        self.current_customer = None
        for customer in self.list_customers():
            if id and str(customer["id"]) == id:
                self.current_customer = customer
            elif name and customer["name"] == name:
                id = customer["id"]
                self.current_customer = customer
            elif phone and customer["phone"] == phone:
                id = customer["id"]
                self.current_customer = customer
        if self.current_customer == None:
            return None
        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def update_customer(self, name=None, postal_code=None, phone=None):
        if not name:
            name = self.current_customer["name"]
        if not postal_code:
            postal_code = self.current_customer["postal_code"]
        if not phone:
            phone = self.current_customer["phone"]
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
            }
        response = requests.put(self.url+f"/customers/{self.current_customer['id']}",
        json=query_params)
        self.current_customer = response.json()
        return response.json()

    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{self.current_customer['id']}")
        return response.json()

    
    #---------------------# VIDEO METHODS #---------------------#
    
    def create_video(self, title="Default Title", release_date=None, total_inventory=1):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        self.current_customer = response.json()
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, id=None, title=None):
        self.current_video = None
        for video in self.list_videos():
            if id and str(video["id"]) == id:
                self.current_video = video
            elif title and video["title"] == title:
                id = video["id"]
                self.current_video = video
        if self.current_video == None:
            return None
        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def update_video(self, title=None, release_date=None, total_inventory=None):
        if not title:
            title = self.current_video["title"]
        if not release_date:
            release_date = self.current_video["release_date"]
        if not total_inventory:
            total_inventory = self.current_video["total_inventory"]
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
            }
        response = requests.put(self.url+f"/videos/{self.current_video['id']}",
        json=query_params)
        self.current_video = response.json()
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.current_video['id']}")
        return response.json()


#---------------------# RENTAL METHODS #---------------------#

    def checkout_video(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
            }
        response = requests.post(self.url+f"/rentals/check-out", json=query_params)
        return response.json()

    def checkin_video(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
            }
        response = requests.post(self.url+f"/rentals/check-in", json=query_params)
        return response.json()


#---------------------# OPTIONAL METHODS #---------------------#

    def list_customer_rentals(self):
        response = requests.get(self.url+f"/customers/{self.current_customer['id']}/rentals")
        return response.json()
    
    def list_video_rentals(self):
        response = requests.get(self.url+f"/videos/{self.current_video['id']}/rentals")
        return response.json()
    
    def get_customer_rental_history(self):
        response = requests.get(self.url+f"/customers/{self.current_video['id']}/history")
        return response.json()

    def get_video_rental_history(self):
        response = requests.get(self.url+f"/videos/{self.current_video['id']}/history")
        return response.json()

    def get_overdue_rentals(self):
        response = requests.get(self.url+f"/rentals/overdue")
        return response.json()