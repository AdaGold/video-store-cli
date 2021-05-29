import requests
import datetime

class VideoStore:
    def __init__(self, url = "http://localhost:5000"):
        self.url = url

    def add_video(self, title, release_date, total_inventory):
        request_body = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos", json = request_body)
        return response.json()

    def edit_video(self, video_id, title = None, release_date = None, total_inventory = None):
        request_body = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory    
        }
        response = requests.put(self.url+f"/videos/{video_id}", json = request_body)
        return response.json()

    def delete_video(self, video_id):
        response = requests.delete(self.url+f"/videos/{video_id}")
        return response.json()

    def get_all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, video_id):
        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()

    def add_customer(self, name, postal_code, phone_number):
        request_body = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone_number
        }
        response = requests.post(self.url+"/customers", json = request_body)
        return response.json()

    def edit_customer(self, customer_id, name = None, postal_code = None, phone_number = None):
        request_body = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone_number
        }
        response = requests.put(self.url+f"/customers{customer_id}", json = request_body)
        return response.json()

    def delete_customer(self, customer_id):
        response = requests.delete(self.url+f"/customers/{customer_id}")
        return response.json()

    def get_all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    def get_customer(self, customer_id):
        response = requests.get(self.url+f"/customer/{customer_id}")
        return response.json()

    def check_out(self, customer_id, video_id):
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-out", json = request_body)
        return response.json
    
    def check_in(self, customer_id, video_id):
        request_body = {
        "customer_id": customer_id,
        "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-in", json = request_body)
        return response.json