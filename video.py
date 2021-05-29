import requests
import datetime

# look at the user stories here for each path 
class Video:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None):
        self.url = url
        self.selected_video = selected_video
    
    # "1": "Add 1 Video to our Extensive Collection "
    def create_video(self,title="Default Title",release_date="Default Release Date",total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date ,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()
    
    # "4": "View all Video Info"
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    ## "5": "Info on 1 Video"
    def get_video(self, title=None, id=None):
        
        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that name or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    # "2": "Update 1 Video's Information"
    def edit_video(self,title=None,release_date=None, total_inventory=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]    

        query_params = {
        "title": title,
        "description": release_date,
        "total_inventory":total_inventory
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
            )
        
        print("response:", response)
        self.selected_video = None
        return response.json()

    # "3": "Delete 1 Video "
    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()
    

    def print_selected(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")