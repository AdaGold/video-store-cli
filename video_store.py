import requests
import datetime
import json

class VideoStore:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com"):
        self.url = url

    def get_all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
    
    def get_video(self, id):
        response = requests.get(self.url+f"/videos/{id}")
        self.video = response.json()
        return response.json()
    
    def update_video(self,id,title,release_date,total_inventory):
        query_params = json.dumps({
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        })
        headers = {
            'Content-Type': 'application/json'
            }
        response = requests.put(self.url+f"/videos/{id}", headers=headers, data=query_params)
        print(response.json())
        return response.json()

    def create_video(self,title,release_date,total_inventory):
        query_params = json.dumps({
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        })
        headers = {
            'Content-Type': 'application/json'
            }
        response = requests.post(self.url+f"/videos", headers=headers, data=query_params)
        print(response.json())
        return response.json()

    def delete_video(self, id):
        response = requests.delete(self.url+f"/videos/{id}")
        print("Deleted: ")
        print(response.json())
        return response.json()

    ## ************** customers functions
    
    def all_customers_are_bastards(self):
        response = requests.get(self.url+"/customers")
        return response.json()
    
    def get_custo(self, id):
        response = requests.get(self.url+f"/customers/{id}")
        self.video = response.json()
        return response.json()

    def update_custo(self,id,name,postal_code,phone):
        query_params = json.dumps({
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        })
        headers = {
            'Content-Type': 'application/json'
            }
        response = requests.put(self.url+f"/customers/{id}", headers=headers, data=query_params)
        print(response.json())
        return response.json()
