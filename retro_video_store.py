import requests
import datetime

class Video_Store:
    def __init__(self, url="http://127.0.0.1:5000", selected_customer=None, selected_video=None, selected_rental=None):
        self.url = url
        self.selected_customer = selected_customer
        self.selected_video = selected_video
        self.selected_rental = selected_rental
    
    def create_customer(self, name="Empty Name", postal_code="Somewhere Near By", phone=None):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def list_of_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, id=None):
        
        for customer in self.list_of_customers():
            if id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "There is no customer under this id number."

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()

    def update_customer(self, id, name=None, postal_code=None, phone=None):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]

        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone" : phone
        }
        response = requests.put(
            self.url+f"/customers/{id}",
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()
        return response.json()

    def delete_customer(self, id):
        response = requests.delete(self.url+f"/customers/{id}")
        return response.json()
#functions for videos************************************************************************************************************************************

    def create_video(self, title="Some Movie", release_date=datetime.now(), total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def list_of_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, id=None):
        
        for video in self.list_of_videos():
            if id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "There is no video that exists under this id number."

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def update_video(self, id, title=None, release_date=datetime.now(), total_inventory=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]

        query_params = {
        "title": title,
        "release_date": release_date,
        "totsl_inventory" : total_inventory
        }
        response = requests.put(
            self.url+f"/videos/{id}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()
        return response.json()

    def delete_video(self, id):
        response = requests.delete(self.url+f"/videos/{id}")
        return response.json()
    
    def check_out_video(self, customer_id, video_id):
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-out", json=request_body)
        return response.json()

    def check_in_video(self, customer_id, video_id):
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-in", json=request_body)
        return response.json()

    def print_selected(self):
        if self.selected_customer:
            print(f"The customer with id {self.selected_customer['id']} is currently selected\n")
        elif self.selected_video:
            print(f"The video with id {self.selected_video['id']} is currently selected\n")
        elif self.selected_rental:
            print(f"The rental with id {self.selected_rental['id']} is currently selected\n")