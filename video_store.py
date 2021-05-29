import requests
import datetime


class VideoStore:
    def __init__(self, url="http://localhost:5000/"):
        self.url = url
        
    def list_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()
      
    def add_customer(self, name="Admin", postal_code="00000", phone="111-111-1111"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()
      
    def select_customer(self, id=None):
        response = requests.get(self.url+f"/customers/{id}")
        return response.json()
      
    def edit_customer(self, id=None, name="Admin", postal_code="00000", phone="111-111-1111"):
        selected_customer = requests.get(self.url+f"/customers/{id}").json()
        if not name:
            name = selected_customer["name"]
        if not postal_code:
            postal_code = selected_customer["postal_code"]
        if not phone:
            phone = selected_customer["phone"]
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{id}",
            json=query_params
        )
        return response.json()
      
    def delete_customer(self, id=None):
        response = requests.delete(self.url+f"/customers/{id}")
        return response.json()
# ----------------------------------------------------------------------
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
      
    def select_video(self, id=None):
        response = requests.get(self.url+f"/videos/{id}")
        return response.json()
      
    def add_video(self, title="Awesome movie", release_date="1988-01-01", total_inventory=10):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()
      
    def edit_video(self, id, title, release_date, total_inventory):
        selected_video = requests.get(self.url+f"/videos/{id}").json()
        if not title:
            title = selected_video["title"]
        if not release_date:
            release_date = selected_video["release_date"]
        if not total_inventory:
            total_inventory = selected_video["total_inventory"]
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.put(self.url+f"/videos/{id}", json=query_params)
        return response.json()
      
    def delete_video(self, id=None):
        response = requests.delete(self.url+f"/videos/{id}")
        return response.json()
# ----------------------------------------------------------------------
    def check_out(self, customer_id=None, video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-out",json=query_params)
        return response.json()
        
    def check_in(self, customer_id=None, video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in",json=query_params)
        return response.json()