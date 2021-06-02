import requests
import datetime

class Videos:
    def __init__(self, URL="https://retro-video-store-api.herokuapp.com", selected_video=None):
        self.url = URL
        self.selected_video = selected_video

    def create_video(self,title="Default Video",release_date="Default Description",total_inventory=int,available_inventory=int):
        query_params = {
            "title": title, 
            "release_date": release_date, 
            "total_inventory": total_inventory,
            "available_inventory": available_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, title=None, id=None):
        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = task

        if self.selected_video == None:
            return "Could not find video by that name or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def update_video(self,title=None,release_date=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]

        query_params = {
        "title": title,
        "release_date": release_date
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()["video"]
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
    self.selected_video = None
    return response.json()