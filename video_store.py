import requests
import datetime
from flask import json


##could also put a helper function for select video in main.py
# 
#  

class Video_store:
    def __init__(self, URL = "https://retro-video-store-api.herokuapp.com", selected_video=None, selected_customer=None): #selected_customer=None, selected_rental=None ):
        self.url = URL
        self.selected_video = selected_video
        self.selected_customer = selected_customer


    ########## video actions to do: edit, still need to decide which query params needed and how to edit (look at routes?)
    ##Check out video to customer: part of video requirements is to be able to check it out to customers, which is through rental routes
    def check_out_video(self, customer_id, video_id):
        query_params={
            "customer_id": customer_id,
            "video_id": video_id
        }
        print(query_params)
        print(self.url+"/rentals/check-out")
        response = requests.post(self.url+"/rentals/check-out", json = query_params)
        
        return response

    def check_in_video(self, customer_id, video_id):
        query_params={
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in", json= query_params)
        return response

    def print_selected(self):
        pass
        if self.selected_video:
            print(f"Video with id {self.selected_video} is selected.") 
        else:
            print("Video not found")

    def create_video(self, title= "Default title", release_date= "Default release date", total_inventory= "default stock"):

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    def list_videos(self): #List videos, get information about all videos  | I can see the store stock  |
        response = requests.get(self.url+"/videos")
        return response.json()

    #| List videos #2 get information about one video  | I can see how many copies
    def get_video(self, title=None, video_id=None, release_date= None):
        
        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    video_id = video["id"]
                    self.selected_video = video
            elif int(video_id) == video["id"]:
                self.selected_video = video
            # elif release_date:
            #     if video["release_date"]==release_date:
            #         self.selected_video = video 

        if self.selected_video == None:
            return "Could not find video in stock"

        response = requests.get(self.url+f"/videos/{video_id}") #self. instead of requests?
        return response.json()

    #edit a video  | the information about the video is accurate
    def update_video(self,title=None, video_id=None, release_date=None, total_inventory=None): 
        if not title:
            title = self.selected_video["title"]
        if not video_id:
            video_id = self.selected_video["id"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]

        query_params = {
            "id": video_id,
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory}
        
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
            )
        print("response:", response) #add ansi color codes here?
        self.selected_video = response.json()
        return response.json()

    # delete a video  | the store records stay up to date  |
    def delete_video(self): #delete a video
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()
    #################################################### end video actions

    #List customers
    def list_customers(self): 
        response = requests.get(self.url+"/customers")
        return response.json()

    #Customer create, edit, delete
    def create_customer(self, name= "Default name", phone= "000-000-0000", postal_code= "00000"):

        query_params = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code,
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    def update_customer(self,customer_id=None,name=None, phone=None, postal_code=None): 
        if not customer_id:
            customer_id = self.selected_customer["id"]
        if not name:
            name = self.selected_customer["name"]
        if not phone:
            phone = self.selected_customer["phone"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]

        query_params = {
            "name": name,
            "phone": phone,
            "postal_code": postal_code,
        }
        
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response) #add ansi color codes here?
        self.selected_video = response.json()
        return response.json()
    
    def delete_customer(self): #delete a customer
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_video = None
        return response.json()
