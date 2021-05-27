import requests
import datetime

class VideoStore:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com"):
        self.url = url
        self.video = None
    
    def get_all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
    
    def get_video(self, id):
        response = requests.get(self.url+f"/videos/{id}")
        self.video = response
        return response.json()
    
    def create_video(self,title="Crows at Work",description="Short Stories Featuring Crows in Various SWE Roles",completed_at=None):
        query_params = {
            "title": title,
            "description": description,
            "completed_at": completed_at
        }
        response = requests.post(self.url+"/tasks",json=query_params)
        return response.json()
