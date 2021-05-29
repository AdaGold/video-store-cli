import requests
import datetime

class VideoList:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video
    
    def create_video(self,title,release_date,total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        print(response)
        print(response.text)
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self,id, title=None): 
        
        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            if id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that name or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def update_video(self,title,release_date,total_inventory):

        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()
        return response.json()
    

    def delete_video(self):
        if not self.selected_video:
            return("You have to select a video id")
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        return response

    def print_selected(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")