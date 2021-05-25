import requests

class VideoStore:
    def __init__(self, url = "https://retro-video-store-api.herokuapp.com", selected_video = None):
        self.url = url
        self.selected_video = selected_video

    def add_video(self, title = "Default Title", release_date = None, total_inventory = None):
        query_params = {
            "title" : title,
            "release date" : release_date,
            "total_inventory" : total_inventory
        }
        response = requests.post(self.url+"/videos", json = query_params)
        return response.json()
    
    def update_video(self, title, release_date, total_inventory):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]
        query_params = {
            "title" : title,
            "release date" : release_date,
            "total_inventory" : total_inventory
        }
        response = requests.put(self.url+f"/videos/{self.selected_video['id']}", json=query_params)
        self.selected_video = response.json()["video"]
        return response.json()