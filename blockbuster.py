import requests
import datetime

class Blockbuster:
    def __init__(self, url="https://mn-retro-video-store.herokuapp.com/"):
        self.url = url

    # add a video so that I can check it out to customers - POST
    def add_video(self, title, release_date, total_inventory):
        request_body = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
            # "available_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos", json=request_body)
        return response.json()

    # edit a video so that the information about the video is accurate - PUT
    def edit_video(self, video_id, title=None, release_date=None, total_inventory=None):
        request_body = {
            "video_id": video_id,
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        # f before videos link is b/c of video_id
        response = requests.put(self.url+f"/videos/{video_id}", json=request_body)
        return response.json()

    # delete a video so that the store records stay up to date - DELETE
    def delete_video(self, video_id):
        response = requests.delete(self.url+f"/videos/{video_id}")
        return response.json()
    
    # get information about all videos so that I can see the store stock - GET
    def all_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()
    
    # get information about a specific video so that I can see how many copies are available - GET
    def single_video(self, video_id):
        response = requests.get(self.url+f"/videos/{video_id}")
        return response.json()

    # add a customer so that I can check out videos to the customer - POST
    def add_customer(self, name, postal_code, phone):
        request_body = {
            "name": name, 
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers", json=request_body)
        return response.json()

    # edit a customer so the information about the customer is accurate - PUT
    def edit_customer(self, customer_id, name=None, postal_code=None, phone=None):
        request_body = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.put(self.url+f"/customers/{customer_id}", json=request_body)
        return response.json()

    # delete a customer so that the customer is no longer in the store records - DELETE
    def delete_customer(self, customer_id):
        response = requests.delete(self.url+f"/customers/{customer_id}")
        return response.json()

    # get information about all customers so that I can see how many customers the store has - GET
    def all_customers(self):
        response = requests.get(self.url+"/customers")
        return response.json()

    # get information about a specific customer so I can see how many videos a customer has rented currently - GET
    def single_customer(self, customer_id):
        response = requests.get(self.url+f"/customers/{customer_id}")
        return response.json()

    # check out a video to a customer so that the store has a record of who has the video - POST
    def check_out(self, customer_id, video_id):
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-out", json=request_body)
        return response.json

    # check in a video from a customer so that the video will be available to other customers - POST
    def check_in(self, customer_id, video_id):
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+f"/rentals/check-in", json=request_body)
        return response.json








