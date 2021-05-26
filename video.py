import requests
import datetime

# do I need to make separate classes for customers, videos, and rental
# like I did in my API?

# do you have to "select" something before updating/deleting it? why?

class Video:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video

    def add_video(self, title="Default Title", release_date=\
        "Default Release Date", total_inventory=0, available_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
            "available_inventory": available_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def update_video(self, title=None,release_date=None,
        total_inventory=0,available_inventory=0):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
            "available_inventory": available_inventory
        }
        response = requests.put(
            self.url+f"/videos/{self.get_video['video']}",
            json=query_params
            )
        print("response:", response)
        self.selected_task = response.json()["video"]
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.get_video['id']}")
        self.selected_video = None
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, title=None, video_id=None):

        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    video_id = video["id"]
                    self.selected_video = video
            elif video_id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that name or id"

        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()

    def print_selected_video(self):
        if self.selected_video:
            print(f"Video with id {self.get_video['video_id']} is currently selected\n")
