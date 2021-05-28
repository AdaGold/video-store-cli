import requests
import datetime
from constants import *

class VideoStore:
    # def __init__(self, url="http://localhost:5000", selected_task=None):
    #     self.url = url
    #     self.selected_task = selected_task

    # using constants.py
    def __init__(self, url=BACKUP_URL, selected_video=None, \
        selected_customer=None): #check_out_video, check_in_video
        self.url = url
        # self.selected_customer = selected_customer
        # self.selected_video = selected_video
# will rental be a child of VideoStore? or will it be like this:
    

    # # create --- Video ---
    # def create_video(self,title="Default Title",  
    #     release_date="", total_inventory=0):

    #     query_params = {"title": title,
    #                     "release_date": release_date,
    #                     "total_inventory": total_inventory}

    #     response = requests.post(self.url+"/videos",json=query_params)
    #     return response.json()

    # # GET  *******Customer*********
    # def list_customers(self):
    #     response = requests.get(self.url+"/customers")
    #     return response.json()

    # GET  --- Video ---
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    # # GET  by id *******Customer*********
    # #### I"M HERE!
    # def get_customer(self, name=None, id=None):
        
    #     for task in self.list_tasks():
    #         if title:
    #             if task["title"]==title:
    #                 id = task["id"]
    #                 self.selected_task = task
    #         elif id == task["id"]:
    #             self.selected_task = task

    #     if self.selected_task == None:
    #         return "Could not find task by that name or id"

    #     response = requests.get(self.url+f"/tasks/{id}")
    #     return response.json()

    
    # Task list
    # ---------------------------------------------------------------
    def create_task(self,title="Default Task",description="Default \
        Description",completed_at=None):
        query_params = {
            "title": title,
            "description": description,
            "completed_at": completed_at
        }
        response = requests.post(self.url+"/tasks",json=query_params)
        return response.json()

    def list_tasks(self):
        response = requests.get(self.url+"/tasks")
        return response.json()

    def get_task(self, title=None, id=None):
        
        for task in self.list_tasks():
            if title:
                if task["title"]==title:
                    id = task["id"]
                    self.selected_task = task
            elif id == task["id"]:
                self.selected_task = task

        if self.selected_task == None:
            return "Could not find task by that name or id"

        response = requests.get(self.url+f"/tasks/{id}")
        return response.json()

    def update_task(self,title=None,description=None):
        if not title:
            title = self.selected_task["title"]
        if not description:
            description = self.selected_task["description"]

        query_params = {
        "title": title,
        "description": description
        #"completed_at": self.selected_task["is_complete"]
        }
        response = requests.put(
            self.url+f"/tasks/{self.selected_task['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_task = response.json()["task"]
        return response.json()

    def delete_task(self):
        response = requests.delete(self.url+f"/tasks/{self.selected_task['id']}")
        self.selected_task = None
        return response.json()
    
    def mark_complete(self):
        response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_complete")
        self.selected_task = response.json()["task"]
        return response.json()

    def mark_incomplete(self):
        response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_incomplete")
        self.selected_task = response.json()["task"]
        return response.json()

    def print_selected(self):
        if self.selected_task:
            print(f"Task with id {self.selected_task['id']} is currently selected\n")


        
