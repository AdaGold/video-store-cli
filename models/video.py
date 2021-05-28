import requests
from datetime import date, timedelta
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

class Video:
    def __init__(self, url=BACKUP_URL, selected_video=None):
        self.url = url
        self.selected_video = selected_video
    
    def create_video(self,title="Default Video", release_date=str(date.today() - timedelta(15000)), total_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()
    
    def list_videos(self):
        response = requests.get(self.url + "/videos")
        return response.json()

    def get_one_video(self, video_id=None):
        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()

    def update_video(self, video_id, release_date=str(date.today() - timedelta(15000)), total_inventory=0, title=None):
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
            self.url+f"/videos/{video_id}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()
