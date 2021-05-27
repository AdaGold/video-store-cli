import requests 
import datetime 

class Videostore:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video
        # self.selected_customer = selected_customer 

#all for videos 
    #1 - add a video so that I can check it out to the customers
    def create_video(self,title="Default Video", release_date="Default"):
        query_params = {
            "title": title,
            "release_date": release_date
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    #2 - edit a video so that information about the video is accurate 
    def update_video(self,title="title"):
        if not title:
            title = self.selected_video["title"]

        query_params = {
        "title": title,
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_task['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()["video"]
        return response.json()

    #3 - delete a video so that the store records stay up to date
    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_task['id']}")
        self.selected_task = None
        return response.json()

    #4 - get information about all videos so that I can see the store stock
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    #5 - get information about one video so that I can see how many copies are available 
    def get_video(self, title=None, id=None):
        
        for video in self.get_video():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_task = video

        if self.selected_video == None:
            return "Could not find task by that name or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()


