import requests
import datetime
from requests.models import Response

class VideoList:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video 

    def get_videos(self):
        r = requests.get(self.url+"/videos")
        return r.json()

    def add_video(self, title, release_date, total_inventory):
        new_video ={"title":title,
                    "release_date":release_date,
                    "total_inventory":total_inventory
        }
        response = requests.post(self.url+"/videos",json=new_video)
        return response.json()

    def get_one_video(self, title=None, id=None):
        
        for video in self.get_videos():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that title or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()
    
    def edit_one_video(self, title, release_date, total_inventory):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]
        
        edit_video={
            "title":title,
            "release_date":release_date,
            "total_inventory":total_inventory
        }

        response = requests.put(self.url+f"/videos/{self.selected_video['id']}",
            json = edit_video )
            
        print("response:",response)
        self.selected_video=response.json()
        print(response.json())
        
    def delete_a_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()

    def print_selected(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")