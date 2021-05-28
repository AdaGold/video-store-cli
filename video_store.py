import requests

class VideoStore:

    def __init__(self, url="http://localhost:5000", selected_video=None, selected_customer=None):
        self.url = url
        self.selected_video = selected_video
        self.selected_customer = selected_customer


    # "1": "Add a Video" 
    def create_video(self, title="default", release_date="default", total_inventory=0):

        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory
        }
        response = requests.post(self.url+"/videos", json=query_params)
        return response.json()


    # "2": "Edit a Video"
    def update_video(self, title=None, release_date=None, total_inventory=None):
        
        if not title:
            title = self.selected_video["title"]
        if not release_date:
            release_date = self.selected_video["release_date"]
        if not total_inventory:
            total_inventory = self.selected_video["total_inventory"]
        
        available_inventory = (int(total_inventory) - int(self.selected_video["total_inventory"])) + int(self.selected_video["available_inventory"])
        
        query_params = {
            "title": title,
            "release_date": release_date,
            "total_inventory": total_inventory,
            "available_inventory": available_inventory
            }
        
        response = requests.put(
            self.url+f"/videos/{self.selected_video['id']}",
            json=query_params
            )
        self.selected_video = response.json()["id"]
        return response.json()


    # "3": "Delete a Video"
    def delete_video(self):

        response = requests.delete(self.url+f"/videos/{self.selected_video['id']}")
        self.selected_video = None
        return response.json()


    # "4": "Get all Videos"
    def list_videos(self):

        response = requests.get(self.url+"/videos")
        return response.json()


    # "5": "Get One Video"
    def get_video(self, title=None, id=None):
    
        for video in self.list_videos():
            if title:
                if video["title"]==title:
                    id = video["id"]
                    self.selected_video = video
            elif id == video["id"]:
                self.selected_video = video

        if self.selected_video == None:
            return None

        response = requests.get(self.url+f"/videos/{id}")
        return response.json()


    # "6": "Add a Customer"
    def create_customer(self, name="default", postal_code=None, phone="xxx-xxx-xxxx"):
        
        #consider validating postal_code and phone for format
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
        }
        response = requests.post(self.url+"/customers", json=query_params)
        return response.json()


    # "7": "Edit a Customer"
    def update_customer(self, name=None, postal_code=None, phone=None):
        
        if not name:
            name = self.selected_customer["name"]
        if not postal_code:
            postal_code = self.selected_customer["postal_code"]
        if not phone:
            phone = self.selected_customer["phone"]
        
        query_params = {
            "name": name,
            "postal_code": postal_code,
            "phone": phone
            }
        
        response = requests.put(
            self.url+f"/customers/{self.selected_customer['id']}",
            json=query_params
            )
        self.selected_customer = response.json()["id"]
        return response.json()


    # "8": "Delete a Customer"
    def delete_customer(self):

        response = requests.delete(self.url+f"/customers/{self.selected_customer['id']}")
        self.selected_customer = None
        return response.json()


    # "9": "Get Customer Info for One Customer"
    def get_customer(self, name=None, id=None):

        for customer in self.list_customers():
            if name:
                if customer["name"]==name:
                    id = customer["id"]
                    self.selected_customer = customer
            elif id == customer["id"]:
                self.selected_customer = customer

        if self.selected_customer == None:
            return None

        response = requests.get(self.url+f"/customers/{id}")
        return response.json()


    # "10": "Get Customer Info for All Customers"
    def list_customers(self):

        response = requests.get(self.url+"/customers")
        return response.json()


    # "11": "Check OUT a Video"
    def check_out_video_to_customer(self, customer_id=None, video_id=None):
        
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-out", json=query_params)
        return response.json()


    # "12": "Check IN a Video"
    def check_in_video_to_customer(self, customer_id=None, video_id=None):
        
        #PROBLEM: customers can "check-in" videos that aren't checked out to them
        #this needs to be fixed in the API
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }
        response = requests.post(self.url+"/rentals/check-in", json=query_params)
        return response.json()

