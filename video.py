
import requests
BACKUP_URL = "https://retro-video-store-api.herokuapp.com"

class Video:
    def __init__(self, url = BACKUP_URL,selected_video=None):
        self.url = url
        self.selected_video = selected_video

    
    # def list_videos(self):
    #     response = requests.get(self.url+"/videos")
    #     return response.json()
    
    # def create_video(self,title, release_date):
    #     query_params = {
    #     "title": title,
    #     "release_date": release_date
    #     }
    #     response = requests.post(self.url+"/videos",json=query_params)
    #     return response.json()

    
    # def delete_video(self):
    #     response = requests.delete(self.url+f"/videos/{self.video['id']}")
    #     self.video = None
    #     return response.json()
    
    
    # def get_video(self,id=None):
    #     for video in self.list_videos():
    #         if not video:
    #             return "No customer can be found by that id"
    #         if id==video["id"]:
    #             self.selected_video = video
            
    #     response = requests.get(self.url+f"/videos/{id}")
    #     return response.json()