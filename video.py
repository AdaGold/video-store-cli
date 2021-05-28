import requests
import datetime

class Video:
    def __init__(self, url="http://localhost:5000", selected_video=None):
        self.url = url
        self.selected_video = selected_video
    
    def create_video(self,title="Default Video",release_date="Default date",total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, title=None, id=None):
        
        for video in self.list_videos():
            if video:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return "Could not find video by that name or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

    def update_video(self,title=None,release_date=None,total_inventory=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["relase_date"]
        if not total_inventory:
            total_inventory=self.total_inventory["total_inventory"]

        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory":total_inventory
        #"completed_at": self.selected_task["is_complete"]
        }
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_video = response.json()["video"]
        return response.json()

    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()
    
    # def mark_complete(self):
    #     response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_complete")
    #     self.selected_task = response.json()["task"]
    #     return response.json()

    # def mark_incomplete(self):
    #     response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_incomplete")
    #     self.selected_task = response.json()["task"]
    #     return response.json()

    def print_selected(self):
        if self.selected_video:
            print(f"Video with id {self.selected_video['id']} is currently selected\n")