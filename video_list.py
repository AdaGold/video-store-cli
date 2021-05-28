import requests
import datetime
from requests.api import post

class VideoList:
    def __init__(self, url='https://retro-video-store-api.herokuapp.com', selected_video=None):
        self.url = url
        self.selected_video = selected_video
    
    def get_video(self,id=None):
        for video in self.list_all_videos():
            if video["id"] == id:
                self.selected_video = video

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def create_video(self, title="", release_date=None, total_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
        }
        response = requests.post(self.url+"/videos", json=query_params )
        return response.json()
    def update_video(self, title=None, release_date=None, total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
        }
        response = requests.put(self.url+f"/videos/{self.selected_video['id']}", json=query_params )
        return response.json()

    def delete_video(self, id=None):
        response = requests.delete(self.url +f"/videos/{self.selected_video['id']}")
        return response.json()
        
    def list_all_videos(self):
        response = requests.get(self.url +"/videos")
        return response.json()
        pass
