import requests
import datetime


class VideoList:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video

    def add_video(self, title="Default Video", release_date="1922-01-01", total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos", json=query_params)
        return response.json()
    # Number 4 GET all videos

    def list_video(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, title=None, id=None):

        for video in self.list_video():
            if title:
                if video["title"] == title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that name or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def edit_video(self):

        query_params = {
            "title": self.selected_video['title'],
            "release_date": self.selected_video['release_date'],
            "total_inventory": self.selected_video['total_inventory']
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
        )
        print("response:", response)
        self.selected_video = response.json()
        return response.json()

    def delete_video(self):
        response = requests.delete(
            self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()

    def mark_complete(self):
        response = requests.patch(
            self.url+f"/videos/{self.selected_video['id']}/mark_complete")
        self.selected_video = response.json()["video"]
        return response.json()

    def mark_incomplete(self):
        response = requests.patch(
            self.url+f"/videos/{self.selected_video['id']}/mark_incomplete")
        self.selected_video = response.json()["video"]
        return response.json()

    def print_selected(self):
        if self.selected_video:
            print(
                f"Video with id {self.selected_video['id']} is currently selected\n")
