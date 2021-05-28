import requests
from datetime import datetime

class VideoOperations:
    def __init__(self, url="http://localhost:5000"):
        self.url = url
        
         
    def add_video(self, title="default video title", release_date=str(datetime.now()), total_inventory=0):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()
    
    
    def edit_video(self, video_id, title=None, release_date=datetime.now(), total_inventory=0):
        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory}
        
        response = requests.put(
            self.url+f"/videos/{video_id}",json=query_params)
        print("response:", response)
        return response.json()


    def delete_video(self, video_id):
        response = requests.delete(self.url+f"/videos/{video_id}")
        return response.json()
    
    
    def get_all_video_information(self):
        response = requests.get(self.url+"/videos")
        return response.json()
    
    
    def get_one_video_information(self, video_id=None):
        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()
