import requests
import datetime


class Video:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None):
        self.url = url
        self.selected_video = selected_video

    def create_video(self, name="Default Video", postal_code="Default Postal", phone="Default Phone"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/videos", json=query_params)
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, name=None, id=None):
        for video in self.list_videos():
            if name:
                if name["name"] == name:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find vieo by that name or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def upgrade_video(self, name=None, description=None):
        if not name:
