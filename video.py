from os import sendfile
import requests

class Video:
    def __init__(self, url="https://retro-video-store-api.herokuapp.com", selected_video=None):
        self.url = url
        self.selected_video = selected_video

    # adds video to connected API with the specified query parameters
    def add_video(self, title="Default Video", release_date=None, total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos", json=query_params)
        return response.json()
    
    # generates a list of all videos
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
    
    # retrieves video specific data - with options to 
    # search by title, id, and release date
    def get_video(self, title=None, id=None, release_date=None):

        for video in self.list_videos():
            if title:
                if video["title"] == title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video
            elif release_date:
                if video["release_date"] == release_date:
                    id = video["id"]
                    self.selected_video = video
        
        if self.selected_video == None:
            return "Could not find video with the details you have provided"
    
        response = requests.get(self.url+f"/videos/{id}")
        return response.json()
    
    # updates video in connected API with the specified query parameters
    def update_video(self, title=None, release_date=None, total_inventory=None):
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
        response = requests.put(self.url+f"/videos/{self.selected_video['id']}", json=query_params)
        self.selected_video = response.json()["video"]
        return response.json()
    
    # deletes the selected video
    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()
    
    # prints out the selected video's data
    def print_selected(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")
        else:
            print("Apologies, that video could not be found")
