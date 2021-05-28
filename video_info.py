import requests
from datetime import datetime

class VideoInfo:
    # Where the CLI is accessing the DB, chose to access my local machine
    def __init__(self, url="http://localhost:5000"):
        self.url = url
        self.selected_video = None
        
    # Video store employee adding new video into inventory 
    def add_video(self, title="default video title", release_date=str(datetime.now()), total_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()
    
    # Video store employee making edits to a current video by ID 
    def edit_video(self, video_id, title=None, release_date=datetime.now(), total_inventory=0):
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
            self.url+f"/videos/{video_id}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()
        return response.json()

    # Video store employee deleting a video from inventory by video ID 
    def delete_video(self, video_id):
        response = requests.delete(self.url+f"/videos/{video_id}")
        return response.json()
    
    # Video store employee getting all videos in inventory 
    def get_all_video_information(self):
        response = requests.get(self.url+"/videos")
        return response.json()
    
    # Video store employee getting information for one video by ID  
    def get_one_video_information(self, video_id):
        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()

    # Video store employee selecting a specific video to perform future actions on
    def print_selected(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")