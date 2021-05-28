import requests
import datetime


class Video:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None):
        self.url = url
        self.selected_video = selected_video

    def create_video(self, title="Default Video", release_date="Default Date", total_inventory="Default Total"):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
            "available_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos", json=query_params)
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, title=None, id=None):
        for video in self.list_videos():
            if title:
                if title["title"] == title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that title or ID"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def upgrade_video(self, id=None, title=None, release_date=None, total_inventory=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]

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
        # self.selected_video = response.json()["video"]
        return response.json()

    def delete_video(self):
        response = requests.delete(
            self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()
