import requests
# import datetime

class VideoList:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
        
    def add_video(self, title, release_date, total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }

        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def get_video(self, title=None, id=None):

        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    self.selected_video = video 
                    id = video["id"] 
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that name or id."

        response = requests.get(self.url+f"/videos/{id}") # could also return video from lines 27, 30 as "return video" in place of 36
        return response.json()

    def update_video(self, title, release_date, total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
        }

        response = requests.put(self.url+f"/videos/{self.selected_video['id']}", json=query_params)
        self.selected_video = response
        return response.json()

    def delete_video(self):

        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None # replaces instance of video (dictionary) that was just obtained
        return response.json()





