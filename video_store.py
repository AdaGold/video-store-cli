import requests 
import datetime 

class Videostore:
    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer 

# ==========All For Video Options========== 

    # Option 1: Add a video 
    def create_video(self,title="default", release_date="default", total_inventory=None):
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos",json=query_params)
        return response.json()

    # Option 2: Edit a video 
    def update_video(self,video_id="default", title="title", release_date="default", total_inventory=None):
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]

        query_params = {
        "title": title,
        "release_date": release_date,
        "total_inventory": total_inventory
        }

        response = requests.put(
            self.url+f"/videos/{video_id}", 
            json=query_params
            )
        # print("response:", response)
        self.selected_video = response.json() 
        return response.json()

    # Option 3: Delete a video 
    def delete_video(self):
        response = requests.delete(self.url+f"/videos/{id}") 
        return response.json()

    # Option 4: Get information about all videos
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    # Option 5: Get information of one video 
    def get_video(self, title="title", id="default"):
        
        for video in self.get_video():
            if title:
                if video["title"]==title:
                    title = video["title"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_task = video

        if self.selected_video == None:
            return "Could not find video by that name or id"

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()

# ==========All For Customers Options========== 

    # Option 6: Add a customer 
    def create_customer(self,name="name",postal_code="postal_code",phone="phone"):
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers",json=query_params)
        return response.json()

    # Option 7: Edit a customer 
    def update_customer(self,customer_id= "default", name="name",postal_code="postal_code",phone="phone"):
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone =self.selected_customer["phone"]

        query_params = {
        "name": name,
        "postal_code": postal_code,
        "phone": phone
        }
        response = requests.put(
            self.url+f"/customers/{customer_id}"," #{self.selected_customer['id']}",
            json=query_params
            )
        print("response:", response)
        self.selected_customer = response.json()["customer"]
        return response.json()

    # Option 8: Delete a customer 
    def delete_customer(self):
        response = requests.delete(self.url+f"/customers/{id}") 
        return response.json()

    # Option 9: Get informaton of one customer 
    def get_customer(self, id="default", name=None, postal_code=None, phone=None):
        for customer in self.list():
            if name:
                if customer["name"]==name:
                    id = customer["id"]
                    self.selected_customer = customer
            
            elif postal_code == customer["postal"]:
                self.selected_customer = customer
            elif phone == customer["phone"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return "Could not find customer by that name or id"

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()
    
    # Option 10: Get information of all customers 
    def list_customer(self):
        response = requests.get(self.url+"/customers")
        return response.json()

# ==========Check-in and Check-out: video and customers relationship========== 

    # Option 11: Check out a video to a customer 
    def check_out(self, customer_id, video_id):
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-out", json=request_body)
        return response
        
    # Option 12: Check in a video from a customer 
    def check_in(self, customer_id, video_id):
        request_body = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in", json=request_body) 
        return response



