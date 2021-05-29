import requests
from requests.api import post

BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

class VideoStoreManagement:#wrapper class allows me to interact with the API through the url. Handles all interactions with API. 
    def __init__(self, url=BACKUP_URL):
        self.url = url
        
    def create_customer(self,name,postal_code,phone):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
            }
        response = requests.post(self.url+"/customers",json=query_params)
        print(response.json())
        return response.json()
    
    def create_video(self,title, release_date):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": 1
            
            }
        response = requests.post(self.url+"/videos",json=query_params)
        print(response.json())
        return response.json()
    
    def get_video(self,id=None):
        response = requests.get(self.url+f"/videos/{id}")
        print(response.json())
        return response.json()
    
    def get_customer(self,id=None):
        response = requests.get(self.url+f"/customers/{id}")
        print(response.json())
        return response.json()
    
    def list_customers(self):
        response = requests.get(self.url+"/customers")
        print(response.json)
        return(response.json())
    
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        print(response.json())
        return response.json()

    def delete_video(self,id=None):
        response = requests.delete(self.url+f"/videos/{id}")
        print(response.json())
        return response.json()
    
    def delete_customer(self,id=None):
        response = requests.delete(self.url+f"/customers/{id}")
        print(response.json())
        return response.json()
    
    def check_out(self,customer_id=None,video_id=None):
        query_params = {
            "customer_id": customer_id,
            "video_id" : video_id
        }
        response = requests.post(self.url+"/rentals/check-out",json=query_params)
        print(response.json())
        return response.json()
    
    def check_in(self,customer_id,video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in",json=query_params)
        print(response.json())
        return response.json()