import requests

class Video:
    def __init__(self, url = "https://localhost:5000", selected_video = None):
        self.url = url
        self.selected_video = selected_video

    def add_video(self, title = "Default Title", release_date = None, total_inventory = None):
        query_params = {
            "title" : title,
            "release_date" : release_date,
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
    
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
    
    def get_video(self, title=None, id=None, release_date=None):
        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            elif release_date:
                if video["release_date"]==release_date:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "I'm sorry, I couldn't find that video"
        
        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()
        
    def print_selected(self):
        if self.selected_video:
            print(f"Video {self.selected_video['title']} is currently selected.")