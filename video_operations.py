import requests
import datetime

class VideoOperations:
    def __init__(self, url="http://localhost:5000"):
        self.url = url
        self.selected_video = None
         
    def add_video(self, title="default video title", release_date=datetime.now(), total_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()
    
    def edit_video(self, title=None, release_date=datetime.now(), total_inventory=0):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self. selected_video["total_inventory"]

        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory}
        
        response = requests.put(
            self.url+f"/videos/{self.selected_video['video_id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()["videos"]
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['video_id']}")
        self.selected_video = None
        return response.json()
    
    def get_all_video_information(self):
        response = requests.get(self.url+"/videos")
        return response.json()
    
    def get_one_video_info(self, title=None, video_id=None):
        
        for video in self.get_all_video_information():
            if title:
                if video["title"]==title:
                    video_id = video["video_id"]
                    self.selected_video = video
            elif video_id == video["video_id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that title or id"

        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()
    
    