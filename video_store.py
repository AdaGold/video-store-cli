import requests
import datetime
from flask import json

class VideoStore():
    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer
    
    def print_selected(self, choice):
            #     if self.choice:
            # print(f"You have selected #{self.choice}\n")
        if choice:
            print(f"You have selected #{choice}\n")

#1 
    def create_video(self, title, release_date, total_inventory):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        video_url = self.url+"/videos"
        print(f"about to send request to {video_url}")
        response = requests.post(video_url,json=query_params)
        print(response)
        # if time allows: check for: if response.status_code == 200:
        return response.json()
        # else: 


#2 - got 500 internal server error
    def edit_video(self, title, release_date, total_inventory):
        request_body = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        video_url = self.url+"/videos/"+str(self.selected_video["id"])
        print(f"about to send request to {video_url}")
        response = requests.put(video_url,json=request_body)
        print(response)
        # if time allows: check for: if response.status_code == 200:
        return response.json()

#3 - works
    def delete_video(self, selected_video):
        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()

#4 - basics work
    def get_all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

#5 - basics work
    def get_video_by_id(self, id=id):
        response = requests.get(self.url+f"/videos/{id}")
        # if time allows: check for: if response.status_code == 200:
        self.selected_video = response.json()
        return response.json()   

#6- basics work
    def create_customer(self, name, postal_code, phone):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

#7 - got 500 internal server error
    def edit_customer(self, name, postal_code, phone):
        request_body = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        customer_url = self.url+"/customers/"+str(self.selected_customer["id"])
        print(f"about to send request to {customer_url}")
        response = requests.put(customer_url,data=request_body)
        print(response)
        # if time allows: check for: if response.status_code == 200:
        return response.json()

#8- basics work
    def delete_customer(self, selected_customer):
        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()

#9- basics work
    def get_all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

#10- basics work
    def get_customer_by_id(self, id=id):
        response = requests.get(self.url+f"/customers/{id}")
        # if time allows: check for: if response.status_code == 200:
        self.selected_customer = response.json()
        return response.json()   

#11 
    def check_out(self, video_id, customer_id):
        query_params = {
            "video_id": video_id,
            "customer_id": customer_id
        }
        response = requests.post(self.url+f"/rentals/check-out", json=query_params)
        return response

#12 
    def check_in(self, video_id, customer_id):
        query_params = {
            "video_id": video_id,
            "customer_id": customer_id
        }
        response = requests.post(self.url+f"/rentals/check-in", json=query_params)
        return response



        # query_params = {
        #     "title": title,
        #     "release_date": release_date,
        #     "available_inventory": available_inventory
        # }
        # video_url = self.url+"/videos"
        # print(f"about to send request to {video_url}")
        # response = requests.post(video_url,data=query_params)
        # print(response)
        # # if time allows: check for: if response.status_code == 200:
        # return response.json()


    # def update_task(self,title=None,description=None):
    #     if not title:
    #         title = self.selected_task["title"]
    #     if not description:
    #         description = self.selected_task["description"]

    #     query_params = {
    #     "title": title,
    #     "description": description
    #     #"completed_at": self.selected_task["is_complete"]
    #     }
    #     response = requests.put(
    #         self.url+f"/tasks/{self.selected_task['id']}",
    #         json=query_params
    #         )
    #     print("response:", response)
    #     self.selected_task = response.json()["task"]
    #     return response.json()


    
    # def mark_complete(self):
    #     response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_complete")
    #     self.selected_task = response.json()["task"]
    #     return response.json()

    # def mark_incomplete(self):
    #     response = requests.patch(self.url+f"/tasks/{self.selected_task['id']}/mark_incomplete")
    #     self.selected_task = response.json()["task"]
    #     return response.json()



