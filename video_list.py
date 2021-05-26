import requests
import datetime

class VideoList:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video

    # list all videos (see store stock)
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
        
    # add a video so I can check it out to customers
    def add_video(self, title, release_date, total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    # get details of one video
    def get_video(self, title=None, id=None):

        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    self.selected_video = video # does this solely serve line 35?
                    id = video["id"] # used for line 39
            elif id == video["id"]:
                self.selected_video = video

        # for video in self.list_videos(): # why does this return the id after???????
        #     if title:
        #         video["title"]==title
        #         self.selected_video = video # does this solely serve line 35?
        #         id = video["id"] # used for line 39
        #     elif id:
        #         video["id"]==id
        #         self.selected_video = video

        if self.selected_video == None:
            return "Could not find any video by that name or id."

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    # edit a video to ensure information accuracy
    def update_video(self, title, release_date, total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
        }
        response = requests.put(self.url+f"/videos/{self.selected_video['id']}", json=query_params)

        print("response:", response) # take this out why is this here
        self.selected_video = response
        return response.json()

    # delete a video
    def delete_video(self):

        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()





