import requests
from datetime import datetime

class Video:
    def __init__(self, url="http://localhost:5000"):
        self.url = url

    def add_video(self, title="Default Title", release_date=\
        "Default Release Date", total_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def update_video(self, video_id=None, title=None,release_date=None,
        total_inventory=0):

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }

        response = requests.put(self.url+f"/videos/{video_id}",
            json=query_params)
        if response.status_code != 200:
            return "Could not find video by that id"
        print("response:", response)
        return response.json()

    def delete_video(self, video_id=None):
        response = requests.delete(self.url+f"/videos/{video_id}")
        if response.status_code != 200:
            return "Could not find video by that id"
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, video_id=None):
        response = requests.get(self.url+f"/videos/{video_id}")
        if response.status_code != 200:
            return "Could not find video by that id"
        return response.json()
