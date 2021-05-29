import requests
import datetime

class VideoStore:

    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_customer=None, selected_video=None):
        self.url = url
        self.selected_customer = selected_customer
        self.selected_video = selected_video

#VIDEO MANAGEMENT
    #1: add a video
    def add_video(self,title,release_date,total_inventory):

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()  

    #2: edit a video 
    def edit_video(self,video_id,title,release_date,total_inventory):
        if not title: 
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]   

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
        }
        response = requests.put(
            self.url+f"/videos/{video_id}",
            json=query_params
            )

        self.selected_video = response.json()
        return response.json()

    #3: delete a video 
    def delete_video(self, id):
        response = requests.delete(self.url+f"/videos/{id}")
        return response.json()

    #4: get information of all videos
    def list_all_videos(self):
        response = requests.get(self.url+"/videos") 
        return response.json()

    #5: get information of one video
    def get_video(self, id):
        response = requests.get(self.url+f"/videos/{id}")
        self.video = response.json()
        return response.json()


#CUSTOMER MANAGEMENT
    #6: add a customer
    def add_customer(self, name, postal_code, phone):

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json() 

    #7: edit a customer
    def update_customer(self,customer_id, name, postal_code, phone):

        if not name: 
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]   

        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone,
        }
        response = requests.put(
            self.url+f"/customers/{customer_id}",
            json=query_params
            )

        self.selected_customer = response.json()
        return response.json()

    #8: delete a customer
    def delete_customer(self, id):
        response = requests.delete(self.url+f"/customers/{id}")
        return response.json()

    #9: get information of all customers
    def list_all_customers(self):
        response = requests.get(self.url+"/customers") 
        return response.json()

    #10: get information of one customer
    def get_customer(self, id):
        response = requests.get(self.url+f"/customers/{id}")
        self.customer = response.json()
        return response.json()


#RENTAL MANAGEMENT
    #11: check out a video
    def checkout_video(self, customer_id, video_id,):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-out", json=query_params)
        return response

    #12: check in
    def checkin_video(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in", json=query_params)
        return response 