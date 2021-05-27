import requests
import datetime

class VideoRequests:
    def __init__(self, url="http://localhost:5000", videos=None):
        self.url = url
        self.videos = videos

    def create_video(self, title="Default Title", release_date="Default Description", total_inventory="Default Description"):
        query_params = {
            "title" : title,
            "release_date" : release_date,
            "total_inventory": total_inventory
        }

        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def list_all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_specific_video(self, title=None, id=None):
        
        for video in self.list_all_videos():
            
            if self.videos == None:
                return "Could not find a video by that name or id"
    
            if title:
                if video["title"] == title:
                    id = video["id"]
                    self.videos = video

            elif id == video["id"]:
                self.videos = video
            
        response = requests.get(self.url+"/videos")
        return response.json()
    

    def update_video(self, title=None, release_date=None, total_inventory=None):
        #should total_inventory default be 0?

        if not title:
            title = self.videos["title"]
        
        if not release_date:
            release_date = self.videos["release_date"]

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }

        response = requests.put(
            self.url+f"/videos/{self.videos['id']}",
            json=query_params
        )

        print("response:", response)
        self.videos = response.json()["video"]
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.videos['id']}")
        self.videos = None
        return response.json()

    def print_video(self):
        if self.videos:
            print(f"Video with id{self.videos['id'] is currently selected\n")