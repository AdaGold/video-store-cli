import requests
import datetime
from rental import RentalOps

class VideoOps:
    def __init__(self, url = "https://retro-video-store-api.herokuapp.com", selected_video=None):
        self.url = url
        self.selected_video = selected_video

    def add_video(self, title, release_date, total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos", json=query_params)
        return response.json()

    def update_video(self, title, release_date=datetime.datetime.now(),total_inventory=0):
        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
        }

        response = requests.put(self.url+f"/videos/+{self.selected_video['id']}", json=query_params)
        return response.json()

    def delete_video(self, video_id):
        response = requests.delete(self.url+f"/videos/{video_id}")
        return response.json()

    def list_all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, id):
        response = requests.get(self.url+"/videos/"+str(id))
        response=response.json()
        self.selected_video=response
        return response
    
    def print_selected(self):
        print(self.selected_video)
        return
