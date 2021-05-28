import requests
import datetime

class Video:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None):
        self.url = url
        self.selected_video = selected_video 

    def create_video(self, title="Default Name", release_date=None, total_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory":total_inventory,
            #"available_inventory": available_inventory
            }
        response = requests.post(self.url + "/videos", json=query_params)
        return response.json()

    def update_video(self, video_id=None, title="Default Name", release_date=0, total_inventory=0):
        query_params = {
            "title": title,
            "release_date":release_date,
            "total_inventory":total_inventory,
        }
        response = requests.put(self.url + f"/videos/{video_id}", json=query_params)
        return response.json()

    def delete_video(self, video_id=None):
        response = requests.delete(self.url+f"/videos/{video_id}")
        return response.json()

    def all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, video_id=None):      
        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()
        