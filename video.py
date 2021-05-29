import requests
import datetime

class Video:
    def __init__(self, url="http://localhost:5000"):
        self.url = url

    def create_video(self, title, release_date, total_inventory):
        request_body = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
    
    def update_video(self, title=None, release_date=None, total_inventory=None):
        request_body = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }

        response = requests.get(self.url+f"/videos/{video_id}", json=request_body)
        return response.json()

    # def delete_video(self, video_id)

    def all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def single_video(self, video_id):
        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()

