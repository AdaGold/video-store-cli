import requests
import datetime

class Videos:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
    
    
    def add_video(self, title=None,release_date=None,total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        url = self.url+"/videos"
        response = requests.post(url, json=query_params)
        return response.json()
    

    def update_video(self, video_id=None, title=None,release_date=None,
                     total_inventory=0):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.total_inventory["total_inventory"]
            
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.put(self.url+f"/videos/{video_id}",
            json=query_params)
        print("response:", response)
        return response.json()
    


    def delete_video(self, video_id=None):
        response = requests.delete(self.url+f"/videos/{video_id}")
        print(response)
        return response.json()
    


    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, video_id=None):
        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()
